#!/usr/bin/env python3
"""CECos consultoria e apoio"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cecos", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cecos_consultoria", "status": "ativo",
                          "descricao": "CECos consultoria e apoio",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cecos_consultoria",
                          "descricao": "CECos consultoria e apoio",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cecos_consultoria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
