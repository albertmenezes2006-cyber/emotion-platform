#!/usr/bin/env python3
"""Diffusion Responsibility"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_s/diffusion_responsibility", tags=["psicologia_social_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_social__diffusion_responsibility","s":"ativo","d":"Diffusion Responsibility","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_social__diffusion_responsibility"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
