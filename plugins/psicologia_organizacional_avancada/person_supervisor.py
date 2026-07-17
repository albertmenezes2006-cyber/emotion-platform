#!/usr/bin/env python3
"""Person Supervisor"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/person_supervisor", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_person_supervisor","s":"ativo","d":"Person Supervisor","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_person_supervisor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
