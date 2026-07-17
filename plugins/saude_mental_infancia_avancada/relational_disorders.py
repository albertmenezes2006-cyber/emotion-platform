#!/usr/bin/env python3
"""Relational Disorders"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/relational_disorders", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_relational_disorders","s":"ativo","d":"Relational Disorders","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_relational_disorders"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
