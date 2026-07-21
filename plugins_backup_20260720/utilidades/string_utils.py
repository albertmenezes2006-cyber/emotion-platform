#!/usr/bin/env python3
"""Utilitários de strings"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/strings", tags=["string_utils"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "string_utils", "status": "ativo",
                          "descricao": "Utilitários de strings",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "string_utils"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
