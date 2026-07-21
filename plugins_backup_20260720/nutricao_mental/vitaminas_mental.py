#!/usr/bin/env python3
"""Vitaminas e minerais para saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/vitaminas", tags=["Nutricao Mental"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "vitaminas_mental", "status": "ativo",
                          "descricao": "Vitaminas e minerais para saúde mental",
                          "versao": "1.0.0",
                          "categoria": "nutricao_mental",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "vitaminas_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
