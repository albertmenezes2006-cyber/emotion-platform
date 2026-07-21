#!/usr/bin/env python3
"""Estimador de tempo de leitura"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/leitura", tags=["Utilidades"])

@router.post("/estimar")
async def estimar_leitura(texto: str = ""):
    palavras = len(texto.split())
    minutos = max(1, round(palavras / 200))
    return JSONResponse({"palavras": palavras, "minutos": minutos,
                         "texto": f"{minutos} min de leitura"})

class LeituraPlugin(PluginBase):
    name = "tempo_leitura"
    def setup(self, app): app.include_router(router)
plugin = LeituraPlugin()
