#!/usr/bin/env python3
"""Relatorio avancado em HTML para impressao/PDF"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/relatorio-html", tags=["Relatório"])

@router.get("/paciente/{nome}", response_class=HTMLResponse)
async def relatorio_paciente(nome: str, phq9: int = 8, gad7: int = 6):
    data = datetime.now().strftime("%d/%m/%Y")
    nivel_phq = "leve" if phq9 < 10 else "moderado" if phq9 < 15 else "grave"
    nivel_gad = "leve" if gad7 < 10 else "moderado" if gad7 < 15 else "grave"
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Relatório Clínico — {nome}</title>
<style>
@media print{{.no-print{{display:none}}}}
body{{font-family:"Times New Roman",serif;margin:40px;color:#222;line-height:1.6}}
.header{{border-bottom:3px solid #667eea;padding-bottom:20px;margin-bottom:30px}}
.logo{{color:#667eea;font-size:22px;font-weight:700}}
h1{{font-size:24px;margin:8px 0 4px}}
.meta{{color:#666;font-size:14px}}
.secao{{margin-bottom:28px}}
.secao h2{{color:#667eea;font-size:18px;border-bottom:1px solid #eee;
           padding-bottom:6px;margin-bottom:12px}}
table{{width:100%;border-collapse:collapse;margin:12px 0}}
td,th{{padding:10px;border:1px solid #ddd;text-align:left;font-size:14px}}
th{{background:#f0f4ff;font-weight:700;color:#333}}
.score{{font-size:32px;font-weight:700;color:#667eea}}
.nivel{{padding:4px 12px;border-radius:20px;font-size:13px;font-weight:700}}
.leve{{background:#fef9c3;color:#854d0e}}
.moderado{{background:#fed7aa;color:#c2410c}}
.grave{{background:#fecaca;color:#b91c1c}}
.footer{{margin-top:40px;border-top:1px solid #eee;padding-top:16px;
         font-size:13px;color:#888;text-align:center}}
.btn-print{{background:#667eea;color:white;border:none;padding:12px 24px;
  border-radius:8px;cursor:pointer;font-size:16px;margin:16px 0}}
</style></head><body>

<div class="header">
  <div class="logo">🧠 Emotion Intelligence Platform</div>
  <h1>Relatório Clínico — {nome}</h1>
  <div class="meta">Data: {data} · Gerado automaticamente pela plataforma</div>
</div>

<button class="btn-print no-print" onclick="window.print()">🖨️ Imprimir / Salvar PDF</button>

<div class="secao">
  <h2>📊 Instrumentos Aplicados</h2>
  <table>
    <tr><th>Instrumento</th><th>Score</th><th>Nível</th><th>Data</th></tr>
    <tr>
      <td>PHQ-9 (Depressão)</td>
      <td><span class="score">{phq9}</span>/27</td>
      <td><span class="nivel {nivel_phq}">{nivel_phq.title()}</span></td>
      <td>{data}</td>
    </tr>
    <tr>
      <td>GAD-7 (Ansiedade)</td>
      <td><span class="score">{gad7}</span>/21</td>
      <td><span class="nivel {nivel_gad}">{nivel_gad.title()}</span></td>
      <td>{data}</td>
    </tr>
  </table>
</div>

<div class="secao">
  <h2>📝 Interpretação Clínica</h2>
  <p><strong>PHQ-9 Score {phq9}:</strong> Indica nível {nivel_phq} de sintomas depressivos.
  {"Recomenda-se monitoramento quinzenal e avaliação de necessidade de intervenção." if phq9 < 10
  else "Recomenda-se intervenção terapêutica e reavaliação em 4 semanas." if phq9 < 15
  else "Recomenda-se intervenção intensiva e possível encaminhamento para psiquiatria."}</p>
  <p style="margin-top:12px"><strong>GAD-7 Score {gad7}:</strong> Indica nível {nivel_gad} de
  sintomas de ansiedade generalizada.
  {"Monitorar e orientar técnicas de manejo de ansiedade." if gad7 < 10
  else "Considerar técnicas de regulação emocional e manejo de estresse." if gad7 < 15
  else "Avaliar necessidade de intervenção farmacológica em conjunto com psiquiatria."}</p>
</div>

<div class="secao">
  <h2>🎯 Plano Terapêutico Sugerido</h2>
  <table>
    <tr><th>Área</th><th>Intervenção</th><th>Frequência</th></tr>
    <tr><td>Avaliação de humor</td><td>PHQ-9/GAD-7</td><td>Quinzenal</td></tr>
    <tr><td>Sessões terapêuticas</td><td>Psicoterapia individual</td><td>Semanal</td></tr>
    <tr><td>Monitoramento</td><td>Diário emocional digital</td><td>Diário</td></tr>
    <tr><td>Suporte entre sessões</td><td>Chat IA da plataforma</td><td>Conforme necessidade</td></tr>
  </table>
</div>

<div class="secao">
  <h2>⚠️ Recursos de Crise</h2>
  <p>Em caso de ideação suicida ou crise aguda, orientar o paciente a contatar:</p>
  <p><strong>CVV — Centro de Valorização da Vida:</strong> Ligue 188 (24h, gratuito)</p>
  <p><strong>SAMU:</strong> 192 · <strong>Bombeiros:</strong> 193</p>
</div>

<div class="footer">
  <p>Relatório gerado pelo Emotion Intelligence Platform em {data}</p>
  <p>emotion-platform-albert.onrender.com · Instrumento validado para população brasileira</p>
  <p><em>Este relatório é confidencial e destinado exclusivamente ao uso clínico.</em></p>
</div>
</body></html>""")

class RelatorioAvancadoPlugin(PluginBase):
    name = "relatorio_html_avancado"
    def setup(self, app): app.include_router(router)
plugin = RelatorioAvancadoPlugin()
