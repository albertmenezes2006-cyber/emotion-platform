#!/usr/bin/env python3
"""Suporte no divórcio"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/divorcio", tags=["Familia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "divorcio_suporte", "status": "ativo",
                          "descricao": "Suporte no divórcio",
                          "versao": "1.0.0",
                          "categoria": "familia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "divorcio_suporte"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
