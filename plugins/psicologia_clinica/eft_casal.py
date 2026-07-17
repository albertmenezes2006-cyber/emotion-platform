#!/usr/bin/env python3
"""Eft Casal em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/eft_casal", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_eft_casal","status":"ativo","desc":"Eft Casal em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_eft_casal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
