#!/usr/bin/env python3
"""SCL-90-R Sintomas psicopatológicos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/scl90", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "scl90r_sintomas", "status": "ativo",
                          "descricao": "SCL-90-R Sintomas psicopatológicos",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "scl90r_sintomas",
                          "descricao": "SCL-90-R Sintomas psicopatológicos",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "scl90r_sintomas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
