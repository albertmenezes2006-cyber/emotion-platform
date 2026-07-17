#!/usr/bin/env python3
"""Dual Task Assessment"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/dual_task_assessment", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_dual_task_assessment","s":"ativo","d":"Dual Task Assessment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_dual_task_assessment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
