#!/usr/bin/env python3
"""Tecnica 5-4-3-2-1 Grounding para ansiedade"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
router = APIRouter(prefix="/grounding", tags=["Grounding"])
@router.get("", response_class=HTMLResponse)
async def grounding():
    return HTMLResponse("""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grounding 5-4-3-2-1</title>
<style>*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:linear-gradient(180deg,#1a1a2e,#16213e);
min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px;color:white}
.card{background:rgba(255,255,255,0.05);border-radius:24px;padding:36px;
max-width:480px;width:100%;backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.1)}
h1{text-align:center;font-size:26px;margin-bottom:6px;color:#a78bfa}
.sub{text-align:center;color:rgba(255,255,255,0.6);margin-bottom:28px;font-size:14px;line-height:1.6}
.prog{display:flex;gap:6px;justify-content:center;margin-bottom:24px}
.pt{width:12px;height:12px;border-radius:50%;background:rgba(255,255,255,0.2);transition:background 0.3s}
.pt.ok{background:#a78bfa}
.etapa{display:none} .etapa.ativa{display:block;animation:fade 0.5s ease}
@keyframes fade{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.num{font-size:52px;font-weight:900;color:#a78bfa;text-align:center;margin-bottom:6px}
.titulo{font-size:20px;font-weight:700;text-align:center;margin-bottom:8px}
.desc{color:rgba(255,255,255,0.7);margin-bottom:16px;line-height:1.6;text-align:center;font-size:14px}
input{width:100%;padding:10px;border-radius:8px;background:rgba(255,255,255,0.1);
border:1px solid rgba(255,255,255,0.2);color:white;font-size:14px;
margin-bottom:6px;box-sizing:border-box}
input::placeholder{color:rgba(255,255,255,0.4)}
input:focus{outline:none;border-color:#a78bfa}
.btn{background:#a78bfa;color:#1a1a2e;border:none;border-radius:12px;
padding:14px;font-size:15px;font-weight:700;width:100%;cursor:pointer;margin-top:8px}
.final{text-align:center;display:none}
.final h2{color:#a78bfa;font-size:28px;margin-bottom:12px}
.final p{color:rgba(255,255,255,0.7);line-height:1.7}
</style></head><body><div class="card">
<h1>Grounding 5-4-3-2-1</h1>
<p class="sub">Tecnica para ancoragem no momento presente.<br>Reduz ansiedade em minutos.</p>
<div class="prog"><div class="pt ok" id="p0"></div><div class="pt" id="p1"></div>
<div class="pt" id="p2"></div><div class="pt" id="p3"></div><div class="pt" id="p4"></div></div>
<div class="etapa ativa" id="e0">
  <div class="num">5</div><div class="titulo">VEJA 5 coisas</div>
  <div class="desc">Olhe ao redor e nomeie 5 coisas que pode ver agora</div>
  <input id="v1" placeholder="1a coisa que vejo...">
  <input id="v2" placeholder="2a coisa que vejo...">
  <input id="v3" placeholder="3a coisa que vejo...">
  <input id="v4" placeholder="4a coisa que vejo...">
  <input id="v5" placeholder="5a coisa que vejo...">
</div>
<div class="etapa" id="e1">
  <div class="num">4</div><div class="titulo">TOQUE 4 coisas</div>
  <div class="desc">Toque 4 objetos e perceba a textura deles</div>
  <input id="t1" placeholder="1a coisa que toco...">
  <input id="t2" placeholder="2a coisa que toco...">
  <input id="t3" placeholder="3a coisa que toco...">
  <input id="t4" placeholder="4a coisa que toco...">
</div>
<div class="etapa" id="e2">
  <div class="num">3</div><div class="titulo">OUCA 3 sons</div>
  <div class="desc">Feche os olhos e identifique 3 sons ao redor</div>
  <input id="s1" placeholder="1o som que ouco...">
  <input id="s2" placeholder="2o som que ouco...">
  <input id="s3" placeholder="3o som que ouco...">
</div>
<div class="etapa" id="e3">
  <div class="num">2</div><div class="titulo">CHEIRE 2 aromas</div>
  <div class="desc">Identifique 2 cheiros ao seu redor agora</div>
  <input id="c1" placeholder="1o aroma...">
  <input id="c2" placeholder="2o aroma...">
</div>
<div class="etapa" id="e4">
  <div class="num">1</div><div class="titulo">SABOREIE 1 sabor</div>
  <div class="desc">Perceba 1 sabor na sua boca agora</div>
  <input id="sa1" placeholder="Sabor que percebo...">
</div>
<div class="final" id="final">
  <h2>Voce esta presente!</h2>
  <p>Excelente trabalho. Voce acabou de ancorar sua atencao no momento presente.<br><br>
  Respire fundo 3 vezes. A ansiedade ja diminuiu.</p>
  <button class="btn" onclick="reiniciar()" style="margin-top:20px">Praticar novamente</button>
</div>
<button class="btn" id="btnp" onclick="proximo()">Proxima etapa</button>
</div>
<script>
var e=0;
function proximo(){
  document.getElementById("e"+e).classList.remove("ativa");
  document.getElementById("p"+e).classList.remove("ok");
  e++;
  if(e>=5){
    document.getElementById("final").style.display="block";
    document.getElementById("btnp").style.display="none";return;
  }
  document.getElementById("e"+e).classList.add("ativa");
  document.getElementById("p"+e).classList.add("ok");
  if(e===4)document.getElementById("btnp").textContent="Finalizar";
}
function reiniciar(){
  e=0;
  document.querySelectorAll(".etapa").forEach(function(x){x.classList.remove("ativa");});
  document.querySelectorAll(".pt").forEach(function(x){x.classList.remove("ok");});
  document.getElementById("e0").classList.add("ativa");
  document.getElementById("p0").classList.add("ok");
  document.getElementById("final").style.display="none";
  document.getElementById("btnp").style.display="block";
  document.getElementById("btnp").textContent="Proxima etapa";
}
</script></div></body></html>""")
class Plugin(PluginBase):
    name = "grounding_54321"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
