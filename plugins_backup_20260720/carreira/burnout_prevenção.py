#!/usr/bin/env python3
"""Prevenção de burnout na carreira"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/burnout-prev", tags=["Carreira"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "burnout_prev_career", "status": "ativo",
                          "descricao": "Prevenção de burnout na carreira",
                          "versao": "1.0.0",
                          "categoria": "carreira",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "burnout_prev_career"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
