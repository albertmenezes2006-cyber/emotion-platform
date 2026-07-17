#!/usr/bin/env python3
"""Adoption Studies"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/adoption_studies", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_adoption_studies","s":"ativo","d":"Adoption Studies","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_adoption_studies"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
