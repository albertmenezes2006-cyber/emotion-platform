#!/usr/bin/env python3
"""Gerador de senhas seguras"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import secrets, string

router = APIRouter(prefix="/api/v1/senha", tags=["Utilidades"])

@router.get("/gerar")
async def gerar_senha(tamanho: int = 16, especiais: bool = True):
    chars = string.ascii_letters + string.digits
    if especiais: chars += "!@#$%&*"
    tamanho = min(max(tamanho, 8), 64)
    senha = "".join(secrets.choice(chars) for _ in range(tamanho))
    forca = "forte" if tamanho >= 12 and especiais else "media" if tamanho >= 8 else "fraca"
    return JSONResponse({"senha": senha, "tamanho": tamanho,
                         "forca": forca, "entropia_bits": round(tamanho * 6.5, 1)})

class SenhaPlugin(PluginBase):
    name = "gerador_senha"
    def setup(self, app): app.include_router(router)
plugin = SenhaPlugin()
