#!/usr/bin/env python3
"""California Verbal Learning"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/california_verbal_learning", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_california_verbal_learnin","s":"ativo","d":"California Verbal Learning","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_california_verbal_learnin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
