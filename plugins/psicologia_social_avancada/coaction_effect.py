#!/usr/bin/env python3
"""Coaction Effect"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/coaction_effect", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__coaction_effect","s":"ativo","d":"Coaction Effect","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__coaction_effect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
