import os
from fastapi import FastAPI
from app.api.endpoints import portfolio

app = FastAPI(
    title="IBKR MCP Server - Local",
    description="Local FastAPI application for IBKR portfolio management",
    version="1.0.0",
    docs_url="/docs",  # Always enable docs for local usage
    redoc_url="/redoc"  # Always enable redoc for local usage
)

# Include routers
app.include_router(portfolio.router, prefix="/api/v1", tags=["portfolio"])

@app.get("/")
async def read_root():
    """Root endpoint with basic information"""
    return {
        "message": "Welcome to the IBKR MCP Server (Local)", 
        "version": "1.0.0",
        "status": "healthy"
    }

if __name__ == "__main__":
    import uvicorn
    
    # Local-only configuration
    host = "127.0.0.1"  # Always localhost for local usage
    port = int(os.getenv("PORT", "8000"))
    
    uvicorn.run(
        app, 
        host=host, 
        port=port,
        reload=True  # Enable auto-reload for local development
    )