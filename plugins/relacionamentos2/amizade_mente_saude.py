#!/usr/bin/env python3
"""Amizade Mente Saude em relacionamentos2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relacionamentos/amizade_mente_saude", tags=["relacionamentos2"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relacionamentos2_amizade_mente_saude", "status": "ativo",
                          "descricao": "Amizade Mente Saude em relacionamentos2", "categoria": "relacionamentos2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relacionamentos2_amizade_mente_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
