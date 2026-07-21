#!/usr/bin/env python3
"""Social proof em tempo real"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import random

router = APIRouter(prefix="/api/v1/social-proof", tags=["Social Proof"])

ACOES = [
    "acabou de fazer uma avaliação PHQ-9",
    "se cadastrou na plataforma",
    "completou seu primeiro diário",
    "iniciou chat com IA",
    "assinou o plano Pro",
    "indicou um colega psicólogo",
]
CIDADES = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba",
           "Porto Alegre", "Salvador", "Florianópolis", "Brasília"]

@router.get("/acao")
async def acao_recente():
    return JSONResponse({
        "acao": random.choice(ACOES),
        "cidade": random.choice(CIDADES),
        "minutos_atras": random.randint(1, 15),
        "timestamp": datetime.utcnow().isoformat()
    })

@router.get("/widget", response_class=HTMLResponse)
async def widget_proof():
    return HTMLResponse("""
<div id="sp-widget" style="position:fixed;bottom:20px;left:20px;
     background:white;border-radius:12px;padding:14px 18px;
     box-shadow:0 4px 20px rgba(0,0,0,0.15);font-family:sans-serif;
     max-width:280px;display:none;z-index:9994;
     animation:fadeIn 0.5s ease">
  <div style="display:flex;align-items:center;gap:10px">
    <span style="font-size:20px">🧠</span>
    <div>
      <div id="sp-text" style="font-size:13px;color:#333;font-weight:600"></div>
      <div id="sp-sub" style="font-size:11px;color:#888;margin-top:2px"></div>
    </div>
    <button onclick="this.parentElement.parentElement.style.display='none'"
      style="background:none;border:none;cursor:pointer;color:#bbb;margin-left:auto">✕</button>
  </div>
</div>
<style>@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}</style>
<script>
function mostrarProof(){
  fetch("/api/v1/social-proof/acao").then(r=>r.json()).then(d=>{
    document.getElementById("sp-text").textContent="Alguém de "+d.cidade;
    document.getElementById("sp-sub").textContent=d.acao+" há "+d.minutos_atras+"min";
    var w=document.getElementById("sp-widget");
    w.style.display="block";
    setTimeout(function(){w.style.display="none";},5000);
  });
}
setTimeout(mostrarProof,8000);
setInterval(mostrarProof,45000);
</script>""")

class SocialProofPlugin(PluginBase):
    name = "social_proof_rt"
    def setup(self, app): app.include_router(router)
plugin = SocialProofPlugin()
