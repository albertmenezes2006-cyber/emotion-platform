#!/usr/bin/env python3
"""Timer de meditacao mindfulness"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/meditacao", tags=["Meditação"])

@router.get("", response_class=HTMLResponse)
async def timer_meditacao():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Meditação — Emotion Platform</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:linear-gradient(135deg,#0f0f1a,#1a1a2e);
  min-height:100vh;display:flex;flex-direction:column;align-items:center;
  justify-content:center;color:white;padding:20px;text-align:center}
h1{font-size:32px;margin-bottom:8px}
.timer{font-size:80px;font-weight:900;color:#667eea;
  text-shadow:0 0 40px rgba(102,126,234,0.8);margin:40px 0;font-family:monospace}
.frases{font-size:18px;color:rgba(255,255,255,0.7);
  max-width:400px;line-height:1.6;margin-bottom:40px;min-height:60px}
.tempos{display:flex;gap:12px;margin-bottom:40px;flex-wrap:wrap;justify-content:center}
.btn-t{background:rgba(255,255,255,0.1);border:2px solid rgba(255,255,255,0.2);
  color:white;padding:10px 20px;border-radius:50px;cursor:pointer;font-size:14px}
.btn-t.ativo{background:#667eea;border-color:#667eea}
.controles{display:flex;gap:16px}
.btn{padding:16px 32px;border-radius:50px;border:none;cursor:pointer;
  font-size:18px;font-weight:700;transition:all 0.2s}
.btn-iniciar{background:linear-gradient(135deg,#667eea,#764ba2);color:white}
.btn-parar{background:rgba(255,255,255,0.1);color:white;
  border:2px solid rgba(255,255,255,0.3)}
.circulo-outer{width:300px;height:300px;border-radius:50%;
  border:3px solid rgba(102,126,234,0.3);display:flex;align-items:center;
  justify-content:center;margin:0 auto 20px;position:relative}
.circulo-inner{width:200px;height:200px;border-radius:50%;
  background:radial-gradient(circle,rgba(102,126,234,0.2),transparent);
  border:2px solid rgba(102,126,234,0.5);
  animation:pulsar 4s ease-in-out infinite;display:flex;
  align-items:center;justify-content:center}
@keyframes pulsar{0%,100%{transform:scale(1);opacity:0.7}50%{transform:scale(1.1);opacity:1}}
</style></head><body>
<h1>🧘 Meditação Guiada</h1>
<p style="color:rgba(255,255,255,0.6);margin-bottom:30px">Mindfulness baseado em evidências</p>

<div class="tempos">
  <button class="btn-t ativo" onclick="setTempo(300,this)">5 min</button>
  <button class="btn-t" onclick="setTempo(600,this)">10 min</button>
  <button class="btn-t" onclick="setTempo(900,this)">15 min</button>
  <button class="btn-t" onclick="setTempo(1200,this)">20 min</button>
</div>

<div class="circulo-outer">
  <div class="circulo-inner">
    <div class="timer" id="timer">05:00</div>
  </div>
</div>

<div class="frases" id="frase">Encontre uma posição confortável e respire profundamente</div>

<div class="controles">
  <button class="btn btn-iniciar" onclick="iniciar()">▶ Iniciar</button>
  <button class="btn btn-parar" onclick="parar()">⏹ Parar</button>
</div>

<script>
var tempoTotal=300, tempoRestante=300, intervalo=null, rodando=false;
var frases=["Observe sua respiração sem julgamento",
  "Deixe os pensamentos passar como nuvens",
  "Foque no momento presente",
  "Sinta seu corpo relaxar a cada expiração",
  "Você está seguro. Você está presente.",
  "Observe as sensações sem tentar mudá-las",
  "Cada respiração é um novo começo",
  "Permita-se estar aqui, agora"];
var fidx=0;

function setTempo(s,btn){
  if(rodando) return;
  tempoTotal=s; tempoRestante=s;
  document.querySelectorAll(".btn-t").forEach(function(b){b.classList.remove("ativo");});
  btn.classList.add("ativo");
  atualizar();
}

function fmt(s){var m=Math.floor(s/60);return (m<10?"0":"")+m+":"+(s%60<10?"0":"")+(s%60);}

function atualizar(){document.getElementById("timer").textContent=fmt(tempoRestante);}

function iniciar(){
  if(rodando) return;
  rodando=true;
  intervalo=setInterval(function(){
    if(tempoRestante<=0){
      clearInterval(intervalo);rodando=false;
      document.getElementById("frase").textContent="✅ Parabéns! Sessão concluída.";
      document.getElementById("timer").textContent="00:00";
      return;
    }
    tempoRestante--;
    atualizar();
    if(tempoRestante%30===0){
      fidx=(fidx+1)%frases.length;
      document.getElementById("frase").textContent=frases[fidx];
    }
  },1000);
}

function parar(){
  clearInterval(intervalo);rodando=false;
  tempoRestante=tempoTotal;
  atualizar();
  document.getElementById("frase").textContent="Pressione Iniciar para começar";
}
</script>
</body></html>""")

class MeditacaoPlugin(PluginBase):
    name = "meditacao_timer"
    def setup(self, app): app.include_router(router)
plugin = MeditacaoPlugin()
