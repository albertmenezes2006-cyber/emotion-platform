#!/usr/bin/env python3
"""Non Directive Play"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/non_directive_play", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_non_directive_play","s":"ativo","d":"Non Directive Play","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_non_directive_play"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
