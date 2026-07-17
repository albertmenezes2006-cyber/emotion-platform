#!/usr/bin/env python3
"""Recursos em LIBRAS"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/libras", tags=["Diversidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "acessivel_surdos", "status": "ativo",
                          "descricao": "Recursos em LIBRAS",
                          "versao": "1.0.0",
                          "categoria": "diversidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "acessivel_surdos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
