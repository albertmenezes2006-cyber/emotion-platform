#!/usr/bin/env python3
"""Rey Auditory Verbal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/rey_auditory_verbal", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_rey_auditory_verbal","s":"ativo","d":"Rey Auditory Verbal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_rey_auditory_verbal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
