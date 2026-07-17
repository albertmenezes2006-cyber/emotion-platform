#!/usr/bin/env python3
"""Cursos Pos Graduacao em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/cursos_pos_graduacao", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__cursos_pos_graduacao","status":"ativo","desc":"Cursos Pos Graduacao em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__cursos_pos_graduacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
