#!/usr/bin/env python3
"""Existential Death"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/existential_death", tags=["saude_mental_idoso_avancado"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_idoso_existential_death","s":"ativo","d":"Existential Death","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_idoso_existential_death"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
