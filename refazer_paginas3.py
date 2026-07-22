#!/usr/bin/env python3
"""Refaz páginas restantes com design profissional"""
from pathlib import Path

CSS_BASE = """
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --primary: #667eea; --primary-dark: #764ba2; --accent: #38a169;
  --danger: #e53e3e; --bg: #f8fafc; --text: #1a202c; --text2: #4a5568;
  --text3: #718096; --border: #e2e8f0;
  --shadow: 0 4px 24px rgba(102,126,234,0.10);
  --shadow-lg: 0 8px 48px rgba(102,126,234,0.15);
  --gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --radius: 16px;
}
body { font-family: 'Inter', -apple-system, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }
nav { position: fixed; top: 0; left: 0; right: 0; background: rgba(255,255,255,0.95); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); z-index: 100; padding: 0 2rem; height: 64px; display: flex; align-items: center; justify-content: space-between; }
.nav-brand { font-size: 1.25rem; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }
.nav-links { display: flex; align-items: center; gap: 2rem; list-style: none; }
.nav-links a { color: var(--text2); text-decoration: none; font-size: 0.9rem; font-weight: 500; }
.nav-links a:hover { color: var(--primary); }
.nav-cta { display: flex; gap: 0.75rem; }
.btn { padding: 0.6rem 1.5rem; border-radius: 50px; font-weight: 600; font-size: 0.9rem; cursor: pointer; border: none; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; transition: all 0.2s; }
.btn-primary { background: var(--gradient); color: white; box-shadow: 0 4px 16px rgba(102,126,234,0.35); }
.btn-primary:hover { transform: translateY(-1px); }
.btn-outline { background: transparent; border: 1.5px solid var(--border); color: var(--text2); }
.btn-outline:hover { border-color: var(--primary); color: var(--primary); }
.btn-lg { padding: 0.9rem 2.5rem; font-size: 1rem; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 2rem; }
.section { padding: 5rem 0; }
.grad { background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.section-badge { display: inline-block; background: rgba(102,126,234,0.1); color: var(--primary); padding: 0.3rem 1rem; border-radius: 50px; font-size: 0.8rem; font-weight: 600; margin-bottom: 1rem; }
.section-title { font-size: clamp(1.8rem,4vw,2.8rem); font-weight: 800; line-height: 1.2; margin-bottom: 1rem; }
.section-desc { font-size: 1.1rem; color: var(--text2); max-width: 580px; line-height: 1.7; }
.card { background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; }
input, textarea, select { width: 100%; padding: 0.75rem 1rem; border: 1.5px solid var(--border); border-radius: 12px; font-size: 0.95rem; font-family: inherit; transition: border-color 0.2s; background: white; color: var(--text); }
input:focus, textarea:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(102,126,234,0.1); }
label { font-size: 0.85rem; font-weight: 600; color: var(--text2); display: block; margin-bottom: 0.4rem; }
.form-group { margin-bottom: 1.25rem; }
footer { background: #1a202c; color: #a0aec0; padding: 3rem 2rem; }
.footer-grid { max-width: 1100px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; }
.footer-brand { font-size: 1.25rem; font-weight: 800; color: white; margin-bottom: 0.75rem; }
.footer-col h4 { color: white; font-size: 0.9rem; font-weight: 700; margin-bottom: 1rem; }
.footer-col a { display: block; color: #a0aec0; text-decoration: none; font-size: 0.85rem; margin-bottom: 0.5rem; }
.footer-col a:hover { color: white; }
.footer-bottom { max-width: 1100px; margin: 2rem auto 0; padding-top: 1.5rem; border-top: 1px solid #2d3748; display: flex; justify-content: space-between; font-size: 0.8rem; flex-wrap: wrap; gap: 1rem; }
@media (max-width: 768px) { .nav-links { display: none; } .footer-grid { grid-template-columns: 1fr 1fr; } }
"""

NAV = """<nav><a href="/" class="nav-brand">🧠 EmotionAI</a>
<ul class="nav-links"><li><a href="/#features">Recursos</a></li><li><a href="/planos">Preços</a></li><li><a href="/sobre">Sobre</a></li><li><a href="/contato">Contato</a></li></ul>
<div class="nav-cta"><a href="/app/login" class="btn btn-outline">Entrar</a><a href="/app/login" class="btn btn-primary">Começar grátis</a></div></nav>"""

FOOTER = """<footer><div class="footer-grid">
<div><div class="footer-brand">🧠 EmotionAI</div><p style="font-size:0.9rem;line-height:1.6">Plataforma de gestão clínica para psicólogos brasileiros.</p></div>
<div class="footer-col"><h4>Produto</h4><a href="/#features">Recursos</a><a href="/planos">Preços</a><a href="/app/login">Entrar</a></div>
<div class="footer-col"><h4>Empresa</h4><a href="/sobre">Sobre</a><a href="/blog">Blog</a><a href="/contato">Contato</a><a href="/afiliado">Afiliados</a></div>
<div class="footer-col"><h4>Legal</h4><a href="/privacidade">Privacidade</a><a href="/termos">Termos</a><a href="/faq">FAQ</a></div>
</div><div class="footer-bottom"><span>© 2026 EmotionAI</span><span>Feito com ❤️ em Sergipe, Brasil</span></div></footer>"""

