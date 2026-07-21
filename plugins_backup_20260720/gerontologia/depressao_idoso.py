#!/usr/bin/env python3
"""Depressão no idoso GDS"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dep-idoso", tags=["Gerontologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "depressao_idoso", "status": "ativo",
                          "descricao": "Depressão no idoso GDS",
                          "versao": "1.0.0",
                          "categoria": "gerontologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "depressao_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
