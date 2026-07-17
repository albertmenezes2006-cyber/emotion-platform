#!/usr/bin/env python3
"""Tentativa Familia em relacionamentos2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relacionamentos/tentativa_familia", tags=["relacionamentos2"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relacionamentos2_tentativa_familia", "status": "ativo",
                          "descricao": "Tentativa Familia em relacionamentos2", "categoria": "relacionamentos2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relacionamentos2_tentativa_familia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