# ══════════════════════════════════════════════════
# 1. BLOG.HTML
# ══════════════════════════════════════════════════
blog_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Blog</title>
<meta name="description" content="Artigos sobre saúde mental, psicologia e bem-estar emocional.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 4rem; background: white; text-align: center; }}
.posts-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 3rem; }}
.post-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: all 0.2s; cursor: pointer; }}
.post-card:hover {{ box-shadow: var(--shadow-lg); transform: translateY(-3px); }}
.post-thumb {{ height: 180px; display: flex; align-items: center; justify-content: center; font-size: 4rem; }}
.post-body {{ padding: 1.5rem; }}
.post-tag {{ display: inline-block; background: rgba(102,126,234,0.1); color: var(--primary); padding: 0.2rem 0.7rem; border-radius: 50px; font-size: 0.75rem; font-weight: 600; margin-bottom: 0.75rem; }}
.post-title {{ font-size: 1.05rem; font-weight: 700; line-height: 1.4; margin-bottom: 0.5rem; }}
.post-desc {{ font-size: 0.85rem; color: var(--text2); line-height: 1.6; margin-bottom: 1rem; }}
.post-meta {{ font-size: 0.75rem; color: var(--text3); display: flex; gap: 1rem; }}
.newsletter {{ background: var(--gradient); border-radius: var(--radius); padding: 2.5rem; text-align: center; color: white; margin-top: 4rem; }}
.newsletter h3 {{ font-size: 1.5rem; font-weight: 800; margin-bottom: 0.5rem; }}
.newsletter p {{ opacity: 0.85; margin-bottom: 1.5rem; }}
.newsletter-form {{ display: flex; gap: 0.75rem; max-width: 400px; margin: 0 auto; }}
.newsletter-form input {{ background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.3); color: white; border-radius: 50px; }}
.newsletter-form input::placeholder {{ color: rgba(255,255,255,0.6); }}
</style>
</head>
<body>
{NAV}
<div style="height:64px"></div>
<div class="hero">
  <div class="container">
    <span class="section-badge">📝 Blog</span>
    <h1 class="section-title">Conhecimento sobre <span class="grad">saúde mental</span></h1>
    <p class="section-desc" style="margin:0 auto">Artigos, dicas e pesquisas para psicólogos e pacientes.</p>
  </div>
</div>
<section class="section" style="background:var(--bg)">
  <div class="container">
    <div class="posts-grid">
      <div class="post-card" onclick="window.location='/blog/ansiedade-tecnicas'">
        <div class="post-thumb" style="background:linear-gradient(135deg,#667eea20,#764ba220)">😰</div>
        <div class="post-body">
          <span class="post-tag">Ansiedade</span>
          <div class="post-title">5 técnicas baseadas em evidências para reduzir a ansiedade</div>
          <div class="post-desc">Aprenda técnicas validadas clinicamente para manejar a ansiedade no dia a dia.</div>
          <div class="post-meta"><span>📅 Jul 2026</span><span>⏱️ 5 min</span></div>
        </div>
      </div>
      <div class="post-card" onclick="window.location='/blog/phq9-guia'">
        <div class="post-thumb" style="background:linear-gradient(135deg,#38a16920,#276749220)">📊</div>
        <div class="post-body">
          <span class="post-tag">Escalas</span>
          <div class="post-title">Guia completo do PHQ-9: como aplicar e interpretar</div>
          <div class="post-desc">Tudo que você precisa saber sobre a escala PHQ-9 para avaliação de depressão.</div>
          <div class="post-meta"><span>📅 Jul 2026</span><span>⏱️ 8 min</span></div>
        </div>
      </div>
      <div class="post-card" onclick="window.location='/blog/telepsicologia'">
        <div class="post-thumb" style="background:linear-gradient(135deg,#d69e2e20,#74421020)">💻</div>
        <div class="post-body">
          <span class="post-tag">Telepsicologia</span>
          <div class="post-title">Telepsicologia no Brasil: guia completo das resoluções do CFP</div>
          <div class="post-desc">Entenda as normas vigentes e como atender pacientes online com segurança.</div>
          <div class="post-meta"><span>📅 Jul 2026</span><span>⏱️ 10 min</span></div>
        </div>
      </div>
      <div class="post-card" onclick="window.location='/blog/ia-saude-mental'">
        <div class="post-thumb" style="background:linear-gradient(135deg,#667eea20,#764ba220)">🤖</div>
        <div class="post-body">
          <span class="post-tag">Tecnologia</span>
          <div class="post-title">IA na saúde mental: oportunidades e limites éticos</div>
          <div class="post-desc">Como a inteligência artificial pode apoiar (sem substituir) o trabalho do psicólogo.</div>
          <div class="post-meta"><span>📅 Jul 2026</span><span>⏱️ 7 min</span></div>
        </div>
      </div>
      <div class="post-card" onclick="window.location='/blog/diario-emocional'">
        <div class="post-thumb" style="background:linear-gradient(135deg,#e53e3e20,#c5303020)">📓</div>
        <div class="post-body">
          <span class="post-tag">Bem-estar</span>
          <div class="post-title">Por que manter um diário emocional transforma sua saúde mental</div>
          <div class="post-desc">Pesquisas mostram que registrar emoções diariamente reduz ansiedade e melhora o autoconhecimento.</div>
          <div class="post-meta"><span>📅 Jun 2026</span><span>⏱️ 4 min</span></div>
        </div>
      </div>
      <div class="post-card" onclick="window.location='/blog/burnout-psicologo'">
        <div class="post-thumb" style="background:linear-gradient(135deg,#38a16920,#27674920)">🔥</div>
        <div class="post-body">
          <span class="post-tag">Para Psicólogos</span>
          <div class="post-title">Burnout no psicólogo: como identificar e prevenir</div>
          <div class="post-desc">Cuidar de quem cuida: estratégias de autocuidado para profissionais de saúde mental.</div>
          <div class="post-meta"><span>📅 Jun 2026</span><span>⏱️ 6 min</span></div>
        </div>
      </div>
    </div>
    <div class="newsletter">
      <h3>📬 Newsletter semanal</h3>
      <p>Receba artigos sobre saúde mental toda semana no seu email.</p>
      <div class="newsletter-form">
        <input type="email" id="nl-email" placeholder="seu@email.com">
        <button class="btn btn-primary" onclick="assinarNewsletter()" style="white-space:nowrap">Assinar</button>
      </div>
      <div id="nl-msg" style="margin-top:0.75rem;font-size:0.85rem"></div>
    </div>
  </div>
