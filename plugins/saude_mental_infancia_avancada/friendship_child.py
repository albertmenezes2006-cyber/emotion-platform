#!/usr/bin/env python3
"""Friendship Child"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/friendship_child", tags=["saude_mental_infancia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_infan_friendship_child","s":"ativo","d":"Friendship Child","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_infan_friendship_child"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
