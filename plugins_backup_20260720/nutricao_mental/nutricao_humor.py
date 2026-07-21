#!/usr/bin/env python3
"""Nutrição e impacto no humor"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/nutricao-humor", tags=["Nutricao Mental"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "nutricao_humor", "status": "ativo",
                          "descricao": "Nutrição e impacto no humor",
                          "versao": "1.0.0",
                          "categoria": "nutricao_mental",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "nutricao_humor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
