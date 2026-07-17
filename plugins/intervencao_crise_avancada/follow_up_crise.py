#!/usr/bin/env python3
"""Follow Up Crise em intervencao crise avancada"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencao_cri/follow_up_crise", tags=["intervencao_crise_avancada"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencao_crise_av_follow_up_crise","status":"ativo","desc":"Follow Up Crise em intervencao crise avancada","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencao_crise_av_follow_up_crise"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
