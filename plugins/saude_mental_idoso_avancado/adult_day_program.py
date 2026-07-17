#!/usr/bin/env python3
"""Adult Day Program"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/adult_day_program", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_adult_day_program","s":"ativo","d":"Adult Day Program","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_adult_day_program"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
