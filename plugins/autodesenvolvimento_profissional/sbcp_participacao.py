#!/usr/bin/env python3
"""Sbcp Participacao em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/sbcp_participacao", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__sbcp_participacao","status":"ativo","desc":"Sbcp Participacao em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__sbcp_participacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
