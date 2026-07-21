#!/usr/bin/env python3
"""Analise de sentimento em texto"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import re

router = APIRouter(prefix="/api/v1/sentimento", tags=["Sentimento"])

POSITIVAS = ["feliz","alegre","ótimo","excelente","maravilhoso","amor","gratidão",
             "esperança","calmo","tranquilo","bem","melhor","animado","satisfeito",
             "realizado","contente","sorrindo","otimista","grato","paz"]
NEGATIVAS = ["triste","ansioso","deprimido","medo","raiva","dor","sofrimento",
             "desesperado","angústia","cansado","exausto","sozinho","perdido",
             "culpa","vergonha","fracasso","inútil","sem esperança","mal","pior"]

@router.post("/analisar")
async def analisar_sentimento(request: Request):
    try:
        d = await request.json()
    except Exception:
        d = {}
    texto = d.get("texto", "").lower()
    if not texto:
        return JSONResponse({"sentimento": "neutro", "emoji": "😐", "score": 0, "palavras_positivas": 0, "palavras_negativas": 0, "total_analisado": 0, "alertar_profissional": False, "recursos_crise": None})
    palavras = re.findall(r"\w+", texto)
    pos = sum(1 for p in palavras if p in POSITIVAS)
    neg = sum(1 for p in palavras if p in NEGATIVAS)
    total = max(1, pos + neg)
    score = (pos - neg) / total
    if score > 0.3: sentimento, emoji = "positivo", "😊"
    elif score < -0.3: sentimento, emoji = "negativo", "😟"
    else: sentimento, emoji = "neutro", "😐"
    alertar = neg > 3 or any(p in texto for p in ["suicídio","morrer","acabar"])
    return JSONResponse({
        "sentimento": sentimento, "emoji": emoji,
        "score": round(score, 2), "palavras_positivas": pos,
        "palavras_negativas": neg, "total_analisado": len(palavras),
        "alertar_profissional": alertar,
        "recursos_crise": "/api/v1/crise/ajuda" if alertar else None
    })

@router.get("/demo")
async def demo_sentimento():
    return JSONResponse({"exemplos": [
        {"texto": "Estou muito feliz e grato hoje!", "sentimento_esperado": "positivo"},
        {"texto": "Me sinto triste e ansioso sem motivo", "sentimento_esperado": "negativo"},
        {"texto": "Mais um dia normal de trabalho", "sentimento_esperado": "neutro"}
    ], "endpoint": "POST /api/v1/sentimento/analisar"})

class SentimentoPlugin(PluginBase):
    name = "analise_sentimento"
    def setup(self, app): app.include_router(router)
plugin = SentimentoPlugin()
