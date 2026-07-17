#!/usr/bin/env python3
"""Tecnica Pomodoro adaptada para saude mental"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/pomodoro", tags=["Bem-estar"])

@router.get("", response_class=HTMLResponse)
async def pomodoro():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pomodoro Mental — Emotion Platform</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:linear-gradient(135deg,#e53e3e,#c53030);
  min-height:100vh;display:flex;flex-direction:column;align-items:center;
  justify-content:center;color:white;padding:20px;text-align:center}
.card{background:rgba(255,255,255,0.1);border-radius:24px;padding:48px;max-width:400px;width:100%;backdrop-filter:blur(10px)}
.timer{font-size:90px;font-weight:900;font-family:monospace;text-shadow:0 4px 20px rgba(0,0,0,0.3);margin:24px 0}
.fase{font-size:20px;font-weight:700;opacity:0.9;margin-bottom:8px}
.desc{font-size:14px;opacity:0.7;margin-bottom:32px;line-height:1.6}
.modos{display:flex;gap:8px;justify-content:center;margin-bottom:32px;flex-wrap:wrap}
.modo{background:rgba(255,255,255,0.15);border:2px solid rgba(255,255,255,0.3);color:white;
  padding:8px 16px;border-radius:50px;cursor:pointer;font-size:13px;font-weight:600}
.modo.ativo{background:white;color:#e53e3e}
.controles{display:flex;gap:12px;justify-content:center}
.btn{padding:14px 28px;border-radius:50px;border:none;cursor:pointer;
  font-size:16px;font-weight:700;transition:transform 0.2s}
.btn:hover{transform:scale(1.05)}
.btn-start{background:white;color:#e53e3e}
.btn-stop{background:rgba(255,255,255,0.2);color:white;border:2px solid rgba(255,255,255,0.4)}
.ciclos{margin-top:24px;font-size:14px;opacity:0.8}
.progress{background:rgba(255,255,255,0.2);border-radius:20px;height:6px;margin:16px 0;overflow:hidden}
.progress-bar{background:white;height:100%;border-radius:20px;transition:width 1s linear}
</style></head><body>
<div class="card">
  <h1 style="font-size:28px;margin-bottom:8px">🍅 Pomodoro Mental</h1>
  <p style="opacity:0.8;margin-bottom:24px;font-size:14px">Técnica de foco adaptada para bem-estar</p>
  <div class="modos">
    <div class="modo ativo" onclick="setModo(25,'trabalho',this)">Foco 25min</div>
    <div class="modo" onclick="setModo(5,'descanso',this)">Pausa 5min</div>
    <div class="modo" onclick="setModo(15,'longa',this)">Pausa Longa 15min</div>
  </div>
  <div class="fase" id="fase">Tempo de Foco</div>
  <div class="timer" id="timer">25:00</div>
  <div class="progress"><div class="progress-bar" id="pb" style="width:100%"></div></div>
  <div class="desc" id="desc">Foque em uma tarefa importante. Sem distrações por 25 minutos.</div>
  <div class="controles">
    <button class="btn btn-start" onclick="iniciar()" id="btn-start">▶ Iniciar</button>
    <button class="btn btn-stop" onclick="parar()">⏹ Parar</button>
  </div>
  <div class="ciclos" id="ciclos">🍅 0 pomodoros completos</div>
</div>
<script>
var tempo=25*60,total=25*60,modo="trabalho",timer=null,rodando=false,pomodoros=0;
var descricoes={trabalho:"Foque em uma tarefa importante. Sem distrações por 25 minutos.",
  descanso:"Descanse! Alongue-se, hidrate-se, respire fundo. Você merece.",
  longa:"Pausa longa. Caminhe, medite ou faça algo prazeroso."};
function fmt(s){return (Math.floor(s/60)<10?"0":"")+Math.floor(s/60)+":"+(s%60<10?"0":"")+s%60;}
function setModo(min,m,el){
  if(rodando)return;
  tempo=min*60;total=min*60;modo=m;
  document.querySelectorAll(".modo").forEach(b=>b.classList.remove("ativo"));
  el.classList.add("ativo");
  document.getElementById("timer").textContent=fmt(tempo);
  document.getElementById("pb").style.width="100%";
  var fases={trabalho:"Tempo de Foco",descanso:"Pausa Curta",longa:"Pausa Longa"};
  document.getElementById("fase").textContent=fases[m];
  document.getElementById("desc").textContent=descricoes[m];
}
function iniciar(){
  if(rodando)return;
  rodando=true;
  document.getElementById("btn-start").textContent="⏸ Pausar";
  timer=setInterval(function(){
    tempo--;
    document.getElementById("timer").textContent=fmt(tempo);
    document.getElementById("pb").style.width=(tempo/total*100)+"%";
    if(tempo<=0){
      clearInterval(timer);rodando=false;
      document.getElementById("btn-start").textContent="▶ Iniciar";
      if(modo==="trabalho"){pomodoros++;document.getElementById("ciclos").textContent="🍅 "+pomodoros+" pomodoros completos";}
      var sons=modo==="trabalho"?"⏰ Foco concluído! Hora de descansar!":"✅ Pausa terminada! Pronto para focar?";
      alert(sons);
    }
  },1000);
}
function parar(){clearInterval(timer);rodando=false;document.getElementById("btn-start").textContent="▶ Iniciar";}
</script></body></html>""")

class PomodoroPlugin(PluginBase):
    name = "pomodoro_mental"
    def setup(self, app): app.include_router(router)
plugin = PomodoroPlugin()
