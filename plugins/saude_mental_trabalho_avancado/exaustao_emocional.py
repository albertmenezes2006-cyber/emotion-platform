#!/usr/bin/env python3
"""Exaustao Emocional em saude mental trabalho avancado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental_tr/exaustao_emocional", tags=["saude_mental_trabalho_avancado"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_mental_trabalh_exaustao_emocional","status":"ativo","desc":"Exaustao Emocional em saude mental trabalho avancado","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_trabalh_exaustao_emocional"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
