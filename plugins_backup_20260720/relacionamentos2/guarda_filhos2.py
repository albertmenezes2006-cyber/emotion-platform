#!/usr/bin/env python3
"""Guarda Filhos2 em relacionamentos2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relacionamentos/guarda_filhos2", tags=["relacionamentos2"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relacionamentos2_guarda_filhos2", "status": "ativo",
                          "descricao": "Guarda Filhos2 em relacionamentos2", "categoria": "relacionamentos2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relacionamentos2_guarda_filhos2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
