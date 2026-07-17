#!/usr/bin/env python3
"""Homework Compliance"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_c/homework_compliance", tags=["psicologia_clinica_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_clinica_homework_compliance","s":"ativo","d":"Homework Compliance","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_clinica_homework_compliance"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
