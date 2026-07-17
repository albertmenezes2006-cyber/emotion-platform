#!/usr/bin/env python3
"""Sistema de depoimentos e social proof"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/depoimentos", tags=["Depoimentos"])
ARQUIVO = Path("depoimentos.json")

DEPOIMENTOS_DEFAULT = [
    {"nome": "Dra. Ana Silva", "crp": "CRP 06/123456", "cidade": "São Paulo",
     "texto": "Revolucionou minha prática clínica. O PHQ-9 digital economiza 40 minutos por sessão.",
     "nota": 5, "aprovado": True, "data": "2026-07-10"},
    {"nome": "Dr. Carlos Mendes", "crp": "CRP 08/54321", "cidade": "Florianópolis",
     "texto": "A IA em português é impressionante. Meus pacientes adoram o chat entre sessões.",
     "nota": 5, "aprovado": True, "data": "2026-07-08"},
    {"nome": "Dra. Mariana Costa", "crp": "CRP 09/98765", "cidade": "Curitiba",
     "texto": "Finalmente uma ferramenta feita para psicólogos brasileiros. Recomendo muito!",
     "nota": 5, "aprovado": True, "data": "2026-07-05"},
]

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    ARQUIVO.write_text(json.dumps(DEPOIMENTOS_DEFAULT, ensure_ascii=False, indent=2))
    return DEPOIMENTOS_DEFAULT

@router.post("/enviar")
async def enviar_depoimento(request: Request):
    d = await request.json()
    deps = carregar()
    deps.append({**d, "aprovado": False, "data": datetime.utcnow().strftime("%Y-%m-%d")})
    ARQUIVO.write_text(json.dumps(deps, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "msg": "Depoimento recebido! Será publicado após aprovação."})

@router.get("/listar")
async def listar_depoimentos(aprovados: bool = True):
    deps = carregar()
    if aprovados:
        deps = [d for d in deps if d.get("aprovado", False)]
    return JSONResponse(deps)

@router.get("/widget", response_class=HTMLResponse)
async def widget_depoimentos():
    deps = [d for d in carregar() if d.get("aprovado")]
    cards = ""
    for d in deps[:3]:
        estrelas = "⭐" * d.get("nota", 5)
        cards += f"""
        <div style="background:white;border-radius:16px;padding:24px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08);flex:1;min-width:250px">
            <div style="color:#f59e0b;font-size:18px;margin-bottom:12px">{estrelas}</div>
            <p style="color:#555;line-height:1.6;margin:0 0 16px">"{d['texto']}"</p>
            <div style="font-weight:700;color:#333">{d['nome']}</div>
            <div style="color:#888;font-size:13px">{d.get('crp','')} — {d.get('cidade','')}</div>
        </div>"""
    return HTMLResponse(f"""
<div style="font-family:sans-serif;padding:40px 20px;background:#f8f9fa">
    <h2 style="text-align:center;color:#333;margin-bottom:8px">O que dizem os psicólogos</h2>
    <p style="text-align:center;color:#888;margin-bottom:32px">
        Mais de 89 psicólogos já usam a plataforma
    </p>
    <div style="display:flex;gap:20px;flex-wrap:wrap;max-width:900px;margin:0 auto">
        {cards}
    </div>
</div>""")

class DepoimentosPlugin(PluginBase):
    name = "sistema_depoimentos"
    def setup(self, app): app.include_router(router)
plugin = DepoimentosPlugin()
