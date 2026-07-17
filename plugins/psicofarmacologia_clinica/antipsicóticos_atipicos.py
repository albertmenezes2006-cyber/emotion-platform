#!/usr/bin/env python3
"""Antipsicóticos Atipicos em psicofarmacologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofarmacolog/antipsicóticos_atipicos", tags=["psicofarmacologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicofarmacologia_cl_antipsicóticos_atipicos","status":"ativo","desc":"Antipsicóticos Atipicos em psicofarmacologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofarmacologia_cl_antipsicóticos_atipicos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
