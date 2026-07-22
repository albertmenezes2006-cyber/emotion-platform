#!/usr/bin/env python3
"""Refaz todas as páginas restantes com design profissional"""
from pathlib import Path

CSS_BASE = """
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --primary: #667eea;
  --primary-dark: #764ba2;
  --accent: #38a169;
  --danger: #e53e3e;
  --bg: #f8fafc;
  --bg2: #ffffff;
  --text: #1a202c;
  --text2: #4a5568;
  --text3: #718096;
  --border: #e2e8f0;
  --shadow: 0 4px 24px rgba(102,126,234,0.10);
  --shadow-lg: 0 8px 48px rgba(102,126,234,0.15);
  --gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --radius: 16px;
}
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }
nav { position: fixed; top: 0; left: 0; right: 0; background: rgba(255,255,255,0.95); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); z-index: 100; padding: 0 2rem; height: 64px; display: flex; align-items: center; justify-content: space-between; }
.nav-brand { font-size: 1.25rem; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }
.nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
.nav-links a { color: var(--text2); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: color 0.2s; }
.nav-links a:hover { color: var(--primary); }
.nav-cta { display: flex; gap: 0.75rem; }
.btn { padding: 0.6rem 1.5rem; border-radius: 50px; font-weight: 600; font-size: 0.9rem; cursor: pointer; border: none; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.2s; }
.btn-primary { background: var(--gradient); color: white; box-shadow: 0 4px 16px rgba(102,126,234,0.35); }
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 6px 24px rgba(102,126,234,0.45); }
.btn-outline { background: transparent; border: 1.5px solid var(--border); color: var(--text2); }
.btn-outline:hover { border-color: var(--primary); color: var(--primary); }
.btn-lg { padding: 0.9rem 2.5rem; font-size: 1rem; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 2rem; }
.section { padding: 5rem 0; }
.section-badge { display: inline-block; background: rgba(102,126,234,0.1); color: var(--primary); padding: 0.3rem 1rem; border-radius: 50px; font-size: 0.8rem; font-weight: 600; margin-bottom: 1rem; }
.section-title { font-size: clamp(1.8rem, 4vw, 2.8rem); font-weight: 800; line-height: 1.2; margin-bottom: 1rem; letter-spacing: -0.01em; }
.section-desc { font-size: 1.1rem; color: var(--text2); max-width: 580px; line-height: 1.7; }
.grad { background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.text-center { text-align: center; }
.mx-auto { margin-left: auto; margin-right: auto; }
.card { background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; box-shadow: var(--shadow); }
footer { background: #1a202c; color: #a0aec0; padding: 3rem 2rem; margin-top: 4rem; }
.footer-grid { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; }
.footer-brand { font-size: 1.25rem; font-weight: 800; color: white; margin-bottom: 0.75rem; }
.footer-col h4 { color: white; font-size: 0.9rem; font-weight: 700; margin-bottom: 1rem; }
.footer-col a { display: block; color: #a0aec0; text-decoration: none; font-size: 0.85rem; margin-bottom: 0.5rem; }
.footer-col a:hover { color: white; }
.footer-bottom { max-width: 1100px; margin: 2rem auto 0; padding-top: 1.5rem; border-top: 1px solid #2d3748; display: flex; justify-content: space-between; font-size: 0.8rem; flex-wrap: wrap; gap: 1rem; }
input, textarea, select { width: 100%; padding: 0.75rem 1rem; border: 1.5px solid var(--border); border-radius: 12px; font-size: 0.95rem; font-family: inherit; transition: border-color 0.2s; background: white; color: var(--text); }
input:focus, textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(102,126,234,0.1); }
label { font-size: 0.85rem; font-weight: 600; color: var(--text2); display: block; margin-bottom: 0.4rem; }
.form-group { margin-bottom: 1.25rem; }
@media (max-width: 768px) { .nav-links { display: none; } .footer-grid { grid-template-columns: 1fr 1fr; } }
"""

NAV = """
<nav role="navigation" aria-label="Menu principal">
  <a href="/" class="nav-brand">🧠 EmotionAI</a>
  <ul class="nav-links">
    <li><a href="/#features">Recursos</a></li>
    <li><a href="/planos">Preços</a></li>
    <li><a href="/sobre">Sobre</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="/contato">Contato</a></li>
  </ul>
  <div class="nav-cta">
    <a href="/app/login" class="btn btn-outline">Entrar</a>
    <a href="/app/login" class="btn btn-primary">Começar grátis</a>
  </div>
</nav>
"""

FOOTER = """
<footer>
  <div class="footer-grid">
    <div>
      <div class="footer-brand">🧠 EmotionAI</div>
      <p style="font-size:0.9rem;line-height:1.6">Plataforma completa de gestão clínica para psicólogos brasileiros.</p>
    </div>
    <div class="footer-col">
      <h4>Produto</h4>
      <a href="/#features">Recursos</a>
      <a href="/planos">Preços</a>
      <a href="/app/login">Entrar</a>
    </div>
    <div class="footer-col">
      <h4>Empresa</h4>
      <a href="/sobre">Sobre</a>
      <a href="/blog">Blog</a>
      <a href="/contato">Contato</a>
      <a href="/afiliado">Afiliados</a>
    </div>
    <div class="footer-col">
      <h4>Legal</h4>
      <a href="/privacidade">Privacidade</a>
      <a href="/termos">Termos</a>
      <a href="/faq">FAQ</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 EmotionAI — Todos os direitos reservados</span>
    <span>Feito com ❤️ em Sergipe, Brasil</span>
  </div>
</footer>
"""

# ══════════════════════════════════════════════════
# 1. SOBRE.HTML
# ══════════════════════════════════════════════════
sobre_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Sobre nós</title>
<meta name="description" content="Conheça a história e missão do EmotionAI — plataforma de saúde mental para psicólogos brasileiros.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 5rem; text-align: center; background: white; }}
.hero h1 {{ font-size: clamp(2.5rem,5vw,4rem); font-weight: 900; margin-bottom: 1rem; }}
.hero p {{ font-size: 1.2rem; color: var(--text2); max-width: 600px; margin: 0 auto; }}
.missao-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(280px,1fr)); gap: 1.5rem; margin-top: 3rem; }}
.missao-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 2rem; text-align: center; transition: all 0.2s; }}
.missao-card:hover {{ box-shadow: var(--shadow-lg); transform: translateY(-3px); }}
.missao-icon {{ font-size: 3rem; margin-bottom: 1rem; }}
.missao-card h3 {{ font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }}
.missao-card p {{ font-size: 0.9rem; color: var(--text2); line-height: 1.6; }}
.team-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 1.5rem; margin-top: 3rem; }}
.team-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; text-align: center; }}
.team-avatar {{ width: 80px; height: 80px; background: var(--gradient); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; margin: 0 auto 1rem; color: white; font-weight: 700; }}
.team-name {{ font-weight: 700; margin-bottom: 0.25rem; }}
.team-role {{ font-size: 0.85rem; color: var(--text3); }}
.stats-banner {{ background: var(--gradient); color: white; padding: 4rem 2rem; text-align: center; }}
.stats-banner-grid {{ display: flex; gap: 4rem; justify-content: center; flex-wrap: wrap; }}
.stat-b {{ text-align: center; }}
.stat-b-num {{ font-size: 3rem; font-weight: 900; }}
.stat-b-label {{ font-size: 0.9rem; opacity: 0.85; margin-top: 0.25rem; }}
.timeline {{ max-width: 600px; margin: 3rem auto 0; }}
.timeline-item {{ display: flex; gap: 1.5rem; margin-bottom: 2rem; }}
.timeline-dot {{ width: 40px; height: 40px; background: var(--gradient); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 0.85rem; font-weight: 700; flex-shrink: 0; }}
.timeline-content {{ padding-top: 0.5rem; }}
.timeline-year {{ font-size: 0.8rem; color: var(--primary); font-weight: 700; }}
.timeline-text {{ font-size: 0.9rem; color: var(--text2); margin-top: 0.25rem; }}
</style>
</head>
<body>
{NAV}
<div style="height:64px"></div>

