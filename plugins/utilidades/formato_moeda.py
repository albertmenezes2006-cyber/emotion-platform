#!/usr/bin/env python3
"""Formatação de moeda BRL"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/moeda", tags=["formato_moeda"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "formato_moeda", "status": "ativo",
                          "descricao": "Formatação de moeda BRL",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "formato_moeda"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
