#!/usr/bin/env python3
"""Normas CFP para telepsicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cfp-normas", tags=["Telepsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cfp_normas_tele", "status": "ativo",
                          "descricao": "Normas CFP para telepsicologia",
                          "versao": "1.0.0",
                          "categoria": "telepsicologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cfp_normas_tele"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
