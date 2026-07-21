#!/usr/bin/env python3
"""Landing page para clínicas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/para-clinicas", tags=["landing_clinicas"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "landing_clinicas", "status": "ativo",
                          "descricao": "Landing page para clínicas",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "landing_clinicas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
