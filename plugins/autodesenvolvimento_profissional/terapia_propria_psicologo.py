#!/usr/bin/env python3
"""Terapia Propria Psicologo em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/terapia_propria_psicologo", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__terapia_propria_psicologo","status":"ativo","desc":"Terapia Propria Psicologo em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__terapia_propria_psicologo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
