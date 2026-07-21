#!/usr/bin/env python3
"""Columbia Suicide Severity Rating Scale simplificada"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/columbia", tags=["Crise"])

@router.get("", response_class=HTMLResponse)
async def columbia_ssrs():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Avaliação de Risco — Emotion Platform</title>
<style>body{font-family:sans-serif;background:#fff5f5;padding:20px;margin:0}
.container{max-width:600px;margin:0 auto}
.urgente{background:#e53e3e;color:white;border-radius:16px;padding:24px;margin-bottom:20px}
.card{background:white;border-radius:14px;padding:20px;margin-bottom:14px;box-shadow:0 2px 8px rgba(0,0,0,0.08)}
.q{font-weight:600;color:#333;margin-bottom:12px}
.opts{display:flex;gap:10px}
.opt{background:#f0f0f0;border:2px solid #e0e0e0;border-radius:8px;padding:10px 16px;
  cursor:pointer;font-size:14px;font-weight:600;transition:all 0.2s}
.opt.sel-sim{background:#e53e3e;color:white;border-color:#e53e3e}
.opt.sel-nao{background:#38a169;color:white;border-color:#38a169}
button{background:#667eea;color:white;border:none;border-radius:12px;padding:14px;
  font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-top:8px}
</style></head><body><div class="container">
<div class="urgente">
  <h1 style="margin:0 0 8px">⚠️ Avaliação de Risco</h1>
  <p style="margin:0;opacity:0.9">Se você está em crise agora: <strong>ligue 188 (CVV)</strong></p>
</div>
<p style="color:#555;margin-bottom:20px;line-height:1.7">
  As perguntas a seguir são sobre pensamentos que algumas pessoas têm. Responda honestamente.
  Suas respostas são confidenciais e serão usadas para oferecer o melhor suporte.
</p>
<div class="card"><div class="q">1. Você já desejou estar morto ou adormecer e não acordar mais?</div>
<div class="opts"><div class="opt" onclick="resp(1,'sim',this)">Sim</div><div class="opt" onclick="resp(1,'nao',this)">Não</div></div></div>
<div class="card"><div class="q">2. Você teve pensamentos de se machucar ou se matar?</div>
<div class="opts"><div class="opt" onclick="resp(2,'sim',this)">Sim</div><div class="opt" onclick="resp(2,'nao',this)">Não</div></div></div>
<div class="card"><div class="q">3. Você pensou em métodos para se machucar?</div>
<div class="opts"><div class="opt" onclick="resp(3,'sim',this)">Sim</div><div class="opt" onclick="resp(3,'nao',this)">Não</div></div></div>
<div class="card"><div class="q">4. Você teve intenção de agir sobre esses pensamentos?</div>
<div class="opts"><div class="opt" onclick="resp(4,'sim',this)">Sim</div><div class="opt" onclick="resp(4,'nao',this)">Não</div></div></div>
<div class="card"><div class="q">5. Você tem planos concretos para se machucar?</div>
<div class="opts"><div class="opt" onclick="resp(5,'sim',this)">Sim</div><div class="opt" onclick="resp(5,'nao',this)">Não</div></div></div>
<button onclick="avaliar()">Ver avaliação →</button>
<div id="resultado" style="margin-top:20px"></div>
</div><script>
var respostas={};
function resp(q,v,el){
  respostas[q]=v;
  var parent=el.parentElement;
  parent.querySelectorAll(".opt").forEach(function(o){o.className="opt";});
  el.classList.add("sel-"+v);
}
function avaliar(){
  var sims=Object.values(respostas).filter(v=>v==="sim").length;
  var r=document.getElementById("resultado");
  if(respostas[4]==="sim"||respostas[5]==="sim"){
    r.innerHTML='<div style="background:#e53e3e;color:white;border-radius:16px;padding:24px">'+
    '<h2>🆘 Risco ALTO — Ação Imediata</h2>'+
    '<p>Por favor, entre em contato AGORA:</p>'+
    '<a href="tel:188" style="display:block;background:white;color:#e53e3e;padding:14px;border-radius:8px;text-align:center;text-decoration:none;font-weight:800;margin:8px 0;font-size:18px">📞 CVV — 188</a>'+
    '<a href="tel:192" style="display:block;background:rgba(255,255,255,0.2);color:white;padding:14px;border-radius:8px;text-align:center;text-decoration:none;font-weight:800">🚑 SAMU — 192</a>'+
    '</div>';
  } else if(sims>=2){
    r.innerHTML='<div style="background:#dd6b20;color:white;border-radius:16px;padding:24px">'+
    '<h2>⚠️ Risco MODERADO</h2>'+
    '<p>Recomendamos falar com um psicólogo ou psiquiatra o mais breve possível.</p>'+
    '<p>CVV disponível 24h: <strong>188</strong></p></div>';
  } else {
    r.innerHTML='<div style="background:#38a169;color:white;border-radius:16px;padding:24px">'+
    '<h2>✅ Risco BAIXO</h2>'+
    '<p>Continue monitorando seu bem-estar. Se os pensamentos aumentarem, procure ajuda.</p>'+
    '<p>CVV: <strong>188</strong> | Sempre disponível.</p></div>';
  }
}
</script></body></html>""")

class ColumbiaPlugin(PluginBase):
    name = "columbia_ssrs_crise"
    def setup(self, app): app.include_router(router)
plugin = ColumbiaPlugin()
