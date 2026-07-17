#!/usr/bin/env python3
"""Picture Completion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/picture_completion", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_picture_completion","s":"ativo","d":"Picture Completion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_picture_completion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
