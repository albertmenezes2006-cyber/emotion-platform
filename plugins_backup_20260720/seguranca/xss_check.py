from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from starlette.middleware.base import BaseHTTPMiddleware

class XSSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

router = APIRouter(prefix="/api/v1/xss", tags=["Seguranca"])

@router.get("/check")
async def check():
    return JSONResponse({"xss_protection": "ativo", "headers": ["X-XSS-Protection", "X-Content-Type-Options"]})

class Plugin(PluginBase):
    name = "xss_check_endpoint"
    def setup(self, app):
        app.add_middleware(XSSMiddleware)
        app.include_router(router)

plugin = Plugin()
