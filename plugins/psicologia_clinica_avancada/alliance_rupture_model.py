#!/usr/bin/env python3
"""Alliance Rupture Model"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/alliance_rupture_model", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_alliance_rupture_model","s":"ativo","d":"Alliance Rupture Model","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_alliance_rupture_model"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
