#!/usr/bin/env python3
"""Olanzapina Clinica em psicofarmacologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofarmacolog/olanzapina_clinica", tags=["psicofarmacologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicofarmacologia_cl_olanzapina_clinica","status":"ativo","desc":"Olanzapina Clinica em psicofarmacologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofarmacologia_cl_olanzapina_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
