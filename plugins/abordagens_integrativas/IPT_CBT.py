#!/usr/bin/env python3
"""Ipt Cbt"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/IPT_CBT", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_IPT_CBT","s":"ativo","d":"Ipt Cbt","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_IPT_CBT"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
