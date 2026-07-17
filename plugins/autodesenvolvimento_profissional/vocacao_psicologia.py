#!/usr/bin/env python3
"""Vocacao Psicologia em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/vocacao_psicologia", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__vocacao_psicologia","status":"ativo","desc":"Vocacao Psicologia em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__vocacao_psicologia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
