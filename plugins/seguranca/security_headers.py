#!/usr/bin/env python3
"""Security headers — proteção avançada"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from starlette.middleware.base import BaseHTTPMiddleware

router = APIRouter(prefix="/api/v1/security-headers", tags=["Security"])

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=(self)"
        )
        response.headers["Strict-Transport-Security"] = (
            "max-age=31536000; includeSubDomains"
        )
        return response

@router.get("/check")
async def check_headers():
    return {
        "headers_ativos": [
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Referrer-Policy",
            "Permissions-Policy",
            "Strict-Transport-Security"
        ],
        "status": "protegido"
    }

class SecurityHeadersPlugin(PluginBase):
    name = "security_headers"
    def setup(self, app):
        app.add_middleware(SecurityHeadersMiddleware)
        app.include_router(router)

plugin = SecurityHeadersPlugin()
