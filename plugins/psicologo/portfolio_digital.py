#!/usr/bin/env python3
"""Portfolio digital do psicologo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/portfolio", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "portfolio_psicologo", "status": "ativo",
                          "descricao": "Portfolio digital do psicologo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "portfolio_psicologo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
