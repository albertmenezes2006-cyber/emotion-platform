#!/usr/bin/env python3
"""Bayesian Brain"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/bayesian_brain", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_bayesian_brain","s":"ativo","d":"Bayesian Brain","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_bayesian_brain"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
