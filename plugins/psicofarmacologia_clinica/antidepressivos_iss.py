#!/usr/bin/env python3
"""Antidepressivos Iss em psicofarmacologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofarmacolog/antidepressivos_iss", tags=["psicofarmacologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicofarmacologia_cl_antidepressivos_iss","status":"ativo","desc":"Antidepressivos Iss em psicofarmacologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofarmacologia_cl_antidepressivos_iss"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
