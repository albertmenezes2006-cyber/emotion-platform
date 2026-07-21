#!/usr/bin/env python3
"""Calculadora rapida de burnout"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/burnout", tags=["Burnout"])

@router.get("/calcular")
async def calcular_burnout(exaustao: int = 0, despersonalizacao: int = 0, realizacao: int = 0):
    score = exaustao + despersonalizacao + (30 - realizacao)
    nivel = "Sem burnout" if score < 20 else "Leve" if score < 35 else "Moderado" if score < 50 else "Grave"
    return JSONResponse({"score": score, "nivel": nivel,
                         "exaustao": exaustao, "despersonalizacao": despersonalizacao,
                         "realizacao": realizacao,
                         "recomendacao": "Busque apoio profissional" if score >= 35 else "Continue monitorando"})

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_burnout():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<title>Calculadora de Burnout</title>
<style>body{font-family:sans-serif;max-width:600px;margin:40px auto;padding:20px}
h1{color:#667eea} label{display:block;margin:16px 0 4px;font-weight:700}
input{width:100%;padding:8px;border-radius:8px;border:1px solid #ddd}
button{background:#667eea;color:white;border:none;padding:12px 24px;
       border-radius:8px;cursor:pointer;font-size:16px;margin-top:16px;width:100%}
#resultado{margin-top:20px;padding:20px;border-radius:12px;background:#f0f4ff}</style>
</head><body>
<h1>🔥 Calculadora de Burnout</h1>
<label>Exaustão emocional (0-10):</label>
<input type="number" id="ex" min="0" max="10" value="0">
<label>Despersonalização (0-10):</label>
<input type="number" id="de" min="0" max="10" value="0">
<label>Realização profissional (0-10):</label>
<input type="number" id="re" min="0" max="10" value="10">
<button onclick="calcular()">Calcular Burnout</button>
<div id="resultado"></div>
<script>
function calcular(){
  var ex=parseInt(document.getElementById("ex").value);
  var de=parseInt(document.getElementById("de").value);
  var re=parseInt(document.getElementById("re").value);
  fetch("/api/v1/burnout/calcular?exaustao="+ex+"&despersonalizacao="+de+"&realizacao="+re)
  .then(r=>r.json()).then(d=>{
    document.getElementById("resultado").innerHTML=
    "<h2>Score: "+d.score+"</h2><p><strong>Nível:</strong> "+d.nivel+"</p>"+
    "<p>"+d.recomendacao+"</p>";
  });
}
</script></body></html>""")

class BurnoutPlugin(PluginBase):
    name = "burnout_calc"
    def setup(self, app):
        app.include_router(router)

plugin = BurnoutPlugin()
