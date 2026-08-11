"""Calculadora publica GAD-7 (SEO + conversao)"""
import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(tags=["Calculadoras"])

GAD7_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GAD-7 Online Gratis: Calculadora de Ansiedade Generalizada | EmotionAI</title>
<meta name="description" content="Aplique o GAD-7 em 2 minutos. Score automatico e interpretacao clinica. Rastreio de ansiedade generalizada validado para populacao brasileira.">
<meta name="keywords" content="GAD-7, GAD7 online, escala de ansiedade, calculadora GAD-7, teste de ansiedade, transtorno de ansiedade generalizada, rastreio ansiedade, SATEPSI">
<link rel="canonical" href="https://emotion-platform-albert.onrender.com/gad-7">

<meta property="og:title" content="GAD-7 Online: Calculadora de Ansiedade Gratuita">
<meta property="og:description" content="Aplique o GAD-7 em 2 minutos com score automatico.">
<meta property="og:type" content="website">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "name": "GAD-7 Online - Calculadora de Ansiedade",
  "description": "Ferramenta gratuita de rastreio de ansiedade usando a escala GAD-7",
  "audience": [
    {"@type": "MedicalAudience", "audienceType": "Patient"},
    {"@type": "MedicalAudience", "audienceType": "Psychologist"}
  ],
  "about": {
    "@type": "MedicalCondition",
    "name": "Transtorno de Ansiedade Generalizada",
    "code": {"@type": "MedicalCode", "code": "F41.1", "codingSystem": "ICD-10"}
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "O que e o GAD-7?", "acceptedAnswer": {"@type": "Answer", "text": "O GAD-7 (Generalized Anxiety Disorder 7-item) e uma escala de auto-relato para rastrear e medir a gravidade do transtorno de ansiedade generalizada."}},
    {"@type": "Question", "name": "Como interpretar o resultado?", "acceptedAnswer": {"@type": "Answer", "text": "0-4 ansiedade minima; 5-9 leve; 10-14 moderada; 15-21 grave. Ponto de corte clinico >= 10."}}
  ]
}
</script>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; }
.crisis-banner { background: linear-gradient(135deg, #dc2626, #b91c1c); color: white; text-align: center; padding: 10px 20px; font-size: 14px; font-weight: 500; position: sticky; top: 0; z-index: 100; }
.crisis-banner a { color: #fef3c7; text-decoration: underline; font-weight: 700; }
.nav { background: white; padding: 15px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); position: sticky; top: 44px; z-index: 99; }
.nav-inner { max-width: 800px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
.logo { font-size: 20px; font-weight: 800; background: linear-gradient(135deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }
.nav-link { color: #64748b; text-decoration: none; font-size: 14px; font-weight: 500; }
.hero { max-width: 800px; margin: 0 auto; padding: 40px 20px 20px; text-align: center; }
.badge { display: inline-block; background: #ecfdf5; color: #059669; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }
h1 { font-size: 32px; font-weight: 800; margin-bottom: 12px; color: #0f172a; }
.subtitle { color: #64748b; font-size: 16px; max-width: 600px; margin: 0 auto; }
.container { max-width: 800px; margin: 0 auto; padding: 20px; }
.card { background: white; border-radius: 16px; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 20px; }
.progress-bar { height: 6px; background: #e2e8f0; border-radius: 3px; margin-bottom: 25px; overflow: hidden; }
.progress-fill { height: 100%; background: linear-gradient(90deg, #6366f1, #8b5cf6); border-radius: 3px; transition: width 0.3s ease; width: 0%; }
.progress-text { text-align: center; color: #64748b; font-size: 13px; margin-bottom: 20px; font-weight: 500; }
.instrucao { background: #eff6ff; border-left: 4px solid #3b82f6; padding: 15px 20px; border-radius: 8px; margin-bottom: 25px; color: #1e40af; font-size: 14px; }
.question { border-bottom: 1px solid #e2e8f0; padding: 20px 0; }
.question:last-child { border-bottom: none; }
.question-title { font-size: 15px; font-weight: 500; color: #1e293b; margin-bottom: 12px; }
.question-title .num { color: #6366f1; font-weight: 700; margin-right: 5px; }
.options { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
.option { background: #f1f5f9; border: 2px solid transparent; padding: 12px 8px; border-radius: 10px; text-align: center; cursor: pointer; transition: all 0.15s; font-size: 12px; font-weight: 500; color: #475569; }
.option:hover { background: #e2e8f0; }
.option.selected { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border-color: #6366f1; }
.option-num { display: block; font-size: 18px; font-weight: 700; margin-bottom: 2px; }
.btn-calcular { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border: none; padding: 16px 32px; border-radius: 12px; font-size: 16px; font-weight: 700; cursor: pointer; width: 100%; margin-top: 20px; transition: all 0.2s; }
.btn-calcular:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(99,102,241,0.35); }
.btn-calcular:disabled { background: #cbd5e1; cursor: not-allowed; }
.resultado { display: none; }
.resultado.show { display: block; animation: fadeIn 0.5s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.score-box { text-align: center; padding: 30px 20px; border-radius: 16px; margin-bottom: 20px; }
.score-box.minima { background: linear-gradient(135deg, #dcfce7, #bbf7d0); }
.score-box.leve { background: linear-gradient(135deg, #fef3c7, #fde68a); }
.score-box.moderada { background: linear-gradient(135deg, #fed7aa, #fdba74); }
.score-box.grave { background: linear-gradient(135deg, #fca5a5, #f87171); }
.score-num { font-size: 72px; font-weight: 800; line-height: 1; color: #0f172a; }
.score-max { font-size: 24px; color: #64748b; }
.score-nivel { font-size: 20px; font-weight: 700; margin-top: 10px; color: #0f172a; }
.score-faixa { color: #64748b; font-size: 13px; margin-top: 5px; }
.interpretacao { background: #f8fafc; border-radius: 12px; padding: 20px; margin: 20px 0; }
.interpretacao h3 { font-size: 16px; margin-bottom: 10px; color: #0f172a; }
.interpretacao p { color: #475569; font-size: 14px; margin-bottom: 8px; }
.tabela-scores { background: #f8fafc; border-radius: 12px; padding: 20px; margin: 20px 0; }
.tabela-scores h3 { font-size: 15px; margin-bottom: 12px; color: #0f172a; }
.tabela-scores table { width: 100%; border-collapse: collapse; font-size: 13px; }
.tabela-scores th { text-align: left; padding: 8px; background: white; color: #64748b; font-weight: 600; }
.tabela-scores td { padding: 8px; border-top: 1px solid #e2e8f0; }
.tabela-scores tr.atual { background: rgba(99,102,241,0.1); font-weight: 700; }
.acoes { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 20px 0; }
.btn-acao { background: white; border: 2px solid #e2e8f0; padding: 12px; border-radius: 10px; font-size: 13px; font-weight: 600; color: #475569; cursor: pointer; text-align: center; text-decoration: none; transition: all 0.2s; }
.btn-acao:hover { border-color: #6366f1; color: #6366f1; }
.cta-psi { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; border-radius: 16px; padding: 30px; text-align: center; margin: 30px 0; }
.cta-psi h3 { font-size: 22px; margin-bottom: 10px; }
.cta-psi p { opacity: 0.9; margin-bottom: 20px; }
.cta-psi .btn { display: inline-block; background: white; color: #6366f1; padding: 14px 28px; border-radius: 10px; text-decoration: none; font-weight: 700; }
.disclaimer { background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px 20px; border-radius: 8px; color: #78350f; font-size: 13px; margin: 20px 0; }
.info-secao { margin: 40px 0; }
.info-secao h2 { font-size: 22px; margin-bottom: 15px; color: #0f172a; }
.info-secao p { color: #475569; margin-bottom: 12px; }
.faq-item { background: white; border-radius: 12px; padding: 20px; margin-bottom: 10px; cursor: pointer; }
.faq-q { font-weight: 600; color: #0f172a; display: flex; justify-content: space-between; align-items: center; }
.faq-a { color: #64748b; font-size: 14px; margin-top: 12px; display: none; }
.faq-item.open .faq-a { display: block; }
.combo-cta { background: linear-gradient(135deg, #ecfdf5, #d1fae5); border-radius: 16px; padding: 20px; text-align: center; margin: 20px 0; border: 2px solid #10b981; }
.combo-cta h3 { color: #065f46; font-size: 18px; margin-bottom: 8px; }
.combo-cta p { color: #047857; font-size: 14px; margin-bottom: 12px; }
.combo-cta a { display: inline-block; background: #10b981; color: white; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 600; }
.footer { text-align: center; padding: 40px 20px; color: #94a3b8; font-size: 12px; }
.footer a { color: #6366f1; text-decoration: none; }
@media (max-width: 600px) {
  h1 { font-size: 24px; }
  .options { grid-template-columns: repeat(2, 1fr); }
  .card { padding: 20px; }
  .score-num { font-size: 56px; }
  .acoes { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<div class="crisis-banner">
  Em crise? Ligue <a href="tel:188">188 (CVV)</a> 24h ou <a href="tel:192">192 (SAMU)</a>
</div>

<nav class="nav">
  <div class="nav-inner">
    <a href="/" class="logo">EmotionAI</a>
    <a href="/phq-9" class="nav-link">PHQ-9 (Depressao)</a>
  </div>
</nav>

<header class="hero">
  <span class="badge">Ferramenta Gratuita</span>
  <h1>GAD-7 Online</h1>
  <p class="subtitle">Escala de rastreio de ansiedade generalizada com 7 itens. Pontuacao automatica e interpretacao clinica em 2 minutos.</p>
</header>

<div class="container">

  <div class="card" id="questionario">
    <div class="instrucao">
      <strong>Durante as ultimas 2 semanas</strong>, com que frequencia voce foi incomodado(a) pelos seguintes problemas?
    </div>

    <div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
    <div class="progress-text" id="progress-text">0 de 7 respondidas</div>

    <div id="perguntas"></div>

    <button class="btn-calcular" id="btn-calc" disabled onclick="calcular()">Responda as 7 perguntas</button>
  </div>

  <div class="card resultado" id="resultado">
    <div class="score-box" id="score-box">
      <div>
        <span class="score-num" id="score-num">0</span>
        <span class="score-max">/21</span>
      </div>
      <div class="score-nivel" id="score-nivel">-</div>
      <div class="score-faixa" id="score-faixa">-</div>
    </div>

    <div class="interpretacao">
      <h3>Interpretacao Clinica</h3>
      <p id="interpretacao-txt"></p>
      <p id="conduta-txt" style="margin-top:10px"></p>
    </div>

    <div class="tabela-scores">
      <h3>Referencia de Pontuacao GAD-7</h3>
      <table>
        <thead><tr><th>Score</th><th>Nivel de Ansiedade</th></tr></thead>
        <tbody id="tabela-body">
          <tr data-min="0" data-max="4"><td>0-4</td><td>Minima</td></tr>
          <tr data-min="5" data-max="9"><td>5-9</td><td>Leve</td></tr>
          <tr data-min="10" data-max="14"><td>10-14</td><td>Moderada</td></tr>
          <tr data-min="15" data-max="21"><td>15-21</td><td>Grave</td></tr>
        </tbody>
      </table>
    </div>

    <div class="combo-cta">
      <h3>Aplique tambem o PHQ-9</h3>
      <p>Ansiedade e depressao aparecem juntas em 60% dos casos. Recomendado avaliar as duas.</p>
      <a href="/phq-9">Aplicar PHQ-9 agora</a>
    </div>

    <div class="acoes">
      <button class="btn-acao" onclick="compartilharWhatsApp()">Compartilhar WhatsApp</button>
      <button class="btn-acao" onclick="imprimir()">Imprimir Resultado</button>
      <button class="btn-acao" onclick="refazer()">Refazer Teste</button>
      <a class="btn-acao" href="/phq-9">Aplicar PHQ-9</a>
    </div>

    <div class="disclaimer">
      <strong>Aviso:</strong> O GAD-7 e instrumento de rastreio, nao de diagnostico. O resultado nao substitui avaliacao psicologica ou psiquiatrica.
    </div>

    <div class="cta-psi">
      <h3>E psicologo(a)?</h3>
      <p>Envie o GAD-7 por link ao paciente. Score cai automatico no prontuario, com curva de evolucao.</p>
      <a href="/planos" class="btn">Ver Planos EmotionAI</a>
    </div>
  </div>

  <div class="info-secao">
    <h2>Sobre o GAD-7</h2>
    <p>O <strong>GAD-7 (Generalized Anxiety Disorder 7-item)</strong> foi desenvolvido por Spitzer, Kroenke, Williams e Lowe (2006) para rastrear transtorno de ansiedade generalizada e medir sua gravidade.</p>
    <p>Cada item e pontuado de 0 a 3, gerando escore total de 0 a 21. Possui excelente propriedades psicometricas em populacao brasileira, com sensibilidade de 89% e especificidade de 82% para deteccao de TAG.</p>
    <p>Frequentemente aplicado em conjunto com o PHQ-9, ja que ansiedade e depressao apresentam alta comorbidade (~60%).</p>
  </div>

  <div class="info-secao">
    <h2>Perguntas Frequentes</h2>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Qual o ponto de corte clinico? <span>v</span></div>
      <div class="faq-a">O ponto de corte usual e <strong>>= 10</strong>, indicando ansiedade clinicamente significativa. Scores 5-9 (leve) exigem monitoramento; >= 15 requer avaliacao urgente.</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">GAD-7 diagnostica TAG? <span>v</span></div>
      <div class="faq-a">Nao. E rastreio, nao diagnostico. O TAG (Transtorno de Ansiedade Generalizada) requer avaliacao clinica completa baseada em criterios DSM-5/CID-11.</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Devo aplicar GAD-7 e PHQ-9 juntos? <span>v</span></div>
      <div class="faq-a">Sim, e altamente recomendado. Ansiedade e depressao tem comorbidade de ~60%. Aplicar ambos oferece visao clinica mais completa.</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Com que frequencia devo reaplicar? <span>v</span></div>
      <div class="faq-a">Recomenda-se <strong>2-4 semanas</strong> durante tratamento. Reducao >= 50% no score = boa resposta terapeutica.</div>
    </div>
  </div>

  <div class="info-secao">
    <h2>Referencias</h2>
    <p style="font-size: 13px; color: #64748b;">
      Spitzer RL, Kroenke K, Williams JB, Lowe B. <em>A brief measure for assessing generalized anxiety disorder: the GAD-7.</em> Arch Intern Med. 2006;166(10):1092-7.
    </p>
  </div>

</div>

<footer class="footer">
  <p><strong>EmotionAI</strong> - Saude mental com IA para psicologos brasileiros</p>
  <p style="margin-top:8px">Conforme LGPD e Resolucoes CFP 01/2009, 06/2019 e 09/2024</p>
  <p style="margin-top:15px">Em crise: <a href="tel:188">188 (CVV)</a> ou <a href="tel:192">192 (SAMU)</a></p>
</footer>

<script>
const perguntas = [
  "Sentir-se nervoso(a), ansioso(a) ou muito tenso(a)",
  "Nao conseguir parar ou controlar as preocupacoes",
  "Preocupar-se muito com diversas coisas",
  "Dificuldade para relaxar",
  "Ficar tao agitado(a) que se torna dificil permanecer parado(a)",
  "Ficar facilmente aborrecido(a) ou irritado(a)",
  "Sentir medo como se algo horrivel fosse acontecer"
];

const opcoes = [
  {num: 0, txt: "Nenhuma vez"},
  {num: 1, txt: "Varios dias"},
  {num: 2, txt: "Mais da metade dos dias"},
  {num: 3, txt: "Quase todos os dias"}
];

const respostas = {};

function renderPerguntas() {
  const container = document.getElementById("perguntas");
  container.innerHTML = perguntas.map((p, i) => `
    <div class="question">
      <div class="question-title"><span class="num">${i+1}.</span>${p}</div>
      <div class="options">
        ${opcoes.map(o => `
          <div class="option" data-q="${i}" data-v="${o.num}" onclick="responder(${i}, ${o.num}, this)">
            <span class="option-num">${o.num}</span>
            ${o.txt}
          </div>
        `).join("")}
      </div>
    </div>
  `).join("");
}

function responder(q, v, el) {
  respostas[q] = v;
  document.querySelectorAll(`[data-q="${q}"]`).forEach(e => e.classList.remove("selected"));
  el.classList.add("selected");
  atualizarProgresso();
}

function atualizarProgresso() {
  const n = Object.keys(respostas).length;
  const pct = (n / 7) * 100;
  document.getElementById("progress").style.width = pct + "%";
  document.getElementById("progress-text").textContent = `${n} de 7 respondidas`;
  const btn = document.getElementById("btn-calc");
  if (n === 7) {
    btn.disabled = false;
    btn.textContent = "Ver Resultado";
  } else {
    btn.disabled = true;
    btn.textContent = `Responda mais ${7-n} pergunta${7-n>1?"s":""}`;
  }
}

function calcular() {
  const total = Object.values(respostas).reduce((a,b) => a+b, 0);

  let nivel, faixa, classe, interpretacao, conduta;
  if (total <= 4) {
    nivel = "Minima";
    faixa = "Score 0-4";
    classe = "minima";
    interpretacao = "Nao ha evidencia de sintomas ansiosos clinicamente significativos.";
    conduta = "Nao ha necessidade de intervencao especifica. Manter monitoramento em contextos de estresse.";
  } else if (total <= 9) {
    nivel = "Leve";
    faixa = "Score 5-9";
    classe = "leve";
    interpretacao = "Sintomas ansiosos leves. Monitoramento clinico recomendado.";
    conduta = "Psicoeducacao, tecnicas de relaxamento, higiene do sono. Reaplicar GAD-7 em 2-4 semanas.";
  } else if (total <= 14) {
    nivel = "Moderada";
    faixa = "Score 10-14";
    classe = "moderada";
    interpretacao = "Sintomas ansiosos moderados. Intervencao terapeutica indicada.";
    conduta = "TCC para ansiedade, tecnicas de exposicao. Considerar avaliacao psiquiatrica se comorbidade.";
  } else {
    nivel = "Grave";
    faixa = "Score 15-21";
    classe = "grave";
    interpretacao = "Sintomas ansiosos graves. Tratamento intensivo indicado.";
    conduta = "Psicoterapia semanal + avaliacao psiquiatrica para farmacoterapia. Investigar comorbidade com depressao (aplicar PHQ-9).";
  }

  document.getElementById("score-num").textContent = total;
  document.getElementById("score-nivel").textContent = nivel;
  document.getElementById("score-faixa").textContent = faixa;
  document.getElementById("interpretacao-txt").textContent = interpretacao;
  document.getElementById("conduta-txt").textContent = "Conduta sugerida: " + conduta;

  const box = document.getElementById("score-box");
  box.className = "score-box " + classe;

  document.querySelectorAll("#tabela-body tr").forEach(tr => {
    const min = parseInt(tr.dataset.min);
    const max = parseInt(tr.dataset.max);
    if (total >= min && total <= max) tr.classList.add("atual");
    else tr.classList.remove("atual");
  });

  document.getElementById("resultado").classList.add("show");
  document.getElementById("resultado").scrollIntoView({behavior: "smooth", block: "start"});
}

function compartilharWhatsApp() {
  const total = Object.values(respostas).reduce((a,b) => a+b, 0);
  const nivel = document.getElementById("score-nivel").textContent;
  const txt = `GAD-7: ${total}/21 (${nivel}) - Calcule tambem: https://emotion-platform-albert.onrender.com/gad-7`;
  window.open(`https://wa.me/?text=${encodeURIComponent(txt)}`, "_blank");
}

function imprimir() { window.print(); }

function refazer() {
  Object.keys(respostas).forEach(k => delete respostas[k]);
  document.querySelectorAll(".option").forEach(o => o.classList.remove("selected"));
  document.getElementById("resultado").classList.remove("show");
  atualizarProgresso();
  window.scrollTo({top: 0, behavior: "smooth"});
}

renderPerguntas();
</script>

</body>
</html>"""

@router.get("/gad-7", response_class=HTMLResponse)
async def gad7():
    return HTMLResponse(GAD7_HTML)

@router.get("/gad7", response_class=HTMLResponse)
async def gad7_alt():
    return HTMLResponse(GAD7_HTML)

class GAD7Plugin(PluginBase):
    name = "gad7_publico"
    def setup(self, app):
        app.include_router(router)

plugin = GAD7Plugin()
