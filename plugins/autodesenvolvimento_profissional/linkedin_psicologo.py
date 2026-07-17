#!/usr/bin/env python3
"""Linkedin Psicologo em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/linkedin_psicologo", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__linkedin_psicologo","status":"ativo","desc":"Linkedin Psicologo em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__linkedin_psicologo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
