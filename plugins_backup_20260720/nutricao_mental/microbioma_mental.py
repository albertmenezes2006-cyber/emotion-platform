#!/usr/bin/env python3
"""Microbioma intestinal e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/microbioma", tags=["Nutricao Mental"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "microbioma_gut", "status": "ativo",
                          "descricao": "Microbioma intestinal e saúde mental",
                          "versao": "1.0.0",
                          "categoria": "nutricao_mental",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "microbioma_gut"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
