#!/usr/bin/env python3
"""Sistema de referral — indique e ganhe"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json, hashlib
from pathlib import Path

router = APIRouter(prefix="/api/v1/referral", tags=["Referral"])
ARQUIVO = Path("referrals.json")

def gerar_codigo(email: str) -> str:
    return hashlib.md5(email.encode()).hexdigest()[:8].upper()

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return {}

@router.get("/gerar/{email}")
async def gerar_referral(email: str):
    dados = carregar()
    codigo = gerar_codigo(email)
    if codigo not in dados:
        dados[codigo] = {"email": email, "indicacoes": 0,
                         "criado": datetime.utcnow().isoformat()}
        ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
    d = dados[codigo]
    url = f"https://emotion-platform-albert.onrender.com/?ref={codigo}"
    return JSONResponse({
        "codigo": codigo, "url": url,
        "indicacoes": d["indicacoes"],
        "beneficio": "30 dias gratis por indicacao",
        "whatsapp": f"https://wa.me/?text=Use meu codigo {codigo} no Emotion Platform e ganhe 30 dias gratis: {url}"
    })

@router.get("/usar/{codigo}")
async def usar_referral(codigo: str):
    dados = carregar()
    if codigo in dados:
        dados[codigo]["indicacoes"] += 1
        ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
        return JSONResponse({"ok": True, "desconto": "30 dias gratis aplicado"})
    return JSONResponse({"erro": "Codigo invalido"}, status_code=404)

@router.get("/stats")
async def stats_referral():
    dados = carregar()
    total = sum(d["indicacoes"] for d in dados.values())
    return JSONResponse({"total_codigos": len(dados),
                         "total_indicacoes": total, "top": list(dados.values())[:5]})

class ReferralPlugin(PluginBase):
    name = "sistema_referral"
    def setup(self, app):
        app.include_router(router)

plugin = ReferralPlugin()
