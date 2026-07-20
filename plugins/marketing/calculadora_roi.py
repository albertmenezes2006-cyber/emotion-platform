#!/usr/bin/env python3
"""Calculadora de ROI para psicologos"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/roi", tags=["Marketing"])

@router.get("", response_class=HTMLResponse)
async def calculadora_roi():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Calculadora de ROI — Emotion Platform</title>
<style>
body{font-family:sans-serif;background:linear-gradient(135deg,#667eea,#764ba2);
  min-height:100vh;display:flex;align-items:center;justify-content:center;margin:0;padding:20px}
.card{background:white;border-radius:24px;padding:40px;max-width:500px;width:100%;
      box-shadow:0 25px 50px rgba(0,0,0,0.2)}
h1{color:#333;margin:0 0 8px;font-size:24px} p{color:#888;margin:0 0 24px}
label{display:block;margin:12px 0 4px;font-weight:600;color:#444;font-size:14px}
input{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;
  font-size:16px;box-sizing:border-box}
input:focus{border-color:#667eea;outline:none}
.resultado{background:#f0f4ff;border-radius:16px;padding:24px;margin-top:24px}
.metric{display:flex;justify-content:space-between;padding:8px 0;
        border-bottom:1px solid #e0e0e0}
.metric:last-child{border:none}
.valor{font-weight:700;color:#667eea;font-size:18px}
.destaque{background:linear-gradient(135deg,#667eea,#764ba2);color:white;
  border-radius:12px;padding:16px;text-align:center;margin-top:16px}
button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;
  border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;
  cursor:pointer;margin-top:16px}
</style></head><body><div class="card">
<h1>💰 Calculadora de ROI</h1>
<p>Veja quanto você economiza usando o Emotion Platform</p>
<label>Número de pacientes ativos</label>
<input type="number" id="pacientes" value="20" min="1" oninput="calcular()">
<label>Tempo gasto por avaliação manual (minutos)</label>
<input type="number" id="tempo" value="30" min="5" oninput="calcular()">
<label>Valor da sua hora (R$)</label>
<input type="number" id="hora" value="150" min="50" oninput="calcular()">
<label>Avaliações por paciente por mês</label>
<input type="number" id="avals" value="2" min="1" oninput="calcular()">
<div class="resultado" id="res"></div>
</div>
<script>
function calcular(){
  var pac=parseInt(document.getElementById("pacientes").value)||0;
  var tempo=parseInt(document.getElementById("tempo").value)||0;
  var hora=parseInt(document.getElementById("hora").value)||0;
  var avals=parseInt(document.getElementById("avals").value)||0;
  var horas_mes=(pac*tempo*avals)/60;
  var custo_manual=horas_mes*hora;
  var custo_plataforma=99.90;
  var economia=custo_manual-custo_plataforma;
  var roi=custo_plataforma>0?((economia/custo_plataforma)*100):0;
  document.getElementById("res").innerHTML=
    "<h3 style='margin:0 0 12px;color:#333'>📊 Resultado Mensal</h3>"+
    "<div class='metric'><span>Horas gastas manualmente</span><span class='valor'>"+horas_mes.toFixed(1)+"h</span></div>"+
    "<div class='metric'><span>Custo do seu tempo</span><span class='valor'>R$ "+custo_manual.toFixed(2)+"</span></div>"+
    "<div class='metric'><span>Custo da plataforma</span><span class='valor'>R$ "+custo_plataforma.toFixed(2)+"</span></div>"+
    "<div class='destaque'><div style='font-size:13px;opacity:0.9'>Você economiza</div>"+
    "<div style='font-size:36px;font-weight:800'>R$ "+Math.max(0,economia).toFixed(2)+"</div>"+
    "<div style='font-size:13px;opacity:0.9'>ROI de "+Math.max(0,roi).toFixed(0)+"%</div></div>"+
    res+="<button onclick='window.location="/app/planos"'">Assinar agora</button>";
}
calcular();
</script></body></html>""")

@router.get("/calcular")
async def api_roi(pacientes: int = 20, tempo: int = 30, hora: float = 150, avals: int = 2):
    horas = (pacientes * tempo * avals) / 60
    custo_manual = horas * hora
    custo_plataforma = 99.90
    economia = custo_manual - custo_plataforma
    return JSONResponse({"horas_economizadas": round(horas, 1),
                         "custo_manual": round(custo_manual, 2),
                         "custo_plataforma": custo_plataforma,
                         "economia_mensal": round(max(0, economia), 2),
                         "roi_percentual": round(max(0, (economia/custo_plataforma)*100), 0)})

class ROIPlugin(PluginBase):
    name = "calculadora_roi"
    def setup(self, app): app.include_router(router)
plugin = ROIPlugin()
