#!/usr/bin/env python3
"""Apego Desorganizado Clinico em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/apego_desorganizado_clinico", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_apego_desorganizado_clini","status":"ativo","desc":"Apego Desorganizado Clinico em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_apego_desorganizado_clini"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
