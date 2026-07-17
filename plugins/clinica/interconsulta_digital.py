#!/usr/bin/env python3
"""Interconsulta digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/interconsulta", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "interconsulta", "status": "ativo",
                          "descricao": "Interconsulta digital",
                          "versao": "1.0.0",
                          "categoria": "clinica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "interconsulta"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
