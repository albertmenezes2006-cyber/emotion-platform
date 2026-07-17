#!/usr/bin/env python3
"""GEIH internação hospitalar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/geih", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "geih_internacao", "status": "ativo",
                          "descricao": "GEIH internação hospitalar",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "geih_internacao",
                          "descricao": "GEIH internação hospitalar",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "geih_internacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
