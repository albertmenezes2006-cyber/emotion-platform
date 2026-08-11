"""Calculadora publica PHQ-9 (SEO + conversao)"""
import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(tags=["Calculadoras"])

PHQ9_HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PHQ-9 Online Gratis: Calculadora de Depressao (SATEPSI) | EmotionAI</title>
<meta name="description" content="Aplique o PHQ-9 em 2 minutos. Score automatico, interpretacao clinica, alerta do item 9 e PDF. Rastreio, nao diagnostico. Para psicologos e pacientes no Brasil.">
<meta name="keywords" content="PHQ-9, PHQ9 online, escala de depressao, calculadora PHQ-9, teste de depressao, questionario de saude do paciente, rastreio depressao, SATEPSI, psicologo brasileiro">
<link rel="canonical" href="https://emotion-platform-albert.onrender.com/phq-9">

<meta property="og:title" content="PHQ-9 Online: Calculadora de Depressao Gratuita">
<meta property="og:description" content="Aplique o PHQ-9 em 2 minutos com score automatico e interpretacao clinica.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://emotion-platform-albert.onrender.com/phq-9">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalWebPage",
  "name": "PHQ-9 Online - Calculadora de Depressao",
  "description": "Ferramenta gratuita de rastreio de depressao usando a escala PHQ-9",
  "audience": [
    {"@type": "MedicalAudience", "audienceType": "Patient"},
    {"@type": "MedicalAudience", "audienceType": "Psychologist"}
  ],
  "about": {
    "@type": "MedicalCondition",
    "name": "Depressao",
    "code": {"@type": "MedicalCode", "code": "F32", "codingSystem": "ICD-10"}
  },
  "mainEntity": {
    "@type": "MedicalTest",
    "name": "Patient Health Questionnaire-9 (PHQ-9)",
    "usedToDiagnose": {"@type": "MedicalCondition", "name": "Transtorno Depressivo"}
  }
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "O que e o PHQ-9?", "acceptedAnswer": {"@type": "Answer", "text": "O PHQ-9 (Patient Health Questionnaire-9) e um instrumento de rastreio de depressao com 9 itens baseados nos criterios do DSM-5. Validado para populacao brasileira por Santos et al. (2013)."}},
    {"@type": "Question", "name": "Como interpretar o resultado?", "acceptedAnswer": {"@type": "Answer", "text": "0-4 sem depressao significativa; 5-9 depressao leve; 10-14 moderada; 15-19 moderadamente grave; 20-27 grave. Ponto de corte clinico >= 10."}},
    {"@type": "Question", "name": "O PHQ-9 diagnostica depressao?", "acceptedAnswer": {"@type": "Answer", "text": "Nao. E instrumento de rastreio, nao substitui avaliacao psicologica ou psiquiatrica. O diagnostico so pode ser feito por profissional habilitado em avaliacao clinica completa."}},
    {"@type": "Question", "name": "O que fazer se o item 9 (ideacao suicida) for maior que zero?", "acceptedAnswer": {"@type": "Answer", "text": "Qualquer pontuacao > 0 no item 9 exige avaliacao imediata de risco por profissional. Em crise, ligue 188 (CVV) ou 192 (SAMU)."}},
    {"@type": "Question", "name": "Quando devo reaplicar o PHQ-9?", "acceptedAnswer": {"@type": "Answer", "text": "Recomendado a cada 2-4 semanas para acompanhar evolucao do tratamento. Curva de 8 semanas oferece visao clinica util."}},
    {"@type": "Question", "name": "Posso usar o PHQ-9 no meu consultorio?", "acceptedAnswer": {"@type": "Answer", "text": "Sim. O PHQ-9 e de dominio publico, com parecer favoravel do SATEPSI/CFP. Deve ser aplicado por profissional psicologo ou medico com interpretacao no contexto clinico."}}
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
.nav-link:hover { color: #6366f1; }

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
.score-box.mod-grave { background: linear-gradient(135deg, #fecaca, #fca5a5); }
.score-box.grave { background: linear-gradient(135deg, #fca5a5, #f87171); }

.score-num { font-size: 72px; font-weight: 800; line-height: 1; color: #0f172a; }
.score-max { font-size: 24px; color: #64748b; }
.score-nivel { font-size: 20px; font-weight: 700; margin-top: 10px; color: #0f172a; }
.score-faixa { color: #64748b; font-size: 13px; margin-top: 5px; }

.alerta-item9 { background: #fef2f2; border: 2px solid #dc2626; border-radius: 12px; padding: 20px; margin: 20px 0; }
.alerta-item9 h3 { color: #dc2626; margin-bottom: 10px; font-size: 16px; }
.alerta-item9 p { color: #7f1d1d; font-size: 14px; }
.alerta-item9 a { color: #dc2626; font-weight: 700; }

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
.faq-item.open .faq-icon { transform: rotate(180deg); }
.faq-icon { transition: transform 0.2s; }

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
    <a href="/gad-7" class="nav-link">GAD-7 (Ansiedade)</a>
  </div>
</nav>

<header class="hero">
  <span class="badge">Ferramenta Gratuita</span>
  <h1>PHQ-9 Online</h1>
  <p class="subtitle">Escala de rastreio de depressao com 9 itens. Pontuacao automatica, interpretacao clinica e PDF para o prontuario.</p>
</header>

<div class="container">

  <div class="card" id="questionario">
    <div class="instrucao">
      <strong>Durante as ultimas 2 semanas</strong>, com que frequencia voce foi incomodado por qualquer um dos seguintes problemas?
    </div>

    <div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
    <div class="progress-text" id="progress-text">0 de 9 respondidas</div>

    <div id="perguntas"></div>

    <button class="btn-calcular" id="btn-calc" disabled onclick="calcular()">Responda as 9 perguntas</button>
  </div>

  <div class="card resultado" id="resultado">
    <div class="score-box" id="score-box">
      <div>
        <span class="score-num" id="score-num">0</span>
        <span class="score-max">/27</span>
      </div>
      <div class="score-nivel" id="score-nivel">-</div>
      <div class="score-faixa" id="score-faixa">-</div>
    </div>

    <div class="alerta-item9" id="alerta-item9" style="display:none">
      <h3>Alerta: Item 9 requer atencao</h3>
      <p>Voce indicou pensamentos de se ferir. <strong>Isso pede avaliacao imediata de um profissional.</strong></p>
      <p style="margin-top:10px">Em crise agora: <a href="tel:188">188 (CVV, 24h)</a> ou <a href="tel:192">192 (SAMU)</a></p>
    </div>

    <div class="interpretacao">
      <h3>Interpretacao Clinica</h3>
      <p id="interpretacao-txt"></p>
      <p id="conduta-txt" style="margin-top:10px"></p>
    </div>

    <div class="tabela-scores">
      <h3>Referencia de Pontuacao PHQ-9</h3>
      <table>
        <thead><tr><th>Score</th><th>Nivel de Depressao</th></tr></thead>
        <tbody id="tabela-body">
          <tr data-min="0" data-max="4"><td>0-4</td><td>Minima ou ausente</td></tr>
          <tr data-min="5" data-max="9"><td>5-9</td><td>Leve</td></tr>
          <tr data-min="10" data-max="14"><td>10-14</td><td>Moderada</td></tr>
          <tr data-min="15" data-max="19"><td>15-19</td><td>Moderadamente grave</td></tr>
          <tr data-min="20" data-max="27"><td>20-27</td><td>Grave</td></tr>
        </tbody>
      </table>
    </div>

    <div class="acoes">
      <button class="btn-acao" onclick="compartilharWhatsApp()">Compartilhar WhatsApp</button>
      <button class="btn-acao" onclick="imprimir()">Imprimir Resultado</button>
      <button class="btn-acao" onclick="baixarCard()">Baixar Card</button>
      <button class="btn-acao" onclick="refazer()">Refazer Teste</button>
    </div>

    <div class="disclaimer">
      <strong>Aviso:</strong> O PHQ-9 e instrumento de rastreio, nao de diagnostico. O resultado nao substitui avaliacao psicologica ou psiquiatrica. Se pontuacao >= 10 ou item 9 > 0, procure um profissional.
    </div>

    <div class="cta-psi">
      <h3>E psicologo(a)?</h3>
      <p>Envie o PHQ-9 por link ao paciente e o score cai automatico no prontuario. Curva de 8 semanas incluida.</p>
      <a href="/planos" class="btn">Ver Planos EmotionAI</a>
    </div>
  </div>

  <div class="info-secao">
    <h2>Sobre o PHQ-9</h2>
    <p>O <strong>PHQ-9 (Patient Health Questionnaire-9)</strong> e um instrumento de rastreio de depressao amplamente utilizado. Foi desenvolvido por Kroenke, Spitzer e Williams (2001) com base nos criterios diagnosticos do DSM-5 para transtorno depressivo maior.</p>
    <p>No Brasil, foi validado por Santos et al. (2013), demonstrando sensibilidade de 88% e especificidade de 88% para deteccao de depressao maior. Possui parecer favoravel do SATEPSI/CFP para uso clinico.</p>
    <p>Cada item e pontuado de 0 a 3, gerando escore total de 0 a 27. O <strong>item 9</strong> pergunta sobre ideacao suicida ou pensamento de morte, exigindo atencao especial em qualquer pontuacao > 0.</p>
  </div>

  <div class="info-secao">
    <h2>Perguntas Frequentes</h2>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">O PHQ-9 diagnostica depressao? <span class="faq-icon">v</span></div>
      <div class="faq-a">Nao. E instrumento de <strong>rastreio</strong>, nao de diagnostico. O diagnostico so pode ser feito por profissional habilitado em avaliacao clinica completa (entrevista + criterios DSM-5/CID-11).</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Qual o ponto de corte clinico? <span class="faq-icon">v</span></div>
      <div class="faq-a">O ponto de corte usual e <strong>>= 10</strong>, indicando depressao clinicamente significativa que provavelmente requer intervencao. Scores 5-9 (leve) exigem monitoramento; >= 15 requer avaliacao urgente.</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">O que fazer com o item 9 (ideacao suicida)? <span class="faq-icon">v</span></div>
      <div class="faq-a"><strong>Qualquer pontuacao > 0 no item 9 exige avaliacao imediata de risco.</strong> Aplique escala de risco (ex: Columbia Suicide Severity Rating Scale). Nao termine a sessao sem plano de seguranca. Em crise ativa: 188 (CVV) ou 192 (SAMU).</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Com que frequencia devo reaplicar? <span class="faq-icon">v</span></div>
      <div class="faq-a">Recomenda-se reaplicacao a cada <strong>2-4 semanas</strong> durante tratamento ativo. A curva de 8 semanas permite avaliar resposta terapeutica (queda >= 50% = boa resposta).</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Posso usar no consultorio? <span class="faq-icon">v</span></div>
      <div class="faq-a">Sim. O PHQ-9 e de dominio publico, com parecer favoravel do SATEPSI/CFP. Deve ser aplicado por psicologo ou medico com interpretacao no contexto clinico. Nao substitui entrevista.</div>
    </div>

    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">O EmotionAI armazena minhas respostas? <span class="faq-icon">v</span></div>
      <div class="faq-a">Nao. Se voce nao esta logado, nada e salvo. As respostas ficam apenas no seu navegador. Psicologos com conta podem salvar historicos no prontuario com consentimento do paciente (LGPD Art. 11).</div>
    </div>
  </div>

  <div class="info-secao">
    <h2>Referencias</h2>
    <p style="font-size: 13px; color: #64748b;">
      Kroenke K, Spitzer RL, Williams JB. <em>The PHQ-9: validity of a brief depression severity measure.</em> J Gen Intern Med. 2001;16(9):606-13.<br><br>
      Santos IS, Tavares BF, Munhoz TN, et al. <em>Sensibilidade e especificidade do Patient Health Questionnaire-9 (PHQ-9) entre adultos da populacao geral.</em> Cad Saude Publica. 2013;29(8):1533-43.
    </p>
  </div>

</div>

<footer class="footer">
  <p><strong>EmotionAI</strong> - Saude mental com IA para psicologos brasileiros</p>
  <p style="margin-top:8px">Conforme LGPD (Lei 13.709/2018) e Resolucoes CFP 01/2009, 06/2019 e 09/2024</p>
  <p style="margin-top:8px"><a href="/privacidade">Privacidade</a> - <a href="/termos">Termos</a> - <a href="/">Home</a></p>
  <p style="margin-top:15px">Em crise: <a href="tel:188">188 (CVV)</a> ou <a href="tel:192">192 (SAMU)</a></p>
</footer>

<script>
const perguntas = [
  "Pouco interesse ou pouco prazer em fazer as coisas",
  "Se sentir para baixo, deprimido(a) ou sem perspectiva",
  "Dificuldade para pegar no sono ou permanecer dormindo, ou dormir mais do que de costume",
  "Se sentir cansado(a) ou com pouca energia",
  "Falta de apetite ou comer demais",
  "Se sentir mal consigo mesmo(a), ou achar que voce e um fracasso ou que decepcionou sua familia ou voce mesmo(a)",
  "Dificuldade para se concentrar nas coisas (como ler o jornal ou ver televisao)",
  "Lentidao para se movimentar ou falar (a ponto de outras pessoas perceberem), ou o oposto - estar tao agitado(a) ou irrequieto(a) que voce fica andando de um lado para o outro muito mais do que de costume",
  "Pensar em se ferir de alguma maneira ou que seria melhor estar morto(a)"
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
  const pct = (n / 9) * 100;
  document.getElementById("progress").style.width = pct + "%";
  document.getElementById("progress-text").textContent = `${n} de 9 respondidas`;
  const btn = document.getElementById("btn-calc");
  if (n === 9) {
    btn.disabled = false;
    btn.textContent = "Ver Resultado";
  } else {
    btn.disabled = true;
    btn.textContent = `Responda mais ${9-n} pergunta${9-n>1?"s":""}`;
  }
}

function calcular() {
  const total = Object.values(respostas).reduce((a,b) => a+b, 0);
  const item9 = respostas[8] || 0;

  let nivel, faixa, classe, interpretacao, conduta;
  if (total <= 4) {
    nivel = "Minima ou ausente";
    faixa = "Score 0-4";
    classe = "minima";
    interpretacao = "Nao ha evidencia de sintomas depressivos clinicamente significativos.";
    conduta = "Nao ha necessidade de intervencao especifica para depressao. Manter monitoramento em contextos de estresse.";
  } else if (total <= 9) {
    nivel = "Leve";
    faixa = "Score 5-9";
    classe = "leve";
    interpretacao = "Sintomas depressivos leves. Monitoramento clinico recomendado.";
    conduta = "Psicoeducacao, ativacao comportamental, monitorar evolucao. Reaplicar PHQ-9 em 2-4 semanas.";
  } else if (total <= 14) {
    nivel = "Moderada";
    faixa = "Score 10-14";
    classe = "moderada";
    interpretacao = "Sintomas depressivos moderados. Intervencao terapeutica indicada.";
    conduta = "Psicoterapia estruturada (TCC recomendada). Considerar avaliacao psiquiatrica. Reaplicar em 2 semanas.";
  } else if (total <= 19) {
    nivel = "Moderadamente grave";
    faixa = "Score 15-19";
    classe = "mod-grave";
    interpretacao = "Sintomas depressivos moderadamente graves. Tratamento ativo urgente.";
    conduta = "Psicoterapia + avaliacao psiquiatrica para farmacoterapia. Avaliar risco de suicidio semanalmente.";
  } else {
    nivel = "Grave";
    faixa = "Score 20-27";
    classe = "grave";
    interpretacao = "Sintomas depressivos graves. Requer intervencao imediata e intensiva.";
    conduta = "Psicoterapia semanal + avaliacao psiquiatrica urgente. Avaliar risco suicida em toda sessao. Considerar internacao se ideacao ativa.";
  }

  document.getElementById("score-num").textContent = total;
  document.getElementById("score-nivel").textContent = nivel;
  document.getElementById("score-faixa").textContent = faixa;
  document.getElementById("interpretacao-txt").textContent = interpretacao;
  document.getElementById("conduta-txt").textContent = "Conduta sugerida: " + conduta;

  const box = document.getElementById("score-box");
  box.className = "score-box " + classe;

  if (item9 > 0) {
    document.getElementById("alerta-item9").style.display = "block";
  }

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
  const txt = `PHQ-9: ${total}/27 (${nivel}) - Calcule tambem: https://emotion-platform-albert.onrender.com/phq-9`;
  window.open(`https://wa.me/?text=${encodeURIComponent(txt)}`, "_blank");
}

function imprimir() { window.print(); }

function baixarCard() {
  const total = Object.values(respostas).reduce((a,b) => a+b, 0);
  const nivel = document.getElementById("score-nivel").textContent;
  const data = new Date().toLocaleDateString("pt-BR");
  alert(`PHQ-9: ${total}/27 (${nivel})\nData: ${data}\n\nCard para stories em desenvolvimento. Por enquanto, use "Imprimir" para PDF.`);
}

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

@router.get("/phq-9", response_class=HTMLResponse)
async def phq9():
    return HTMLResponse(PHQ9_HTML)

@router.get("/phq9", response_class=HTMLResponse)
async def phq9_alt():
    return HTMLResponse(PHQ9_HTML)

class PHQ9Plugin(PluginBase):
    name = "phq9_publico"
    def setup(self, app):
        app.include_router(router)

plugin = PHQ9Plugin()
