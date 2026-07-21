#!/usr/bin/env python3
"""Box Breathing - Respiracao quadrada animada"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/box-breathing", tags=["Respiracao"])
@router.get("", response_class=HTMLResponse)
async def box():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Box Breathing</title>
<style>*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:#0d1117;min-height:100vh;display:flex;
flex-direction:column;align-items:center;justify-content:center;color:white;padding:20px}
h1{color:#58a6ff;margin-bottom:8px;font-size:24px}
.sub{color:#8b949e;margin-bottom:32px;text-align:center;font-size:14px}
.box{width:240px;height:240px;border:3px solid #58a6ff;border-radius:12px;
position:relative;margin:0 auto 24px}
.dot{width:18px;height:18px;background:#58a6ff;border-radius:50%;
position:absolute;top:-9px;left:-9px;box-shadow:0 0 15px #58a6ff;transition:all 1s linear}
.center{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center}
.fase{font-size:18px;font-weight:700;color:#58a6ff}
.num{font-size:56px;font-weight:900}
.btns{display:flex;gap:12px;justify-content:center}
.btn{padding:12px 24px;border-radius:50px;border:none;cursor:pointer;font-size:15px;font-weight:700}
.start{background:#58a6ff;color:#0d1117}
.stop{background:rgba(88,166,255,0.15);color:#58a6ff;border:2px solid #58a6ff}
.ciclos{margin-top:16px;color:#8b949e;font-size:14px}
</style></head><body>
<h1>Box Breathing</h1>
<p class="sub">Tecnica usada por Navy SEALs para controle do estresse</p>
<div class="box">
  <div class="dot" id="dot"></div>
  <div class="center"><div class="fase" id="fase">Pronto</div><div class="num" id="num">4</div></div>
</div>
<div class="btns">
  <button class="btn start" onclick="iniciar()">Iniciar</button>
  <button class="btn stop" onclick="parar()">Parar</button>
</div>
<div class="ciclos" id="ciclos"></div>
<script>
var fase=0,conta=4,ciclos=0,timer=null,rodando=false;
var W=240,sz=18,off=sz/2;
var pos=[
  function(t){return{top:(t/4*W-off)+"px",left:(-off)+"px"}},
  function(t){return{top:(W-off)+"px",left:(t/4*W-off)+"px"}},
  function(t){return{top:((1-t/4)*W-off)+"px",left:(W-off)+"px"}},
  function(t){return{top:(-off)+"px",left:((1-t/4)*W-off)+"px"}}
];
var nomes=["Inspire","Segure","Expire","Segure"];
function mover(f,c){
  var p=pos[f](4-c);
  var d=document.getElementById("dot");
  d.style.top=p.top;d.style.left=p.left;
}
function tick(){
  if(!rodando)return;
  document.getElementById("fase").textContent=nomes[fase];
  document.getElementById("num").textContent=conta;
  mover(fase,conta);
  conta--;
  if(conta<0){fase=(fase+1)%4;conta=4;if(fase===0){ciclos++;document.getElementById("ciclos").textContent=ciclos+" ciclo(s) completo(s)";}}
  timer=setTimeout(tick,1000);
}
function iniciar(){if(rodando)return;rodando=true;fase=0;conta=4;tick();}
function parar(){clearTimeout(timer);rodando=false;document.getElementById("fase").textContent="Parado";document.getElementById("num").textContent="4";}
</script></body></html>""")
class Plugin(PluginBase):
    name = "box_breathing_completo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
