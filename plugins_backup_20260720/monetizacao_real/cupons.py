#!/usr/bin/env python3
"""Sistema de cupons de desconto"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/cupons", tags=["Cupons"])
ARQUIVO = Path("cupons.json")

CUPONS_DEFAULT = {
    "BEMVINDO": {"desconto": 50, "tipo": "percentual", "limite": 100, "usado": 0,
                 "validade": "2026-12-31", "descricao": "50% off primeiro mes"},
    "PSICOLOGO": {"desconto": 30, "tipo": "percentual", "limite": 50, "usado": 0,
                  "validade": "2026-12-31", "descricao": "30% para psicologos"},
    "LAUNCH": {"desconto": 100, "tipo": "percentual", "limite": 10, "usado": 0,
               "validade": "2026-08-01", "descricao": "Gratis no lancamento"},
    "ALBERT10": {"desconto": 10, "tipo": "reais", "limite": 999, "usado": 0,
                 "validade": "2026-12-31", "descricao": "R$ 10 de desconto"}
}

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    ARQUIVO.write_text(json.dumps(CUPONS_DEFAULT, indent=2))
    return CUPONS_DEFAULT

@router.get("/validar/{codigo}")
async def validar_cupom(codigo: str):
    cupons = carregar()
    c = cupons.get(codigo.upper())
    if not c:
        return JSONResponse({"valido": False, "erro": "Cupom nao encontrado"}, status_code=404)
    if c["usado"] >= c["limite"]:
        return JSONResponse({"valido": False, "erro": "Cupom esgotado"}, status_code=400)
    return JSONResponse({
        "valido": True, "codigo": codigo.upper(),
        "desconto": c["desconto"], "tipo": c["tipo"],
        "descricao": c["descricao"], "validade": c["validade"],
        "usos_restantes": c["limite"] - c["usado"]
    })

@router.post("/usar/{codigo}")
async def usar_cupom(codigo: str):
    cupons = carregar()
    c = cupons.get(codigo.upper())
    if not c:
        return JSONResponse({"erro": "Cupom invalido"}, status_code=404)
    if c["usado"] >= c["limite"]:
        return JSONResponse({"erro": "Cupom esgotado"}, status_code=400)
    cupons[codigo.upper()]["usado"] += 1
    ARQUIVO.write_text(json.dumps(cupons, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "desconto_aplicado": c["desconto"],
                         "tipo": c["tipo"]})

@router.get("/listar")
async def listar_cupons():
    return JSONResponse(carregar())

class CuponsPlugin(PluginBase):
    name = "sistema_cupons"
    def setup(self, app):
        app.include_router(router)

plugin = CuponsPlugin()
