"""
Request models for input validation
"""
from pydantic import BaseModel, Field
from typing import Optional


class PortfolioRequest(BaseModel):
    """
    Request model for portfolio endpoint
    """
    account_id: Optional[str] = Field(
        None, 
        description="Specific account ID to fetch portfolio for",
        max_length=50,
        regex="^[A-Za-z0-9_-]*$"
    )
    include_positions: bool = Field(
        True,
        description="Whether to include position details"
    )
    include_summary: bool = Field(
        True,
        description="Whether to include account summary"
    )


class HealthCheckResponse(BaseModel):
    """
    Response model for health check endpoint
    """
    status: str = Field(..., description="Service status")
    version: str = Field(..., description="Application version")
    timestamp: str = Field(..., description="Current timestamp")