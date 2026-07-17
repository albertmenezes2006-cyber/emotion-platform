#!/usr/bin/env python3
"""Representacoes Mentais em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/representacoes_mentais", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_representacoes_mentais","status":"ativo","desc":"Representacoes Mentais em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_representacoes_mentais"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
