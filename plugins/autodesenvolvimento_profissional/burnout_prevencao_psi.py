#!/usr/bin/env python3
"""Burnout Prevencao Psi em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/burnout_prevencao_psi", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__burnout_prevencao_psi","status":"ativo","desc":"Burnout Prevencao Psi em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__burnout_prevencao_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
