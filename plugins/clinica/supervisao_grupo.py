#!/usr/bin/env python3
"""Supervisão em grupo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/supervisao-grupo", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "supervisao_grupo", "status": "ativo",
                          "descricao": "Supervisão em grupo",
                          "versao": "1.0.0",
                          "categoria": "clinica",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "supervisao_grupo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
