#!/usr/bin/env python3
"""AA e grupos de doze passos info"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/aa-info", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grupo_AA_info", "status": "ativo",
                          "descricao": "AA e grupos de doze passos info",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grupo_AA_info",
                          "descricao": "AA e grupos de doze passos info",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grupo_AA_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
