#!/usr/bin/env python3
"""Jet Lag Mental em neurociencia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurociencia_cl/jet_lag_mental", tags=["neurociencia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"neurociencia_clinica_jet_lag_mental","status":"ativo","desc":"Jet Lag Mental em neurociencia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_clinica_jet_lag_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
