#!/usr/bin/env python3
"""Late Life Spirituality"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/late_life_spirituality", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_late_life_spirituality","s":"ativo","d":"Late Life Spirituality","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_late_life_spirituality"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
