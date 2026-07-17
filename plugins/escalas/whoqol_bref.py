#!/usr/bin/env python3
"""WHOQOL-BREF Qualidade de Vida OMS"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/whoqol", tags=["Escalas"])

DOMINIOS = {
    "fisico": {"nome": "Físico", "cor": "#e53e3e", "itens": [3,4,10,15,16,17,18]},
    "psicologico": {"nome": "Psicológico", "cor": "#667eea", "itens": [5,6,7,11,19,26]},
    "social": {"nome": "Relações Sociais", "cor": "#38a169", "itens": [20,21,22]},
    "ambiental": {"nome": "Meio Ambiente", "cor": "#f59e0b", "itens": [8,9,12,13,14,23,24,25]},
}

@router.get("", response_class=HTMLResponse)
async def pagina_whoqol():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>WHOQOL-BREF — Qualidade de Vida</title>
<style>body{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}
.container{max-width:700px;margin:0 auto}
.header{background:linear-gradient(135deg,#38a169,#2d6a4f);color:white;border-radius:16px;padding:28px;margin-bottom:24px}
.dominio{background:white;border-radius:12px;padding:20px;margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
button{background:linear-gradient(135deg,#38a169,#2d6a4f);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-top:16px}
.escala{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.opt{background:#f0f0f0;border:2px solid #e0e0e0;border-radius:8px;padding:6px 14px;cursor:pointer;font-size:13px;transition:all 0.2s}
.opt.sel{background:#38a169;color:white;border-color:#38a169}
</style></head><body><div class="container">
<a href="/" style="color:#38a169;text-decoration:none">← Voltar</a>
<div class="header">
  <h1 style="margin:0 0 8px">🌱 WHOQOL-BREF</h1>
  <p style="opacity:0.9;margin:0">Avaliação de Qualidade de Vida — Organização Mundial da Saúde</p>
</div>
<p style="color:#888;margin-bottom:20px">As perguntas a seguir referem-se a como você se sentiu nas <strong>últimas duas semanas</strong>.</p>
<div class="dominio">
  <h3 style="color:#667eea;margin:0 0 12px">Q1. Como você avaliaria sua qualidade de vida?</h3>
  <div class="escala">
    <div class="opt" onclick="sel('q1',1,this)">1 - Muito ruim</div>
    <div class="opt" onclick="sel('q1',2,this)">2 - Ruim</div>
    <div class="opt" onclick="sel('q1',3,this)">3 - Nem ruim nem boa</div>
    <div class="opt" onclick="sel('q1',4,this)">4 - Boa</div>
    <div class="opt" onclick="sel('q1',5,this)">5 - Muito boa</div>
  </div>
</div>
<div class="dominio">
  <h3 style="color:#667eea;margin:0 0 12px">Q2. Quão satisfeito(a) você está com sua saúde?</h3>
  <div class="escala">
    <div class="opt" onclick="sel('q2',1,this)">1 - Muito insatisfeito</div>
    <div class="opt" onclick="sel('q2',2,this)">2 - Insatisfeito</div>
    <div class="opt" onclick="sel('q2',3,this)">3 - Nem satisfeito nem insatisfeito</div>
    <div class="opt" onclick="sel('q2',4,this)">4 - Satisfeito</div>
    <div class="opt" onclick="sel('q2',5,this)">5 - Muito satisfeito</div>
  </div>
</div>
<p style="color:#888;font-size:14px;background:#f0f4ff;padding:12px;border-radius:8px">
  <strong>Nota:</strong> A versão completa do WHOQOL-BREF tem 26 questões. Esta é uma demonstração dos domínios. 
  A aplicação completa deve ser feita com suporte de um profissional de saúde.
</p>
<button onclick="mostrarResultado()">Ver avaliação parcial →</button>
<div id="resultado" style="margin-top:20px"></div>
</div><script>
var respostas={};
function sel(q,v,el){
  respostas[q]=v;
  el.parentElement.querySelectorAll(".opt").forEach(function(o){o.classList.remove("sel")});
  el.classList.add("sel");
}
function mostrarResultado(){
  var total=Object.values(respostas).reduce(function(a,b){return a+b},0);
  var n=Object.keys(respostas).length;
  if(n<2){alert("Responda as perguntas primeiro");return;}
  var media=(total/n)*20;
  var nivel=media>=75?"Boa":media>=50?"Moderada":"Baixa";
  document.getElementById("resultado").innerHTML=
    '<div style="background:white;border-radius:16px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,0.1)">'+
    '<h2 style="color:#38a169">Qualidade de Vida: '+nivel+'</h2>'+
    '<p style="color:#666">Score parcial: '+media.toFixed(0)+'/100</p>'+
    '<p style="color:#555;line-height:1.6">Para uma avaliação completa com os 26 itens do WHOQOL-BREF, '+
    'consulte seu psicólogo ou profissional de saúde.</p></div>';
}
</script></body></html>""")

class WHOQOLPlugin(PluginBase):
    name = "whoqol_bref"
    def setup(self, app): app.include_router(router)
plugin = WHOQOLPlugin()