</section>
{FOOTER}
<script>
async function assinarNewsletter() {{
  const email = document.getElementById('nl-email').value.trim();
  const msg = document.getElementById('nl-msg');
  if (!email) return;
  try {{
    await fetch('/api/v1/newsletter/inscrever', {{
      method: 'POST',
      headers: {{'Content-Type':'application/json'}},
      body: JSON.stringify({{email}})
    }});
  }} catch(e) {{}}
  msg.textContent = '✅ Inscrito com sucesso!';
  msg.style.color = 'rgba(255,255,255,0.9)';
  document.getElementById('nl-email').value = '';
}}
</script>
</body></html>"""

# ══════════════════════════════════════════════════
# 2. TERAPIA.HTML
# ══════════════════════════════════════════════════
terapia_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Terapia Online</title>
<meta name="description" content="Encontre um psicólogo online no EmotionAI e comece sua jornada de saúde mental.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 5rem; background: white; }}
.hero-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
.hero h1 {{ font-size: clamp(2rem,5vw,3.5rem); font-weight: 900; line-height: 1.1; margin-bottom: 1.5rem; }}
.hero p {{ font-size: 1.1rem; color: var(--text2); line-height: 1.7; margin-bottom: 2rem; }}
.tipos-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 1rem; margin-top: 3rem; }}
.tipo-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; text-align: center; transition: all 0.2s; cursor: pointer; }}
.tipo-card:hover {{ box-shadow: var(--shadow-lg); transform: translateY(-3px); border-color: rgba(102,126,234,0.3); }}
.tipo-emoji {{ font-size: 2.5rem; margin-bottom: 0.75rem; }}
.tipo-nome {{ font-weight: 700; margin-bottom: 0.25rem; }}
.tipo-desc {{ font-size: 0.8rem; color: var(--text3); }}
.como-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 1.5rem; margin-top: 3rem; }}
.como-step {{ text-align: center; padding: 1.5rem; }}
.como-num {{ width: 52px; height: 52px; background: var(--gradient); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin: 0 auto 1rem; }}
.como-step h3 {{ font-size: 0.95rem; font-weight: 700; margin-bottom: 0.5rem; }}
.como-step p {{ font-size: 0.85rem; color: var(--text2); line-height: 1.6; }}
.hero-visual {{ background: var(--gradient); border-radius: 24px; padding: 2rem; color: white; }}
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
        <span class="section-badge">🧘 Terapia Online</span>
        <h1>Cuide da sua <span class="grad">saúde mental</span> onde estiver</h1>
        <p>Acesse apoio psicológico de qualidade, converse com nossa IA de suporte e monitore seu bem-estar emocional.</p>
        <div style="display:flex;gap:1rem;flex-wrap:wrap">
          <a href="/app/login" class="btn btn-primary btn-lg">Começar agora →</a>
          <a href="/app/avaliacao" class="btn btn-outline btn-lg">Fazer avaliação</a>
        </div>
        <p style="font-size:0.85rem;color:var(--text3);margin-top:1rem">✅ Gratuito para começar · ✅ Sem compromisso</p>
      </div>
      <div class="hero-visual">
        <div style="font-weight:700;margin-bottom:1.5rem;font-size:1.1rem">💙 Sofia — IA de Suporte</div>
        <div style="background:rgba(255,255,255,0.15);border-radius:12px;padding:1rem;margin-bottom:0.75rem;font-size:0.9rem">
          Olá! Como você está se sentindo hoje? Estou aqui para te ouvir. 💙
        </div>
        <div style="background:rgba(255,255,255,0.25);border-radius:12px;padding:1rem;margin-bottom:0.75rem;font-size:0.9rem;margin-left:2rem">
          Estou me sentindo ansioso com o trabalho...
        </div>
        <div style="background:rgba(255,255,255,0.15);border-radius:12px;padding:1rem;font-size:0.9rem">
          Entendo. A ansiedade no trabalho é muito comum. Vamos tentar uma técnica de respiração? 🌬️
        </div>
        <div style="margin-top:1rem;font-size:0.8rem;opacity:0.8;text-align:center">
          IA disponível 24/7 · Não substitui terapia
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg)">
  <div class="container">
    <div style="text-align:center">
      <span class="section-badge">🎯 O que oferecemos</span>
      <h2 class="section-title">Suporte completo para <span class="grad">sua jornada</span></h2>
    </div>
    <div class="tipos-grid">
      <div class="tipo-card" onclick="window.location='/app/chat'">
        <div class="tipo-emoji">🤖</div>
        <div class="tipo-nome">Chat com IA</div>
        <div class="tipo-desc">Apoio emocional 24/7 com IA especializada em saúde mental</div>
      </div>
      <div class="tipo-card" onclick="window.location='/app/avaliacao'">
        <div class="tipo-emoji">📊</div>
        <div class="tipo-nome">Avaliações</div>
        <div class="tipo-desc">PHQ-9, GAD-7 e PSS — escalas validadas para monitorar sua saúde</div>
      </div>
      <div class="tipo-card" onclick="window.location='/app/diario'">
        <div class="tipo-emoji">📓</div>
        <div class="tipo-nome">Diário emocional</div>
        <div class="tipo-desc">Registre seu humor e acompanhe sua evolução emocional</div>
      </div>
      <div class="tipo-card" onclick="window.location='/respiracao'">
        <div class="tipo-emoji">🌬️</div>
        <div class="tipo-nome">Respiração guiada</div>
        <div class="tipo-desc">Técnicas de respiração para ansiedade e estresse</div>
      </div>
      <div class="tipo-card" onclick="window.location='/meditacao'">
        <div class="tipo-emoji">🧘</div>
        <div class="tipo-nome">Meditação</div>
        <div class="tipo-desc">Sessões guiadas de mindfulness e meditação</div>
      </div>
      <div class="tipo-card" onclick="window.location='/app/gamificacao'">
        <div class="tipo-emoji">🎮</div>
        <div class="tipo-nome">Gamificação</div>
        <div class="tipo-desc">XP, conquistas e streak para manter a consistência</div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:white">
  <div class="container">
    <div style="text-align:center">
      <span class="section-badge">🚀 Como começar</span>
      <h2 class="section-title">Em <span class="grad">3 passos simples</span></h2>
    </div>
    <div class="como-grid">
      <div class="como-step">
        <div class="como-num">1</div>
        <h3>Crie sua conta grátis</h3>
        <p>Cadastro em 30 segundos. Sem cartão de crédito necessário.</p>
      </div>
      <div class="como-step">
        <div class="como-num">2</div>
        <h3>Faça uma avaliação</h3>
        <p>Responda o PHQ-9 ou GAD-7 para entender seu estado atual.</p>
      </div>
      <div class="como-step">
        <div class="como-num">3</div>
        <h3>Comece sua jornada</h3>
        <p>Use o chat, o diário e as ferramentas de bem-estar.</p>
      </div>
    </div>
    <div style="text-align:center;margin-top:3rem">
      <a href="/app/login" class="btn btn-primary btn-lg">Começar grátis agora →</a>
      <p style="margin-top:1rem;font-size:0.85rem;color:var(--text3)">
        ⚠️ O EmotionAI não substitui psicoterapia profissional.<br>
        Em caso de crise, ligue 188 (CVV) ou acesse cvv.org.br
      </p>
    </div>
  </div>
</section>
{FOOTER}
</body></html>"""

