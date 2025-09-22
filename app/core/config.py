import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Only keep essential local configuration
    IBKR_HOST = os.getenv("IBKR_HOST", "127.0.0.1")
    IBKR_PORT = int(os.getenv("IBKR_PORT", "7496"))