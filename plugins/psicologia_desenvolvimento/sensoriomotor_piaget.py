#!/usr/bin/env python3
"""Sensoriomotor Piaget"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_d/sensoriomotor_piaget", tags=["psicologia_desenvolvimento"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_desenvo_sensoriomotor_piaget","s":"ativo","d":"Sensoriomotor Piaget","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_desenvo_sensoriomotor_piaget"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
