#!/usr/bin/env python3
"""Multi Trait Multi Method em tecnicas avaliacao"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/tecnicas_avalia/multi_trait_multi_method", tags=["tecnicas_avaliacao"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"tecnicas_avaliacao_multi_trait_multi_method","status":"ativo","desc":"Multi Trait Multi Method em tecnicas avaliacao","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "tecnicas_avaliacao_multi_trait_multi_method"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
