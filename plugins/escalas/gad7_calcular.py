#!/usr/bin/env python3
"""Escala GAD-7 — Ansiedade Generalizada"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/gad7", tags=["Escalas"])

PERGUNTAS = [
    "Sentir-se nervoso, ansioso ou muito tenso",
    "Nao ser capaz de impedir ou controlar as preocupacoes",
    "Preocupar-se muito com diversas coisas",
    "Dificuldade para relaxar",
    "Ficar tao agitado que se torna dificil permanecer sentado",
    "Ficar facilmente aborrecido ou irritavel",
    "Sentir medo como se algo horrivel fosse acontecer",
]

@router.get("", response_class=HTMLResponse)
async def pagina_gad7():
    pergs = ""
    opcoes = ["Nunca (0)", "Varios dias (1)", "Mais da metade (2)", "Quase todos os dias (3)"]
    for i, p in enumerate(PERGUNTAS):
        opts = "".join(
            f'<label style="display:flex;align-items:center;gap:8px;padding:4px 0;cursor:pointer">' +
            f'<input type="radio" name="q{i}" value="{j}"> {o}</label>'
            for j, o in enumerate(opcoes)
        )
        pergs += f'<div style="background:#f8f9fa;border-radius:12px;padding:16px;margin-bottom:12px"><p style="font-weight:600;margin:0 0 10px">{i+1}. {p}</p>{opts}</div>'
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>GAD-7</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px}}
.container{{max-width:700px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border-radius:16px;padding:28px;margin-bottom:24px}}
button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
</style></head><body><div class="container">
<div class="header"><h1 style="margin:0 0 8px">GAD-7</h1>
<p style="opacity:0.9;margin:0">Escala de Ansiedade — Ultimos 14 dias</p></div>
<form onsubmit="calcular(event)">{pergs}
<button type="submit">Calcular Score</button></form>
<div id="resultado" style="margin-top:20px"></div>
</div><script>
function calcular(e){{e.preventDefault();var total=0;
for(var i=0;i<7;i++){{var r=document.querySelector('input[name="q'+i+'"]:checked');
if(!r){{alert("Responda todas");return;}}total+=parseInt(r.value);}}
var nivel=total<=4?"Minima":total<=9?"Leve":total<=14?"Moderada":"Grave";
var cor=total<=4?"#38a169":total<=9?"#d69e2e":total<=14?"#dd6b20":"#e53e3e";
document.getElementById("resultado").innerHTML='<div style="background:white;border-radius:16px;padding:28px"><h2 style="color:'+cor+'">Score: '+total+'/21</h2><p style="color:'+cor+';font-weight:700">Ansiedade '+nivel+'</p></div>';}}
</script></body></html>""")

@router.post("/calcular")
async def calcular_gad7(request: Request):
    try:
        body = await request.json()
        respostas = body if isinstance(body, list) else body.get("respostas", [])
    except Exception:
        respostas = []
    total = 0
    for v in respostas[:7]:
        try:
            total += int(v)
        except Exception:
            pass
    nivel = "Minima" if total <= 4 else "Leve" if total <= 9 else "Moderada" if total <= 14 else "Grave"
    return JSONResponse({
        "score": total, "max": 21, "nivel": nivel,
        "percentual": round(total/21*100, 1),
        "alerta": total >= 15
    })

@router.get("/info")
async def info_gad7():
    return JSONResponse({"nome": "GAD-7", "perguntas": 7, "max": 21,
                         "classificacao": {"0-4": "Minima", "5-9": "Leve",
                                           "10-14": "Moderada", "15-21": "Grave"}})

class GAD7Plugin(PluginBase):
    name = "gad7_ansiedade"
    def setup(self, app):
        app.include_router(router)

plugin = GAD7Plugin()