# ══════════════════════════════════════════════════
# 3. PRIVACIDADE.HTML
# ══════════════════════════════════════════════════
privacidade_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Política de Privacidade</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.doc-container {{ max-width: 760px; margin: 0 auto; padding: 6rem 2rem 4rem; }}
.doc-header {{ margin-bottom: 3rem; }}
.doc-title {{ font-size: 2rem; font-weight: 800; margin-bottom: 0.5rem; }}
.doc-meta {{ font-size: 0.85rem; color: var(--text3); }}
.doc-section {{ margin-bottom: 2.5rem; }}
.doc-section h2 {{ font-size: 1.2rem; font-weight: 700; margin-bottom: 1rem; color: var(--primary); display: flex; align-items: center; gap: 0.5rem; }}
.doc-section p {{ font-size: 0.95rem; color: var(--text2); line-height: 1.8; margin-bottom: 0.75rem; }}
.doc-section ul {{ margin: 0.75rem 0 0.75rem 1.5rem; }}
.doc-section ul li {{ font-size: 0.95rem; color: var(--text2); line-height: 1.7; margin-bottom: 0.25rem; }}
.highlight {{ background: rgba(102,126,234,0.05); border-left: 4px solid var(--primary); border-radius: 0 12px 12px 0; padding: 1rem 1.25rem; margin: 1rem 0; }}
.toc {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; margin-bottom: 2rem; }}
.toc h3 {{ font-size: 0.9rem; font-weight: 700; margin-bottom: 1rem; }}
.toc a {{ display: block; font-size: 0.85rem; color: var(--primary); text-decoration: none; padding: 0.25rem 0; }}
.toc a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
{NAV}
<div class="doc-container" id="main-content">
  <div class="doc-header">
    <span class="section-badge">🔒 Legal</span>
    <h1 class="doc-title">Política de Privacidade</h1>
    <div class="doc-meta">Última atualização: 21 de julho de 2026 · Versão 2.0</div>
  </div>

  <div class="toc">
    <h3>📋 Índice</h3>
    <a href="#coleta">1. Dados que coletamos</a>
    <a href="#uso">2. Como usamos seus dados</a>
    <a href="#compartilhamento">3. Compartilhamento</a>
    <a href="#seguranca">4. Segurança</a>
    <a href="#direitos">5. Seus direitos (LGPD)</a>
    <a href="#cookies">6. Cookies</a>
    <a href="#contato">7. Contato</a>
  </div>

  <div class="highlight">
    <strong>Resumo simples:</strong> Seus dados são seus. Nunca vendemos informações para terceiros.
    Tudo é criptografado. Você pode excluir sua conta a qualquer momento.
  </div>

  <div class="doc-section" id="coleta">
    <h2>📥 1. Dados que coletamos</h2>
    <p>Coletamos apenas os dados necessários para oferecer nossos serviços:</p>
    <ul>
      <li><strong>Dados de cadastro:</strong> nome, email, tipo de conta</li>
      <li><strong>Dados de uso:</strong> entradas no diário, resultados de escalas, conversas com IA</li>
      <li><strong>Dados técnicos:</strong> endereço IP, tipo de navegador, horários de acesso</li>
      <li><strong>Dados de pagamento:</strong> processados pelo Stripe (não armazenamos dados de cartão)</li>
    </ul>
  </div>

  <div class="doc-section" id="uso">
    <h2>⚙️ 2. Como usamos seus dados</h2>
    <p>Utilizamos seus dados exclusivamente para:</p>
    <ul>
      <li>Fornecer e melhorar os serviços da plataforma</li>
      <li>Personalizar sua experiência</li>
      <li>Enviar comunicações relacionadas ao serviço</li>
      <li>Garantir a segurança da plataforma</li>
      <li>Cumprir obrigações legais</li>
    </ul>
    <p><strong>Nunca usamos seus dados para:</strong> vender para terceiros, publicidade de outras empresas ou qualquer finalidade não descrita aqui.</p>
  </div>

  <div class="doc-section" id="compartilhamento">
    <h2>🤝 3. Compartilhamento de dados</h2>
    <p>Seus dados só são compartilhados com:</p>
    <ul>
      <li><strong>Stripe:</strong> processamento de pagamentos</li>
      <li><strong>Render.com:</strong> hospedagem da plataforma</li>
      <li><strong>Mistral AI:</strong> processamento do chat (sem identificação pessoal)</li>
    </ul>
    <p>Todos os parceiros seguem políticas rígidas de privacidade e LGPD.</p>
  </div>

  <div class="doc-section" id="seguranca">
    <h2>🔒 4. Segurança</h2>
    <p>Implementamos as seguintes medidas de segurança:</p>
    <ul>
      <li>Criptografia TLS/SSL em todas as comunicações</li>
      <li>Senhas armazenadas com hash (nunca em texto puro)</li>
      <li>Backups automáticos diários</li>
      <li>Tokens JWT com expiração automática</li>
      <li>Rate limiting para prevenir ataques</li>
    </ul>
  </div>

  <div class="doc-section" id="direitos">
    <h2>⚖️ 5. Seus direitos (LGPD)</h2>
    <p>Conforme a Lei Geral de Proteção de Dados (Lei 13.709/2018), você tem direito a:</p>
    <ul>
      <li>Confirmar a existência de tratamento dos seus dados</li>
      <li>Acessar seus dados pessoais</li>
      <li>Corrigir dados incompletos ou incorretos</li>
      <li>Solicitar a exclusão dos seus dados</li>
      <li>Revogar o consentimento a qualquer momento</li>
      <li>Exportar seus dados em formato aberto</li>
    </ul>
    <p>Para exercer seus direitos, entre em contato: <strong>albertmenezes2006@gmail.com</strong></p>
  </div>

  <div class="doc-section" id="cookies">
    <h2>🍪 6. Cookies</h2>
    <p>Utilizamos apenas cookies essenciais para o funcionamento da plataforma (sessão de login). Não utilizamos cookies de rastreamento ou publicidade.</p>
  </div>

  <div class="doc-section" id="contato">
    <h2>📬 7. Contato</h2>
    <p>Dúvidas sobre privacidade? Entre em contato:</p>
    <ul>
      <li>Email: albertmenezes2006@gmail.com</li>
      <li>Formulário: <a href="/contato" style="color:var(--primary)">emotionald.ai/contato</a></li>
    </ul>
  </div>
