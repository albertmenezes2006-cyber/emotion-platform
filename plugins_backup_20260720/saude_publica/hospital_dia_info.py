#!/usr/bin/env python3
"""Hospital Dia informações"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/hospital-dia", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "hospital_dia_info", "status": "ativo",
                          "descricao": "Hospital Dia informações",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "hospital_dia_info",
                          "descricao": "Hospital Dia informações",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "hospital_dia_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
