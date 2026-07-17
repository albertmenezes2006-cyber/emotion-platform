#!/usr/bin/env python3
"""Consentimento em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/consentimento", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "consentimento_mental", "status": "ativo",
                          "descricao": "Consentimento em saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "consentimento_mental",
                          "descricao": "Consentimento em saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "consentimento_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
