#!/usr/bin/env python3
"""Theta Gamma Coupling"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/theta_gamma_coupling", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_theta_gamma_coupling","s":"ativo","d":"Theta Gamma Coupling","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_theta_gamma_coupling"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
