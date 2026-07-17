#!/usr/bin/env python3
"""Abpmc Participacao em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/abpmc_participacao", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__abpmc_participacao","status":"ativo","desc":"Abpmc Participacao em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__abpmc_participacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
