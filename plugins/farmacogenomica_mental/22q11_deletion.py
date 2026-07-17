#!/usr/bin/env python3
"""22Q11 Deletion"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacogenom/22q11_deletion", tags=["farmacogenomica_mental"])
@router.get("")
async def info():
    return JSONResponse({"p":"farmacogenomica_me_22q11_deletion","s":"ativo","d":"22Q11 Deletion","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacogenomica_me_22q11_deletion"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
