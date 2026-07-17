#!/usr/bin/env python3
"""Escala de Autoestima de Rosenberg"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/rosenberg", tags=["Escalas"])

ITENS = [
    ("Sinto que sou uma pessoa de valor, pelo menos tanto quanto as outras", False),
    ("Sinto que tenho muitas qualidades", False),
    ("No geral, inclino-me a achar que sou um fracasso", True),
    ("Sou capaz de fazer coisas tão bem quanto a maioria das pessoas", False),
    ("Sinto que não tenho muito do que me orgulhar", True),
    ("Tenho uma atitude positiva em relação a mim mesmo", False),
    ("No geral, estou satisfeito comigo mesmo", False),
    ("Gostaria de ter mais respeito por mim mesmo", True),
    ("Às vezes me sinto inútil", True),
    ("Às vezes acho que não tenho préstimo algum", True),
]

@router.get("", response_class=HTMLResponse)
async def pagina_rosenberg():
    opts_label = ["Discordo totalmente", "Discordo", "Concordo", "Concordo totalmente"]
    pergs = ""
    for i, (item, reverso) in enumerate(ITENS):
        opts = "".join(f'<label style="display:flex;align-items:center;gap:6px;cursor:pointer;padding:4px 0"><input type="radio" name="q{i}" value="{j}"> <span style="font-size:13px;color:#555">{o}</span></label>' for j, o in enumerate(opts_label))
        pergs += f'<div style="background:#f8f9fa;border-radius:12px;padding:16px;margin-bottom:12px"><p style="font-weight:600;color:#333;margin:0 0 10px">{i+1}. {item}</p>{opts}</div>'
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Escala de Autoestima de Rosenberg</title>
<style>body{{font-family:sans-serif;background:#fff5f0;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#f59e0b,#d97706);color:white;border-radius:16px;padding:28px;margin-bottom:24px}}
button{{background:linear-gradient(135deg,#f59e0b,#d97706);color:white;border:none;border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
</style></head><body><div class="container">
<a href="/" style="color:#f59e0b;text-decoration:none">← Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">💛 Escala de Autoestima</h1>
<p style="opacity:0.9;margin:0">Rosenberg Self-Esteem Scale — Como você se vê</p></div>
<form onsubmit="calcular(event)">{pergs}
<button type="submit">Ver meu resultado →</button></form>
<div id="res" style="margin-top:20px"></div>
</div><script>
function calcular(e){{e.preventDefault();var total=0;
for(var i=0;i<10;i++){{var r=document.querySelector('input[name="q'+i+'"]:checked');
if(!r){{alert("Responda todas as perguntas");return;}}
var v=parseInt(r.value);var reverso=[2,4,7,8,9].includes(i);
total+=reverso?(3-v):v;}}
var nivel=total>=25?"Alta":total>=15?"Média":"Baixa";
var cor=total>=25?"#38a169":total>=15?"#d69e2e":"#e53e3e";
document.getElementById("res").innerHTML='<div style="background:white;border-radius:16px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.1)"><h2 style="color:'+cor+'">Score: '+total+'/30</h2><p style="font-size:20px;font-weight:700;color:'+cor+'">Autoestima '+nivel+'</p><p style="color:#666;line-height:1.6">'+
(total>=25?"Você demonstra boa autoestima e senso positivo de valor pessoal. Continue cultivando isso!":
total>=15?"Autoestima moderada. Há espaço para fortalecer sua autoimagem com suporte profissional.":
"Autoestima baixa identificada. Um psicólogo pode ajudá-lo a desenvolver uma visão mais positiva de si mesmo.")+
'</p></div>';}}
</script></body></html>""")

class RosenbergPlugin(PluginBase):
    name = "rosenberg_autoestima"
    def setup(self, app): app.include_router(router)
plugin = RosenbergPlugin()