</div>
{FOOTER}
</body></html>"""

# ══════════════════════════════════════════════════
# 4. TERMOS.HTML
# ══════════════════════════════════════════════════
termos_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Termos de Uso</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.doc-container {{ max-width: 760px; margin: 0 auto; padding: 6rem 2rem 4rem; }}
.doc-section h2 {{ font-size: 1.2rem; font-weight: 700; margin-bottom: 1rem; color: var(--primary); }}
.doc-section p {{ font-size: 0.95rem; color: var(--text2); line-height: 1.8; margin-bottom: 0.75rem; }}
.doc-section ul {{ margin: 0.75rem 0 0.75rem 1.5rem; }}
.doc-section ul li {{ font-size: 0.95rem; color: var(--text2); line-height: 1.7; margin-bottom: 0.25rem; }}
.doc-section {{ margin-bottom: 2.5rem; }}
.warning {{ background: #fff5f5; border: 1px solid #fed7d7; border-radius: 12px; padding: 1rem 1.25rem; margin: 1rem 0; color: #c53030; font-size: 0.9rem; }}
</style>
</head>
<body>
{NAV}
<div class="doc-container" id="main-content">
  <div style="margin-bottom:3rem">
    <span class="section-badge">📋 Legal</span>
    <h1 style="font-size:2rem;font-weight:800;margin-bottom:0.5rem">Termos de Uso</h1>
    <div style="font-size:0.85rem;color:var(--text3)">Última atualização: 21 de julho de 2026</div>
  </div>

  <div class="warning">
    ⚠️ <strong>Importante:</strong> O EmotionAI NÃO substitui psicoterapia ou tratamento médico. Em caso de crise, ligue 188 (CVV) ou procure um profissional de saúde.
  </div>

  <div class="doc-section">
    <h2>1. Aceitação dos Termos</h2>
    <p>Ao usar o EmotionAI, você concorda com estes termos. Se não concordar, não utilize a plataforma.</p>
  </div>

  <div class="doc-section">
    <h2>2. Sobre o Serviço</h2>
    <p>O EmotionAI oferece:</p>
    <ul>
      <li>Ferramentas digitais de apoio à saúde mental</li>
      <li>Chat com IA para suporte emocional</li>
      <li>Escalas psicológicas para autoavaliação</li>
      <li>Diário emocional e gamificação</li>
      <li>Gestão clínica para psicólogos</li>
    </ul>
    <p><strong>O EmotionAI NÃO é:</strong> serviço de psicoterapia, diagnóstico médico ou substituto para tratamento profissional.</p>
  </div>

  <div class="doc-section">
    <h2>3. Responsabilidades do Usuário</h2>
    <ul>
      <li>Fornecer informações verdadeiras no cadastro</li>
      <li>Manter a confidencialidade da sua senha</li>
      <li>Usar a plataforma de forma ética e legal</li>
      <li>Não usar para fins ilegais ou prejudiciais</li>
      <li>Respeitar outros usuários e profissionais</li>
    </ul>
  </div>

  <div class="doc-section">
    <h2>4. Planos e Pagamentos</h2>
    <ul>
      <li>O plano gratuito é disponibilizado sem garantias de disponibilidade futura</li>
      <li>Planos pagos são cobrados conforme descrito na página de preços</li>
      <li>Cancelamentos podem ser feitos a qualquer momento</li>
      <li>Reembolsos seguem a política de 30 dias</li>
    </ul>
  </div>

  <div class="doc-section">
    <h2>5. Propriedade Intelectual</h2>
    <p>Todo o conteúdo da plataforma (código, design, textos) é propriedade do EmotionAI. Seus dados pessoais pertencem a você.</p>
  </div>

  <div class="doc-section">
    <h2>6. Limitação de Responsabilidade</h2>
    <p>O EmotionAI não se responsabiliza por:</p>
    <ul>
      <li>Decisões tomadas com base nas avaliações da plataforma</li>
      <li>Indisponibilidade temporária do serviço</li>
      <li>Conteúdo gerado pela IA (sempre consulte um profissional)</li>
    </ul>
  </div>

  <div class="doc-section">
    <h2>7. Contato</h2>
    <p>Dúvidas sobre os termos: <strong>albertmenezes2006@gmail.com</strong></p>
  </div>
</div>
{FOOTER}
</body></html>"""

