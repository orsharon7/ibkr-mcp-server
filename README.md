# Local IBKR MCP Server - Optimized for Local Usage

This is a **simplified, local-only** FastAPI application that connects to your local Interactive Brokers (IBKR) TWS/Gateway to fetch portfolio data.

## 🏠 Local-Only Design

This version has been optimized specifically for local usage with:
- ✅ **No authentication** - Safe for single-user local access
- ✅ **No rate limiting** - No restrictions for local usage  
- ✅ **No CORS/security headers** - Unnecessary complexity removed
- ✅ **Minimal dependencies** - Only essential packages included
- ✅ **Always-on API docs** - Swagger UI available at `/docs`
- ✅ **Full error details** - Complete error messages for easier debugging

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn python-dotenv ib_async pydantic
   ```

2. **Configure IBKR connection:**
   ```bash
   # Edit .env file
   IBKR_HOST=127.0.0.1
   IBKR_PORT=7496  # 7497 for paper trading
   ```

3. **Start your IBKR TWS or Gateway** on your local machine

4. **Run the server:**
   ```bash
   python app/main.py
   ```

5. **Access the API:**
   - API Documentation: http://localhost:8000/docs
   - Portfolio Data: http://localhost:8000/api/v1/portfolio
   - Health Check: http://localhost:8000/api/v1/health

## 📦 Minimal Dependencies

This local version only uses essential packages:
- `fastapi` - Web framework
- `uvicorn` - ASGI server  
- `ib_async` - IBKR connection library
- `pydantic` - Data validation
- `python-dotenv` - Environment configuration

**Removed dependencies:**
- ❌ `requests` - Unused in code
- ❌ `httpx` - Unused in code  
- ❌ `slowapi` - Rate limiting not needed locally

## 🔧 Configuration

Simple `.env` configuration:
```env
IBKR_HOST=127.0.0.1
IBKR_PORT=7496
PORT=8000
```

## 📊 API Endpoints

### Portfolio Data (No Auth Required)
```
GET /api/v1/portfolio
```

Optional query parameters:
- `account_id` - Specific account ID
- `include_positions` - Include position details (default: true)
- `include_summary` - Include account summary (default: true)

### Health Check
```
GET /api/v1/health
```

## 🔗 Data Flow

```
Your IBKR TWS/Gateway (127.0.0.1:7496) ←→ This Server (127.0.0.1:8000) ←→ Your Browser
```

- ✅ All connections stay on localhost
- ✅ Read-only access to IBKR data
- ✅ No external network traffic
- ✅ No third-party data transmission

## 🛠️ Development

Auto-reload is enabled for local development:
```bash
# Server automatically restarts when code changes
python app/main.py
```

## 📋 IBKR Setup

1. Install and run IBKR TWS or Gateway
2. Enable API connections in TWS/Gateway settings
3. Set socket port to 7496 (live) or 7497 (paper)
4. Allow connections from localhost (127.0.0.1)

## 🔒 Security Note

This local version removes production security features that are unnecessary for single-user local access:
- No authentication (safe since it's localhost-only)
- No rate limiting (single user doesn't need limits)
- No CORS restrictions (same-origin policy irrelevant)
- No security headers (browser security not applicable)

Your IBKR data stays completely local and private.

## 📄 License

MIT License - Free for local use.
