#!/usr/bin/env python3
"""Person Organization Fit"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/person_organization_fit", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_person_organization_fit","s":"ativo","d":"Person Organization Fit","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_person_organization_fit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