# ══════════════════════════════════════════════════
# 5. AFILIADO.HTML
# ══════════════════════════════════════════════════
afiliado_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Programa de Afiliados</title>
<meta name="description" content="Ganhe 30% de comissão indicando o EmotionAI para outros psicólogos.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
.hero {{ padding: 8rem 0 5rem; background: white; text-align: center; }}
.hero h1 {{ font-size: clamp(2rem,5vw,3.5rem); font-weight: 900; margin-bottom: 1.5rem; }}
.comissao-num {{ font-size: 5rem; font-weight: 900; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; }}
.ganhos-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 1.5rem; margin-top: 3rem; }}
.ganho-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; text-align: center; }}
.ganho-valor {{ font-size: 1.5rem; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.ganho-label {{ font-size: 0.85rem; color: var(--text3); margin-top: 0.25rem; }}
.como-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 1.5rem; margin-top: 3rem; }}
.como-card {{ background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; text-align: center; }}
.como-num {{ width: 48px; height: 48px; background: var(--gradient); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin: 0 auto 1rem; }}
.cadastro-form {{ max-width: 500px; margin: 0 auto; }}
</style>
</head>
<body>
{NAV}
<div style="height:64px"></div>

<div class="hero">
  <div class="container">
    <span class="section-badge">💰 Programa de Afiliados</span>
    <div class="comissao-num">30%</div>
    <h1>de comissão em cada venda</h1>
    <p style="font-size:1.1rem;color:var(--text2);max-width:500px;margin:0 auto 2rem">Indique o EmotionAI para outros psicólogos e ganhe 30% de comissão recorrente todo mês.</p>
    <a href="#cadastro" class="btn btn-primary btn-lg">Quero ser afiliado →</a>
  </div>
</div>

<section class="section" style="background:var(--bg)">
  <div class="container">
    <div style="text-align:center">
      <span class="section-badge">💵 Quanto você pode ganhar</span>
      <h2 class="section-title">Ganhos <span class="grad">recorrentes</span></h2>
    </div>
    <div class="ganhos-grid">
      <div class="ganho-card">
        <div class="ganho-valor">R$ 8,97</div>
        <div class="ganho-label">Por 1 indicação Pro/mês</div>
      </div>
      <div class="ganho-card">
        <div class="ganho-valor">R$ 89,70</div>
        <div class="ganho-label">Por 10 indicações Pro/mês</div>
      </div>
      <div class="ganho-card">
        <div class="ganho-valor">R$ 897</div>
        <div class="ganho-label">Por 100 indicações Pro/mês</div>
      </div>
      <div class="ganho-card">
        <div class="ganho-valor">R$ 29,97</div>
        <div class="ganho-label">Por 1 indicação Clínica/mês</div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:white">
  <div class="container">
    <div style="text-align:center">
      <span class="section-badge">🚀 Como funciona</span>
      <h2 class="section-title">Simples e <span class="grad">transparente</span></h2>
    </div>
    <div class="como-grid">
      <div class="como-card">
        <div class="como-num">1</div>
        <h3 style="font-weight:700;margin-bottom:0.5rem">Cadastre-se</h3>
        <p style="font-size:0.85rem;color:var(--text2)">Crie sua conta de afiliado gratuitamente e receba seu link único.</p>
      </div>
      <div class="como-card">
        <div class="como-num">2</div>
        <h3 style="font-weight:700;margin-bottom:0.5rem">Divulgue</h3>
        <p style="font-size:0.85rem;color:var(--text2)">Compartilhe seu link no Instagram, WhatsApp, LinkedIn e onde quiser.</p>
      </div>
      <div class="como-card">
        <div class="como-num">3</div>
        <h3 style="font-weight:700;margin-bottom:0.5rem">Ganhe</h3>
        <p style="font-size:0.85rem;color:var(--text2)">Receba 30% de cada venda gerada pelo seu link, todo mês.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg)" id="cadastro">
  <div class="container">
    <div style="text-align:center;margin-bottom:2rem">
      <span class="section-badge">✍️ Cadastro</span>
      <h2 class="section-title">Quero ser <span class="grad">afiliado</span></h2>
    </div>
    <div class="cadastro-form card">
      <div class="form-group">
        <label>Nome completo</label>
        <input type="text" id="af-nome" placeholder="Seu nome">
      </div>
      <div class="form-group">
        <label>E-mail</label>
        <input type="email" id="af-email" placeholder="seu@email.com">
      </div>
      <div class="form-group">
        <label>Profissão</label>
        <select id="af-prof">
          <option value="Psicologo">Psicólogo(a)</option>
          <option value="Estudante">Estudante de Psicologia</option>
          <option value="Influencer">Influencer de Saúde Mental</option>
          <option value="Outro">Outro</option>
        </select>
      </div>
      <button class="btn btn-primary btn-lg" style="width:100%;justify-content:center" onclick="cadastrarAfiliado()">
        Criar minha conta de afiliado →
      </button>
      <div id="af-msg" style="display:none;margin-top:1rem"></div>
    </div>
    <div style="text-align:center;margin-top:1.5rem;font-size:0.85rem;color:var(--text3)">
      ✅ Sem custo · ✅ Pagamento mensal · ✅ Mínimo R$ 50 para saque
    </div>
  </div>
