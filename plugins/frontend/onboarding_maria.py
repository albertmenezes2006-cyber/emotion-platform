"""Onboarding com Paciente Maria (demo) - aha em 5 min"""
import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from plugins.plugin_base import PluginBase

router = APIRouter(tags=["Onboarding"])

ONBOARDING_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bem-vindo ao EmotionAI - Primeira nota em 5 minutos</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); color: #1e293b; min-height: 100vh; }

.container { max-width: 900px; margin: 0 auto; padding: 40px 20px; }

.hero { text-align: center; margin-bottom: 40px; }
.hero .badge { display: inline-block; background: #ecfdf5; color: #059669; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }
.hero h1 { font-size: 36px; font-weight: 800; margin-bottom: 12px; }
.hero .subtitle { color: #64748b; font-size: 18px; max-width: 600px; margin: 0 auto; }

.stepper { display: flex; justify-content: center; gap: 20px; margin: 40px 0; }
.step { display: flex; align-items: center; gap: 10px; padding: 10px 20px; background: white; border-radius: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
.step-num { width: 30px; height: 30px; border-radius: 50%; background: #6366f1; color: white; display: flex; align-items: center; justify-content: center; font-weight: 700; }
.step.done .step-num { background: #10b981; }
.step-txt { font-size: 14px; font-weight: 600; color: #475569; }

.card { background: white; border-radius: 20px; padding: 40px; box-shadow: 0 10px 40px rgba(0,0,0,0.08); margin-bottom: 20px; }

.paciente-card { background: linear-gradient(135deg, #eff6ff, #dbeafe); border-radius: 16px; padding: 24px; margin-bottom: 25px; border: 2px solid #93c5fd; }
.paciente-header { display: flex; align-items: center; gap: 15px; margin-bottom: 15px; }
.paciente-avatar { width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #8b5cf6); display: flex; align-items: center; justify-content: center; color: white; font-size: 24px; font-weight: 700; }
.paciente-info h3 { font-size: 20px; color: #1e40af; }
.paciente-info p { font-size: 13px; color: #64748b; }
.paciente-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 10px; }
.tag { background: white; padding: 4px 10px; border-radius: 15px; font-size: 11px; color: #6366f1; font-weight: 600; }

.escala-box { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 15px 20px; border-radius: 10px; margin: 20px 0; }
.escala-box strong { color: #78350f; }
.escala-box p { color: #92400e; font-size: 14px; margin-top: 5px; }

.evolucao-box { background: #f8fafc; border-radius: 12px; padding: 25px; margin: 20px 0; }
.evolucao-box h4 { font-size: 14px; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px; }
.evolucao-texto { color: #1e293b; line-height: 1.7; font-size: 15px; }
.evolucao-tag { display: inline-block; background: #ede9fe; color: #7c3aed; padding: 3px 10px; border-radius: 15px; font-size: 11px; font-weight: 600; margin-right: 5px; }

.actions { display: flex; gap: 12px; margin-top: 30px; }
.btn { padding: 14px 28px; border-radius: 12px; font-weight: 700; font-size: 15px; cursor: pointer; border: none; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s; }
.btn-primary { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; flex: 1; }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(99,102,241,0.35); }
.btn-outline { background: white; border: 2px solid #e2e8f0; color: #475569; }
.btn-outline:hover { border-color: #6366f1; color: #6366f1; }

.tip { background: linear-gradient(135deg, #eff6ff, #dbeafe); border-radius: 12px; padding: 20px; margin: 20px 0; display: flex; gap: 15px; align-items: flex-start; }
.tip-icon { font-size: 24px; }
.tip-text { color: #1e40af; font-size: 14px; line-height: 1.6; }
.tip-text strong { display: block; margin-bottom: 5px; font-size: 15px; }

.progress { background: white; border-radius: 12px; padding: 15px 20px; margin-bottom: 20px; display: flex; align-items: center; gap: 15px; }
.progress-bar-mini { flex: 1; height: 8px; background: #e2e8f0; border-radius: 4px; overflow: hidden; }
.progress-fill-mini { height: 100%; background: linear-gradient(90deg, #6366f1, #8b5cf6); width: 33%; transition: width 0.3s; }
.progress-text-mini { font-size: 13px; color: #64748b; font-weight: 600; }

.confetti { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background: white; padding: 40px; border-radius: 20px; box-shadow: 0 25px 50px rgba(0,0,0,0.25); z-index: 1000; text-align: center; display: none; }
.confetti.show { display: block; animation: pop 0.5s ease; }
@keyframes pop { 0% { transform: translate(-50%, -50%) scale(0); } 70% { transform: translate(-50%, -50%) scale(1.1); } 100% { transform: translate(-50%, -50%) scale(1); } }
.confetti-icon { font-size: 72px; margin-bottom: 15px; }
.confetti h2 { color: #10b981; margin-bottom: 10px; }
.confetti p { color: #64748b; margin-bottom: 20px; }

@media (max-width: 600px) {
  .stepper { flex-direction: column; align-items: stretch; }
  .actions { flex-direction: column; }
  .hero h1 { font-size: 26px; }
}
</style>
</head>
<body>

<div class="container">

  <div class="hero">
    <span class="badge">Onboarding - 5 minutos</span>
    <h1>Vamos gerar sua primeira nota clinica</h1>
    <p class="subtitle">Criamos uma paciente demo (Maria Silva) com PHQ-9 respondido para voce ver o produto em acao. Depois voce troca por pacientes reais.</p>
  </div>

  <div class="progress">
    <div class="progress-text-mini">Etapa 1 de 3</div>
    <div class="progress-bar-mini"><div class="progress-fill-mini"></div></div>
    <div class="progress-text-mini">33%</div>
  </div>

  <div class="stepper">
    <div class="step done"><span class="step-num">1</span><span class="step-txt">Ver Maria</span></div>
    <div class="step"><span class="step-num">2</span><span class="step-txt">Revisar nota</span></div>
    <div class="step"><span class="step-num">3</span><span class="step-txt">Assinar</span></div>
  </div>

  <div class="card">

    <div class="paciente-card">
      <div class="paciente-header">
        <div class="paciente-avatar">M</div>
        <div class="paciente-info">
          <h3>Maria Silva (paciente demo)</h3>
          <p>34 anos - Sessao 3 - 15/08/2026 - 14h30</p>
          <div class="paciente-tags">
            <span class="tag">TCC</span>
            <span class="tag">Ansiedade</span>
            <span class="tag">Semanal</span>
          </div>
        </div>
      </div>
    </div>

    <div class="escala-box">
      <strong>PHQ-9 aplicado antes da sessao</strong>
      <p>Score: 14/27 - Depressao Moderada - Item 9: 1 (leve ideacao passiva)</p>
    </div>

    <div class="evolucao-box">
      <h4>Rascunho da nota clinica (gerado pela IA)</h4>
      <div class="evolucao-texto">
        <strong>S (Subjetivo):</strong> Paciente relata melhora do sono na ultima semana (media 6h/noite) apos aplicacao de tecnicas de higiene do sono. Refere ainda pensamentos automaticos negativos sobre o trabalho, especialmente as segundas-feiras. Nega ideacao ativa, mas manteve item 9 do PHQ-9 em 1.
        <br><br>
        <strong>O (Objetivo):</strong> Aparencia cuidada, humor eutimico durante a sessao, discurso coerente. PHQ-9 = 14 (moderado), estavel em relacao a sessao anterior (15).
        <br><br>
        <strong>A (Avaliacao):</strong> Manutencao dos sintomas depressivos moderados com leve tendencia de melhora. Boa adesao as tarefas de casa. Aliancia terapeutica solida.
        <br><br>
        <strong>P (Plano):</strong> Continuar com reestruturacao cognitiva focada em pensamentos automaticos relacionados ao trabalho. Introduzir tarefa de registro de pensamentos disfuncionais. Manter monitoramento de risco (item 9) semanalmente.
        <br><br>
        <div style="margin-top:15px">
          <span class="evolucao-tag">Tecnica: TCC</span>
          <span class="evolucao-tag">Reestruturacao cognitiva</span>
          <span class="evolucao-tag">Higiene do sono</span>
        </div>
      </div>
    </div>

    <div class="tip">
      <span class="tip-icon">TIP</span>
      <div class="tip-text">
        <strong>Como sera na sua rotina real</strong>
        Voce ira revisar cada rascunho antes de assinar. A IA nunca assina sozinha. Esta nota aqui e apenas um exemplo do que voce vai receber depois de cada sessao real.
      </div>
    </div>

    <div class="actions">
      <a href="/app/dashboard" class="btn btn-outline">Ir para o dashboard</a>
      <button class="btn btn-primary" onclick="assinar()">Revisar e assinar nota</button>
    </div>

  </div>

  <div class="card" style="text-align:center;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:white">
    <h2 style="font-size:22px;margin-bottom:10px">Pronto para atender pacientes de verdade?</h2>
    <p style="opacity:0.9;margin-bottom:20px">No plano Free voce cadastra ate 5 pacientes reais. Sem cartao, sem prazo.</p>
    <a href="/app/dashboard" class="btn" style="background:white;color:#6366f1">Ir para o Dashboard -></a>
  </div>

</div>

<div class="confetti" id="confetti">
  <div class="confetti-icon">OK</div>
  <h2>Primeira nota assinada!</h2>
  <p>Voce ja viu como funciona. Agora e so cadastrar seus pacientes reais.</p>
  <a href="/app/dashboard" class="btn btn-primary">Ir para o Dashboard</a>
</div>

<script>
function assinar() {
  document.getElementById("confetti").classList.add("show");
  setTimeout(() => {
    window.location.href = "/app/dashboard";
  }, 3500);
}
</script>

</body>
</html>"""

@router.get("/onboarding", response_class=HTMLResponse)
async def onboarding():
    return HTMLResponse(ONBOARDING_HTML)

class OnboardingPlugin(PluginBase):
    name = "onboarding_maria"
    def setup(self, app):
        app.include_router(router)

plugin = OnboardingPlugin()
