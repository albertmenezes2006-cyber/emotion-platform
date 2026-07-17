#!/usr/bin/env python3
"""Modelos Operantes Internos em psicologia clinica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_clin/modelos_operantes_internos", tags=["psicologia_clinica"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"psicologia_clinica_modelos_operantes_interno","status":"ativo","desc":"Modelos Operantes Internos em psicologia clinica","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_modelos_operantes_interno"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
