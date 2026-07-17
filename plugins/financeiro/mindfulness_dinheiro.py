#!/usr/bin/env python3
"""Mindfulness com dinheiro"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mindful-money", tags=["Financeiro"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mindful_money", "status": "ativo",
                          "descricao": "Mindfulness com dinheiro",
                          "versao": "1.0.0",
                          "categoria": "financeiro",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mindful_money"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
