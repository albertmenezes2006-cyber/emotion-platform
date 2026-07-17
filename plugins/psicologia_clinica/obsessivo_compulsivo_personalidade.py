#!/usr/bin/env python3
"""Obsessivo Compulsivo Personalidade em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/obsessivo_compulsivo_personali", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_obsessivo_compulsivo_pers","status":"ativo","desc":"Obsessivo Compulsivo Personalidade em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_obsessivo_compulsivo_pers"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
