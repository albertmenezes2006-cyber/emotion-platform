#!/usr/bin/env python3
"""Calculadora ROI para psicologos"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/roi", tags=["Marketing"])

@router.get("", response_class=HTMLResponse)
async def pagina_roi():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Calculadora ROI — Emotion Platform</title>
<style>
body{font-family:sans-serif;max-width:600px;margin:40px auto;padding:20px}
input{width:100%;padding:8px;margin:8px 0;border:1px solid #ddd;border-radius:8px}
button{background:#667eea;color:white;border:none;padding:12px 24px;border-radius:8px;cursor:pointer;font-size:16px}
#resultado{margin-top:20px;padding:20px;background:#f0f4ff;border-radius:12px;display:none}
</style>
</head>
<body>
<h1>Calculadora ROI</h1>
<p>Calcule o retorno do investimento em saúde mental</p>
<label>Pacientes por semana</label>
<input type="number" id="pacientes" value="10">
<label>Sessões por paciente/mês</label>
<input type="number" id="sessoes" value="4">
<label>Valor por sessão (R$)</label>
<input type="number" id="valor" value="150">
<label>Horas admin por semana</label>
<input type="number" id="horas" value="8">
<br><br>
<button onclick="calcular()">Calcular ROI</button>
<div id="resultado">
  <h2>Resultado</h2>
  <div id="res"></div>
  <br>
  <button onclick="irParaPlanos()">Ver Planos</button>
</div>
<script>
function irParaPlanos() {
  window.location.href = "/app/planos";
}
function calcular() {
  var pac = parseInt(document.getElementById("pacientes").value) || 0;
  var ses = parseInt(document.getElementById("sessoes").value) || 0;
  var val = parseInt(document.getElementById("valor").value) || 0;
  var hor = parseInt(document.getElementById("horas").value) || 0;
  var receita = pac * ses * val;
  var economia = hor * 4 * 50;
  var total = receita + economia;
  document.getElementById("res").innerHTML =
    "<p><b>Receita mensal:</b> R$ " + receita.toLocaleString() + "</p>" +
    "<p><b>Economia em tempo:</b> R$ " + economia.toLocaleString() + "</p>" +
    "<p><b>ROI total estimado:</b> R$ " + total.toLocaleString() + "/mes</p>";
  document.getElementById("resultado").style.display = "block";
}
</script>
</body>
</html>""")

class Plugin(PluginBase):
    name = "calculadora_roi_marketing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