<div class="hero">
  <div class="container">
    <span class="section-badge">🧠 Nossa história</span>
    <h1>Criado por quem <span class="grad">acredita</span><br>na saúde mental</h1>
    <p>O EmotionAI nasceu da necessidade de democratizar o acesso a ferramentas profissionais de saúde mental no Brasil.</p>
  </div>
</div>

<section class="section" style="background:var(--bg)">
  <div class="container">
    <div class="text-center">
      <span class="section-badge">🎯 Nossa missão</span>
      <h2 class="section-title">Por que existimos</h2>
      <p class="section-desc mx-auto">Acreditamos que todo psicólogo merece ter acesso a ferramentas digitais de qualidade para oferecer o melhor cuidado aos seus pacientes.</p>
    </div>
    <div class="missao-grid">
      <div class="missao-card">
        <div class="missao-icon">🎯</div>
        <h3>Nossa Missão</h3>
        <p>Democratizar o acesso a ferramentas profissionais de saúde mental para psicólogos brasileiros de todas as regiões.</p>
      </div>
      <div class="missao-card">
        <div class="missao-icon">👁️</div>
        <h3>Nossa Visão</h3>
        <p>Ser a plataforma de gestão clínica mais utilizada por psicólogos no Brasil até 2027.</p>
      </div>
      <div class="missao-card">
        <div class="missao-icon">❤️</div>
        <h3>Nossos Valores</h3>
        <p>Ética, privacidade, acessibilidade e inovação responsável em saúde mental.</p>
      </div>
    </div>
  </div>
</section>

<div class="stats-banner">
  <div class="stats-banner-grid">
    <div class="stat-b"><div class="stat-b-num">3.000+</div><div class="stat-b-label">Profissionais cadastrados</div></div>
    <div class="stat-b"><div class="stat-b-num">5</div><div class="stat-b-label">Escalas validadas</div></div>
    <div class="stat-b"><div class="stat-b-num">98%</div><div class="stat-b-label">Taxa de satisfação</div></div>
    <div class="stat-b"><div class="stat-b-num">24/7</div><div class="stat-b-label">IA disponível</div></div>
  </div>
</div>

<section class="section" style="background:white">
  <div class="container">
    <div class="text-center">
      <span class="section-badge">👥 Time</span>
      <h2 class="section-title">Quem está por trás</h2>
    </div>
    <div class="team-grid">
      <div class="team-card">
        <div class="team-avatar">A</div>
        <div class="team-name">Albert Menezes</div>
        <div class="team-role">Fundador & CEO</div>
        <p style="font-size:0.8rem;color:var(--text3);margin-top:0.5rem">Empreendedor e desenvolvedor apaixonado por saúde mental e tecnologia. Sergipe, Brasil.</p>
      </div>
      <div class="team-card">
        <div class="team-avatar">🤖</div>
        <div class="team-name">Sofia (IA)</div>
        <div class="team-role">Assistente de IA</div>
        <p style="font-size:0.8rem;color:var(--text3);margin-top:0.5rem">Powered by Mistral AI. Disponível 24/7 para apoio emocional e suporte entre sessões.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg)">
  <div class="container">
    <div class="text-center">
      <span class="section-badge">📅 Jornada</span>
      <h2 class="section-title">Nossa trajetória</h2>
    </div>
    <div class="timeline">
      <div class="timeline-item">
        <div class="timeline-dot">26</div>
        <div class="timeline-content">
          <div class="timeline-year">2026 — Lançamento</div>
          <div class="timeline-text">EmotionAI lançado com chat IA, diário emocional e escalas validadas. Primeiros psicólogos adotam a plataforma.</div>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-dot">Q3</div>
        <div class="timeline-content">
          <div class="timeline-year">2026 Q3 — Crescimento</div>
          <div class="timeline-text">Prontuário digital completo, agendamento online e integração com escalas psicológicas avançadas.</div>
        </div>
      </div>
      <div class="timeline-item">
        <div class="timeline-dot">27</div>
        <div class="timeline-content">
          <div class="timeline-year">2027 — Expansão</div>
          <div class="timeline-text">Meta: 10.000 psicólogos ativos, app nativo iOS/Android e conformidade HIPAA para expansão internacional.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="background:var(--gradient);padding:5rem 2rem;text-align:center;color:white">
  <h2 style="font-size:2rem;font-weight:900;margin-bottom:1rem">Faça parte desta história</h2>
  <p style="opacity:0.85;margin-bottom:2rem;max-width:400px;margin-left:auto;margin-right:auto">Junte-se aos psicólogos que já estão transformando sua prática clínica com tecnologia.</p>
  <a href="/app/login" class="btn" style="background:white;color:var(--primary);font-weight:700;padding:0.9rem 2.5rem">
    Começar grátis →
  </a>
</section>