</section>

{FOOTER}
<script>
async function cadastrarAfiliado() {{
  const nome = document.getElementById('af-nome').value.trim();
  const email = document.getElementById('af-email').value.trim();
  const profissao = document.getElementById('af-prof').value;
  const msg = document.getElementById('af-msg');

  if (!nome || !email) {{
    msg.style.display = 'block';
    msg.style.cssText = 'display:block;background:#fff5f5;border:1px solid #fed7d7;color:#c53030;padding:0.75rem 1rem;border-radius:12px;font-size:0.9rem';
    msg.textContent = 'Preencha todos os campos.';
    return;
  }}

  try {{
    const r = await fetch('/api/v1/afiliados/cadastrar', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{nome, email, profissao}})
    }});
    const d = await r.json();
    if (r.ok) {{
      msg.style.cssText = 'display:block;background:#f0fff4;border:1px solid #9ae6b4;color:#276749;padding:1rem;border-radius:12px;font-size:0.9rem';
      msg.innerHTML = '<strong>✅ Cadastro realizado!</strong><br>Seu código: <strong>' + d.codigo + '</strong><br>Link: <a href="' + d.link_afiliado + '" style="color:var(--primary)">' + d.link_afiliado + '</a>';
    }} else {{
      msg.style.cssText = 'display:block;background:#fff5f5;border:1px solid #fed7d7;color:#c53030;padding:0.75rem;border-radius:12px;font-size:0.9rem';
      msg.textContent = 'Erro ao cadastrar. Tente novamente.';
    }}
  }} catch(e) {{
    msg.style.display = 'block';
    msg.textContent = 'Erro de conexão.';
  }}
}}
</script>
</body></html>"""

# ══════════════════════════════════════════════════
# 6. CHECKOUT.HTML
# ══════════════════════════════════════════════════
checkout_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Checkout</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>{CSS_BASE}
body {{ min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem; }}
.checkout-box {{ width: 100%; max-width: 480px; }}
.checkout-header {{ text-align: center; margin-bottom: 2rem; }}
.checkout-header a {{ font-size: 1.5rem; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-decoration: none; }}
.plano-selecionado {{ background: var(--gradient); color: white; border-radius: var(--radius); padding: 1.5rem; margin-bottom: 1.5rem; }}
.plano-nome {{ font-size: 0.9rem; opacity: 0.85; }}
.plano-preco {{ font-size: 2.5rem; font-weight: 900; }}
.plano-features {{ list-style: none; margin-top: 1rem; }}
.plano-features li {{ font-size: 0.85rem; opacity: 0.9; padding: 0.3rem 0; display: flex; align-items: center; gap: 0.5rem; }}
.planos-opcoes {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.75rem; margin-bottom: 1.5rem; }}
.plano-opt {{ border: 2px solid var(--border); border-radius: 12px; padding: 1rem; text-align: center; cursor: pointer; transition: all 0.2s; }}
.plano-opt:hover, .plano-opt.selected {{ border-color: var(--primary); background: rgba(102,126,234,0.05); }}
.plano-opt-nome {{ font-size: 0.85rem; font-weight: 700; }}
.plano-opt-preco {{ font-size: 1.1rem; font-weight: 800; background: var(--gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.garantia {{ text-align: center; font-size: 0.8rem; color: var(--text3); margin-top: 1rem; }}
</style>
</head>
<body>
<div class="checkout-box">
  <div class="checkout-header">
    <a href="/">🧠 EmotionAI</a>
    <p style="color:var(--text3);font-size:0.9rem;margin-top:0.25rem">Escolha seu plano</p>
  </div>

  <div class="planos-opcoes">
    <div class="plano-opt" onclick="selecionarPlano('pro', this)">
      <div class="plano-opt-nome">Pro</div>
      <div class="plano-opt-preco">R$29,90</div>
      <div style="font-size:0.7rem;color:var(--text3)">/mês</div>
    </div>
    <div class="plano-opt selected" onclick="selecionarPlano('clinica', this)">
      <div class="plano-opt-nome">Clínica</div>
      <div class="plano-opt-preco">R$99,90</div>
      <div style="font-size:0.7rem;color:var(--text3)">/mês</div>
    </div>
    <div class="plano-opt" onclick="selecionarPlano('enterprise', this)">
      <div class="plano-opt-nome">Enterprise</div>
      <div class="plano-opt-preco">R$299</div>
      <div style="font-size:0.7rem;color:var(--text3)">/mês</div>
    </div>
  </div>

  <div class="card" style="margin-bottom:1rem">
    <div class="form-group">
      <label>E-mail</label>
      <input type="email" id="checkout-email" placeholder="seu@email.com">
    </div>
    <div class="form-group">
      <label>Cupom de desconto (opcional)</label>
      <div style="display:flex;gap:0.5rem">
        <input type="text" id="checkout-cupom" placeholder="BEMVINDO">
        <button class="btn btn-outline" onclick="aplicarCupom()" style="white-space:nowrap;padding:0.75rem 1rem">Aplicar</button>
      </div>
      <div id="cupom-resultado" style="font-size:0.8rem;margin-top:0.5rem"></div>
    </div>
    <button class="btn btn-primary btn-lg" style="width:100%;justify-content:center" onclick="irParaCheckout()" id="btn-checkout">
      💳 Ir para pagamento →
    </button>
  </div>

  <div style="display:flex;justify-content:center;gap:1rem;font-size:0.75rem;color:var(--text3);margin-bottom:1rem">
    <span>🔒 SSL Seguro</span>
    <span>💳 Stripe</span>
    <span>🔄 Cancele quando quiser</span>
  </div>

  <div class="garantia">🛡️ Garantia de 30 dias. Se não gostar, devolvemos 100%.</div>
  <div id="checkout-msg" style="display:none;margin-top:1rem"></div>
</div>

<script>
let planoSelecionado = 'clinica';

function selecionarPlano(plano, el) {{
  planoSelecionado = plano;
  document.querySelectorAll('.plano-opt').forEach(e => e.classList.remove('selected'));
  el.classList.add('selected');
}}

async function aplicarCupom() {{
  const codigo = document.getElementById('checkout-cupom').value.trim().toUpperCase();
  const resultado = document.getElementById('cupom-resultado');
  const TOKEN = localStorage.getItem('emotion_token');
  if (!codigo) return;
  try {{
    const r = await fetch('/api/v1/cupons/usar/' + codigo, {{
      method: 'POST',
      headers: {{'Content-Type':'application/json','Authorization':'Bearer '+(TOKEN||'')}}
    }});
    const d = await r.json();
    if (r.ok && d.ok) {{
      resultado.style.color = 'var(--accent)';
      resultado.textContent = '✅ Cupom aplicado! ' + d.desconto_aplicado + (d.tipo==='percentual'?'% de desconto':' reais de desconto');
    }} else {{
      resultado.style.color = 'var(--danger)';
      resultado.textContent = '❌ Cupom inválido';
    }}
  }} catch(e) {{
    resultado.style.color = 'var(--danger)';
    resultado.textContent = 'Erro ao aplicar cupom';
  }}
}}

async function irParaCheckout() {{
  const email = document.getElementById('checkout-email').value.trim() ||
                localStorage.getItem('emotion_user_email') || '';
  const TOKEN = localStorage.getItem('emotion_token');
  const btn = document.getElementById('btn-checkout');
  const msg = document.getElementById('checkout-msg');

  if (!email) {{
    msg.style.cssText = 'display:block;background:#fff5f5;border:1px solid #feb2b2;color:#c53030;padding:0.75rem;border-radius:12px;font-size:0.9rem';
    msg.textContent = 'Informe seu e-mail para continuar.';
    return;
  }}

  btn.disabled = true;
  btn.textContent = 'Redirecionando...';

  try {{
    const r = await fetch('/api/v1/stripe-checkout/checkout', {{
      method: 'POST',
      headers: {{'Content-Type':'application/json','Authorization':'Bearer '+(TOKEN||'')}},
      body: JSON.stringify({{plano: planoSelecionado, email}})
    }});
    const d = await r.json();
    if (r.ok && d.url) {{
      window.location.href = d.url;
    }} else {{
      msg.style.cssText = 'display:block;background:#fff5f5;border:1px solid #feb2b2;color:#c53030;padding:0.75rem;border-radius:12px;font-size:0.9rem';
      msg.textContent = 'Erro ao criar checkout. Tente novamente.';
      btn.disabled = false;
      btn.textContent = '💳 Ir para pagamento →';
    }}
  }} catch(e) {{
    btn.disabled = false;
    btn.textContent = '💳 Ir para pagamento →';
    msg.style.display = 'block';
    msg.textContent = 'Erro de conexão.';
  }}
}}

// Pré-preencher email se logado
const emailSalvo = localStorage.getItem('emotion_user_email');
if (emailSalvo) document.getElementById('checkout-email').value = emailSalvo;

// Verificar plano na URL
const params = new URLSearchParams(window.location.search);
const planoUrl = params.get('plano');
if (planoUrl) {{
  document.querySelectorAll('.plano-opt').forEach((el, i) => {{
    const nomes = ['pro','clinica','enterprise'];
    if (nomes[i] === planoUrl) {{ el.click(); }}
  }});
}}
</script>
</body></html>"""

# ══════════════════════════════════════════════════
# SALVAR TODOS
# ══════════════════════════════════════════════════
arquivos = {
    "templates/blog.html": blog_html,
    "templates/terapia.html": terapia_html,
    "templates/privacidade.html": privacidade_html,
    "templates/termos.html": termos_html,
    "templates/afiliado.html": afiliado_html,
    "templates/checkout.html": checkout_html,
}

print("Criando páginas...")
for path, content in arquivos.items():
    Path(path).write_text(content, encoding="utf-8")
    kb = len(content) / 1024
    print(f"  ✅ {path}: {kb:.0f}KB")

print(f"\n✅ {len(arquivos)} páginas criadas com sucesso!")
