#!/usr/bin/env python3
"""Fotos Memorias Luto em relacionamentos2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relacionamentos/fotos_memorias_luto", tags=["relacionamentos2"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relacionamentos2_fotos_memorias_luto", "status": "ativo",
                          "descricao": "Fotos Memorias Luto em relacionamentos2", "categoria": "relacionamentos2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relacionamentos2_fotos_memorias_luto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
