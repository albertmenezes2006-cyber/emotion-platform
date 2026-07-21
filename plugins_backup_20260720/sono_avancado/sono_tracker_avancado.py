#!/usr/bin/env python3
"""Tracker de sono avancado com correlacao de humor"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/sono", tags=["Sono"])
ARQUIVO = Path("sono_tracker.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/registrar")
async def registrar_sono(request: Request):
    d = await request.json()
    registros = carregar()
    hora_inicio = d.get("hora_inicio", "22:00")
    hora_fim = d.get("hora_fim", "06:00")
    registros.append({
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim,
        "qualidade": d.get("qualidade", 3),
        "sonhos": d.get("sonhos", False),
        "acordou_noite": d.get("acordou_noite", 0),
        "humor_manha": d.get("humor_manha", 5),
        "data": datetime.utcnow().strftime("%d/%m/%Y"),
        "timestamp": datetime.utcnow().isoformat()
    })
    ARQUIVO.write_text(json.dumps(registros, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "total_registros": len(registros)})

@router.get("/analise")
async def analisar_sono():
    registros = carregar()
    if not registros:
        return JSONResponse({"msg": "Sem dados de sono ainda"})
    qualidades = [r.get("qualidade", 3) for r in registros]
    humores = [r.get("humor_manha", 5) for r in registros]
    media_qualidade = sum(qualidades) / len(qualidades)
    media_humor = sum(humores) / len(humores)
    return JSONResponse({
        "total_noites": len(registros),
        "qualidade_media": round(media_qualidade, 1),
        "humor_manha_medio": round(media_humor, 1),
        "correlacao": "positiva" if media_qualidade > 3 and media_humor > 5 else "negativa",
        "recomendacao": "Mantenha horários regulares de sono" if media_qualidade < 3
                        else "Seu sono está adequado. Continue assim!"
    })

@router.get("/higiene", response_class=HTMLResponse)
async def higiene_sono():
    dicas = [
        ("🌙", "Horário regular", "Durma e acorde no mesmo horário, inclusive fins de semana"),
        ("📱", "Sem telas", "Evite celular, tablet e TV 1 hora antes de dormir"),
        ("🌡️", "Temperatura", "Mantenha o quarto fresco (18-20°C é ideal para dormir"),
        ("☕", "Cafeína", "Evite café, chá preto e refrigerantes após 14h"),
        ("🏃", "Exercício", "Exercite-se, mas evite atividade intensa 3h antes de dormir"),
        ("😌", "Relaxamento", "Pratique respiração profunda ou meditação antes de dormir"),
        ("🛏️", "Cama = sono", "Use a cama apenas para dormir e sexo, não para trabalhar"),
        ("🌅", "Luz solar", "Exponha-se à luz solar pela manhã para regular o ritmo circadiano"),
    ]
    cards = "".join(f"""
        <div style="background:white;border-radius:12px;padding:20px;
                    box-shadow:0 2px 8px rgba(0,0,0,0.06);display:flex;gap:16px;align-items:start">
          <span style="font-size:32px">{d[0]}</span>
          <div><h3 style="color:#333;margin:0 0 4px">{d[1]}</h3>
          <p style="color:#666;margin:0;font-size:14px;line-height:1.6">{d[2]}</p></div>
        </div>""" for d in dicas)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Higiene do Sono — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#1a1a2e;color:white;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-top:24px}}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#667eea;margin:16px 0">🌙 Higiene do Sono</h1>
<p style="color:rgba(255,255,255,0.7);margin-bottom:8px">8 hábitos baseados em evidências para dormir melhor</p>
<div class="grid">{cards}</div>
<div style="background:#667eea;border-radius:16px;padding:24px;text-align:center;margin-top:24px">
  <h2 style="margin:0 0 8px">Rastreie seu sono</h2>
  <p style="opacity:0.9;margin:0 0 16px">Registre sua qualidade de sono e veja a correlação com seu humor</p>
  <a href="/api/v1/humor/check-in" style="background:white;color:#667eea;padding:12px 24px;
     border-radius:8px;text-decoration:none;font-weight:700">Registrar hoje →</a>
</div>
</div></body></html>""")

class SonoPlugin(PluginBase):
    name = "sono_tracker_avancado"
    def setup(self, app): app.include_router(router)
plugin = SonoPlugin()
