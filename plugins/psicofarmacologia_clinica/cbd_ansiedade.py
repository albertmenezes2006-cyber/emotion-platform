#!/usr/bin/env python3
"""Cbd Ansiedade em psicofarmacologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofarmacolog/cbd_ansiedade", tags=["psicofarmacologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicofarmacologia_cl_cbd_ansiedade","status":"ativo","desc":"Cbd Ansiedade em psicofarmacologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofarmacologia_cl_cbd_ansiedade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
