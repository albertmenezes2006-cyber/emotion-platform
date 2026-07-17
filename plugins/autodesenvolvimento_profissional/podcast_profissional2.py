#!/usr/bin/env python3
"""Podcast Profissional2 em autodesenvolvimento profissional"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/autodesenvolvim/podcast_profissional2", tags=["autodesenvolvimento_profissional"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"autodesenvolvimento__podcast_profissional2","status":"ativo","desc":"Podcast Profissional2 em autodesenvolvimento profissional","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "autodesenvolvimento__podcast_profissional2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
