#!/usr/bin/env python3
"""Double Loop Learning"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/double_loop_learning", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_double_loop_learning","s":"ativo","d":"Double Loop Learning","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_double_loop_learning"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
