#!/usr/bin/env python3
"""Testamento Vital2 em ciclos vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ciclos_vida/testamento_vital2", tags=["ciclos_vida"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ciclos_vida_testamento_vital2", "status": "ativo",
                          "descricao": "Testamento Vital2 em ciclos vida", "categoria": "ciclos_vida",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ciclos_vida_testamento_vital2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
