#!/usr/bin/env python3
"""Depression Elder2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/depression_elder2", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_depression_elder2","s":"ativo","d":"Depression Elder2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_depression_elder2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
