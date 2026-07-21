#!/usr/bin/env python3
"""Diario de gratidao diario"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/gratidao", tags=["Gratidão"])
ARQUIVO = Path("diario_gratidao.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/registrar")
async def registrar(request: Request):
    d = await request.json()
    entradas = carregar()
    entradas.append({
        "itens": d.get("itens", []),
        "humor": d.get("humor", 7),
        "data": datetime.utcnow().strftime("%d/%m/%Y"),
        "timestamp": datetime.utcnow().isoformat()
    })
    ARQUIVO.write_text(json.dumps(entradas, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "total": len(entradas),
                         "streak": len(entradas), "xp_ganho": 20})

@router.get("/historico")
async def historico():
    entradas = carregar()
    return JSONResponse({"total": len(entradas), "streak": len(entradas),
                         "entradas": entradas[-7:]})

@router.get("", response_class=HTMLResponse)
async def pagina_gratidao():
    entradas = carregar()
    historico_html = ""
    for e in reversed(entradas[-5:]):
        itens_html = "".join(f"<li style='padding:4px 0;color:#555'>💚 {i}</li>" for i in e.get("itens", []))
        historico_html += f"""
        <div style="background:white;border-radius:12px;padding:20px;margin-bottom:12px;
                    box-shadow:0 2px 8px rgba(0,0,0,0.06)">
          <div style="color:#888;font-size:13px;margin-bottom:8px">📅 {e['data']}</div>
          <ul style="list-style:none;padding:0;margin:0">{itens_html}</ul>
        </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Diário de Gratidão — Emotion Platform</title>
<style>
body{{font-family:sans-serif;background:linear-gradient(180deg,#fef9c3,#f8f9fa);
  min-height:100vh;padding:20px;margin:0}}
.container{{max-width:600px;margin:0 auto}}
.card{{background:white;border-radius:20px;padding:32px;
       box-shadow:0 8px 30px rgba(0,0,0,0.1);margin-bottom:24px}}
h1{{color:#333;margin:0 0 4px}}
input{{width:100%;padding:12px;border-radius:8px;border:2px solid #e0e0e0;
  font-size:16px;box-sizing:border-box;margin-bottom:8px}}
input:focus{{border-color:#f59e0b;outline:none}}
.btn{{background:linear-gradient(135deg,#f59e0b,#d97706);color:white;border:none;
  border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
.streak{{background:linear-gradient(135deg,#f59e0b,#d97706);color:white;
  border-radius:12px;padding:16px;text-align:center;margin-bottom:24px}}
</style></head><body>
<div class="container">
<div class="streak">
  <div style="font-size:32px">🔥</div>
  <div style="font-size:24px;font-weight:800">{len(entradas)} dias</div>
  <div style="opacity:0.9">de gratidão</div>
</div>
<div class="card">
  <h1>💛 Diário de Gratidão</h1>
  <p style="color:#888;margin:4px 0 20px">3 coisas pelas quais você é grato hoje</p>
  <input type="text" id="g1" placeholder="1. Sou grato por...">
  <input type="text" id="g2" placeholder="2. Agradeço por...">
  <input type="text" id="g3" placeholder="3. Me sinto bem por...">
  <button class="btn" onclick="salvar()">💛 Salvar gratidão do dia</button>
</div>
<h2 style="color:#333;margin-bottom:16px">Últimas entradas</h2>
{historico_html if historico_html else "<p style='color:#888'>Ainda sem entradas. Comece hoje!</p>"}
</div>
<script>
function salvar(){{
  var itens=[document.getElementById("g1").value,
    document.getElementById("g2").value,
    document.getElementById("g3").value].filter(function(i){{return i.trim();}});
  if(itens.length===0){{alert("Digite pelo menos 1 item de gratidão");return;}}
  fetch("/gratidao/registrar",{{method:"POST",
    headers:{{"Content-Type":"application/json"}},
    body:JSON.stringify({{itens:itens,humor:7}})}})
  .then(r=>r.json()).then(d=>{{
    alert("✅ Gratidão salva! +"+d.xp_ganho+" XP");
    location.reload();
  }});
}}
</script></body></html>""")

class GratidaoPlugin(PluginBase):
    name = "diario_gratidao"
    def setup(self, app): app.include_router(router)
plugin = GratidaoPlugin()
