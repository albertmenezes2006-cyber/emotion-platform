#!/usr/bin/env python3
"""Training Transfer"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/training_transfer", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_training_transfer","s":"ativo","d":"Training Transfer","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_training_transfer"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
