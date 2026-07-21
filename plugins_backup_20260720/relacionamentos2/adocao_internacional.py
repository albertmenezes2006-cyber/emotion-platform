#!/usr/bin/env python3
"""Adocao Internacional em relacionamentos2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relacionamentos/adocao_internacional", tags=["relacionamentos2"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "relacionamentos2_adocao_internacional", "status": "ativo",
                          "descricao": "Adocao Internacional em relacionamentos2", "categoria": "relacionamentos2",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "relacionamentos2_adocao_internacional"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
