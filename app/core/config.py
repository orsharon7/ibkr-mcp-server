import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    IBKR_API_KEY = os.getenv("IBKR_API_KEY")
    IBKR_API_SECRET = os.getenv("IBKR_API_SECRET")
    IBKR_BASE_URL = os.getenv("IBKR_BASE_URL", "https://api.ibkr.com/v1")