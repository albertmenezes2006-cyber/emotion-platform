#!/usr/bin/env python3
"""Talk In Interaction"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/talk_in_interaction", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_talk_in_interaction","s":"ativo","d":"Talk In Interaction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_talk_in_interaction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
