#!/usr/bin/env python3
"""Psicoestimulantes Tdah em psicofarmacologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofarmacolog/psicoestimulantes_tdah", tags=["psicofarmacologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicofarmacologia_cl_psicoestimulantes_tdah","status":"ativo","desc":"Psicoestimulantes Tdah em psicofarmacologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofarmacologia_cl_psicoestimulantes_tdah"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
