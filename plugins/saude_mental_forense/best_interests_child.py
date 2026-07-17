#!/usr/bin/env python3
"""Best Interests Child"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/best_interests_child", tags=["saude_mental_forense"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_foren_best_interests_child","s":"ativo","d":"Best Interests Child","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_foren_best_interests_child"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
