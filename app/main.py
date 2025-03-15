from fastapi import FastAPI
from app.api.endpoints import portfolio

app = FastAPI()

app.include_router(portfolio.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the IBKR MCP Server"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)