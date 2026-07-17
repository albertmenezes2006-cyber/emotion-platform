#!/usr/bin/env python3
"""Terapia Luto2 em relacionamentos2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relacionamentos/terapia_luto2", tags=["relacionamentos2"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relacionamentos2_terapia_luto2", "status": "ativo",
                          "descricao": "Terapia Luto2 em relacionamentos2", "categoria": "relacionamentos2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relacionamentos2_terapia_luto2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
