#!/usr/bin/env python3
"""Social Brain Autism"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiologi/social_brain_autism", tags=["neurobiologia_transtornos"])
@router.get("")
async def info():
    return JSONResponse({"p":"neurobiologia_tran_social_brain_autism","s":"ativo","d":"Social Brain Autism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_tran_social_brain_autism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
