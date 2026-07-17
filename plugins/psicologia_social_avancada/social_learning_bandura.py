#!/usr/bin/env python3
"""Social Learning Bandura"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/social_learning_bandura", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__social_learning_bandura","s":"ativo","d":"Social Learning Bandura","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__social_learning_bandura"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
