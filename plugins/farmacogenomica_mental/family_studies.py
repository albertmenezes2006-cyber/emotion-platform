#!/usr/bin/env python3
"""Family Studies"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/family_studies", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_family_studies","s":"ativo","d":"Family Studies","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_family_studies"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
