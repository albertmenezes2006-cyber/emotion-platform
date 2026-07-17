#!/usr/bin/env python3
"""Logoterapia Frankl digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/logoterapia", tags=["Espiritualidade"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "logoterapia", "status": "ativo",
                          "descricao": "Logoterapia Frankl digital",
                          "versao": "1.0.0",
                          "categoria": "espiritualidade",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "logoterapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
