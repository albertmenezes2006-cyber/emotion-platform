#!/usr/bin/env python3
"""Efeito Werther em intervencao crise avancada"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervencao_cri/efeito_werther", tags=["intervencao_crise_avancada"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"intervencao_crise_av_efeito_werther","status":"ativo","desc":"Efeito Werther em intervencao crise avancada","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencao_crise_av_efeito_werther"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
