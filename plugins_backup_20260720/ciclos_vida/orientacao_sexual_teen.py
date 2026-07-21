#!/usr/bin/env python3
"""Orientacao Sexual Teen em ciclos vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ciclos_vida/orientacao_sexual_teen", tags=["ciclos_vida"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ciclos_vida_orientacao_sexual_teen", "status": "ativo",
                          "descricao": "Orientacao Sexual Teen em ciclos vida", "categoria": "ciclos_vida",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ciclos_vida_orientacao_sexual_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
