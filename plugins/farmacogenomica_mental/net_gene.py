#!/usr/bin/env python3
"""Net Gene"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/net_gene", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_net_gene","s":"ativo","d":"Net Gene","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_net_gene"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
