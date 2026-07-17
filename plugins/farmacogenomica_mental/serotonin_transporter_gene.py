#!/usr/bin/env python3
"""Serotonin Transporter Gene"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/serotonin_transporter_gene", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_serotonin_transporter_gen","s":"ativo","d":"Serotonin Transporter Gene","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_serotonin_transporter_gen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
