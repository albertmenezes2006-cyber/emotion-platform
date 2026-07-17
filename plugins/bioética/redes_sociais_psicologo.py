#!/usr/bin/env python3
"""Psicólogo nas redes sociais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/redes-psicologo", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "redes_sociais_psicologo", "status": "ativo",
                          "descricao": "Psicólogo nas redes sociais",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "redes_sociais_psicologo",
                          "descricao": "Psicólogo nas redes sociais",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "redes_sociais_psicologo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
