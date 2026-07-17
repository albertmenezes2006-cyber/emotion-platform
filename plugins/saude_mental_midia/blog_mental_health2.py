#!/usr/bin/env python3
"""Blog Mental Health2"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/blog_mental_health2", tags=["saude_mental_midia"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_midia_blog_mental_health2","s":"ativo","d":"Blog Mental Health2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_midia_blog_mental_health2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
