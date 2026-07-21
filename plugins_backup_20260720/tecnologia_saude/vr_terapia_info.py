#!/usr/bin/env python3
"""VR terapia realidade virtual"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/vr-terapia", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "vr_terapia_info", "status": "ativo",
                          "descricao": "VR terapia realidade virtual",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "vr_terapia_info",
                          "descricao": "VR terapia realidade virtual",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "vr_terapia_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
