#!/usr/bin/env python3
"""Body Awareness Training"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapias_cor/body_awareness_training", tags=["terapias_corpo_mente"])
@router.get("")
async def info():
    return JSONResponse({"p":"terapias_corpo_men_body_awareness_training","s":"ativo","d":"Body Awareness Training","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapias_corpo_men_body_awareness_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
