# IBKR MCP Server

This project is a **secure** FastAPI application that interacts with the Interactive Brokers (IBKR) API to fetch portfolio details.

## 🔒 Security Features

This application has been security-hardened and includes:

- ✅ **API Key Authentication** - All endpoints require valid authentication
- ✅ **Rate Limiting** - Protection against abuse and DoS attacks  
- ✅ **Input Validation** - Pydantic models for request validation
- ✅ **CORS Security** - Configurable cross-origin request handling
- ✅ **Security Headers** - HSTS, XSS protection, content type options
- ✅ **Error Sanitization** - Prevents information disclosure in error messages
- ✅ **HTTPS Support** - SSL/TLS configuration for production
- ✅ **Secure Configuration** - Environment-based configuration management

## Project Structure

```
ibkr-mcp-server
├── app
│   ├── __init__.py
│   ├── main.py                    # FastAPI app with security middleware
│   ├── api
│   │   ├── __init__.py
│   │   └── endpoints
│   │       ├── __init__.py
│   │       └── portfolio.py       # Secured portfolio endpoints
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py             # Configuration management
│   │   └── security.py           # Security utilities and authentication
│   ├── models
│   │   ├── __init__.py
│   │   ├── portfolio.py          # Portfolio data models
│   │   └── requests.py           # Request validation models
│   └── services
│       ├── __init__.py
│       └── ibkr_service.py       # IBKR integration service
├── tests
│   ├── __init__.py
│   └── test_security.py          # Security tests
├── requirements.txt               # Updated with security dependencies
├── .env                          # Development environment (secure permissions)
├── .env.production              # Production environment template
├── .gitignore                   # Security-aware gitignore
├── SECURITY_ANALYSIS_REPORT.md  # Comprehensive security analysis
└── README.md
```

## 🚀 Setup Instructions

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
   ```bash
   # Copy and configure environment file
   cp .env .env.local
   # Edit .env.local with your actual credentials
   ```

   **Required Environment Variables:**
   ```env
   API_KEY=your_secure_api_key_here
   IBKR_HOST=127.0.0.1
   IBKR_PORT=7496
   ENVIRONMENT=development  # or production
   ```

5. **Secure file permissions:**
   ```bash
   chmod 600 .env .env.local .env.production
   ```

6. **Run the application:**
   ```bash
   # Development
   uvicorn app.main:app --reload
   
   # Production
   uvicorn app.main:app --host 0.0.0.0 --port 443 --ssl-keyfile=key.pem --ssl-certfile=cert.pem
   ```

## 🔐 Authentication

All API endpoints (except health check) require authentication using Bearer tokens:

```bash
curl -H "Authorization: Bearer your_api_key" http://localhost:8000/api/v1/portfolio
```

## 📊 API Endpoints

### Health Check (No Auth Required)
```
GET /api/v1/health
```

### Portfolio Data (Auth Required)
```
GET /api/v1/portfolio
Authorization: Bearer <your_api_key>

Query Parameters:
- account_id (optional): Specific account ID
- include_positions (boolean): Include position details (default: true)
- include_summary (boolean): Include account summary (default: true)
```

## 🧪 Testing

Run security tests:
```bash
pip install pytest
pytest tests/test_security.py -v
```

## 🔒 Security Configuration

### Production Deployment

1. **Use HTTPS Only:**
   ```env
   ENVIRONMENT=production
   SSL_KEYFILE=/path/to/key.pem
   SSL_CERTFILE=/path/to/cert.pem
   ```

2. **Configure CORS:**
   ```env
   ALLOWED_ORIGINS=https://yourdomain.com,https://api.yourdomain.com
   ```

3. **Set Strong API Keys:**
   ```env
   API_KEY=your_long_random_secure_api_key_here
   ```

4. **Secure File Permissions:**
   ```bash
   chmod 600 .env.production
   chown app:app .env.production
   ```

### Security Best Practices

- 🔑 Use strong, unique API keys
- 🔒 Always use HTTPS in production
- 🚫 Never commit secrets to version control
- 📊 Monitor and log security events
- 🔄 Regularly update dependencies
- 🧪 Run security tests in CI/CD

## 📈 Monitoring

The application includes built-in security monitoring:

- Request logging with sanitized error messages
- Rate limiting with configurable thresholds
- Security headers for all responses
- Input validation on all endpoints

## 🐛 Security Issues

If you discover a security vulnerability, please email the security team directly rather than opening a public issue.

## 📋 Security Checklist

- [x] Authentication implemented
- [x] Input validation on all endpoints
- [x] Rate limiting configured
- [x] CORS properly configured
- [x] HTTPS support implemented
- [x] Security headers implemented
- [x] Error handling doesn't expose internal details
- [x] Environment variables used for configuration
- [x] No hardcoded secrets in code
- [x] Security testing implemented
- [ ] Dependency vulnerability scanning (recommended)
- [ ] Production monitoring setup (recommended)

## 📄 License

This project is licensed under the MIT License.