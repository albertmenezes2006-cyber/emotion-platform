#!/usr/bin/env python3
"""Dat Gene"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/dat_gene", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_dat_gene","s":"ativo","d":"Dat Gene","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_dat_gene"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
