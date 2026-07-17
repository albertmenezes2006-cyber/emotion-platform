#!/usr/bin/env python3
"""Feedback Related Negativity"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuroimagem_/feedback_related_negativity", tags=["neuroimagem_clinica"])
@router.get("")
async def info():
    return JSONResponse({"p":"neuroimagem_clinic_feedback_related_negativi","s":"ativo","d":"Feedback Related Negativity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuroimagem_clinic_feedback_related_negativi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
