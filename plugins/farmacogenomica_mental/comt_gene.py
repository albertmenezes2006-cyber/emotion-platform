#!/usr/bin/env python3
"""Comt Gene"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/comt_gene", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_comt_gene","s":"ativo","d":"Comt Gene","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_comt_gene"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
