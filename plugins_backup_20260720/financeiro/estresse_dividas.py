#!/usr/bin/env python3
"""Manejo do estresse com dívidas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dividas", tags=["Financeiro"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "estresse_dividas", "status": "ativo",
                          "descricao": "Manejo do estresse com dívidas",
                          "versao": "1.0.0",
                          "categoria": "financeiro",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "estresse_dividas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
