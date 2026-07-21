#!/usr/bin/env python3
"""Escala de Estresse Percebido PSS-10"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/pss", tags=["Escalas"])

PERGUNTAS = [
    ("No último mês, com que frequência ficou chateado por algo inesperado?", False),
    ("No último mês, com que frequência sentiu dificuldade de controlar coisas importantes?", False),
    ("No último mês, com que frequência se sentiu nervoso e estressado?", False),
    ("No último mês, com que frequência sentiu confiança de lidar com problemas?", True),
    ("No último mês, com que frequência as coisas correram como queria?", True),
    ("No último mês, com que frequência sentiu não aguentar tudo que tinha que fazer?", False),
    ("No último mês, com que frequência conseguiu controlar as irritações da vida?", True),
    ("No último mês, com que frequência sentiu estar por cima das dificuldades?", True),
    ("No último mês, com que frequência ficou bravo por coisas fora do seu controle?", False),
    ("No último mês, com que frequência sentiu que dificuldades se acumulavam a ponto de não conseguir superá-las?", False),
]

@router.get("", response_class=HTMLResponse)
async def pagina_pss():
    pergs_html = ""
    opcoes = ["Nunca (0)", "Quase nunca (1)", "Às vezes (2)", "Com alguma frequência (3)", "Muito frequente (4)"]
    for i, (p, reverso) in enumerate(PERGUNTAS):
        opts = "".join(f'<label style="display:flex;align-items:center;gap:6px;cursor:pointer;padding:4px 0"><input type="radio" name="q{i}" value="{j}"> <span style="font-size:13px;color:#555">{o}</span></label>' for j, o in enumerate(opcoes))
        tag = ' <span style="font-size:11px;color:#38a169;background:#e8f5e9;padding:1px 6px;border-radius:10px">R</span>' if reverso else ""
        pergs_html += f'<div style="background:#f8f9fa;border-radius:12px;padding:16px;margin-bottom:12px"><p style="font-weight:600;color:#333;margin:0 0 10px">{i+1}. {p}{tag}</p>{opts}</div>'
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>PSS-10 — Estresse Percebido</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border-radius:16px;padding:28px;margin-bottom:24px}}
button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer;margin-top:8px}}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">📊 PSS-10</h1>
<p style="opacity:0.9;margin:0">Escala de Estresse Percebido — Últimos 30 dias</p></div>
<form onsubmit="calcular(event)">{pergs_html}
<button type="submit">Calcular Score de Estresse →</button></form>
<div id="resultado" style="margin-top:20px"></div>
</div><script>
function calcular(e){{e.preventDefault();var total=0;
for(var i=0;i<10;i++){{var r=document.querySelector('input[name="q'+i+'"]:checked');
if(!r){{alert("Responda todas as perguntas");return;}}
var v=parseInt(r.value);var reverso=[3,4,6,7].includes(i);
total+=reverso?(4-v):v;}}
var nivel=total<=13?"Baixo":total<=26?"Moderado":"Alto";
var cor=total<=13?"#38a169":total<=26?"#d69e2e":"#e53e3e";
document.getElementById("resultado").innerHTML='<div style="background:white;border-radius:16px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.1)"><h2 style="color:'+cor+'">Score: '+total+'/40</h2><p style="font-size:18px;font-weight:700;color:'+cor+'">Estresse '+nivel+'</p><p style="color:#666">'+
(total<=13?"Seu nível de estresse está dentro do esperado. Continue cuidando de si mesmo.":
total<=26?"Nível moderado de estresse. Pratique técnicas de manejo e converse com um psicólogo.":
"Nível alto de estresse. Recomenda-se suporte psicológico urgente. Ligue 188 (CVV) se precisar.")+
'</p><a href="/api/v1/crise/ajuda" style="color:#e53e3e;font-size:14px">Em crise? Acesse recursos de ajuda</a></div>';}}
</script></body></html>""")

@router.post("/calcular")
async def calcular_pss(respostas: list):
    total = 0
    reversos = {3, 4, 6, 7}
    for i, v in enumerate(respostas[:10]):
        total += (4 - v) if i in reversos else v
    nivel = "Baixo" if total <= 13 else "Moderado" if total <= 26 else "Alto"
    return JSONResponse({"score": total, "max": 40, "nivel": nivel,
                         "percentual": round(total/40*100, 1)})

class PSSPlugin(PluginBase):
    name = "pss10_estresse"
    def setup(self, app): app.include_router(router)
plugin = PSSPlugin()