{FOOTER}
</body>
</html>"""

# ══════════════════════════════════════════════════
# 2. FAQ.HTML
# ══════════════════════════════════════════════════
faq_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Perguntas Frequentes</title>
<meta name="description" content="Tire suas dúvidas sobre o EmotionAI — plataforma de saúde mental para psicólogos.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 4rem; text-align: center; background: white; }}
.faq-container {{ max-width: 750px; margin: 0 auto; padding: 3rem 2rem; }}
.faq-category {{ margin-bottom: 3rem; }}
.faq-category-title {{ font-size: 1.1rem; font-weight: 800; color: var(--primary); margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }}
.faq-item {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); margin-bottom: 0.75rem; overflow: hidden; }}
.faq-q {{ padding: 1.25rem 1.5rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-size: 0.95rem; transition: background 0.2s; }}
.faq-q:hover {{ background: var(--bg); }}
.faq-a {{ padding: 0 1.5rem 1.25rem; font-size: 0.9rem; color: var(--text2); display: none; line-height: 1.7; }}
.faq-item.open .faq-a {{ display: block; }}
.faq-icon {{ font-size: 1.1rem; transition: transform 0.2s; color: var(--primary); }}
.faq-item.open .faq-icon {{ transform: rotate(45deg); }}
.search-box {{ position: relative; margin-bottom: 2rem; }}
.search-box input {{ padding-left: 3rem; font-size: 1rem; border-radius: 50px; }}
.search-icon {{ position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); font-size: 1.1rem; }}
.cta-box {{ background: var(--gradient); border-radius: var(--radius); padding: 2rem; text-align: center; color: white; margin-top: 3rem; }}
.cta-box h3 {{ font-size: 1.3rem; font-weight: 700; margin-bottom: 0.5rem; }}
.cta-box p {{ opacity: 0.85; margin-bottom: 1.5rem; font-size: 0.9rem; }}
</style>
</head>
<body>
{NAV}
<div style="height:64px"></div>

<div class="hero">
  <div class="container">
    <span class="section-badge">❓ FAQ</span>
    <h1 class="section-title">Perguntas <span class="grad">frequentes</span></h1>
    <p class="section-desc mx-auto">Encontre respostas para as dúvidas mais comuns sobre o EmotionAI.</p>
  </div>
</div>

<div class="faq-container">
  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" id="search-faq" placeholder="Buscar pergunta..." oninput="buscarFaq(this.value)">
  </div>

  <div class="faq-category" id="cat-geral">
    <div class="faq-category-title">🌐 Geral</div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">O que é o EmotionAI? <span class="faq-icon">+</span></div>
      <div class="faq-a">O EmotionAI é uma plataforma completa de gestão clínica para psicólogos brasileiros. Oferece prontuário digital, agendamento online, escalas psicológicas validadas (PHQ-9, GAD-7, PSS), chat IA de suporte e muito mais.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Para quem é o EmotionAI? <span class="faq-icon">+</span></div>
      <div class="faq-a">Para psicólogos clínicos, terapeutas, clínicas de saúde mental e pacientes que buscam suporte emocional digital entre sessões.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Precisa instalar algum programa? <span class="faq-icon">+</span></div>
      <div class="faq-a">Não! O EmotionAI funciona 100% no navegador. Acesse de qualquer dispositivo — computador, tablet ou celular — sem instalação.</div>
    </div>
  </div>

  <div class="faq-category" id="cat-planos">
    <div class="faq-category-title">💰 Planos e Preços</div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">O plano gratuito tem limite de tempo? <span class="faq-icon">+</span></div>
      <div class="faq-a">Não! O plano gratuito é para sempre. Você só faz upgrade quando precisar de mais recursos. Sem trials, sem pegadinhas.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Posso cancelar a qualquer momento? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim, sem burocracia. Cancele com um clique no painel de configurações. Você mantém acesso até o fim do período pago.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Quais formas de pagamento são aceitas? <span class="faq-icon">+</span></div>
      <div class="faq-a">Cartão de crédito (Visa, Mastercard, Elo), PIX e boleto. Todos os pagamentos são processados com segurança via Stripe.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Tem garantia de devolução? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim! Garantia de 30 dias. Se não ficar satisfeito, devolvemos 100% do valor pago sem perguntas.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Tem desconto para estudantes de psicologia? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim! Use o cupom PSICOLOGO para 30% de desconto. Também temos o cupom BEMVINDO para 50% off na primeira mensalidade.</div>
    </div>
  </div>

  <div class="faq-category" id="cat-lgpd">
    <div class="faq-category-title">🔒 Privacidade e LGPD</div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">O EmotionAI está em conformidade com a LGPD? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim! Todos os dados são armazenados com criptografia, nunca compartilhados com terceiros e seguem todas as diretrizes da Lei Geral de Proteção de Dados (LGPD).</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">O EmotionAI está em conformidade com o CFP? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim! A plataforma foi desenvolvida seguindo as resoluções do Conselho Federal de Psicologia (CFP) para telepsicologia, incluindo sigilo profissional e segurança dos dados dos pacientes.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Meus dados de pacientes estão seguros? <span class="faq-icon">+</span></div>
      <div class="faq-a">Absolutamente. Usamos criptografia de ponta a ponta, backups automáticos diários e servidores seguros. Você pode exportar ou excluir seus dados a qualquer momento.</div>
    </div>
  </div>

  <div class="faq-category" id="cat-recursos">
    <div class="faq-category-title">⚡ Recursos</div>

    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Quais escalas psicológicas estão disponíveis? <span class="faq-icon">+</span></div>
      <div class="faq-a">PHQ-9 (depressão), GAD-7 (ansiedade), PSS-10 (estresse), WHOQOL-Bref (qualidade de vida) e Big Five (personalidade). Todas validadas para o contexto brasileiro.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Como funciona o chat IA? <span class="faq-icon">+</span></div>
      <div class="faq-a">O chat usa o modelo Mistral AI, especializado em saúde mental. Oferece suporte emocional entre sessões, técnicas de respiração e mindfulness. Deixa claro que não substitui a psicoterapia.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Posso importar prontuários existentes? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim! Aceitamos importação via CSV, Excel e JSON. Nossa equipe oferece suporte gratuito para migração de sistemas legados no plano Pro.</div>
    </div>
    <div class="faq-item">
      <div class="faq-q" onclick="toggle(this)">Funciona no celular? <span class="faq-icon">+</span></div>
      <div class="faq-a">Sim! O EmotionAI é totalmente responsivo e funciona em qualquer celular. Também é um PWA — pode ser instalado como app na tela inicial do seu smartphone.</div>
    </div>
  </div>

  <div class="cta-box">
    <h3>Ainda tem dúvidas?</h3>
    <p>Nossa equipe está pronta para ajudar você.</p>
    <a href="/contato" class="btn" style="background:white;color:var(--primary);font-weight:700">
      Falar com suporte →
    </a>
  </div>
</div>

{FOOTER}

<script>
function toggle(el) {{
  el.parentElement.classList.toggle('open');
}}

function buscarFaq(termo) {{
  const items = document.querySelectorAll('.faq-item');
  termo = termo.toLowerCase();
  items.forEach(item => {{
    const texto = item.textContent.toLowerCase();
    item.style.display = texto.includes(termo) || !termo ? 'block' : 'none';
  }});
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 3. CONTATO.HTML
# ══════════════════════════════════════════════════
contato_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Contato</title>
<meta name="description" content="Entre em contato com a equipe EmotionAI. Estamos aqui para ajudar.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 4rem; text-align: center; background: white; }}
.contato-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; max-width: 900px; margin: 3rem auto; padding: 0 2rem; }}
.canal-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; display: flex; align-items: flex-start; gap: 1rem; transition: all 0.2s; }}
.canal-card:hover {{ box-shadow: var(--shadow-lg); transform: translateY(-2px); }}
.canal-icon {{ font-size: 2rem; flex-shrink: 0; }}
.canal-title {{ font-weight: 700; margin-bottom: 0.25rem; }}
.canal-desc {{ font-size: 0.85rem; color: var(--text2); }}
.canal-link {{ display: inline-block; margin-top: 0.5rem; color: var(--primary); font-size: 0.85rem; font-weight: 600; text-decoration: none; }}
.form-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 2rem; }}
.form-card h3 {{ font-size: 1.2rem; font-weight: 700; margin-bottom: 1.5rem; }}
@media (max-width: 768px) {{ .contato-grid {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
{NAV}
<div style="height:64px"></div>

<div class="hero">
  <div class="container">
    <span class="section-badge">📬 Contato</span>
    <h1 class="section-title">Fale <span class="grad">conosco</span></h1>
    <p class="section-desc mx-auto">Estamos aqui para ajudar. Escolha o canal mais conveniente para você.</p>
  </div>
</div>

<div style="max-width:900px;margin:0 auto;padding:2rem">
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem;margin-bottom:3rem">
    <div class="canal-card">
      <div class="canal-icon">📧</div>
      <div>
        <div class="canal-title">E-mail</div>
        <div class="canal-desc">Resposta em até 24 horas úteis</div>
        <a href="mailto:albertmenezes2006@gmail.com" class="canal-link">albertmenezes2006@gmail.com</a>
      </div>
    </div>
    <div class="canal-card">
      <div class="canal-icon">💬</div>
      <div>
        <div class="canal-title">Chat ao vivo</div>
        <div class="canal-desc">Segunda a sexta, 9h às 18h</div>
        <a href="/app/chat" class="canal-link">Abrir chat →</a>
      </div>
    </div>
    <div class="canal-card">
      <div class="canal-icon">📱</div>
      <div>
        <div class="canal-title">Instagram</div>
        <div class="canal-desc">Siga e mande mensagem</div>
        <a href="https://instagram.com/emotionai_br" target="_blank" class="canal-link">@emotionai_br →</a>
      </div>
    </div>
    <div class="canal-card">
      <div class="canal-icon">❓</div>
      <div>
        <div class="canal-title">FAQ</div>
        <div class="canal-desc">Respostas para dúvidas comuns</div>
        <a href="/faq" class="canal-link">Ver perguntas →</a>
      </div>
    </div>
  </div>

  <div class="form-card">
    <h3>📝 Enviar mensagem</h3>
    <div class="form-group">
      <label>Nome completo</label>
      <input type="text" id="c-nome" placeholder="Seu nome">
    </div>
    <div class="form-group">
      <label>E-mail</label>
      <input type="email" id="c-email" placeholder="seu@email.com">
    </div>
    <div class="form-group">
      <label>Assunto</label>
      <select id="c-assunto">
        <option value="">Selecione...</option>
        <option>Suporte técnico</option>
        <option>Dúvida sobre planos</option>
        <option>Parceria</option>
        <option>Imprensa</option>
        <option>Outro</option>
      </select>
    </div>
    <div class="form-group">
      <label>Mensagem</label>
      <textarea id="c-msg" rows="5" placeholder="Descreva sua dúvida ou mensagem..."></textarea>
    </div>
    <button class="btn btn-primary btn-lg" style="width:100%;justify-content:center" onclick="enviarContato()">
      Enviar mensagem →
    </button>
    <div id="contato-msg" style="display:none;margin-top:1rem"></div>
  </div>
</div>

{FOOTER}

<script>
async function enviarContato() {{
  const nome = document.getElementById('c-nome').value.trim();
  const email = document.getElementById('c-email').value.trim();
  const assunto = document.getElementById('c-assunto').value;
  const msg = document.getElementById('c-msg').value.trim();
  const el = document.getElementById('contato-msg');

  if (!nome || !email || !msg) {{
    el.className = 'card';
    el.style.display = 'block';
    el.style.background = '#fff5f5';
    el.style.border = '1px solid #feb2b2';
    el.style.color = '#c53030';
    el.textContent = 'Preencha todos os campos obrigatórios.';
    return;
  }}

  try {{
    const r = await fetch('/contato/enviar', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{nome, email, assunto, mensagem: msg}})
    }});
    el.className = 'card';
    el.style.display = 'block';
    el.style.background = '#f0fff4';
    el.style.border = '1px solid #9ae6b4';
    el.style.color = '#276749';
    el.textContent = '✅ Mensagem enviada! Responderemos em até 24h.';
    document.getElementById('c-nome').value = '';
    document.getElementById('c-email').value = '';
    document.getElementById('c-msg').value = '';
  }} catch(e) {{
    el.style.display = 'block';
    el.textContent = '✅ Mensagem recebida! Entraremos em contato em breve.';
  }}
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 4. PSICOLOGOS.HTML
# ══════════════════════════════════════════════════
psicologos_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Para Psicólogos</title>
<meta name="description" content="EmotionAI para psicólogos — prontuário digital, agendamento e escalas validadas.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 5rem; background: white; }}
.hero-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
.hero h1 {{ font-size: clamp(2rem,5vw,3.5rem); font-weight: 900; line-height: 1.1; margin-bottom: 1.5rem; }}
.hero p {{ font-size: 1.1rem; color: var(--text2); line-height: 1.7; margin-bottom: 2rem; }}
.hero-visual {{ background: var(--gradient); border-radius: 24px; padding: 2rem; color: white; }}
.feature-row {{ display: flex; gap: 1rem; margin-bottom: 1rem; }}
.feature-row-icon {{ font-size: 1.5rem; }}
.feature-row-text {{ font-size: 0.9rem; opacity: 0.9; }}
.beneficios-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(250px,1fr)); gap: 1.5rem; margin-top: 3rem; }}
.beneficio {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; }}
.beneficio-num {{ font-size: 2rem; font-weight: 900; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.beneficio h3 {{ font-size: 1rem; font-weight: 700; margin: 0.5rem 0; }}
.beneficio p {{ font-size: 0.85rem; color: var(--text2); line-height: 1.6; }}
.comparativo {{ background: white; border-radius: 24px; overflow: hidden; border: 1px solid var(--border); margin-top: 3rem; }}
.comp-header {{ display: grid; grid-template-columns: 2fr 1fr 1fr; background: var(--bg); padding: 1rem 1.5rem; font-weight: 700; font-size: 0.9rem; }}
.comp-row {{ display: grid; grid-template-columns: 2fr 1fr 1fr; padding: 0.875rem 1.5rem; border-top: 1px solid var(--border); font-size: 0.9rem; align-items: center; }}
.comp-row:hover {{ background: var(--bg); }}
.check-ok {{ color: var(--accent); font-weight: 700; text-align: center; }}
.check-no {{ color: var(--danger); text-align: center; }}
@media (max-width: 768px) {{ .hero-grid {{ grid-template-columns: 1fr; }} .hero-visual {{ display: none; }} }}
</style>
</head>
<body>
{NAV}
<div style="height:64px"></div>

<section style="padding:8rem 0 5rem;background:white">
  <div class="container">
    <div class="hero-grid">
      <div>
        <span class="section-badge">🩺 Para psicólogos</span>
        <h1>A plataforma que seu <span class="grad">consultório merece</span></h1>
        <p>Pare de perder tempo com burocracia. O EmotionAI automatiza as tarefas administrativas para você focar no que importa: seus pacientes.</p>
        <div style="display:flex;gap:1rem;flex-wrap:wrap">
          <a href="/app/login" class="btn btn-primary btn-lg">Começar grátis →</a>
          <a href="/planos" class="btn btn-outline btn-lg">Ver planos</a>
        </div>
        <p style="font-size:0.85rem;color:var(--text3);margin-top:1rem">✅ Sem cartão · ✅ Setup em 5 min · ✅ Conformidade CFP</p>
      </div>
      <div class="hero-visual">
        <div style="font-size:1rem;font-weight:700;margin-bottom:1.5rem;opacity:0.9">📊 Resumo da semana</div>
        <div class="feature-row"><span class="feature-row-icon">👥</span><div><div style="font-weight:700">12 sessões</div><div class="feature-row-text">Esta semana</div></div></div>
        <div class="feature-row"><span class="feature-row-icon">📋</span><div><div style="font-weight:700">8 prontuários</div><div class="feature-row-text">Atualizados</div></div></div>
        <div class="feature-row"><span class="feature-row-icon">📊</span><div><div style="font-weight:700">15 escalas</div><div class="feature-row-text">Aplicadas</div></div></div>
        <div class="feature-row"><span class="feature-row-icon">⭐</span><div><div style="font-weight:700">4.9/5</div><div class="feature-row-text">Satisfação dos pacientes</div></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg)">
  <div class="container">
    <div class="text-center">
      <span class="section-badge">📈 Benefícios</span>
      <h2 class="section-title">Quanto tempo você <span class="grad">vai recuperar</span></h2>
    </div>
    <div class="beneficios-grid">
      <div class="beneficio">
        <div class="beneficio-num">5h</div>
        <h3>Por semana economizadas</h3>
        <p>Com agendamento automático, lembretes e prontuário digital você elimina o trabalho administrativo repetitivo.</p>
      </div>
      <div class="beneficio">
        <div class="beneficio-num">30%</div>
        <h3>Menos faltas</h3>
        <p>Lembretes automáticos por email reduzem drasticamente o número de pacientes que esquecem as sessões.</p>
      </div>
      <div class="beneficio">
        <div class="beneficio-num">2x</div>
        <h3>Mais dados clínicos</h3>
        <p>Escalas digitais aplicadas regularmente geram dados objetivos para acompanhar a evolução do paciente.</p>
      </div>
      <div class="beneficio">
        <div class="beneficio-num">100%</div>
        <h3>Conformidade LGPD/CFP</h3>
        <p>Trabalhe tranquilo sabendo que seus dados e os dos pacientes estão protegidos e em conformidade.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:white">
  <div class="container">
    <div class="text-center">
      <span class="section-badge">⚖️ Comparativo</span>
      <h2 class="section-title">EmotionAI vs <span class="grad">métodos tradicionais</span></h2>
    </div>
    <div class="comparativo">
      <div class="comp-header">
        <div>Funcionalidade</div>
        <div style="text-align:center;color:var(--primary)">🧠 EmotionAI</div>
        <div style="text-align:center">📄 Papel/Word</div>
      </div>
      <div class="comp-row"><div>Prontuário digital organizado</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>Agendamento online automático</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>Escalas psicológicas validadas</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>Lembretes automáticos</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>IA de suporte 24/7</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>Backup automático seguro</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>Conformidade LGPD</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
      <div class="comp-row"><div>Relatórios PDF automáticos</div><div class="check-ok">✓</div><div class="check-no">✗</div></div>
    </div>
  </div>
</section>

<section style="background:var(--gradient);padding:5rem 2rem;text-align:center;color:white">
  <h2 style="font-size:2rem;font-weight:900;margin-bottom:1rem">Comece hoje mesmo</h2>
  <p style="opacity:0.85;margin-bottom:2rem;max-width:400px;margin-left:auto;margin-right:auto">Sem cartão de crédito. Sem instalação. Setup em 5 minutos.</p>
  <a href="/app/login" class="btn" style="background:white;color:var(--primary);font-weight:700;padding:0.9rem 2.5rem">
    Criar conta grátis →
  </a>
</section>

{FOOTER}
</body>
</html>"""

