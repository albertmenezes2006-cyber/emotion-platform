#!/usr/bin/env python3
"""Tecnicas de respiracao guiada com animacao"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/respiracao", tags=["Respiração"])

@router.get("", response_class=HTMLResponse)
async def pagina_respiracao():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Respiração Guiada — Emotion Platform</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:linear-gradient(135deg,#1a1a2e,#16213e);
  min-height:100vh;display:flex;flex-direction:column;align-items:center;
  justify-content:center;color:white;padding:20px}
h1{font-size:28px;margin-bottom:8px;text-align:center}
.sub{color:rgba(255,255,255,0.7);margin-bottom:40px;text-align:center}
.tecnicas{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-bottom:40px}
.btn-tec{background:rgba(255,255,255,0.1);border:2px solid rgba(255,255,255,0.3);
  color:white;padding:10px 20px;border-radius:50px;cursor:pointer;font-size:14px;
  transition:all 0.2s}
.btn-tec.ativo,.btn-tec:hover{background:#667eea;border-color:#667eea}
.circulo-container{position:relative;width:200px;height:200px;margin:0 auto 32px}
.circulo{width:200px;height:200px;border-radius:50%;
  background:radial-gradient(circle,rgba(102,126,234,0.8),rgba(118,75,162,0.4));
  transition:transform 1s ease-in-out;display:flex;align-items:center;
  justify-content:center;font-size:16px;font-weight:700;
  box-shadow:0 0 60px rgba(102,126,234,0.5)}
.instrucao{font-size:32px;font-weight:800;color:#667eea;margin-bottom:8px;
  min-height:50px;text-align:center}
.fase{font-size:18px;color:rgba(255,255,255,0.8);margin-bottom:32px;text-align:center}
.controles{display:flex;gap:12px}
.btn{background:#667eea;color:white;border:none;padding:14px 28px;
  border-radius:12px;cursor:pointer;font-size:16px;font-weight:700}
.btn.stop{background:rgba(255,255,255,0.1);border:2px solid rgba(255,255,255,0.3)}
.ciclos{color:rgba(255,255,255,0.6);margin-top:20px;font-size:14px;text-align:center}
</style></head><body>
<h1>🫁 Respiração Guiada</h1>
<p class="sub">Técnicas baseadas em evidências para reduzir ansiedade</p>

<div class="tecnicas">
  <button class="btn-tec ativo" onclick="setTec('478')">4-7-8</button>
  <button class="btn-tec" onclick="setTec('box')">Box Breathing</button>
  <button class="btn-tec" onclick="setTec('coerente')">Respiração Coerente</button>
  <button class="btn-tec" onclick="setTec('478')">Wim Hof (simplificado)</button>
</div>

<div class="circulo-container">
  <div class="circulo" id="circulo">Pronto</div>
</div>
<div class="instrucao" id="instrucao">0</div>
<div class="fase" id="fase">Selecione uma técnica e pressione Iniciar</div>
<div class="controles">
  <button class="btn" onclick="iniciar()">▶ Iniciar</button>
  <button class="btn stop" onclick="parar()">⏹ Parar</button>
</div>
<div class="ciclos" id="ciclos"></div>

<script>
var tecnicas = {
  "478": {nome:"4-7-8",fases:[{n:"Inspire",d:4},{n:"Segure",d:7},{n:"Expire",d:8}]},
  "box": {nome:"Box Breathing",fases:[{n:"Inspire",d:4},{n:"Segure",d:4},{n:"Expire",d:4},{n:"Segure",d:4}]},
  "coerente": {nome:"Coerente",fases:[{n:"Inspire",d:5},{n:"Expire",d:5}]}
};
var tecAtual="478", timer=null, ciclo=0, faseidx=0, conta=0, rodando=false;

function setTec(id){
  tecAtual=id;
  document.querySelectorAll(".btn-tec").forEach(function(b,i){b.classList.remove("ativo");});
  event.target.classList.add("ativo");
  document.getElementById("fase").textContent=tecnicas[id].nome+" selecionado";
}

function iniciar(){
  if(rodando) return;
  rodando=true; ciclo=0; faseidx=0; conta=0;
  prox();
}

function prox(){
  if(!rodando) return;
  var tec=tecnicas[tecAtual];
  if(faseidx>=tec.fases.length){faseidx=0;ciclo++;}
  var fase=tec.fases[faseidx];
  conta=fase.d;
  document.getElementById("fase").textContent=fase.n;
  var inspirar=fase.n==="Inspire";
  var segurar=fase.n==="Segure";
  document.getElementById("circulo").style.transform=
    inspirar?"scale(1.4)":segurar?"scale(1.4)":"scale(0.8)";
  document.getElementById("ciclos").textContent="Ciclo "+ciclo+" completo";
  var t=setInterval(function(){
    if(!rodando){clearInterval(t);return;}
    document.getElementById("instrucao").textContent=conta;
    conta--;
    if(conta<0){clearInterval(t);faseidx++;prox();}
  },1000);
}

function parar(){
  rodando=false;
  document.getElementById("circulo").style.transform="scale(1)";
  document.getElementById("circulo").textContent="Pronto";
  document.getElementById("instrucao").textContent="";
  document.getElementById("fase").textContent="Parado. Pressione Iniciar para recomeçar.";
  document.getElementById("ciclos").textContent="";
}
</script>
</body></html>""")

class RespiracaoGuidadaPlugin(PluginBase):
    name = "respiracao_guiada_animada"
    def setup(self, app): app.include_router(router)
plugin = RespiracaoGuidadaPlugin()
