#!/usr/bin/env python3
"""Face Name Association"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/avaliacao_ne/face_name_association", tags=["avaliacao_neuropsicologica"])
@router.get("")
async def info():
    return JSONResponse({"p":"avaliacao_neuropsi_face_name_association","s":"ativo","d":"Face Name Association","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "avaliacao_neuropsi_face_name_association"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
