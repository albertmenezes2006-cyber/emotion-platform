#!/usr/bin/env python3
"""Parent Child Therapy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/parent_child_therapy", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_parent_child_therapy","s":"ativo","d":"Parent Child Therapy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_parent_child_therapy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