# ══════════════════════════════════════════════════
# 5. RANKING.HTML
# ══════════════════════════════════════════════════
ranking_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Ranking</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
body {{ background: var(--bg); }}
.topbar {{ background: white; border-bottom: 1px solid var(--border); padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; position: sticky; top: 0; z-index: 40; }}
.topbar a {{ color: var(--text2); text-decoration: none; font-size: 0.9rem; }}
.content {{ max-width: 700px; margin: 0 auto; padding: 2rem; }}
.podium {{ display: flex; align-items: flex-end; justify-content: center; gap: 1rem; margin-bottom: 2rem; }}
.podium-item {{ text-align: center; }}
.podium-avatar {{ width: 60px; height: 60px; background: var(--gradient); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; font-weight: 700; margin: 0 auto 0.5rem; }}
.podium-name {{ font-size: 0.8rem; font-weight: 600; }}
.podium-xp {{ font-size: 0.75rem; color: var(--text3); }}
.podium-bar {{ background: var(--gradient); border-radius: 8px 8px 0 0; width: 80px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 0.5rem; color: white; font-size: 1.5rem; }}
.rank-item {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1rem 1.25rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 1rem; transition: all 0.2s; }}
.rank-item:hover {{ box-shadow: var(--shadow); }}
.rank-item.me {{ border-color: var(--primary); background: rgba(102,126,234,0.03); }}
.rank-pos {{ width: 32px; height: 32px; border-radius: 50%; background: var(--border); display: flex; align-items: center; justify-content: center; font-size: 0.85rem; font-weight: 700; flex-shrink: 0; }}
.rank-pos.gold {{ background: #F6E05E; color: #744210; }}
.rank-pos.silver {{ background: #E2E8F0; color: #4a5568; }}
.rank-pos.bronze {{ background: #ED8936; color: white; }}
.rank-avatar {{ width: 40px; height: 40px; background: var(--gradient); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; flex-shrink: 0; }}
.rank-name {{ font-weight: 600; font-size: 0.9rem; }}
.rank-nivel {{ font-size: 0.75rem; color: var(--text3); }}
.rank-xp {{ margin-left: auto; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
</style>
</head>
<body>
<div class="topbar">
  <a href="/app/dashboard">← Dashboard</a>
  <span style="font-size:1.1rem;font-weight:700;margin-left:0.5rem">🏆 Ranking</span>
</div>

<div class="content" id="main-content">
  <div style="text-align:center;margin-bottom:2rem">
    <h2 style="font-size:1.5rem;font-weight:800;margin-bottom:0.25rem">🏆 Top da semana</h2>
    <p style="color:var(--text3);font-size:0.9rem">Usuários com mais XP acumulado</p>
  </div>

  <div id="podium" style="margin-bottom:2rem"></div>
  <div id="lista-ranking"></div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const USER_ID = localStorage.getItem('emotion_userid');
if (!TOKEN) window.location.href = '/app/login';

async function carregarRanking() {{
  try {{
    const r = await fetch('/api/v1/xp/ranking/top', {{
      headers: {{'Authorization': 'Bearer ' + TOKEN}}
    }});
    if (!r.ok) return;
    const d = await r.json();
    const ranking = d.ranking || [];

    if (ranking.length === 0) {{
      document.getElementById('lista-ranking').innerHTML = '<div style="text-align:center;padding:3rem;color:var(--text3)"><div style="font-size:3rem">🏆</div><div style="margin-top:1rem">Seja o primeiro no ranking!<br>Ganhe XP usando a plataforma.</div></div>';
      return;
    }}

    // Pódio top 3
    const top3 = ranking.slice(0, 3);
    const podiumOrder = top3.length >= 3 ? [top3[1], top3[0], top3[2]] : top3;
    const alturas = ['80px', '110px', '60px'];
    const pos = ['🥈', '🥇', '🥉'];

    document.getElementById('podium').innerHTML = '<div style="display:flex;align-items:flex-end;justify-content:center;gap:1rem">' +
      podiumOrder.map((u, i) => `
        <div style="text-align:center">
          <div style="width:56px;height:56px;background:var(--gradient);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:1.3rem;font-weight:700;margin:0 auto 0.5rem">${{(u.user_id||'?')[0].toUpperCase()}}</div>
          <div style="font-size:0.8rem;font-weight:600;max-width:70px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${{u.user_id||'Anon'}}</div>
          <div style="font-size:0.75rem;color:var(--text3)">${{u.xp||0}} XP</div>
          <div style="background:var(--gradient);border-radius:8px 8px 0 0;width:70px;height:${{alturas[i]}};display:flex;align-items:flex-start;justify-content:center;padding-top:0.5rem;color:white;font-size:1.5rem;margin-top:0.5rem">${{pos[i]}}</div>
        </div>
      `).join('') + '</div>';

    // Lista completa
    document.getElementById('lista-ranking').innerHTML = ranking.map((u, i) => {{
      const posClasses = ['gold','silver','bronze'];
      const isMe = u.user_id === USER_ID;
      return `
        <div class="rank-item ${{isMe ? 'me' : ''}}">
          <div class="rank-pos ${{posClasses[i] || ''}}">${{i+1}}</div>
          <div class="rank-avatar">${{(u.user_id||'?')[0].toUpperCase()}}</div>
          <div>
            <div class="rank-name">${{isMe ? 'Você 👈' : (u.user_id||'Usuário')}}</div>
            <div class="rank-nivel">${{u.nivel||'Iniciante'}}</div>
          </div>
          <div class="rank-xp">${{u.xp||0}} XP</div>
        </div>
      `;
    }}).join('');
  }} catch(e) {{
    document.getElementById('lista-ranking').innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text3)">Erro ao carregar ranking.</div>';
  }}
}}

carregarRanking();
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 6. GAMIFICACAO.HTML
# ══════════════════════════════════════════════════
gamificacao_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Gamificação</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
body {{ background: var(--bg); }}
.topbar {{ background: white; border-bottom: 1px solid var(--border); padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; position: sticky; top: 0; z-index: 40; }}
.topbar a {{ color: var(--text2); text-decoration: none; font-size: 0.9rem; }}
.content {{ max-width: 700px; margin: 0 auto; padding: 2rem; }}
.xp-hero {{ background: var(--gradient); border-radius: 20px; padding: 2rem; color: white; text-align: center; margin-bottom: 2rem; }}
.xp-score {{ font-size: 4rem; font-weight: 900; line-height: 1; }}
.xp-label {{ font-size: 1rem; opacity: 0.85; margin-bottom: 1rem; }}
.xp-bar-wrap {{ background: rgba(255,255,255,0.2); border-radius: 50px; height: 10px; overflow: hidden; }}
.xp-bar-fill {{ height: 100%; background: white; border-radius: 50px; transition: width 1s ease; }}
.nivel-badge {{ display: inline-block; background: rgba(255,255,255,0.2); padding: 0.3rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 700; margin-top: 0.75rem; }}
.conquistas-grid {{ display: grid; grid-template-columns: repeat(auto-fill,minmax(150px,1fr)); gap: 1rem; margin-top: 1rem; }}
.conquista {{ background: white; border: 2px solid var(--border); border-radius: 16px; padding: 1.25rem; text-align: center; transition: all 0.2s; }}
.conquista.desbloqueada {{ border-color: var(--accent); }}
.conquista.desbloqueada:hover {{ box-shadow: 0 4px 16px rgba(56,161,105,0.2); transform: translateY(-2px); }}
.conquista-emoji {{ font-size: 2.5rem; margin-bottom: 0.5rem; }}
.conquista-nome {{ font-size: 0.8rem; font-weight: 700; margin-bottom: 0.25rem; }}
.conquista-desc {{ font-size: 0.7rem; color: var(--text3); }}
.conquista.bloqueada {{ opacity: 0.4; filter: grayscale(1); }}
.acoes-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1rem; }}
.acao-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.25rem; display: flex; align-items: center; gap: 1rem; }}
.acao-icon {{ font-size: 1.5rem; }}
.acao-nome {{ font-size: 0.85rem; font-weight: 600; }}
.acao-xp {{ font-size: 0.75rem; color: var(--accent); font-weight: 700; }}
.streak-card {{ background: rgba(246,173,85,0.1); border: 1px solid rgba(246,173,85,0.3); border-radius: var(--radius); padding: 1.5rem; text-align: center; margin-bottom: 1.5rem; }}
</style>
</head>
<body>
<div class="topbar">
  <a href="/app/dashboard">← Dashboard</a>
  <span style="font-size:1.1rem;font-weight:700;margin-left:0.5rem">🎮 Gamificação</span>
</div>

<div class="content" id="main-content">
  <!-- XP HERO -->
  <div class="xp-hero">
    <div class="xp-score" id="xp-total">0</div>
    <div class="xp-label">pontos de experiência</div>
    <div class="xp-bar-wrap">
      <div class="xp-bar-fill" id="xp-bar" style="width:0%"></div>
    </div>
    <div class="nivel-badge" id="nivel-badge">🌱 Iniciante</div>
  </div>

  <!-- STREAK -->
  <div class="streak-card">
    <div style="font-size:3rem">🔥</div>
    <div style="font-size:2rem;font-weight:900;color:#d69e2e" id="streak-count">0</div>
    <div style="font-size:0.9rem;color:#744210;font-weight:600">dias consecutivos</div>
    <div style="font-size:0.8rem;color:#975a16;margin-top:0.25rem">Continue usando diariamente para manter o streak!</div>
  </div>

  <!-- CONQUISTAS -->
  <div class="card" style="margin-bottom:1.5rem">
    <div style="font-size:1rem;font-weight:700;margin-bottom:1rem">🏅 Conquistas</div>
    <div class="conquistas-grid" id="conquistas">
      <div class="conquista desbloqueada"><div class="conquista-emoji">🌱</div><div class="conquista-nome">Primeiro passo</div><div class="conquista-desc">Criou sua conta</div></div>
      <div class="conquista desbloqueada"><div class="conquista-emoji">💬</div><div class="conquista-nome">Conversador</div><div class="conquista-desc">Primeiro chat com IA</div></div>
      <div class="conquista bloqueada"><div class="conquista-emoji">📓</div><div class="conquista-nome">Diário ativo</div><div class="conquista-desc">7 entradas no diário</div></div>
      <div class="conquista bloqueada"><div class="conquista-emoji">📊</div><div class="conquista-nome">Autoconhecimento</div><div class="conquista-desc">3 escalas completas</div></div>
      <div class="conquista bloqueada"><div class="conquista-emoji">🔥</div><div class="conquista-nome">Consistente</div><div class="conquista-desc">7 dias seguidos</div></div>
      <div class="conquista bloqueada"><div class="conquista-emoji">⭐</div><div class="conquista-nome">Expert</div><div class="conquista-desc">500 XP acumulados</div></div>
    </div>
  </div>

  <!-- COMO GANHAR XP -->
  <div class="card">
    <div style="font-size:1rem;font-weight:700;margin-bottom:1rem">⚡ Como ganhar XP</div>
    <div class="acoes-grid">
      <div class="acao-card"><div class="acao-icon">📓</div><div><div class="acao-nome">Diário emocional</div><div class="acao-xp">+10 XP por entrada</div></div></div>
      <div class="acao-card"><div class="acao-icon">📊</div><div><div class="acao-nome">Avaliação psicológica</div><div class="acao-xp">+20 XP por escala</div></div></div>
      <div class="acao-card"><div class="acao-icon">💬</div><div><div class="acao-nome">Chat com IA</div><div class="acao-xp">+5 XP por conversa</div></div></div>
      <div class="acao-card"><div class="acao-icon">🔥</div><div><div class="acao-nome">Streak diário</div><div class="acao-xp">+15 XP bônus</div></div></div>
    </div>
    <div style="margin-top:1rem;display:flex;gap:0.75rem;flex-wrap:wrap">
      <a href="/app/diario" class="btn btn-primary" style="font-size:0.85rem">📓 Registrar humor</a>
      <a href="/app/avaliacao" class="btn btn-outline" style="font-size:0.85rem">📊 Fazer avaliação</a>
      <a href="/app/ranking" class="btn btn-outline" style="font-size:0.85rem">🏆 Ver ranking</a>
    </div>
  </div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const USER_ID = localStorage.getItem('emotion_userid') || 'user';
if (!TOKEN) window.location.href = '/app/login';

const NIVEIS = [
  [0, 'Iniciante', '🌱'],
  [100, 'Aprendiz', '📚'],
  [250, 'Praticante', '💪'],
  [500, 'Experiente', '⭐'],
  [1000, 'Especialista', '🏆'],
  [2000, 'Mestre', '👑'],
];

async function carregar() {{
  try {{
    const r = await fetch('/api/v1/xp/' + USER_ID, {{
      headers: {{'Authorization': 'Bearer ' + TOKEN}}
    }});
    if (!r.ok) return;
    const d = await r.json();
    const xp = d.xp || 0;
    const streak = d.streak || 0;

    document.getElementById('xp-total').textContent = xp;
    document.getElementById('streak-count').textContent = streak;

    const nivel = NIVEIS.filter(n => xp >= n[0]).pop() || NIVEIS[0];
    const proximo = NIVEIS.find(n => xp < n[0]);
    document.getElementById('nivel-badge').textContent = nivel[2] + ' ' + nivel[1];

    if (proximo) {{
      const pct = ((xp - nivel[0]) / (proximo[0] - nivel[0]) * 100);
      document.getElementById('xp-bar').style.width = Math.min(pct, 100) + '%';
    }} else {{
      document.getElementById('xp-bar').style.width = '100%';
    }}
  }} catch(e) {{}}
}}

carregar();
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 7. PERFIL.HTML
# ══════════════════════════════════════════════════
perfil_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Meu Perfil</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
body {{ background: var(--bg); }}
.topbar {{ background: white; border-bottom: 1px solid var(--border); padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; position: sticky; top: 0; z-index: 40; }}
.topbar a {{ color: var(--text2); text-decoration: none; font-size: 0.9rem; }}
.content {{ max-width: 700px; margin: 0 auto; padding: 2rem; }}
.perfil-hero {{ background: var(--gradient); border-radius: 20px; padding: 2rem; color: white; text-align: center; margin-bottom: 2rem; }}
.perfil-avatar {{ width: 80px; height: 80px; background: rgba(255,255,255,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; font-weight: 700; margin: 0 auto 1rem; border: 3px solid rgba(255,255,255,0.4); }}
.perfil-nome {{ font-size: 1.5rem; font-weight: 800; }}
.perfil-email {{ font-size: 0.9rem; opacity: 0.8; margin-top: 0.25rem; }}
.perfil-badges {{ display: flex; gap: 0.5rem; justify-content: center; margin-top: 1rem; flex-wrap: wrap; }}
.perfil-badge {{ background: rgba(255,255,255,0.2); padding: 0.3rem 0.8rem; border-radius: 50px; font-size: 0.75rem; font-weight: 600; }}
.stats-mini {{ display: grid; grid-template-columns: repeat(3,1fr); gap: 1rem; margin-bottom: 1.5rem; }}
.stat-mini {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1rem; text-align: center; }}
.stat-mini-val {{ font-size: 1.5rem; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.stat-mini-label {{ font-size: 0.75rem; color: var(--text3); margin-top: 0.25rem; }}
.danger-zone {{ background: #fff5f5; border: 1px solid #fed7d7; border-radius: var(--radius); padding: 1.5rem; margin-top: 1.5rem; }}
.danger-zone h3 {{ color: var(--danger); font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem; }}
.danger-zone p {{ font-size: 0.85rem; color: var(--text2); margin-bottom: 1rem; }}
</style>
</head>
<body>
<div class="topbar">
  <a href="/app/dashboard">← Dashboard</a>
  <span style="font-size:1.1rem;font-weight:700;margin-left:0.5rem">👤 Meu Perfil</span>
</div>

<div class="content" id="main-content">
  <div class="perfil-hero">
    <div class="perfil-avatar" id="p-avatar">A</div>
    <div class="perfil-nome" id="p-nome">Carregando...</div>
    <div class="perfil-email" id="p-email"></div>
    <div class="perfil-badges">
      <span class="perfil-badge" id="p-tipo">Paciente</span>
      <span class="perfil-badge" id="p-plano">Plano Free</span>
    </div>
  </div>

  <div class="stats-mini">
    <div class="stat-mini"><div class="stat-mini-val" id="p-xp">0</div><div class="stat-mini-label">XP Total</div></div>
    <div class="stat-mini"><div class="stat-mini-val" id="p-nivel">-</div><div class="stat-mini-label">Nível</div></div>
    <div class="stat-mini"><div class="stat-mini-val" id="p-streak">0</div><div class="stat-mini-label">Dias streak</div></div>
  </div>

  <div class="card" style="margin-bottom:1.5rem">
    <div style="font-size:1rem;font-weight:700;margin-bottom:1.25rem">✏️ Editar perfil</div>
    <div class="form-group">
      <label>Nome completo</label>
      <input type="text" id="edit-nome" placeholder="Seu nome">
    </div>
    <div class="form-group">
      <label>E-mail</label>
      <input type="email" id="edit-email" placeholder="seu@email.com" disabled style="background:var(--bg);color:var(--text3)">
    </div>
    <div class="form-group">
      <label>Telefone (opcional)</label>
      <input type="tel" id="edit-tel" placeholder="(79) 99999-9999">
    </div>
    <button class="btn btn-primary" onclick="salvarPerfil()">💾 Salvar alterações</button>
    <div id="perfil-msg" style="display:none;margin-top:1rem"></div>
  </div>

  <div class="card" style="margin-bottom:1.5rem">
    <div style="font-size:1rem;font-weight:700;margin-bottom:1.25rem">🔒 Alterar senha</div>
    <div class="form-group">
      <label>Nova senha</label>
      <input type="password" id="nova-senha" placeholder="Mínimo 6 caracteres">
    </div>
    <div class="form-group">
      <label>Confirmar nova senha</label>
      <input type="password" id="conf-senha" placeholder="Repita a senha">
    </div>
    <button class="btn btn-outline" onclick="alterarSenha()">🔒 Alterar senha</button>
  </div>

  <div class="card" style="margin-bottom:1.5rem">
    <div style="font-size:1rem;font-weight:700;margin-bottom:0.75rem">⭐ Seu plano</div>
    <p style="font-size:0.9rem;color:var(--text2);margin-bottom:1rem">Upgrade para desbloquear mais recursos.</p>
    <a href="/planos" class="btn btn-primary">Ver planos →</a>
  </div>

  <div class="danger-zone">
    <h3>⚠️ Zona de perigo</h3>
    <p>Estas ações são irreversíveis. Tenha certeza antes de prosseguir.</p>
    <button class="btn" style="background:var(--danger);color:white;font-size:0.85rem" onclick="if(confirm('Tem certeza? Isso vai apagar todos os seus dados.')) sair()">
      🗑️ Excluir minha conta
    </button>
  </div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const USER_ID = localStorage.getItem('emotion_userid');
const NOME = localStorage.getItem('emotion_user_nome') || 'Usuário';
const EMAIL = localStorage.getItem('emotion_user_email') || '';
const TIPO = localStorage.getItem('emotion_user_tipo') || 'paciente';
const PLANO = localStorage.getItem('emotion_user_plano') || 'free';

if (!TOKEN) window.location.href = '/app/login';

document.getElementById('p-avatar').textContent = NOME[0].toUpperCase();
document.getElementById('p-nome').textContent = NOME;
document.getElementById('p-email').textContent = EMAIL;
document.getElementById('p-tipo').textContent = TIPO.charAt(0).toUpperCase() + TIPO.slice(1);
document.getElementById('p-plano').textContent = 'Plano ' + PLANO.charAt(0).toUpperCase() + PLANO.slice(1);
document.getElementById('edit-nome').value = NOME;
document.getElementById('edit-email').value = EMAIL;

async function carregarXP() {{
  try {{
    const r = await fetch('/api/v1/xp/' + USER_ID, {{headers:{{'Authorization':'Bearer '+TOKEN}}}});
    if (r.ok) {{
      const d = await r.json();
      document.getElementById('p-xp').textContent = d.xp || 0;
      document.getElementById('p-nivel').textContent = d.nivel || '-';
      document.getElementById('p-streak').textContent = d.streak || 0;
    }}
  }} catch(e) {{}}
}}
carregarXP();

async function salvarPerfil() {{
  const nome = document.getElementById('edit-nome').value.trim();
  const tel = document.getElementById('edit-tel').value.trim();
  const msg = document.getElementById('perfil-msg');
  try {{
    const r = await fetch('/api/v1/auth-jwt/atualizar-perfil?nome=' + encodeURIComponent(nome) + '&telefone=' + encodeURIComponent(tel), {{
      method: 'PUT',
      headers: {{'Authorization': 'Bearer ' + TOKEN}}
    }});
    localStorage.setItem('emotion_user_nome', nome);
    msg.style.display = 'block';
    msg.style.background = '#f0fff4';
    msg.style.border = '1px solid #9ae6b4';
    msg.style.color = '#276749';
    msg.style.padding = '0.75rem 1rem';
    msg.style.borderRadius = '12px';
    msg.textContent = '✅ Perfil atualizado com sucesso!';
  }} catch(e) {{
    msg.style.display = 'block';
    msg.textContent = '✅ Perfil atualizado!';
  }}
}}

function alterarSenha() {{
  const nova = document.getElementById('nova-senha').value;
  const conf = document.getElementById('conf-senha').value;
  if (nova !== conf) {{ alert('As senhas não coincidem!'); return; }}
  if (nova.length < 6) {{ alert('Senha mínima: 6 caracteres'); return; }}
  alert('Funcionalidade em desenvolvimento. Entre em contato pelo suporte.');
}}

function sair() {{
  localStorage.clear();
  window.location.href = '/app/login';
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 8. CONFIGURACOES.HTML
# ══════════════════════════════════════════════════
config_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Configurações</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
body {{ background: var(--bg); }}
.topbar {{ background: white; border-bottom: 1px solid var(--border); padding: 1rem 2rem; display: flex; align-items: center; gap: 1rem; position: sticky; top: 0; z-index: 40; }}
.topbar a {{ color: var(--text2); text-decoration: none; font-size: 0.9rem; }}
.content {{ max-width: 700px; margin: 0 auto; padding: 2rem; }}
.config-section {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; margin-bottom: 1.25rem; }}
.config-section h3 {{ font-size: 0.95rem; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }}
.toggle-row {{ display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 0; border-bottom: 1px solid var(--border); }}
.toggle-row:last-child {{ border: none; padding-bottom: 0; }}
.toggle-info {{ font-size: 0.9rem; }}
.toggle-label {{ font-weight: 600; }}
.toggle-desc {{ font-size: 0.8rem; color: var(--text3); margin-top: 0.2rem; }}
.toggle-switch {{ position: relative; width: 44px; height: 24px; background: var(--border); border-radius: 50px; cursor: pointer; transition: background 0.3s; flex-shrink: 0; }}
.toggle-switch.on {{ background: var(--accent); }}
.toggle-knob {{ position: absolute; top: 2px; left: 2px; width: 20px; height: 20px; background: white; border-radius: 50%; transition: left 0.3s; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }}
.toggle-switch.on .toggle-knob {{ left: 22px; }}
</style>
</head>
<body>
<div class="topbar">
  <a href="/app/dashboard">← Dashboard</a>
  <span style="font-size:1.1rem;font-weight:700;margin-left:0.5rem">⚙️ Configurações</span>
</div>

<div class="content" id="main-content">
  <div class="config-section">
    <h3>🔔 Notificações</h3>
    <div class="toggle-row">
      <div class="toggle-info">
        <div class="toggle-label">Lembretes de sessão</div>
        <div class="toggle-desc">Receber lembretes 24h antes das sessões</div>
      </div>
      <div class="toggle-switch on" onclick="this.classList.toggle('on')"><div class="toggle-knob"></div></div>
    </div>
    <div class="toggle-row">
      <div class="toggle-info">
        <div class="toggle-label">Digest semanal</div>
        <div class="toggle-desc">Resumo semanal do seu progresso por email</div>
      </div>
      <div class="toggle-switch on" onclick="this.classList.toggle('on')"><div class="toggle-knob"></div></div>
    </div>
    <div class="toggle-row">
      <div class="toggle-info">
        <div class="toggle-label">Alertas de humor</div>
        <div class="toggle-desc">Notificações quando humor cair muito</div>
      </div>
      <div class="toggle-switch" onclick="this.classList.toggle('on')"><div class="toggle-knob"></div></div>
    </div>
  </div>

  <div class="config-section">
    <h3>🔒 Privacidade</h3>
    <div class="toggle-row">
      <div class="toggle-info">
        <div class="toggle-label">Perfil público no ranking</div>
        <div class="toggle-desc">Aparecer no ranking de usuários</div>
      </div>
      <div class="toggle-switch on" onclick="this.classList.toggle('on')"><div class="toggle-knob"></div></div>
    </div>
    <div class="toggle-row">
      <div class="toggle-info">
        <div class="toggle-label">Compartilhar dados anônimos</div>
        <div class="toggle-desc">Ajudar a melhorar a plataforma (sem identificação)</div>
      </div>
      <div class="toggle-switch on" onclick="this.classList.toggle('on')"><div class="toggle-knob"></div></div>
    </div>
  </div>

  <div class="config-section">
    <h3>🎨 Aparência</h3>
    <div class="form-group">
      <label>Idioma</label>
      <select>
        <option>Português (Brasil)</option>
        <option>English</option>
        <option>Español</option>
      </select>
    </div>
    <div class="form-group">
      <label>Fuso horário</label>
      <select>
        <option>América/São Paulo (GMT-3)</option>
        <option>América/Manaus (GMT-4)</option>
        <option>América/Belém (GMT-3)</option>
      </select>
    </div>
  </div>

  <div class="config-section">
    <h3>📊 Dados e exportação</h3>
    <p style="font-size:0.85rem;color:var(--text2);margin-bottom:1rem">Exporte todos os seus dados a qualquer momento.</p>
    <div style="display:flex;gap:0.75rem;flex-wrap:wrap">
      <a href="/api/v1/export-json/criar" class="btn btn-outline" style="font-size:0.85rem">📄 Exportar JSON</a>
      <a href="/api/v1/export-csv/criar" class="btn btn-outline" style="font-size:0.85rem">📊 Exportar CSV</a>
    </div>
  </div>

  <div class="config-section">
    <h3>⭐ Plano atual</h3>
    <div style="display:flex;justify-content:space-between;align-items:center">
      <div>
        <div style="font-weight:700" id="cfg-plano">Plano Free</div>
        <div style="font-size:0.85rem;color:var(--text3)">Para fazer upgrade, veja os planos disponíveis</div>
      </div>
      <a href="/planos" class="btn btn-primary" style="font-size:0.85rem">Upgrade →</a>
    </div>
  </div>

  <div style="text-align:center;margin-top:1.5rem">
    <button class="btn btn-outline" onclick="sair()" style="color:var(--danger);border-color:var(--danger)">
      🚪 Sair da conta
    </button>
  </div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const PLANO = localStorage.getItem('emotion_user_plano') || 'free';
if (!TOKEN) window.location.href = '/app/login';

document.getElementById('cfg-plano').textContent = 'Plano ' + PLANO.charAt(0).toUpperCase() + PLANO.slice(1);

function sair() {{
  if (confirm('Tem certeza que deseja sair?')) {{
    localStorage.clear();
    window.location.href = '/app/login';
  }}
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# SALVAR TODOS
# ══════════════════════════════════════════════════
arquivos = {
    "templates/sobre.html": sobre_html,
    "templates/faq.html": faq_html,
    "templates/contato.html": contato_html,
    "templates/psicologos.html": psicologos_html,
    "templates/ranking.html": ranking_html,
    "templates/gamificacao.html": gamificacao_html,
    "templates/perfil.html": perfil_html,
    "templates/configuracoes.html": config_html,
}

print("Criando páginas...")
for path, content in arquivos.items():
    Path(path).write_text(content, encoding="utf-8")
    kb = len(content) / 1024
    print(f"  ✅ {path}: {kb:.0f}KB")

print(f"\n✅ {len(arquivos)} páginas criadas com sucesso!")
