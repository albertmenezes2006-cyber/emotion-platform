#!/usr/bin/env python3
"""Tracker de humor diario simples"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/humor", tags=["Humor"])
ARQUIVO = Path("humor_diario.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/registrar")
async def registrar_humor(request: Request):
    d = await request.json()
    registros = carregar()
    registros.append({"humor": d.get("humor", 5), "nota": d.get("nota", ""),
                      "emocao": d.get("emocao", ""), "data": datetime.utcnow().isoformat()})
    ARQUIVO.write_text(json.dumps(registros, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "total": len(registros)})

@router.get("/historico")
async def historico_humor():
    r = carregar()
    media = sum(x["humor"] for x in r)/len(r) if r else 0
    return JSONResponse({"media": round(media,1), "total": len(r), "ultimos": r[-7:]})

@router.get("/check-in", response_class=HTMLResponse)
async def checkin_humor():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<title>Check-in de Humor</title>
<style>body{font-family:sans-serif;background:#f0f4ff;display:flex;align-items:center;
justify-content:center;min-height:100vh;margin:0}
.card{background:white;border-radius:20px;padding:40px;max-width:400px;width:100%;text-align:center;
      box-shadow:0 10px 40px rgba(0,0,0,0.1)}
.emojis{font-size:40px;display:flex;justify-content:center;gap:12px;margin:20px 0}
.emoji{cursor:pointer;transition:transform 0.2s;padding:8px;border-radius:50%}
.emoji:hover{transform:scale(1.3)}
.emoji.sel{background:#e8f0fe;transform:scale(1.3)}
button{background:#667eea;color:white;border:none;padding:14px 32px;
       border-radius:12px;cursor:pointer;font-size:16px;font-weight:700;width:100%}
textarea{width:100%;border:1px solid #eee;border-radius:8px;padding:12px;
         font-size:14px;resize:none;height:80px;margin:12px 0;box-sizing:border-box}</style>
</head><body><div class="card">
<h1 style="color:#333;margin-bottom:4px">Como você está?</h1>
<p style="color:#888">Check-in diário de humor</p>
<div class="emojis">
  <span class="emoji" onclick="sel(1,this)" title="Muito mal">😢</span>
  <span class="emoji" onclick="sel(3,this)" title="Mal">😟</span>
  <span class="emoji" onclick="sel(5,this)" title="Neutro">😐</span>
  <span class="emoji" onclick="sel(7,this)" title="Bem">🙂</span>
  <span class="emoji" onclick="sel(9,this)" title="Muito bem">😄</span>
</div>
<textarea id="nota" placeholder="Como foi seu dia? (opcional)"></textarea>
<button onclick="enviar()">Registrar humor</button>
</div>
<script>
var humor=5;
function sel(n,el){humor=n;document.querySelectorAll(".emoji").forEach(e=>e.classList.remove("sel"));el.classList.add("sel");}
function enviar(){
  fetch("/api/v1/humor/registrar",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({humor:humor,nota:document.getElementById("nota").value})
  }).then(()=>{document.querySelector(".card").innerHTML="<h2>✅ Registrado!</h2><p>Até amanhã!</p>";});
}
</script></body></html>""")

class HumorPlugin(PluginBase):
    name = "humor_tracker_diario"
    def setup(self, app):
        app.include_router(router)

plugin = HumorPlugin()
