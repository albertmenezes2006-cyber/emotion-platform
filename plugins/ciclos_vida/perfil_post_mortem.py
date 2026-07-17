#!/usr/bin/env python3
"""Perfil Post Mortem em ciclos vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ciclos_vida/perfil_post_mortem", tags=["ciclos_vida"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ciclos_vida_perfil_post_mortem", "status": "ativo",
                          "descricao": "Perfil Post Mortem em ciclos vida", "categoria": "ciclos_vida",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ciclos_vida_perfil_post_mortem"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
