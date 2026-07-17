#!/usr/bin/env python3
"""Leitura Profissional em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/leitura_profissional", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__leitura_profissional","status":"ativo","desc":"Leitura Profissional em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__leitura_profissional"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
