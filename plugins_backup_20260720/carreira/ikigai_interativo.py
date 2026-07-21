#!/usr/bin/env python3
"""Ikigai - Encontrando seu proposito"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from pathlib import Path
import json
router = APIRouter(prefix="/ikigai", tags=["Carreira"])
ARQUIVO = Path("ikigai_dados.json")
@router.post("/salvar")
async def salvar(request: Request):
    d = await request.json()
    ARQUIVO.write_text(json.dumps(d, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True})
@router.get("", response_class=HTMLResponse)
async def ikigai():
    dados = json.loads(ARQUIVO.read_text()) if ARQUIVO.exists() else {}
    return HTMLResponse(f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ikigai - Seu Proposito</title>
<style>body{{font-family:sans-serif;background:#fff9f0;padding:20px;margin:0}}
.container{{max-width:800px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#f59e0b,#ef4444);color:white;
border-radius:20px;padding:28px;margin-bottom:24px;text-align:center}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:24px}}
.secao{{background:white;border-radius:16px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}}
textarea{{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;
font-size:14px;resize:vertical;min-height:100px;box-sizing:border-box;font-family:inherit}}
textarea:focus{{outline:none}}
.amor{{border-top:4px solid #ef4444}}.amor h2{{color:#ef4444}}
.bom{{border-top:4px solid #f59e0b}}.bom h2{{color:#f59e0b}}
.pago{{border-top:4px solid #10b981}}.pago h2{{color:#10b981}}
.mundo{{border-top:4px solid #667eea}}.mundo h2{{color:#667eea}}
button{{background:linear-gradient(135deg,#f59e0b,#ef4444);color:white;border:none;
border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
.resultado{{background:white;border-radius:16px;padding:24px;margin-top:20px;display:none;
box-shadow:0 4px 20px rgba(0,0,0,0.08);text-align:center}}
@media(max-width:600px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body><div class="container">
<a href="/" style="color:#f59e0b;text-decoration:none">Voltar</a>
<div class="header"><h1 style="margin:0 0 8px">Ikigai</h1>
<p style="opacity:0.9;margin:0">Encontre sua razao de ser</p></div>
<div class="grid">
  <div class="secao amor"><h2>O que voce AMA</h2>
  <textarea id="amor" placeholder="O que te traz alegria?">{dados.get("amor","")}</textarea></div>
  <div class="secao bom"><h2>No que e BOM</h2>
  <textarea id="bom" placeholder="Suas habilidades e talentos...">{dados.get("bom","")}</textarea></div>
  <div class="secao mundo"><h2>O que o MUNDO precisa</h2>
  <textarea id="mundo" placeholder="Que problemas pode resolver?">{dados.get("mundo","")}</textarea></div>
  <div class="secao pago"><h2>Pelo que pode ser PAGO</h2>
  <textarea id="pago" placeholder="Como monetizar suas habilidades?">{dados.get("pago","")}</textarea></div>
</div>
<button onclick="calcular()">Encontrar meu Ikigai</button>
<div class="resultado" id="resultado">
  <div style="font-size:48px;margin-bottom:12px">Seu Ikigai</div>
  <p style="color:#666;line-height:1.7">No centro de tudo que voce ama, e bom, o mundo precisa e pode ser pago esta seu proposito de vida.</p>
</div>
</div>
<script>
function calcular(){{
  var a=document.getElementById("amor").value;
  var b=document.getElementById("bom").value;
  var m=document.getElementById("mundo").value;
  var p=document.getElementById("pago").value;
  if(!a||!b||!m||!p){{alert("Preencha todos os campos");return;}}
  fetch("/ikigai/salvar",{{method:"POST",headers:{{"Content-Type":"application/json"}},
  body:JSON.stringify({{amor:a,bom:b,mundo:m,pago:p}})}});
  document.getElementById("resultado").style.display="block";
  window.scrollTo(0,document.getElementById("resultado").offsetTop);
}}
</script></body></html>""")
class Plugin(PluginBase):
    name = "ikigai_interativo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
