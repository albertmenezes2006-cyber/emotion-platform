#!/usr/bin/env python3
"""Modos Esquema em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/modos_esquema", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_modos_esquema","status":"ativo","desc":"Modos Esquema em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_modos_esquema"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
