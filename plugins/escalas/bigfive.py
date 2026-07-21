#!/usr/bin/env python3
"""Big Five — Personalidade"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/bigfive", tags=["Escalas"])

@router.get("/info")
async def info():
    return JSONResponse({"nome": "Big Five", "dimensoes": 5,
                         "fatores": ["Abertura", "Conscienciosidade", "Extroversao", "Amabilidade", "Neuroticismo"]})

@router.post("/calcular")
async def calcular(request: Request):
    try:
        body = await request.json()
        respostas = body if isinstance(body, list) else body.get("respostas", [])
    except Exception:
        respostas = []
    n = len(respostas)
    return JSONResponse({
        "abertura": round(sum(respostas[:n//5]) / max(n//5, 1), 2) if respostas else 0,
        "conscienciosidade": round(sum(respostas[n//5:2*n//5]) / max(n//5, 1), 2) if respostas else 0,
        "extroversao": round(sum(respostas[2*n//5:3*n//5]) / max(n//5, 1), 2) if respostas else 0,
        "amabilidade": round(sum(respostas[3*n//5:4*n//5]) / max(n//5, 1), 2) if respostas else 0,
        "neuroticismo": round(sum(respostas[4*n//5:]) / max(n//5, 1), 2) if respostas else 0,
    })

@router.get("/status")
async def status():
    return JSONResponse({"plugin": "bigfive", "status": "ativo"})

class BigFivePlugin(PluginBase):
    name = "bigfive_personalidade"
    def setup(self, app):
        app.include_router(router)

plugin = BigFivePlugin()
