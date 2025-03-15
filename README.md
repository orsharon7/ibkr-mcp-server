# IBKR MCP Server

This project is a FastAPI application that interacts with the Interactive Brokers (IBKR) API to fetch portfolio details.

## Project Structure

```
ibkr-mcp-server
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   └── endpoints
│   │       ├── __init__.py
│   │       └── portfolio.py
│   ├── core
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models
│   │   ├── __init__.py
│   │   └── portfolio.py
│   └── services
│       ├── __init__.py
│       └── ibkr_service.py
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ibkr-mcp-server
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your IBKR API credentials.

5. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

Once the server is running, you can access the API endpoints to fetch portfolio details. The API documentation will be available at `http://localhost:8000/docs`.

## License

This project is licensed under the MIT License.