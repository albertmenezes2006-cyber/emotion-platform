#!/usr/bin/env python3
"""Theory Mind Development"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/theory_mind_development", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_theory_mind_development","s":"ativo","d":"Theory Mind Development","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_theory_mind_development"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
