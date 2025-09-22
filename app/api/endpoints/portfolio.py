from fastapi import APIRouter, HTTPException, Depends, status
from app.services.ibkr_service import ibkr_service
from app.core.security import verify_api_key, sanitize_error_message
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
    Health check endpoint - no authentication required
    """
    return HealthCheckResponse(
        status="healthy",
        version="1.0.0",
        timestamp=datetime.utcnow().isoformat()
    )


@router.get("/portfolio", response_model=Portfolio)
async def get_portfolio(
    request: PortfolioRequest = Depends(),
    api_key: str = Depends(verify_api_key)
):
    """
    Get portfolio details from IBKR
    
    Requires valid API key authentication via Bearer token.
    """
    try:
        logger.info(f"Portfolio request for account: {request.account_id}")
        
        portfolio = await ibkr_service.fetch_portfolio_details(
            account_id=request.account_id,
            include_positions=request.include_positions,
            include_summary=request.include_summary
        )
        
        logger.info("Portfolio data retrieved successfully")
        return portfolio
        
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        # Log the full error and return sanitized message
        logger.error(f"Portfolio fetch failed: {str(e)}")
        
        sanitized_message = sanitize_error_message(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=sanitized_message
        )