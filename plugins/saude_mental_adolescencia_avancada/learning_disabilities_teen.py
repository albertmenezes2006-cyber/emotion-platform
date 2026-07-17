#!/usr/bin/env python3
"""Learning Disabilities Teen"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/learning_disabilities_teen", tags=["saude_mental_adolescencia_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_adole_learning_disabilities_tee","s":"ativo","d":"Learning Disabilities Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_adole_learning_disabilities_tee"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
