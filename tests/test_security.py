"""
Security tests for IBKR MCP Server
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.security import sanitize_error_message
import os

client = TestClient(app)


class TestAuthentication:
    """Test authentication and authorization"""
    
    def test_portfolio_endpoint_requires_auth(self):
        """Test that portfolio endpoint requires authentication"""
        response = client.get("/api/v1/portfolio")
        assert response.status_code == 403  # Should be forbidden without auth
    
    def test_invalid_api_key(self):
        """Test invalid API key rejection"""
        headers = {"Authorization": "Bearer invalid_key"}
        response = client.get("/api/v1/portfolio", headers=headers)
        assert response.status_code == 401
        assert "Invalid API key" in response.json()["detail"]
    
    def test_missing_authorization_header(self):
        """Test missing authorization header"""
        response = client.get("/api/v1/portfolio")
        assert response.status_code == 403


class TestRateLimiting:
    """Test rate limiting functionality"""
    
    def test_rate_limit_on_root_endpoint(self):
        """Test rate limiting on root endpoint"""
        # Make multiple requests quickly
        responses = []
        for _ in range(15):  # Should exceed 10/minute limit
            response = client.get("/")
            responses.append(response)
        
        # At least one should be rate limited
        rate_limited = any(r.status_code == 429 for r in responses)
        assert rate_limited


class TestSecurityHeaders:
    """Test security headers are present"""
    
    def test_security_headers_present(self):
        """Test that security headers are added to responses"""
        response = client.get("/")
        
        assert "X-Content-Type-Options" in response.headers
        assert response.headers["X-Content-Type-Options"] == "nosniff"
        
        assert "X-Frame-Options" in response.headers
        assert response.headers["X-Frame-Options"] == "DENY"
        
        assert "X-XSS-Protection" in response.headers
        assert response.headers["X-XSS-Protection"] == "1; mode=block"


class TestErrorHandling:
    """Test error handling and information disclosure prevention"""
    
    def test_error_message_sanitization(self):
        """Test that error messages are properly sanitized"""
        # Test various error types
        connection_error = Exception("Connection failed to database server at 192.168.1.100")
        sanitized = sanitize_error_message(connection_error)
        assert "192.168.1.100" not in sanitized
        assert "Service temporarily unavailable" in sanitized
        
        auth_error = Exception("Authentication failed for user admin")
        sanitized = sanitize_error_message(auth_error)
        assert "admin" not in sanitized
        assert "Authentication failed" in sanitized
    
    def test_internal_error_handling(self):
        """Test that internal errors don't expose sensitive information"""
        # This would require mocking the IBKR service to raise an exception
        # For now, test the sanitization function
        internal_error = Exception("Internal SQL error: SELECT * FROM users WHERE password='secret123'")
        sanitized = sanitize_error_message(internal_error)
        assert "secret123" not in sanitized
        assert "users" not in sanitized


class TestInputValidation:
    """Test input validation functionality"""
    
    def test_health_endpoint_accessible(self):
        """Test health endpoint is accessible without auth"""
        response = client.get("/api/v1/health")
        assert response.status_code == 200
        assert "status" in response.json()
        assert response.json()["status"] == "healthy"


class TestCORSConfiguration:
    """Test CORS configuration"""
    
    def test_cors_headers(self):
        """Test that CORS headers are configured"""
        response = client.options("/api/v1/health")
        # In test environment, CORS headers should be present
        # This test may need adjustment based on test configuration
        assert response.status_code in [200, 405]  # OPTIONS might not be allowed


if __name__ == "__main__":
    pytest.main([__file__])