#!/usr/bin/env python3
"""Task Agreement"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/task_agreement", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_task_agreement","s":"ativo","d":"Task Agreement","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_task_agreement"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
