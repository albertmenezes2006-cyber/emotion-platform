#!/usr/bin/env python3
"""NPS - Net Promoter Score automatico"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/nps", tags=["NPS"])

ARQUIVO = Path("nps_dados.json")

_nps_mem = []
def carregar():
    return _nps_mem

@router.post("/responder")
async def responder_nps(request: Request):
    dados = await request.json()
    nota = int(dados.get("nota", 0))
    todos = carregar()
    todos.append({
        "nota": nota,
        "comentario": dados.get("comentario", ""),
        "email": dados.get("email", ""),
        "timestamp": datetime.utcnow().isoformat(),
        "categoria": "promotor" if nota >= 9 else "neutro" if nota >= 7 else "detrator"
    })
    global _nps_mem
    _nps_mem = todos
    return JSONResponse({"ok": True})

@router.get("/calcular")
async def calcular_nps():
    todos = carregar()
    if not todos:
        return {"nps": 0, "total": 0, "msg": "Sem respostas ainda"}
    promotores = len([r for r in todos if r["nota"] >= 9])
    detratores = len([r for r in todos if r["nota"] <= 6])
    total = len(todos)
    nps = round(((promotores - detratores) / total) * 100)
    return {
        "nps": nps,
        "total": total,
        "promotores": promotores,
        "neutros": total - promotores - detratores,
        "detratores": detratores,
        "classificacao": "Excelente" if nps > 70 else "Bom" if nps > 50 else "Regular"
    }

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_nps():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><title>NPS — Emotion Platform</title>
<style>
body{font-family:sans-serif;background:#f0f4ff;display:flex;
     align-items:center;justify-content:center;min-height:100vh;margin:0}
.card{background:white;border-radius:20px;padding:40px;max-width:500px;
      width:100%;text-align:center;box-shadow:0 10px 40px rgba(0,0,0,0.1)}
h1{color:#333;margin-bottom:8px}
.numeros{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:24px 0}
.num{width:44px;height:44px;border-radius:8px;border:2px solid #eee;
     background:white;cursor:pointer;font-size:16px;font-weight:700;
     transition:all 0.2s}
.num:hover{transform:scale(1.1)}
.num.selecionado{background:#667eea;color:white;border-color:#667eea}
.btn{background:#667eea;color:white;border:none;border-radius:12px;
     padding:14px 32px;font-size:16px;font-weight:700;cursor:pointer;width:100%}
</style></head>
<body><div class="card">
<h1>🌟 Recomendaria o Emotion Platform?</h1>
<p style="color:#888">De 0 a 10, qual a probabilidade de recomendar para um colega?</p>
<div class="numeros" id="nums"></div>
<textarea placeholder="Comentário opcional..." id="comentario"
    style="width:100%;border:1px solid #eee;border-radius:8px;padding:12px;
           font-size:14px;resize:none;height:80px;margin-bottom:16px"></textarea>
<button class="btn" onclick="enviar()">Enviar resposta</button>
</div>
<script>
var nota = -1;
for(var i=0;i<=10;i++){
    var btn=document.createElement('button');
    btn.className='num'; btn.textContent=i;
    btn.onclick=(function(n){return function(){
        nota=n;
        document.querySelectorAll('.num').forEach(function(b){b.className='num'});
        this.className='num selecionado';
    }})(i);
    btn.addEventListener('click', function(){this.className='num selecionado'});
    document.getElementById('nums').appendChild(btn);
}
function enviar(){
    if(nota<0){alert('Selecione uma nota!');return}
    fetch('/api/v1/nps/responder',{method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({nota:nota,comentario:document.getElementById('comentario').value})
    }).then(function(){
        document.querySelector('.card').innerHTML=
        '<h1>✅ Obrigado!</h1><p>Sua resposta foi registrada.</p>';
    });
}
</script></body></html>""")

class NPSPlugin(PluginBase):
    name = "nps_automatico"
    def setup(self, app):
        app.include_router(router)

plugin = NPSPlugin()
