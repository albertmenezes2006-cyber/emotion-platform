#!/usr/bin/env python3
"""AR realidade aumentada saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ar-mental", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ar_saude_mental", "status": "ativo",
                          "descricao": "AR realidade aumentada saúde mental",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ar_saude_mental",
                          "descricao": "AR realidade aumentada saúde mental",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ar_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
