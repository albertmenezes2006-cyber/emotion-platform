#!/usr/bin/env python3
"""Info do pool de banco"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/db-info", tags=["db_pool_info"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "db_pool_info", "status": "ativo",
                          "descricao": "Info do pool de banco",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "db_pool_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
