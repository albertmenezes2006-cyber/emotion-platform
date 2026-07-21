#!/usr/bin/env python3
"""Versao e info da API"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/versao", tags=["Info"])

@router.get("")
async def versao_api():
    return JSONResponse({
        "nome": "Emotion Intelligence Platform",
        "versao": "24.4.0",
        "build": datetime.utcnow().strftime("%Y%m%d"),
        "ambiente": "producao",
        "docs": "/admin/docs-secret/albert2024secretdocs",
        "status": "/status",
        "health": "/health",
        "changelog": "/changelog",
        "contato": "albertmenezes2006@gmail.com",
        "site": "https://emotion-platform-albert.onrender.com"
    })

class VersaoPlugin(PluginBase):
    name = "versao_api"
    def setup(self, app): app.include_router(router)
plugin = VersaoPlugin()
