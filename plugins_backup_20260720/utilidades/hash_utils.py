#!/usr/bin/env python3
"""Utilitários de hash"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/hash", tags=["hash_utils"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "hash_utils", "status": "ativo",
                          "descricao": "Utilitários de hash",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "hash_utils"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
