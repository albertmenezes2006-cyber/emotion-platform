"""Pagina comparativa honesta vs PsicoManager (SEO)"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(tags=["Comparativos"])

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI vs PsicoManager: qual escolher em 2026? | EmotionAI</title>
<meta name="description" content="Comparativo honesto entre EmotionAI e PsicoManager. Preco, funcionalidades, IA, PHQ-9, GAD-7. Qual e melhor para o seu consultorio?">
<link rel="canonical" href="https://emotion-platform-albert.onrender.com/vs/psicomanager">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, sans-serif; background: #f8fafc; color: #1e293b; line-height: 1.6; }
.nav { background: white; padding: 15px 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 99; }
.nav-inner { max-width: 1000px; margin: 0 auto; display: flex; justify-content: space-between; }
.logo { font-size: 20px; font-weight: 800; background: linear-gradient(135deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }
.hero { max-width: 900px; margin: 0 auto; padding: 60px 20px; text-align: center; }
.badge { display: inline-block; background: #eff6ff; color: #1e40af; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 600; margin-bottom: 15px; }
h1 { font-size: 40px; font-weight: 800; margin-bottom: 20px; color: #0f172a; }
h1 .grad { background: linear-gradient(135deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.subtitle { color: #64748b; font-size: 18px; max-width: 700px; margin: 0 auto; }
.container { max-width: 1000px; margin: 0 auto; padding: 20px; }
.tldr { background: white; border-radius: 20px; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 30px; border-left: 4px solid #6366f1; }
.tldr h2 { font-size: 20px; margin-bottom: 12px; }
.tldr p { color: #475569; margin-bottom: 10px; }
.card { background: white; border-radius: 20px; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 20px; }
.card h2 { font-size: 24px; margin-bottom: 15px; }
table { width: 100%; border-collapse: collapse; margin: 20px 0; }
th, td { padding: 15px; text-align: left; border-bottom: 1px solid #e2e8f0; font-size: 14px; }
th { background: #f8fafc; font-weight: 700; }
th.us { background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; }
td.check { color: #10b981; font-weight: 700; }
td.no { color: #ef4444; }
td.neutral { color: #64748b; }
.veredito { background: linear-gradient(135deg, #eff6ff, #dbeafe); border-radius: 20px; padding: 30px; margin: 30px 0; }
.veredito h2 { color: #1e40af; margin-bottom: 15px; }
.veredito ul { list-style: none; padding: 0; }
.veredito li { padding: 10px 0 10px 25px; position: relative; color: #1e40af; }
.veredito li:before { content: "->"; position: absolute; left: 0; font-weight: 700; }
.escolha { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0; }
.escolha-card { background: white; border-radius: 16px; padding: 25px; border: 2px solid #e2e8f0; }
.escolha-card.us { border-color: #6366f1; background: linear-gradient(135deg, #f5f3ff, #ede9fe); }
.escolha-card h3 { font-size: 18px; margin-bottom: 12px; }
.escolha-card ul { list-style: none; padding: 0; }
.escolha-card li { padding: 6px 0 6px 22px; color: #475569; font-size: 14px; position: relative; }
.escolha-card li:before { content: "OK"; position: absolute; left: 0; color: #10b981; font-weight: 700; font-size: 11px; }
.btn { display: inline-block; margin-top: 15px; padding: 12px 24px; background: linear-gradient(135deg, #6366f1, #8b5cf6); color: white; text-decoration: none; border-radius: 10px; font-weight: 600; }
.faq-item { background: white; border-radius: 12px; padding: 20px; margin-bottom: 10px; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.faq-q { font-weight: 600; color: #0f172a; }
.faq-a { color: #64748b; font-size: 14px; margin-top: 12px; display: none; }
.faq-item.open .faq-a { display: block; }
.footer { text-align: center; padding: 40px 20px; color: #94a3b8; font-size: 12px; }
.footer a { color: #6366f1; text-decoration: none; }
@media (max-width: 700px) { h1 { font-size: 28px; } .escolha { grid-template-columns: 1fr; } th, td { padding: 10px 8px; font-size: 13px; } }
</style>
</head>
<body>
<nav class="nav">
  <div class="nav-inner">
    <a href="/" class="logo">EmotionAI</a>
    <a href="/planos" style="color:#64748b;text-decoration:none;font-size:14px;font-weight:500">Ver Planos</a>
  </div>
</nav>
<header class="hero">
  <span class="badge">Comparativo Honesto</span>
  <h1>EmotionAI vs <span class="grad">PsicoManager</span></h1>
  <p class="subtitle">Qual escolher em 2026? Comparativo honesto entre dois sistemas brasileiros para psicologos.</p>
</header>
<div class="container">
  <div class="tldr">
    <h2>Resumo em 3 linhas</h2>
    <p><strong>PsicoManager e gestao completa</strong> (agenda + prontuario + NFS-e + Pix + WhatsApp) por R$ 89-119/mes.</p>
    <p><strong>EmotionAI e escala + curva + IA barato</strong> (PHQ-9 e GAD-7 automaticos + evolucao + IA) por R$ 29,90/mes.</p>
    <p><strong>Nao decida sem testar os dois.</strong> Ambos tem plano gratis.</p>
  </div>
  <div class="card">
    <h2>Comparativo detalhado</h2>
    <table>
      <thead><tr><th>Recurso</th><th class="us">EmotionAI</th><th>PsicoManager</th></tr></thead>
      <tbody>
        <tr><td><strong>Preco Pro</strong></td><td class="check">R$ 29,90/mes</td><td class="neutral">R$ 89/mes</td></tr>
        <tr><td>Plano gratis permanente</td><td class="check">Sim (5 pacientes)</td><td class="neutral">7 dias trial</td></tr>
        <tr><td>PHQ-9 automatico com curva</td><td class="check">Sim, nativo</td><td class="no">Nao</td></tr>
        <tr><td>GAD-7 automatico com curva</td><td class="check">Sim, nativo</td><td class="no">Nao</td></tr>
        <tr><td>IA para nota clinica</td><td class="check">Sim</td><td class="check">Sim</td></tr>
        <tr><td>Chat IA (Sofia)</td><td class="check">Sim</td><td class="no">Nao</td></tr>
        <tr><td>Agenda online</td><td class="check">Sim</td><td class="check">Sim</td></tr>
        <tr><td>Prontuario LGPD</td><td class="check">Sim</td><td class="check">Sim</td></tr>
        <tr><td>NFS-e integrada</td><td class="no">Nao (em breve)</td><td class="check">Sim</td></tr>
        <tr><td>App do paciente</td><td class="no">Nao</td><td class="check">Sim</td></tr>
        <tr><td>WhatsApp automatico</td><td class="no">Nao (em breve)</td><td class="check">Sim</td></tr>
        <tr><td>Pix integrado</td><td class="check">Sim (Mercado Pago)</td><td class="check">Sim</td></tr>
        <tr><td>Dashboard emocional</td><td class="check">Sim, foco clinico</td><td class="neutral">Basico</td></tr>
        <tr><td>Anos de mercado</td><td class="neutral">Novo (2026)</td><td class="check">11 anos</td></tr>
        <tr><td>Psicologos ativos</td><td class="neutral">Em crescimento</td><td class="check">+40.000</td></tr>
      </tbody>
    </table>
  </div>
  <div class="veredito">
    <h2>Nossa opiniao honesta</h2>
    <ul>
      <li><strong>Precisa de NFS-e ou WhatsApp automatico:</strong> escolha PsicoManager.</li>
      <li><strong>Quer desfecho clinico mensuravel (PHQ-9, GAD-7):</strong> EmotionAI e melhor. 3x mais barato.</li>
      <li><strong>Esta comecando:</strong> EmotionAI tem plano gratis permanente.</li>
      <li><strong>Clinica com varios profissionais:</strong> PsicoManager tem mais experiencia.</li>
      <li><strong>Psicologo autonomo com foco em qualidade clinica:</strong> EmotionAI foi feito pra voce.</li>
    </ul>
  </div>
  <div class="escolha">
    <div class="escolha-card us">
      <h3>Escolha EmotionAI se:</h3>
      <ul>
        <li>Quer PHQ-9 e GAD-7 automaticos</li>
        <li>Valoriza dashboard emocional</li>
        <li>Precisa de IA para nota clinica</li>
        <li>Quer plano gratis permanente</li>
        <li>Prefere pagar menos (R$ 29,90)</li>
        <li>E psicologo autonomo</li>
      </ul>
      <a href="/planos" class="btn">Ver planos EmotionAI</a>
    </div>
    <div class="escolha-card">
      <h3>Escolha PsicoManager se:</h3>
      <ul>
        <li>Precisa de NFS-e integrada</li>
        <li>Quer app nativo do paciente</li>
        <li>Precisa WhatsApp automatico</li>
        <li>Tem clinica 5+ profissionais</li>
        <li>Ja atende ha muitos anos</li>
        <li>Quer marca consolidada</li>
      </ul>
      <a href="https://psicomanager.com.br" target="_blank" style="display:inline-block;margin-top:15px;padding:12px 24px;background:#e2e8f0;color:#475569;text-decoration:none;border-radius:10px;font-weight:600">Site PsicoManager</a>
    </div>
  </div>
  <div class="card">
    <h2>Perguntas frequentes</h2>
    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Posso migrar do PsicoManager para o EmotionAI?</div>
      <div class="faq-a">Sim. Voce pode exportar seus dados (LGPD Art. 18 V). Nossa equipe ajuda a importar. Sem custo.</div>
    </div>
    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">EmotionAI tem NFS-e?</div>
      <div class="faq-a">Ainda nao. Esta no roadmap 2026. Se precisa agora, PsicoManager e melhor.</div>
    </div>
    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Vocies sao seguros como o PsicoManager?</div>
      <div class="faq-a">Sim. Seguimos LGPD e Resolucoes CFP 01/2009, 06/2019 e 09/2024. AES-256, backup diario.</div>
    </div>
    <div class="faq-item" onclick="this.classList.toggle('open')">
      <div class="faq-q">Por que sao 3x mais barato?</div>
      <div class="faq-a">Startup solo, foco em automatizar. Sem time comercial. O que economizamos, repassamos.</div>
    </div>
  </div>
  <div class="card" style="background:linear-gradient(135deg,#6366f1,#8b5cf6);color:white;text-align:center">
    <h2 style="color:white">Ainda em duvida?</h2>
    <p style="opacity:0.9;margin-bottom:20px">Teste gratis. Sem cartao. Sem fidelidade.</p>
    <a href="/app/login?tab=cadastro" style="display:inline-block;padding:14px 32px;background:white;color:#6366f1;text-decoration:none;border-radius:10px;font-weight:700">Criar conta gratis</a>
  </div>
</div>
<footer class="footer">
  <p><strong>EmotionAI</strong> - Nao afiliado com PsicoManager</p>
  <p style="margin-top:8px">Comparativo baseado em dados publicos em 08/2026.</p>
  <p style="margin-top:15px"><a href="/">Home</a> - <a href="/planos">Planos</a> - <a href="/phq-9">PHQ-9</a> - <a href="/gad-7">GAD-7</a></p>
</footer>
</body>
</html>"""

@router.get("/vs/psicomanager", response_class=HTMLResponse)
async def vs_psicomanager():
    return HTMLResponse(HTML)

class VsPsicoPlugin(PluginBase):
    name = "vs_psicomanager"
    def setup(self, app):
        app.include_router(router)

plugin = VsPsicoPlugin()
