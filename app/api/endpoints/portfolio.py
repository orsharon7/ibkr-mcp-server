from fastapi import APIRouter, HTTPException, status
from app.services.ibkr_service import ibkr_service
from app.models.requests import PortfolioRequest, HealthCheckResponse
from app.models.portfolio import Portfolio
from datetime import datetime
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Health check endpoint
    """
    return HealthCheckResponse(
        status="healthy",
        version="1.0.0",
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/portfolio", response_model=Portfolio)
async def get_portfolio(
    request: PortfolioRequest = None
):
    """
    Get portfolio details from IBKR
    
    Local-only endpoint - no authentication required.
    """
    try:
        # Use default request if none provided
        if request is None:
            request = PortfolioRequest()
            
        logger.info(f"Portfolio request for account: {request.account_id}")
        
        portfolio = await ibkr_service.fetch_portfolio_details(
            account_id=request.account_id,
            include_positions=request.include_positions,
            include_summary=request.include_summary
        )
        
        logger.info("Portfolio data retrieved successfully")
        return portfolio
        
    except Exception as e:
        # Log the full error for local debugging
        logger.error(f"Portfolio fetch failed: {str(e)}")
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to fetch portfolio: {str(e)}"  # Show full error for local debugging
        )