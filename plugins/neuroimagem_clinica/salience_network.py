#!/usr/bin/env python3
"""Salience Network"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/salience_network", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_salience_network","s":"ativo","d":"Salience Network","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_salience_network"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
