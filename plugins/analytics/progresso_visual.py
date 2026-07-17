#!/usr/bin/env python3
"""Visualizacao de progresso terapeutico"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta
import random

router = APIRouter(prefix="/progresso", tags=["Progresso"])

@router.get("", response_class=HTMLResponse)
async def pagina_progresso():
    hoje = datetime.now()
    dados_semanas = []
    for i in range(12):
        data = hoje - timedelta(weeks=11-i)
        phq9 = max(0, min(27, 18 - i + random.randint(-2,2)))
        gad7 = max(0, min(21, 14 - i + random.randint(-2,2)))
        dados_semanas.append({"semana": i+1, "data": data.strftime("%d/%m"),
                              "phq9": phq9, "gad7": gad7})

    labels = str([d["data"] for d in dados_semanas])
    phq9_vals = str([d["phq9"] for d in dados_semanas])
    gad7_vals = str([d["gad7"] for d in dados_semanas])

    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Progresso Terapeutico</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body{{font-family:sans-serif;background:#0d1117;color:white;padding:20px;margin:0}}
.container{{max-width:900px;margin:0 auto}}
h1{{color:#58a6ff;margin-bottom:8px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin:24px 0}}
.card{{background:#161b22;border-radius:12px;padding:20px;border:1px solid #30363d}}
.num{{font-size:36px;font-weight:800;color:#58a6ff}}
.label{{color:#8b949e;font-size:14px;margin-top:4px}}
.trend{{font-size:13px;margin-top:8px}}
.trend.melhora{{color:#3fb950}} .trend.piora{{color:#f85149}}
.chart-container{{background:#161b22;border-radius:12px;padding:20px;
  border:1px solid #30363d;margin-bottom:20px}}
canvas{{max-height:250px}}
</style></head><body>
<div class="container">
<a href="/" style="color:#58a6ff;text-decoration:none">Voltar</a>
<h1 style="margin-top:12px">Evolucao Terapeutica — 12 Semanas</h1>
<div class="grid">
  <div class="card"><div class="num">{dados_semanas[-1]["phq9"]}</div>
    <div class="label">PHQ-9 Atual</div>
    <div class="trend melhora">Reducao de {dados_semanas[0]["phq9"]-dados_semanas[-1]["phq9"]} pontos</div></div>
  <div class="card"><div class="num">{dados_semanas[-1]["gad7"]}</div>
    <div class="label">GAD-7 Atual</div>
    <div class="trend melhora">Reducao de {dados_semanas[0]["gad7"]-dados_semanas[-1]["gad7"]} pontos</div></div>
  <div class="card"><div class="num">12</div>
    <div class="label">Semanas de Acompanhamento</div>
    <div class="trend melhora">Continuidade</div></div>
  <div class="card"><div class="num">87%</div>
    <div class="label">Aderencia ao Tratamento</div>
    <div class="trend melhora">Excelente</div></div>
</div>
<div class="chart-container">
  <h2 style="color:#58a6ff;margin:0 0 16px">PHQ-9 e GAD-7 ao longo do tempo</h2>
  <canvas id="chart"></canvas>
</div>
</div>
<script>
new Chart(document.getElementById("chart"), {{
  type: "line",
  data: {{
    labels: {labels},
    datasets: [
      {{label: "PHQ-9 (Depressao)", data: {phq9_vals},
       borderColor: "#f85149", backgroundColor: "rgba(248,81,73,0.1)",
       fill: true, tension: 0.4}},
      {{label: "GAD-7 (Ansiedade)", data: {gad7_vals},
       borderColor: "#58a6ff", backgroundColor: "rgba(88,166,255,0.1)",
       fill: true, tension: 0.4}}
    ]
  }},
  options: {{
    plugins: {{legend: {{labels: {{color: "#e6edf3"}}}}}},
    scales: {{
      x: {{ticks: {{color: "#8b949e"}}, grid: {{color: "#21262d"}}}},
      y: {{ticks: {{color: "#8b949e"}}, grid: {{color: "#21262d"}}, min: 0, max: 30}}
    }}
  }}
}});
</script></body></html>""")

class ProgressoPlugin(PluginBase):
    name = "progresso_visual"
    def setup(self, app): app.include_router(router)
plugin = ProgressoPlugin()
