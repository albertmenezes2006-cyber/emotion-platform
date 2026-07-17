#!/usr/bin/env python3
"""Person Group Fit"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/person_group_fit", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_person_group_fit","s":"ativo","d":"Person Group Fit","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_person_group_fit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
