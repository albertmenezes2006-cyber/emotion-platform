#!/usr/bin/env python3
"""Avaliação de luto complicado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/luto-complicado", tags=["Luto"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "luto_complicado", "status": "ativo",
                          "descricao": "Avaliação de luto complicado",
                          "versao": "1.0.0",
                          "categoria": "luto",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "luto_complicado"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
