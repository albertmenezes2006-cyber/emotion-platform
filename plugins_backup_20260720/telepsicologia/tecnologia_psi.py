#!/usr/bin/env python3
"""Tecnologia para psicólogos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tec-psi", tags=["Telepsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tecnologia_psi", "status": "ativo",
                          "descricao": "Tecnologia para psicólogos",
                          "versao": "1.0.0",
                          "categoria": "telepsicologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tecnologia_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
