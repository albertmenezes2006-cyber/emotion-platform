#!/usr/bin/env python3
"""Fake news em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/fake-news-mental", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "fake_news_saude_mental", "status": "ativo",
                          "descricao": "Fake news em saúde mental",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "fake_news_saude_mental",
                          "descricao": "Fake news em saúde mental",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "fake_news_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
