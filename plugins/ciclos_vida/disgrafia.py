#!/usr/bin/env python3
"""Disgrafia em ciclos vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ciclos_vida/disgrafia", tags=["ciclos_vida"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ciclos_vida_disgrafia", "status": "ativo",
                          "descricao": "Disgrafia em ciclos vida", "categoria": "ciclos_vida",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ciclos_vida_disgrafia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
