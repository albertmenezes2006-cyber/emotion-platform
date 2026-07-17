#!/usr/bin/env python3
"""Prevenção ao bullying"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bullying", tags=["Escola"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bullying_prev", "status": "ativo",
                          "descricao": "Prevenção ao bullying",
                          "versao": "1.0.0",
                          "categoria": "escola",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bullying_prev"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
