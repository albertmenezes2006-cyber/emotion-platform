#!/usr/bin/env python3
"""Sistema de journaling avancado com prompts"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json, random
from pathlib import Path

router = APIRouter(prefix="/journaling", tags=["Journaling"])
ARQUIVO = Path("journal_entradas.json")

PROMPTS = [
    "O que te trouxe alegria hoje, por menor que seja?",
    "Qual desafio você enfrentou e como se saiu?",
    "Que pensamento tem ocupado sua mente com frequência?",
    "Se você pudesse mudar uma coisa hoje, o que seria?",
    "O que você aprendeu sobre si mesmo esta semana?",
    "Quem você gostaria de agradecer e por quê?",
    "O que seu corpo está te dizendo hoje?",
    "Qual crença sobre si mesmo você gostaria de mudar?",
    "Que versão de si mesmo você quer ser daqui a 1 ano?",
    "O que você está evitando e por quê?",
    "Descreva um momento em que você se sentiu completamente você mesmo.",
    "O que o seu eu mais jovem precisaria ouvir de você hoje?",
    "Que emoção você tem dificuldade de expressar? Por quê?",
    "O que significa para você cuidar de si mesmo?",
    "Qual é o seu maior medo no momento e de onde ele vem?",
]

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/salvar")
async def salvar_entrada(request: Request):
    d = await request.json()
    entradas = carregar()
    entradas.append({
        "id": len(entradas)+1,
        "prompt": d.get("prompt",""),
        "texto": d.get("texto",""),
        "humor": d.get("humor", 5),
        "palavras": len(d.get("texto","").split()),
        "data": datetime.utcnow().strftime("%d/%m/%Y"),
        "timestamp": datetime.utcnow().isoformat()
    })
    ARQUIVO.write_text(json.dumps(entradas, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "id": len(entradas),
                         "palavras": entradas[-1]["palavras"],
                         "xp": min(entradas[-1]["palavras"] * 2, 100)})

@router.get("/historico")
async def historico():
    entradas = carregar()
    total_palavras = sum(e.get("palavras",0) for e in entradas)
    return JSONResponse({"total": len(entradas), "total_palavras": total_palavras,
                         "media_palavras": total_palavras//max(1,len(entradas)),
                         "entradas": entradas[-5:]})

@router.get("", response_class=HTMLResponse)
async def pagina_journal():
    prompt_hoje = random.choice(PROMPTS)
    entradas = carregar()
    historico_html = ""
    for e in reversed(entradas[-3:]):
        historico_html += f"""
        <div style="background:#f8f9fa;border-radius:12px;padding:16px;margin-bottom:10px">
          <div style="color:#888;font-size:12px;margin-bottom:6px">{e['data']} · {e.get('palavras',0)} palavras</div>
          <div style="color:#667eea;font-size:13px;font-style:italic;margin-bottom:6px">"{e.get('prompt','')[:60]}..."</div>
          <div style="color:#555;font-size:14px;line-height:1.6">{e.get('texto','')[:200]}{"..." if len(e.get("texto",""))>200 else ""}</div>
        </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Journaling — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#fefce8;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
.card{{background:white;border-radius:20px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.08);margin-bottom:20px}}
.prompt{{background:linear-gradient(135deg,#f59e0b,#d97706);color:white;border-radius:12px;padding:16px;margin-bottom:16px;font-style:italic;font-size:16px;line-height:1.6}}
textarea{{width:100%;padding:14px;border-radius:12px;border:2px solid #e0e0e0;font-size:15px;resize:vertical;min-height:200px;box-sizing:border-box;font-family:inherit;line-height:1.7}}
textarea:focus{{border-color:#f59e0b;outline:none}}
.stats{{display:flex;gap:16px;margin:12px 0}}
.stat{{background:#fef9c3;border-radius:8px;padding:8px 16px;font-size:13px;color:#854d0e}}
button{{background:linear-gradient(135deg,#f59e0b,#d97706);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
input[type=range]{{accent-color:#f59e0b;width:100%}}
</style></head><body><div class="container">
<a href="/" style="color:#f59e0b;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">📝 Diário Reflexivo</h1>
<div class="card">
  <div class="prompt">💭 "{prompt_hoje}"</div>
  <textarea id="texto" placeholder="Escreva livremente. Não há resposta certa ou errada..." oninput="contar()"></textarea>
  <div class="stats">
    <div class="stat" id="palavras">0 palavras</div>
    <div class="stat" id="tempo">~0 min leitura</div>
  </div>
  <label style="color:#555;font-size:14px;display:block;margin:12px 0 4px">Como está seu humor agora? <span id="hv">5</span>/10</label>
  <input type="range" id="humor" min="1" max="10" value="5" oninput="document.getElementById('hv').textContent=this.value">
  <button style="margin-top:12px" onclick="salvar()">💾 Salvar entrada</button>
</div>
{f'<h2 style="color:#333;margin-bottom:12px">Últimas entradas</h2>{historico_html}' if historico_html else ''}
</div><script>
function contar(){{
  var t=document.getElementById("texto").value;
  var p=t.trim()?t.trim().split(/\\s+/).length:0;
  document.getElementById("palavras").textContent=p+" palavras";
  document.getElementById("tempo").textContent="~"+Math.ceil(p/200)+" min leitura";
}}
function salvar(){{
  var texto=document.getElementById("texto").value;
  if(texto.trim().length<10){{alert("Escreva pelo menos algumas palavras");return;}}
  fetch("/journaling/salvar",{{method:"POST",
    headers:{{"Content-Type":"application/json"}},
    body:JSON.stringify({{prompt:"{prompt_hoje}",texto:texto,humor:parseInt(document.getElementById("humor").value)}})}})
  .then(r=>r.json()).then(function(d){{
    alert("✅ Entrada salva! "+d.palavras+" palavras · +"+d.xp+" XP");
    location.reload();
  }});
}}
</script></body></html>""")

class JournalingPlugin(PluginBase):
    name = "journaling_avancado"
    def setup(self, app): app.include_router(router)
plugin = JournalingPlugin()
