#!/usr/bin/env python3
"""Autocompaixao guiada - Kristin Neff"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
from datetime import datetime
router = APIRouter(prefix="/autocompaixao", tags=["Autocompaixao"])
ARQUIVO = Path("autocompaixao_cartas.json")
@router.post("/salvar")
async def salvar(request: Request):
    d = await request.json()
    cartas = json.loads(ARQUIVO.read_text()) if ARQUIVO.exists() else []
    cartas.append({**d, "data": datetime.utcnow().strftime("%d/%m/%Y")})
    ARQUIVO.write_text(json.dumps(cartas, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True})
@router.get("", response_class=HTMLResponse)
async def autocompaixao():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Autocompaixao - Emotion Platform</title>
<style>body{font-family:sans-serif;background:#fdf4ff;padding:20px;margin:0}
.container{max-width:700px;margin:0 auto}
.header{background:linear-gradient(135deg,#a855f7,#ec4899);color:white;
border-radius:20px;padding:32px;margin-bottom:24px;text-align:center}
.card{background:white;border-radius:16px;padding:28px;margin-bottom:20px;
box-shadow:0 4px 20px rgba(168,85,247,0.1)}
.comp{background:#f5f3ff;border-radius:12px;padding:16px;margin-bottom:12px;border-left:4px solid #a855f7}
.comp h3{color:#7c3aed;margin:0 0 6px;font-size:15px}
.comp p{color:#555;margin:0;font-size:14px;line-height:1.6}
.frase{background:#a855f7;color:white;border-radius:12px;padding:16px;
text-align:center;font-size:15px;font-style:italic;margin:16px 0;line-height:1.6}
textarea{width:100%;padding:12px;border-radius:8px;border:2px solid #e0e0e0;
font-size:14px;resize:vertical;min-height:140px;box-sizing:border-box;font-family:inherit}
textarea:focus{border-color:#a855f7;outline:none}
button{background:linear-gradient(135deg,#a855f7,#ec4899);color:white;border:none;
border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}
</style></head><body><div class="container">
<a href="/" style="color:#a855f7;text-decoration:none">Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">Autocompaixao</h1>
<p style="opacity:0.9;margin:0">Baseado nos trabalhos de Kristin Neff</p></div>
<div class="card">
  <h2 style="color:#7c3aed;margin:0 0 16px">Os 3 Componentes</h2>
  <div class="comp"><h3>Bondade Consigo Mesmo</h3>
  <p>Tratar a si mesmo com calor quando sofre ou falha, em vez de se criticar duramente.</p></div>
  <div class="comp"><h3>Humanidade Compartilhada</h3>
  <p>O sofrimento e a inadequacao fazem parte da experiencia humana compartilhada.</p></div>
  <div class="comp"><h3>Mindfulness</h3>
  <p>Observar pensamentos dolorosos com abertura, sem suprimir nem exagerar.</p></div>
</div>
<div class="card">
  <h2 style="color:#7c3aed;margin:0 0 16px">Carta para Voce Mesmo</h2>
  <p style="color:#666;margin-bottom:16px;line-height:1.7">
  Pense em algo que te causa vergonha. Imagine um amigo querido passando pelo mesmo.
  Escreva para si mesmo com a mesma gentileza.</p>
  <textarea id="carta" placeholder="Querido(a) [seu nome]..."></textarea>
  <button onclick="salvar()" style="margin-top:12px">Salvar minha carta</button>
</div>
<div class="card">
  <h2 style="color:#7c3aed;margin:0 0 12px">Frases de Autocompaixao</h2>
  <div class="frase" id="frase">Este e um momento de sofrimento. O sofrimento faz parte da vida. Que eu possa ser gentil comigo mesmo.</div>
  <button onclick="prox()" style="background:rgba(168,85,247,0.15);color:#a855f7;margin-top:8px">Ver proxima frase</button>
</div>
</div>
<script>
var frases=["Este e um momento de sofrimento. O sofrimento faz parte da vida. Que eu possa ser gentil comigo mesmo.",
"Estou tendo dificuldades agora. Isso e humano. Que eu possa me dar a compaixao de que preciso.",
"Que eu seja feliz. Que eu seja saudavel. Que eu possa viver com facilidade e paz.",
"Todos nos sofremos. Nao estou sozinho nesta dificuldade."];
var fi=0;
function prox(){fi=(fi+1)%frases.length;document.getElementById("frase").textContent=frases[fi];}
function salvar(){
  var c=document.getElementById("carta").value;
  if(c.trim().length<10){alert("Escreva pelo menos algumas palavras.");return;}
  fetch("/autocompaixao/salvar",{method:"POST",headers:{"Content-Type":"application/json"},
  body:JSON.stringify({carta:c})}).then(function(){alert("Carta salva! Releia quando precisar.");});
}
var salva=localStorage.getItem("carta_autocompaixao");
if(salva)document.getElementById("carta").value=salva;
</script></body></html>""")
class Plugin(PluginBase):
    name = "autocompaixao_guiada"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
