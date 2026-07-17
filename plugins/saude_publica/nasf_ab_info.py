#!/usr/bin/env python3
"""NASF-AB informações"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/nasf", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "nasf_ab_info", "status": "ativo",
                          "descricao": "NASF-AB informações",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "nasf_ab_info",
                          "descricao": "NASF-AB informações",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "nasf_ab_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
