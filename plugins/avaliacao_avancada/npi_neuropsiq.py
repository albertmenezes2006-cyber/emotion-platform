#!/usr/bin/env python3
"""NPI inventário neuropsiquiátrico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/npi", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "npi_neuropsiq", "status": "ativo",
                          "descricao": "NPI inventário neuropsiquiátrico",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "npi_neuropsiq",
                          "descricao": "NPI inventário neuropsiquiátrico",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "npi_neuropsiq"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
