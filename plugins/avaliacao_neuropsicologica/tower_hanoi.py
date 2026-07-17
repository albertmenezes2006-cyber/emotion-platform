#!/usr/bin/env python3
"""Tower Hanoi"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/tower_hanoi", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_tower_hanoi","s":"ativo","d":"Tower Hanoi","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_tower_hanoi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
