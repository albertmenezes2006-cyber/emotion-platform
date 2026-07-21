#!/usr/bin/env python3
"""e-Saúde mental no Brasil"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/e-saude", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "e_saude_mental", "status": "ativo",
                          "descricao": "e-Saúde mental no Brasil",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "e_saude_mental",
                          "descricao": "e-Saúde mental no Brasil",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "e_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
