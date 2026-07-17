#!/usr/bin/env python3
"""Parents As Teachers"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/parents_as_teachers", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_parents_as_teachers","s":"ativo","d":"Parents As Teachers","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_parents_as_teachers"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
