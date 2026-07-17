#!/usr/bin/env python3
"""Weight Concerns Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/weight_concerns_teen", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_weight_concerns_teen","s":"ativo","d":"Weight Concerns Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_weight_concerns_teen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
