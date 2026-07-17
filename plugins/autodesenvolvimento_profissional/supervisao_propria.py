#!/usr/bin/env python3
"""Supervisao Propria em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/supervisao_propria", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__supervisao_propria","status":"ativo","desc":"Supervisao Propria em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__supervisao_propria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
