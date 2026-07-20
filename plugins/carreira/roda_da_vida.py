#!/usr/bin/env python3
"""Roda da Vida interativa com Canvas"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/roda-da-vida", tags=["Coaching"])
@router.get("", response_class=HTMLResponse)
async def roda():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Roda da Vida</title>
<style>body{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}
.container{max-width:800px;margin:0 auto}
.header{background:linear-gradient(135deg,#667eea,#764ba2);color:white;
border-radius:20px;padding:28px;margin-bottom:24px;text-align:center}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-bottom:20px}
.area{background:white;border-radius:12px;padding:16px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.area label{display:block;font-weight:700;color:#333;margin-bottom:8px;font-size:14px}
.area .num{color:#667eea;font-size:22px;font-weight:900;margin-top:4px}
input[type=range]{width:100%;accent-color:#667eea}
canvas{display:block;margin:0 auto 16px;border-radius:50%}
button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;
border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-bottom:16px}
.insight{background:white;border-radius:16px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">Roda da Vida</h1>
<p style="opacity:0.9;margin:0">Avalie as 8 areas da sua vida de 0 a 10</p></div>
<div class="grid" id="grid"></div>
<button onclick="desenhar()">Gerar minha Roda da Vida</button>
<canvas id="canvas" width="360" height="360" style="display:none;margin-bottom:20px"></canvas>
<div class="insight" id="insight" style="display:none">
  <h2 style="color:#667eea;margin:0 0 12px">Insights</h2>
  <div id="insight-txt"></div>
</div>
</div>
<script>
var areas=[
  {n:"Saude",c:"#ef4444"},{n:"Carreira",c:"#f59e0b"},{n:"Financeiro",c:"#10b981"},
  {n:"Relacionamentos",c:"#3b82f6"},{n:"Familia",c:"#8b5cf6"},{n:"Desenvolvimento",c:"#06b6d4"},
  {n:"Proposito",c:"#ec4899"},{n:"Lazer",c:"#84cc16"}
];
var vals={};
var g=document.getElementById("grid");
areas.forEach(function(a,i){
  var div=document.createElement("div");div.className="area";
  div.innerHTML="<label>"+a.n+"</label>"+
  "<input type='range' min='0' max='10' value='5' id='r"+i+"' oninput='document.getElementById(\'n"+i+"\'  ).textContent=this.value' style='accent-color:"+a.c+"'>"+
  "<div class='num' id='n"+i+"'>5</div>";
  g.appendChild(div);vals[i]=5;
});
function desenhar(){
  var canvas=document.getElementById("canvas");
  canvas.style.display="block";
  var ctx=canvas.getContext("2d");
  var cx=180,cy=180,R=160;
  ctx.clearRect(0,0,360,360);
  ctx.fillStyle="#f8f9fa";ctx.beginPath();ctx.arc(cx,cy,R,0,Math.PI*2);ctx.fill();
  for(var g2=2;g2<=10;g2+=2){
    ctx.beginPath();ctx.arc(cx,cy,R*g2/10,0,Math.PI*2);
    ctx.strokeStyle="rgba(0,0,0,0.08)";ctx.lineWidth=1;ctx.stroke();
  }
  for(var i=0;i<8;i++){
    var ang=-Math.PI/2+i*Math.PI/4;
    ctx.beginPath();ctx.moveTo(cx,cy);
    ctx.lineTo(cx+R*Math.cos(ang),cy+R*Math.sin(ang));
    ctx.strokeStyle="rgba(0,0,0,0.1)";ctx.lineWidth=1;ctx.stroke();
  }
  var v={};
  for(var i=0;i<8;i++){v[i]=parseInt(document.getElementById("r"+i).value);}
  ctx.beginPath();
  for(var i=0;i<8;i++){
    var ang=-Math.PI/2+i*Math.PI/4;
    var r=R*v[i]/10;
    var x=cx+r*Math.cos(ang),y=cy+r*Math.sin(ang);
    if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
  }
  ctx.closePath();ctx.fillStyle="rgba(102,126,234,0.25)";ctx.fill();
  ctx.strokeStyle="#667eea";ctx.lineWidth=2;ctx.stroke();
  for(var i=0;i<8;i++){
    var ang=-Math.PI/2+i*Math.PI/4;
    var r=R*v[i]/10;
    ctx.beginPath();ctx.arc(cx+r*Math.cos(ang),cy+r*Math.sin(ang),5,0,Math.PI*2);
    ctx.fillStyle=areas[i].c;ctx.fill();
  }
  var soma=Object.values(v).reduce(function(a,b){return a+b},0);
  var media=soma/8;
  var minI=0,maxI=0;
  for(var i=1;i<8;i++){if(v[i]<v[minI])minI=i;if(v[i]>v[maxI])maxI=i;}
  document.getElementById("insight").style.display="block";
  document.getElementById("insight-txt").innerHTML=
  "<p><strong>Media geral: "+media.toFixed(1)+"/10</strong></p><br>"+
  "<p>Area mais forte: <strong>"+areas[maxI].n+" ("+v[maxI]+")</strong></p>"+
  "<p>Area para focar: <strong>"+areas[minI].n+" ("+v[minI]+")</strong></p><br>"+
  "<p style='color:#666'>Que pequena acao voce pode tomar essa semana para melhorar "+areas[minI].n+"?</p>";
  window.scrollTo(0,canvas.offsetTop-20);
}
</script></div></body></html>""")
class Plugin(PluginBase):
    name = "roda_da_vida"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
