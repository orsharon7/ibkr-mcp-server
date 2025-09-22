"""
Security utilities and authentication for IBKR MCP Server
"""
import os
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional


security = HTTPBearer()


def get_api_key() -> str:
    """Get API key from environment variables"""
    api_key = os.getenv("API_KEY")
    if not api_key or api_key == "your_ibkr_api_key":
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key not configured"
        )
    return api_key


async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    """
    Verify API key authentication
    
    Args:
        credentials: HTTP authorization credentials
        
    Returns:
        The verified API key
        
    Raises:
        HTTPException: If authentication fails
    """
    try:
        api_key = get_api_key()
        
        if credentials.credentials != api_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API key",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return credentials.credentials
        
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
            headers={"WWW-Authenticate": "Bearer"},
        )


def sanitize_error_message(error: Exception) -> str:
    """
    Sanitize error messages to prevent information disclosure
    
    Args:
        error: The original exception
        
    Returns:
        A sanitized error message safe for client consumption
    """
    # Log the full error for debugging (in production, use proper logging)
    print(f"Internal error: {str(error)}")
    
    # Return generic error message
    error_str = str(error).lower()
    
    if "connection" in error_str or "network" in error_str:
        return "Service temporarily unavailable"
    elif "authentication" in error_str or "auth" in error_str:
        return "Authentication failed"
    elif "permission" in error_str or "forbidden" in error_str:
        return "Access denied"
    elif "timeout" in error_str:
        return "Request timeout"
    else:
        return "An error occurred while processing your request"