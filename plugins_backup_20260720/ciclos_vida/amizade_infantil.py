#!/usr/bin/env python3
"""Amizade Infantil em ciclos vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ciclos_vida/amizade_infantil", tags=["ciclos_vida"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ciclos_vida_amizade_infantil", "status": "ativo",
                          "descricao": "Amizade Infantil em ciclos vida", "categoria": "ciclos_vida",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ciclos_vida_amizade_infantil"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
