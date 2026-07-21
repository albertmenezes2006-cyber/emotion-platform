#!/usr/bin/env python3
"""Tracker de atividade fisica e impacto no humor"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/atividade", tags=["Exercício"])
ARQUIVO = Path("atividade_fisica.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/registrar")
async def registrar_atividade(request: Request):
    d = await request.json()
    registros = carregar()
    registros.append({
        "tipo": d.get("tipo", ""),
        "duracao_min": d.get("duracao_min", 0),
        "intensidade": d.get("intensidade", "moderada"),
        "humor_antes": d.get("humor_antes", 5),
        "humor_depois": d.get("humor_depois", 5),
        "data": datetime.utcnow().strftime("%d/%m/%Y %H:%M"),
        "timestamp": datetime.utcnow().isoformat()
    })
    ARQUIVO.write_text(json.dumps(registros, ensure_ascii=False, indent=2))
    melhora = d.get("humor_depois", 5) - d.get("humor_antes", 5)
    return JSONResponse({"ok": True, "melhora_humor": melhora,
                         "xp_ganho": d.get("duracao_min", 0) * 2,
                         "msg": "Exercício registrado! O movimento melhora o humor."})

@router.get("/stats")
async def stats_atividade():
    registros = carregar()
    if not registros:
        return JSONResponse({"total_sessoes": 0, "minutos_totais": 0})
    total_min = sum(r.get("duracao_min", 0) for r in registros)
    melhoras = [r.get("humor_depois", 5) - r.get("humor_antes", 5) for r in registros]
    media_melhora = sum(melhoras) / len(melhoras) if melhoras else 0
    return JSONResponse({
        "total_sessoes": len(registros),
        "minutos_totais": total_min,
        "horas_totais": round(total_min/60, 1),
        "melhora_media_humor": round(media_melhora, 1),
        "ultimo_exercicio": registros[-1]["data"] if registros else None
    })

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_atividade():
    tipos = ["Caminhada", "Corrida", "Natação", "Yoga", "Musculação",
             "Ciclismo", "Dança", "Pilates", "Alongamento", "Outro"]
    opts = "".join(f'<option value="{t}">{t}</option>' for t in tipos)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Atividade Física — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f0fff4;padding:20px;margin:0}}
.container{{max-width:600px;margin:0 auto}}
.card{{background:white;border-radius:16px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.08);margin-bottom:20px}}
select,input{{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;margin-bottom:8px;font-size:14px;box-sizing:border-box}}
select:focus,input:focus{{border-color:#38a169;outline:none}}
button{{background:linear-gradient(135deg,#38a169,#2d6a4f);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
.beneficio{{background:#e8f5e9;border-radius:12px;padding:16px;margin-bottom:20px;border-left:4px solid #38a169}}
input[type=range]{{margin:4px 0;accent-color:#38a169}}
</style></head><body><div class="container">
<a href="/" style="color:#38a169;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">🏃 Atividade Física & Humor</h1>
<div class="beneficio">
  <strong style="color:#2d6a4f">💡 Sabia que?</strong>
  <p style="color:#555;margin:6px 0 0;font-size:14px">30 minutos de exercício moderado reduz sintomas de ansiedade em 48% e depressão em 30%. A atividade física libera endorfinas, serotonina e BDNF — o "fertilizante do cérebro".</p>
</div>
<div class="card">
  <h2 style="margin:0 0 16px;color:#333">Registrar Exercício</h2>
  <select id="tipo">{opts}</select>
  <label style="color:#555;font-size:14px">Duração (minutos):</label>
  <input type="number" id="duracao" placeholder="Ex: 30" min="5" max="300">
  <label style="color:#555;font-size:14px">Intensidade:</label>
  <select id="intensidade">
    <option value="leve">Leve (caminhada, alongamento)</option>
    <option value="moderada" selected>Moderada (corrida leve, natação)</option>
    <option value="intensa">Intensa (HIIT, musculação pesada)</option>
  </select>
  <label style="color:#555;font-size:14px">Humor ANTES (1-10): <span id="hav">5</span></label>
  <input type="range" id="humor_antes" min="1" max="10" value="5" oninput="document.getElementById('hav').textContent=this.value">
  <label style="color:#555;font-size:14px">Humor DEPOIS (1-10): <span id="hdv">7</span></label>
  <input type="range" id="humor_depois" min="1" max="10" value="7" oninput="document.getElementById('hdv').textContent=this.value">
  <button style="margin-top:8px" onclick="registrar()">🏃 Registrar atividade</button>
</div>
</div><script>
function registrar(){{
  var d={{tipo:document.getElementById("tipo").value,
    duracao_min:parseInt(document.getElementById("duracao").value)||0,
    intensidade:document.getElementById("intensidade").value,
    humor_antes:parseInt(document.getElementById("humor_antes").value),
    humor_depois:parseInt(document.getElementById("humor_depois").value)}};
  if(!d.duracao_min){{alert("Digite a duração");return;}}
  fetch("/api/v1/atividade/registrar",{{method:"POST",
    headers:{{"Content-Type":"application/json"}},body:JSON.stringify(d)}})
  .then(r=>r.json()).then(function(r){{
    var msg="OK "+r.msg+" "+r.xp_ganho+" XP ganhos!";
    if(r.melhora_humor>0) msg+=" Humor melhorou "+r.melhora_humor+" pontos!";
  }});
}}
</script></body></html>""")

class AtividadePlugin(PluginBase):
    name = "atividade_fisica_tracker"
    def setup(self, app): app.include_router(router)
plugin = AtividadePlugin()
