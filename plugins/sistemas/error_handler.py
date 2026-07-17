#!/usr/bin/env python3
"""Handler de erros global"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/errors", tags=["error_handler"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "error_handler", "status": "ativo",
                          "descricao": "Handler de erros global",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "error_handler"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
