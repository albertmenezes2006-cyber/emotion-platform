#!/usr/bin/env python3
"""DSM-5 critérios diagnósticos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dsm5", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dsm5_criterios", "status": "ativo",
                          "descricao": "DSM-5 critérios diagnósticos",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dsm5_criterios",
                          "descricao": "DSM-5 critérios diagnósticos",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dsm5_criterios"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
