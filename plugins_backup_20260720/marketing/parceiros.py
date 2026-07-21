#!/usr/bin/env python3
"""Página de parceiros"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/parceiros", tags=["parceiros"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "parceiros", "status": "ativo",
                          "descricao": "Página de parceiros",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "parceiros"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
