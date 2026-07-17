#!/usr/bin/env python3
"""Motherwort Coracao em saude integrativa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/saude_integrati/motherwort_coracao", tags=["saude_integrativa"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_integrativa_motherwort_coracao", "status": "ativo",
                          "descricao": "Motherwort Coracao em saude integrativa", "categoria": "saude_integrativa",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_integrativa_motherwort_coracao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
