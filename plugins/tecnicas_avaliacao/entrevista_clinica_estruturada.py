#!/usr/bin/env python3
"""Entrevista Clinica Estruturada em tecnicas avaliacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/tecnicas_avalia/entrevista_clinica_estruturada", tags=["tecnicas_avaliacao"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"tecnicas_avaliacao_entrevista_clinica_estrut","status":"ativo","desc":"Entrevista Clinica Estruturada em tecnicas avaliacao","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "tecnicas_avaliacao_entrevista_clinica_estrut"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
