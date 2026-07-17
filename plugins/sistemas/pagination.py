#!/usr/bin/env python3
"""Sistema de paginação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/paginar", tags=["paginacao"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "paginacao", "status": "ativo",
                          "descricao": "Sistema de paginação",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "paginacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
