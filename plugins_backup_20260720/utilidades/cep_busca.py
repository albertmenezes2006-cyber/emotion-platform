#!/usr/bin/env python3
"""Busca de CEP via ViaCEP"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx

router = APIRouter(prefix="/api/v1/cep", tags=["CEP"])

@router.get("/{cep}")
async def buscar_cep(cep: str):
    cep = cep.replace("-","").replace(".","").strip()
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        if r.status_code == 200:
            return JSONResponse(r.json())
        return JSONResponse({"erro": "CEP nao encontrado"}, status_code=404)

class CEPPlugin(PluginBase):
    name = "cep_busca"
    def setup(self, app): app.include_router(router)
plugin = CEPPlugin()
