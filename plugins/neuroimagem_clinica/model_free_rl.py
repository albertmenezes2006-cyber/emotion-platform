#!/usr/bin/env python3
"""Model Free Rl"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/model_free_rl", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_model_free_rl","s":"ativo","d":"Model Free Rl","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_model_free_rl"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
