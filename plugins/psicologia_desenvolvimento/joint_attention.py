#!/usr/bin/env python3
"""Joint Attention"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/joint_attention", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_joint_attention","s":"ativo","d":"Joint Attention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_joint_attention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
