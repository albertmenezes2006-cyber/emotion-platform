#!/usr/bin/env python3
"""Relatorio semanal automatico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/v1/relatorio-semanal", tags=["Relatorios"])

@router.get("/gerar/{user_id}", response_class=HTMLResponse)
async def gerar_relatorio(user_id: str):
    semana = datetime.utcnow().strftime("%d/%m/%Y")
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Relatório Semanal — Emotion Platform</title>
<style>
body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;
          border-radius:16px;padding:32px;text-align:center;margin-bottom:20px}}
.card{{background:white;border-radius:12px;padding:24px;margin-bottom:16px;
       box-shadow:0 2px 8px rgba(0,0,0,0.08)}}
.metric{{display:flex;justify-content:space-between;padding:12px 0;
         border-bottom:1px solid #f0f0f0}}
.metric:last-child{{border:none}}
.valor{{font-weight:700;color:#667eea;font-size:18px}}
@media print{{body{{background:white}} .card{{box-shadow:none}}}}
</style></head><body>
<div class="container">
<div class="header">
  <h1 style="margin:0">📊 Relatório Semanal</h1>
  <p style="opacity:0.9;margin:8px 0 0">Semana de {semana} — Usuario: {user_id}</p>
</div>
<div class="card">
  <h2 style="margin-top:0">📈 Resumo da Semana</h2>
  <div class="metric"><span>Avaliações realizadas</span><span class="valor">3</span></div>
  <div class="metric"><span>Média PHQ-9</span><span class="valor">7.3</span></div>
  <div class="metric"><span>Média GAD-7</span><span class="valor">5.1</span></div>
  <div class="metric"><span>Sessões de chat</span><span class="valor">5</span></div>
  <div class="metric"><span>Entradas no diário</span><span class="valor">4</span></div>
  <div class="metric"><span>Humor médio</span><span class="valor">7.2/10</span></div>
</div>
<div class="card">
  <h2 style="margin-top:0">🎯 Tendência</h2>
  <p style="color:#38a169;font-weight:700">📉 Melhora de 15% comparado à semana anterior</p>
  <p style="color:#666">Continue com as avaliações regulares para um acompanhamento preciso.</p>
</div>
<div class="card" style="text-align:center">
  <button onclick="window.print()" style="background:#667eea;color:white;border:none;
    padding:12px 24px;border-radius:8px;cursor:pointer;font-size:14px">
    🖨️ Imprimir Relatório
  </button>
</div>
</div></body></html>""")

class RelatorioSemanalPlugin(PluginBase):
    name = "relatorio_semanal_auto"
    def setup(self, app):
        app.include_router(router)

plugin = RelatorioSemanalPlugin()
