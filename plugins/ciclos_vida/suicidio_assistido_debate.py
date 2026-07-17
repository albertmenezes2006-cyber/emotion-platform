#!/usr/bin/env python3
"""Suicidio Assistido Debate em ciclos vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ciclos_vida/suicidio_assistido_debate", tags=["ciclos_vida"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ciclos_vida_suicidio_assistido_debate", "status": "ativo",
                          "descricao": "Suicidio Assistido Debate em ciclos vida", "categoria": "ciclos_vida",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ciclos_vida_suicidio_assistido_debate"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
