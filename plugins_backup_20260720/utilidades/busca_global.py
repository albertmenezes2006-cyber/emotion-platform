#!/usr/bin/env python3
"""Busca global na plataforma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/busca", tags=["Busca"])

INDICE = [
    {"titulo": "Avaliação PHQ-9", "url": "/app/avaliacao", "desc": "Questionário de depressão", "tags": ["phq9", "depressão", "avaliação"]},
    {"titulo": "Avaliação GAD-7", "url": "/app/avaliacao", "desc": "Questionário de ansiedade", "tags": ["gad7", "ansiedade", "avaliação"]},
    {"titulo": "Chat com IA", "url": "/app/chat", "desc": "Converse com nossa inteligência artificial", "tags": ["chat", "ia", "conversa"]},
    {"titulo": "Diário Emocional", "url": "/app/diario", "desc": "Registre seus sentimentos", "tags": ["diário", "humor", "registro"]},
    {"titulo": "Dashboard", "url": "/app/dashboard", "desc": "Veja sua evolução", "tags": ["dashboard", "gráficos", "evolução"]},
    {"titulo": "Planos e Preços", "url": "/precos", "desc": "Assine o plano ideal", "tags": ["plano", "preço", "assinatura"]},
    {"titulo": "Blog", "url": "/blog", "desc": "Artigos sobre saúde mental", "tags": ["blog", "artigos", "saúde mental"]},
    {"titulo": "FAQ", "url": "/faq", "desc": "Perguntas frequentes", "tags": ["faq", "dúvidas", "ajuda"]},
    {"titulo": "Status do Sistema", "url": "/status", "desc": "Verificar disponibilidade", "tags": ["status", "uptime", "sistema"]},
    {"titulo": "Calculadora de Burnout", "url": "/api/v1/burnout/pagina", "desc": "Calcule seu nível de burnout", "tags": ["burnout", "estresse", "trabalho"]},
    {"titulo": "Pagar com PIX", "url": "/api/v1/pix/pagar/99.90", "desc": "Pagamento via PIX", "tags": ["pix", "pagamento", "pagar"]},
    {"titulo": "Protocolo de Crise", "url": "/api/v1/crise/ajuda", "desc": "CVV e recursos de emergência", "tags": ["crise", "cvv", "emergência"]},
    {"titulo": "Widget para Psicólogos", "url": "/widget/demo", "desc": "Adicione ao seu site", "tags": ["widget", "integração", "site"]},
    {"titulo": "ROI Calculator", "url": "/roi", "desc": "Calcule seu retorno", "tags": ["roi", "economia", "valor"]},
]

@router.get("")
async def buscar(q: str = ""):
    # Sanitizar XSS
    import re as _re
    q = _re.sub(r'<[^>]*>', '', q)
    q = q.replace('"', '').replace("'", "").replace(";", "")[:100]
    if not q or len(q) < 2:
        return JSONResponse({"resultados": [], "total": 0})
    q_lower = q.lower()
    resultados = []
    for item in INDICE:
        score = 0
        if q_lower in item["titulo"].lower(): score += 10
        if q_lower in item["desc"].lower(): score += 5
        if any(q_lower in tag for tag in item["tags"]): score += 8
        if score > 0:
            resultados.append({**item, "score": score})
    resultados.sort(key=lambda x: x["score"], reverse=True)
    return JSONResponse({"resultados": resultados[:5], "total": len(resultados), "query": q})

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_busca():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Busca — Emotion Platform</title>
<style>
body{font-family:sans-serif;background:#f8f9fa;padding:40px 20px;margin:0}
.container{max-width:600px;margin:0 auto}
.search-box{display:flex;gap:8px;margin-bottom:20px}
input{flex:1;padding:16px;border-radius:12px;border:2px solid #667eea;font-size:16px;outline:none}
button{background:#667eea;color:white;border:none;border-radius:12px;
  padding:16px 24px;cursor:pointer;font-weight:700}
.resultado{background:white;border-radius:12px;padding:20px;margin-bottom:12px;
  box-shadow:0 2px 8px rgba(0,0,0,0.06);cursor:pointer;transition:transform 0.2s}
.resultado:hover{transform:translateX(4px);border-left:4px solid #667eea}
h3{margin:0 0 4px;color:#333} p{margin:0;color:#888;font-size:14px}
</style></head><body>
<div class="container">
<h1 style="color:#333">🔍 Buscar na Plataforma</h1>
<div class="search-box">
  <input id="q" type="text" placeholder="O que você procura?" oninput="buscar()" autofocus>
  <button onclick="buscar()">Buscar</button>
</div>
<div id="resultados"></div>
</div>
<script>
var timer;
function buscar(){
  clearTimeout(timer);
  timer=setTimeout(function(){
    var q=document.getElementById("q").value;
    if(q.length<2){document.getElementById("resultados").innerHTML="";return;}
    fetch("/api/v1/busca?q="+encodeURIComponent(q))
    .then(r=>r.json()).then(d=>{
      var html="";
      if(d.resultados.length===0){html="<p style='color:#888'>Nenhum resultado encontrado</p>";}
      d.resultados.forEach(function(r){
        html+="<div class='resultado' onclick="location.href='"+r.url+"'">"+
          "<h3>"+r.titulo+"</h3><p>"+r.desc+"</p></div>";
      });
      document.getElementById("resultados").innerHTML=html;
    });
  },300);
}
</script></body></html>""")

class BuscaPlugin(PluginBase):
    name = "busca_global"
    def setup(self, app): app.include_router(router)
plugin = BuscaPlugin()
