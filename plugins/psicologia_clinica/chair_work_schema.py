#!/usr/bin/env python3
"""Chair Work Schema em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/chair_work_schema", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_chair_work_schema","status":"ativo","desc":"Chair Work Schema em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_chair_work_schema"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
