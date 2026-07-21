#!/usr/bin/env python3
"""Refaz todas as 6 páginas principais com design profissional"""
from pathlib import Path

# ══════════════════════════════════════════════════
# CSS BASE compartilhado
# ══════════════════════════════════════════════════
CSS_BASE = """
* { margin: 0; padding: 0; box-sizing: border-box; }
:root {
  --primary: #667eea;
  --primary-dark: #764ba2;
  --accent: #38a169;
  --danger: #e53e3e;
  --warning: #d69e2e;
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
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.6;
}
.btn {
  padding: 0.7rem 1.5rem; border-radius: 50px;
  font-weight: 600; font-size: 0.9rem;
  cursor: pointer; border: none;
  text-decoration: none; display: inline-flex;
  align-items: center; gap: 0.5rem;
  transition: all 0.2s;
}
.btn-primary {
  background: var(--gradient); color: white;
  box-shadow: 0 4px 16px rgba(102,126,234,0.35);
}
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 6px 24px rgba(102,126,234,0.45); }
.btn-outline { background: transparent; border: 1.5px solid var(--border); color: var(--text2); }
.btn-outline:hover { border-color: var(--primary); color: var(--primary); }
.btn-lg { padding: 0.9rem 2.5rem; font-size: 1rem; }
.btn-danger { background: var(--danger); color: white; }
.card {
  background: white; border: 1px solid var(--border);
  border-radius: var(--radius); padding: 1.5rem;
  box-shadow: var(--shadow);
}
input, textarea, select {
  width: 100%; padding: 0.75rem 1rem;
  border: 1.5px solid var(--border); border-radius: 12px;
  font-size: 0.95rem; font-family: inherit;
  transition: border-color 0.2s;
  background: white; color: var(--text);
}
input:focus, textarea:focus, select:focus {
  outline: none; border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(102,126,234,0.1);
}
label { font-size: 0.85rem; font-weight: 600; color: var(--text2); display: block; margin-bottom: 0.4rem; }
.form-group { margin-bottom: 1.25rem; }
.alert { padding: 0.75rem 1rem; border-radius: 12px; font-size: 0.9rem; }
.alert-success { background: #f0fff4; border: 1px solid #9ae6b4; color: #276749; }
.alert-danger { background: #fff5f5; border: 1px solid #feb2b2; color: #c53030; }
.alert-warning { background: #fffff0; border: 1px solid #faf089; color: #744210; }
.alert-info { background: #ebf8ff; border: 1px solid #90cdf4; color: #2c5282; }
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
.fade-up { animation: fadeUp 0.5s ease forwards; }
@keyframes spin { to { transform: rotate(360deg); } }
.spinner {
  width: 20px; height: 20px; border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white; border-radius: 50%;
  animation: spin 0.8s linear infinite; display: inline-block;
}
"""

# ══════════════════════════════════════════════════
# 1. LOGIN.HTML
# ══════════════════════════════════════════════════
login_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Entrar</title>
<meta name="description" content="Entre na sua conta EmotionAI">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
{CSS_BASE}
body {{
  min-height: 100vh;
  display: grid;
  grid-template-columns: 1fr 1fr;
}}
.left-panel {{
  background: var(--gradient);
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  padding: 3rem; color: white; text-align: center;
}}
.left-panel h2 {{
  font-size: 2rem; font-weight: 800;
  margin-bottom: 1rem; line-height: 1.2;
}}
.left-panel p {{
  font-size: 1rem; opacity: 0.85;
  line-height: 1.7; margin-bottom: 2rem;
}}
.benefits {{ list-style: none; text-align: left; }}
.benefits li {{
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.6rem 0; font-size: 0.95rem;
  border-bottom: 1px solid rgba(255,255,255,0.15);
}}
.benefits li:last-child {{ border: none; }}
.benefit-icon {{
  width: 32px; height: 32px;
  background: rgba(255,255,255,0.2);
  border-radius: 50%; display: flex;
  align-items: center; justify-content: center;
  font-size: 1rem; flex-shrink: 0;
}}
.right-panel {{
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  padding: 3rem; background: var(--bg);
}}
.login-box {{
  width: 100%; max-width: 420px;
}}
.brand {{
  text-align: center; margin-bottom: 2rem;
}}
.brand a {{
  font-size: 1.5rem; font-weight: 800;
  background: var(--gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-decoration: none;
}}
.brand p {{
  color: var(--text3); font-size: 0.9rem; margin-top: 0.25rem;
}}
.tabs {{
  display: flex; background: var(--border);
  border-radius: 12px; padding: 4px;
  margin-bottom: 2rem;
}}
.tab {{
  flex: 1; padding: 0.6rem;
  text-align: center; border-radius: 10px;
  font-size: 0.9rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
  color: var(--text3);
}}
.tab.active {{
  background: white;
  color: var(--primary);
  box-shadow: var(--shadow);
}}
.divider {{
  display: flex; align-items: center; gap: 1rem;
  margin: 1.5rem 0; color: var(--text3); font-size: 0.85rem;
}}
.divider::before, .divider::after {{
  content: ''; flex: 1;
  height: 1px; background: var(--border);
}}
.tipo-grid {{
  display: grid; grid-template-columns: 1fr 1fr 1fr;
  gap: 0.5rem; margin-bottom: 1rem;
}}
.tipo-btn {{
  padding: 0.6rem; border-radius: 10px;
  border: 1.5px solid var(--border);
  background: white; cursor: pointer;
  text-align: center; font-size: 0.8rem;
  font-weight: 600; color: var(--text2);
  transition: all 0.2s;
}}
.tipo-btn.selected {{
  border-color: var(--primary);
  background: rgba(102,126,234,0.05);
  color: var(--primary);
}}
.tipo-btn div:first-child {{ font-size: 1.5rem; margin-bottom: 0.25rem; }}
@media (max-width: 768px) {{
  body {{ grid-template-columns: 1fr; }}
  .left-panel {{ display: none; }}
  .right-panel {{ padding: 2rem 1.5rem; }}
}}
</style>
</head>
<body>
<!-- PAINEL ESQUERDO -->
<div class="left-panel">
  <div>
    <div style="font-size:3rem;margin-bottom:1rem">🧠</div>
    <h2>Transforme sua prática clínica</h2>
    <p>Psicólogos que usam EmotionAI atendem<br>mais pacientes com menos esforço.</p>
    <ul class="benefits">
      <li>
        <div class="benefit-icon">📋</div>
        <span>Prontuário digital completo e seguro</span>
      </li>
      <li>
        <div class="benefit-icon">📅</div>
        <span>Agendamento automático sem WhatsApp</span>
      </li>
      <li>
        <div class="benefit-icon">📊</div>
        <span>Escalas PHQ-9, GAD-7 e PSS validadas</span>
      </li>
      <li>
        <div class="benefit-icon">🤖</div>
        <span>IA de suporte disponível 24/7</span>
      </li>
      <li>
        <div class="benefit-icon">🔒</div>
        <span>100% seguro e em conformidade com LGPD</span>
      </li>
    </ul>
  </div>
</div>

<!-- PAINEL DIREITO -->
<div class="right-panel">
  <div class="login-box fade-up">
    <div class="brand">
      <a href="/">🧠 EmotionAI</a>
      <p>Plataforma para psicólogos brasileiros</p>
    </div>

    <!-- TABS -->
    <div class="tabs">
      <div class="tab active" onclick="showForm('login')" id="tab-login">
        Entrar
      </div>
      <div class="tab" onclick="showForm('cadastro')" id="tab-cadastro">
        Criar conta
      </div>
    </div>

    <!-- FORM LOGIN -->
    <div id="form-login">
      <div class="form-group">
        <label>E-mail profissional</label>
        <input type="email" id="login-email" placeholder="seu@email.com" autocomplete="email">
      </div>
      <div class="form-group">
        <label>Senha</label>
        <input type="password" id="login-senha" placeholder="••••••••" autocomplete="current-password">
      </div>
      <div style="text-align:right;margin-top:-0.75rem;margin-bottom:1.25rem">
        <a href="/recuperar-senha" style="font-size:0.85rem;color:var(--primary);text-decoration:none">
          Esqueci minha senha
        </a>
      </div>
      <button class="btn btn-primary" style="width:100%;justify-content:center;margin-bottom:1rem" onclick="fazer_login()" id="btn-login">
        Entrar na plataforma →
      </button>
      <p style="text-align:center;font-size:0.85rem;color:var(--text3)">
        Não tem conta?
        <a href="#" onclick="showForm('cadastro')" style="color:var(--primary);font-weight:600">
          Cadastre-se grátis
        </a>
      </p>
    </div>

    <!-- FORM CADASTRO -->
    <div id="form-cadastro" style="display:none">
      <div class="form-group">
        <label>Você é...</label>
        <div class="tipo-grid">
          <div class="tipo-btn selected" onclick="selectTipo('paciente', this)">
            <div>🧘</div>Paciente
          </div>
          <div class="tipo-btn" onclick="selectTipo('psicologo', this)">
            <div>🩺</div>Psicólogo
          </div>
          <div class="tipo-btn" onclick="selectTipo('clinica', this)">
            <div>🏥</div>Clínica
          </div>
        </div>
        <input type="hidden" id="cad-tipo" value="paciente">
      </div>
      <div class="form-group">
        <label>Nome completo</label>
        <input type="text" id="cad-nome" placeholder="Seu nome completo" autocomplete="name">
      </div>
      <div class="form-group">
        <label>E-mail</label>
        <input type="email" id="cad-email" placeholder="seu@email.com" autocomplete="email">
      </div>
      <div class="form-group">
        <label>Senha (mín. 6 caracteres)</label>
        <input type="password" id="cad-senha" placeholder="••••••••" autocomplete="new-password">
      </div>
      <button class="btn btn-primary" style="width:100%;justify-content:center;margin-bottom:1rem" onclick="fazer_cadastro()" id="btn-cadastro">
        Criar conta grátis →
      </button>
      <p style="text-align:center;font-size:0.8rem;color:var(--text3)">
        Ao criar conta você concorda com os
        <a href="/termos" style="color:var(--primary)">Termos de Uso</a> e
        <a href="/privacidade" style="color:var(--primary)">Política de Privacidade</a>
      </p>
    </div>

    <div id="auth-msg" style="margin-top:1rem;display:none"></div>
  </div>
</div>

<script>
let tipoSelecionado = 'paciente';

function showForm(tipo) {{
  document.getElementById('form-login').style.display = tipo === 'login' ? 'block' : 'none';
  document.getElementById('form-cadastro').style.display = tipo === 'cadastro' ? 'block' : 'none';
  document.getElementById('tab-login').classList.toggle('active', tipo === 'login');
  document.getElementById('tab-cadastro').classList.toggle('active', tipo === 'cadastro');
}}

function selectTipo(tipo, el) {{
  tipoSelecionado = tipo;
  document.getElementById('cad-tipo').value = tipo;
  document.querySelectorAll('.tipo-btn').forEach(b => b.classList.remove('selected'));
  el.classList.add('selected');
}}

function showMsg(msg, tipo) {{
  const el = document.getElementById('auth-msg');
  const classes = {{success:'alert-success', danger:'alert-danger', warning:'alert-warning', info:'alert-info'}};
  el.className = 'alert ' + (classes[tipo] || 'alert-info');
  el.textContent = msg;
  el.style.display = 'block';
}}

function setLoading(btnId, loading) {{
  const btn = document.getElementById(btnId);
  if (loading) {{
    btn.disabled = true;
    btn.innerHTML = '<span class="spinner"></span> Aguarde...';
  }} else {{
    btn.disabled = false;
    btn.innerHTML = btnId === 'btn-login' ? 'Entrar na plataforma →' : 'Criar conta grátis →';
  }}
}}

async function fazer_login() {{
  const email = document.getElementById('login-email').value.trim();
  const senha = document.getElementById('login-senha').value;
  if (!email || !senha) return showMsg('Preencha e-mail e senha', 'warning');
  setLoading('btn-login', true);
  try {{
    const r = await fetch('/api/v1/auth/login', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{email, senha}})
    }});
    const data = await r.json();
    if (r.ok) {{
      localStorage.setItem('emotion_token', data.token || data.access_token);
      localStorage.setItem('emotion_userid', data.user_id);
      localStorage.setItem('emotion_user_email', data.email);
      localStorage.setItem('emotion_user_nome', data.nome);
      localStorage.setItem('emotion_user_tipo', data.tipo || 'paciente');
      localStorage.setItem('emotion_user_plano', data.plano || 'free');
      showMsg('✅ Login realizado! Redirecionando...', 'success');
      setTimeout(() => window.location.href = '/app/dashboard', 1000);
    }} else {{
      showMsg(data.detail || 'E-mail ou senha incorretos', 'danger');
      setLoading('btn-login', false);
    }}
  }} catch(e) {{
    showMsg('Erro de conexão. Tente novamente.', 'danger');
    setLoading('btn-login', false);
  }}
}}

async function fazer_cadastro() {{
  const nome = document.getElementById('cad-nome').value.trim();
  const email = document.getElementById('cad-email').value.trim();
  const senha = document.getElementById('cad-senha').value;
  const tipo = tipoSelecionado;
  if (!nome || !email || !senha) return showMsg('Preencha todos os campos', 'warning');
  if (senha.length < 6) return showMsg('Senha mínima: 6 caracteres', 'warning');
  setLoading('btn-cadastro', true);
  try {{
    const r = await fetch('/api/v1/auth/cadastrar', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{nome, email, senha, tipo}})
    }});
    const data = await r.json();
    if (r.ok) {{
      localStorage.setItem('emotion_token', data.token || data.access_token);
      localStorage.setItem('emotion_userid', data.user_id);
      localStorage.setItem('emotion_user_email', data.email);
      localStorage.setItem('emotion_user_nome', data.nome);
      localStorage.setItem('emotion_user_tipo', data.tipo || tipo);
      localStorage.setItem('emotion_user_plano', data.plano || 'free');
      showMsg('✅ Conta criada! Redirecionando...', 'success');
      setTimeout(() => window.location.href = '/app/dashboard', 1000);
    }} else {{
      showMsg(data.detail || 'Erro no cadastro', 'danger');
      setLoading('btn-cadastro', false);
    }}
  }} catch(e) {{
    showMsg('Erro de conexão. Tente novamente.', 'danger');
    setLoading('btn-cadastro', false);
  }}
}}

document.addEventListener('keydown', e => {{
  if (e.key === 'Enter') {{
    const loginVisible = document.getElementById('form-login').style.display !== 'none';
    if (loginVisible) fazer_login(); else fazer_cadastro();
  }}
}});
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 2. DASHBOARD.HTML
# ══════════════════════════════════════════════════
dashboard_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Dashboard</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
{CSS_BASE}
body {{ display: flex; min-height: 100vh; }}
.sidebar {{
  width: 260px; background: white;
  border-right: 1px solid var(--border);
  display: flex; flex-direction: column;
  position: fixed; top: 0; left: 0;
  height: 100vh; z-index: 50;
  padding: 1.5rem 0;
}}
.sidebar-brand {{
  padding: 0 1.5rem 1.5rem;
  border-bottom: 1px solid var(--border);
  margin-bottom: 1rem;
}}
.sidebar-brand a {{
  font-size: 1.25rem; font-weight: 800;
  background: var(--gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-decoration: none;
}}
.nav-item {{
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.75rem 1.5rem;
  color: var(--text2); text-decoration: none;
  font-size: 0.9rem; font-weight: 500;
  border-radius: 0 50px 50px 0;
  margin-right: 1rem;
  transition: all 0.2s;
}}
.nav-item:hover {{ background: var(--bg); color: var(--primary); }}
.nav-item.active {{
  background: rgba(102,126,234,0.1);
  color: var(--primary); font-weight: 600;
}}
.nav-icon {{ font-size: 1.1rem; width: 20px; text-align: center; }}
.nav-section {{
  padding: 0.5rem 1.5rem;
  font-size: 0.7rem; font-weight: 700;
  color: var(--text3); text-transform: uppercase;
  letter-spacing: 0.08em; margin-top: 1rem;
}}
.sidebar-footer {{
  margin-top: auto; padding: 1rem 1.5rem;
  border-top: 1px solid var(--border);
}}
.user-info {{
  display: flex; align-items: center; gap: 0.75rem;
}}
.user-avatar {{
  width: 38px; height: 38px;
  background: var(--gradient); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: white; font-weight: 700; font-size: 1rem;
}}
.user-name {{ font-size: 0.85rem; font-weight: 600; }}
.user-plan {{
  font-size: 0.75rem; color: var(--text3);
}}
.main {{
  margin-left: 260px; flex: 1;
  background: var(--bg); min-height: 100vh;
}}
.topbar {{
  background: white; border-bottom: 1px solid var(--border);
  padding: 1rem 2rem;
  display: flex; justify-content: space-between; align-items: center;
  position: sticky; top: 0; z-index: 40;
}}
.topbar-greeting {{ font-size: 1.1rem; font-weight: 700; }}
.topbar-sub {{ font-size: 0.85rem; color: var(--text3); }}
.topbar-actions {{ display: flex; gap: 0.75rem; align-items: center; }}
.content {{ padding: 2rem; }}
.stats-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem; margin-bottom: 2rem;
}}
.stat-card {{
  background: white; border: 1px solid var(--border);
  border-radius: var(--radius); padding: 1.5rem;
  transition: all 0.2s;
}}
.stat-card:hover {{ box-shadow: var(--shadow); transform: translateY(-2px); }}
.stat-card-icon {{
  font-size: 1.75rem; margin-bottom: 0.75rem;
}}
.stat-card-value {{
  font-size: 2rem; font-weight: 800;
  background: var(--gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.stat-card-label {{
  font-size: 0.85rem; color: var(--text3);
  margin-top: 0.25rem;
}}
.stat-card-change {{
  font-size: 0.8rem; color: var(--accent);
  margin-top: 0.5rem; font-weight: 600;
}}
.grid-2 {{
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 1.5rem; margin-bottom: 1.5rem;
}}
.section-title {{
  font-size: 1rem; font-weight: 700;
  margin-bottom: 1rem; color: var(--text);
}}
.quick-actions {{
  display: grid; grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}}
.quick-btn {{
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 0.5rem; padding: 1.25rem;
  background: var(--bg); border: 1px solid var(--border);
  border-radius: var(--radius); cursor: pointer;
  text-decoration: none; color: var(--text);
  font-size: 0.85rem; font-weight: 600;
  transition: all 0.2s; text-align: center;
}}
.quick-btn:hover {{
  background: rgba(102,126,234,0.05);
  border-color: var(--primary); color: var(--primary);
  transform: translateY(-2px);
}}
.quick-btn-icon {{ font-size: 1.75rem; }}
.humor-grid {{
  display: flex; gap: 0.75rem; flex-wrap: wrap;
}}
.humor-btn {{
  display: flex; flex-direction: column;
  align-items: center; gap: 0.25rem;
  padding: 0.75rem 1rem;
  border: 2px solid var(--border); border-radius: 12px;
  cursor: pointer; font-size: 0.8rem;
  color: var(--text2); background: white;
  transition: all 0.2s; flex: 1; min-width: 70px;
}}
.humor-btn:hover, .humor-btn.selected {{
  border-color: var(--primary);
  background: rgba(102,126,234,0.05);
  color: var(--primary);
}}
.humor-btn span:first-child {{ font-size: 1.75rem; }}
.xp-bar-container {{
  background: var(--border); border-radius: 50px;
  height: 8px; overflow: hidden; margin: 0.5rem 0;
}}
.xp-bar {{
  height: 100%; background: var(--gradient);
  border-radius: 50px; transition: width 1s ease;
}}
.streak-display {{
  display: flex; align-items: center; gap: 0.75rem;
  padding: 1rem; background: rgba(246,173,85,0.1);
  border: 1px solid rgba(246,173,85,0.3);
  border-radius: 12px; margin-bottom: 1rem;
}}
.streak-fire {{ font-size: 2rem; }}
.streak-num {{ font-size: 1.5rem; font-weight: 800; color: #d69e2e; }}
.streak-label {{ font-size: 0.8rem; color: var(--text3); }}
.session-card {{
  display: flex; align-items: center; gap: 1rem;
  padding: 1rem; background: rgba(102,126,234,0.05);
  border: 1px solid rgba(102,126,234,0.2);
  border-radius: 12px; margin-bottom: 0.75rem;
}}
.session-time {{
  font-weight: 700; font-size: 0.9rem;
  color: var(--primary);
}}
.session-name {{ font-size: 0.85rem; color: var(--text2); }}
.badge {{
  display: inline-block; padding: 0.2rem 0.6rem;
  border-radius: 50px; font-size: 0.7rem; font-weight: 700;
}}
.badge-green {{ background: rgba(56,161,105,0.1); color: var(--accent); }}
.badge-purple {{ background: rgba(102,126,234,0.1); color: var(--primary); }}
@media (max-width: 768px) {{
  .sidebar {{ transform: translateX(-100%); }}
  .sidebar.open {{ transform: translateX(0); }}
  .main {{ margin-left: 0; }}
  .grid-2 {{ grid-template-columns: 1fr; }}
  .stats-grid {{ grid-template-columns: 1fr 1fr; }}
}}
</style>
</head>
<body>
<!-- SIDEBAR -->
<aside class="sidebar" id="sidebar">
  <div class="sidebar-brand">
    <a href="/">🧠 EmotionAI</a>
  </div>
  <a href="/app/dashboard" class="nav-item active">
    <span class="nav-icon">🏠</span> Dashboard
  </a>
  <a href="/app/chat" class="nav-item">
    <span class="nav-icon">💬</span> Chat IA
  </a>
  <a href="/app/diario" class="nav-item">
    <span class="nav-icon">📓</span> Diário Emocional
  </a>
  <a href="/app/avaliacao" class="nav-item">
    <span class="nav-icon">📊</span> Avaliações
  </a>
  <span class="nav-section">Clínica</span>
  <a href="/app/agenda" class="nav-item">
    <span class="nav-icon">📅</span> Agenda
  </a>
  <a href="/app/perfil" class="nav-item">
    <span class="nav-icon">👥</span> Pacientes
  </a>
  <a href="/app/analises" class="nav-item">
    <span class="nav-icon">📈</span> Análises
  </a>
  <span class="nav-section">Conta</span>
  <a href="/app/configuracoes" class="nav-item">
    <span class="nav-icon">⚙️</span> Configurações
  </a>
  <a href="/app/planos" class="nav-item">
    <span class="nav-icon">⭐</span> Planos
  </a>
  <div class="sidebar-footer">
    <div class="user-info">
      <div class="user-avatar" id="avatar-inicial">A</div>
      <div>
        <div class="user-name" id="user-nome">Carregando...</div>
        <div class="user-plan" id="user-plano">Plano Free</div>
      </div>
    </div>
  </div>
</aside>

<!-- MAIN -->
<main class="main" id="main-content">
  <!-- TOPBAR -->
  <div class="topbar">
    <div>
      <div class="topbar-greeting" id="greeting">Bom dia! 👋</div>
      <div class="topbar-sub" id="greeting-sub">Como você está hoje?</div>
    </div>
    <div class="topbar-actions">
      <a href="/app/chat" class="btn btn-primary">
        💬 Falar com IA
      </a>
      <button onclick="sair()" class="btn btn-outline">Sair</button>
    </div>
  </div>

  <!-- CONTENT -->
  <div class="content">
    <!-- STATS -->
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-card-icon">🧠</div>
        <div class="stat-card-value" id="stat-xp">0</div>
        <div class="stat-card-label">Pontos XP</div>
        <div class="stat-card-change" id="stat-nivel">Iniciante</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-icon">📓</div>
        <div class="stat-card-value" id="stat-diario">0</div>
        <div class="stat-card-label">Entradas no diário</div>
        <div class="stat-card-change">↑ Esta semana</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-icon">📊</div>
        <div class="stat-card-value" id="stat-avaliacoes">0</div>
        <div class="stat-card-label">Avaliações feitas</div>
        <div class="stat-card-change">PHQ-9, GAD-7, PSS</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-icon">🔥</div>
        <div class="stat-card-value" id="stat-streak">0</div>
        <div class="stat-card-label">Dias consecutivos</div>
        <div class="stat-card-change">Continue assim!</div>
      </div>
    </div>

    <div class="grid-2">
      <!-- AÇÕES RÁPIDAS -->
      <div class="card">
        <div class="section-title">⚡ Ações rápidas</div>
        <div class="quick-actions">
          <a href="/app/chat" class="quick-btn">
            <span class="quick-btn-icon">💬</span>
            Chat com IA
          </a>
          <a href="/app/diario" class="quick-btn">
            <span class="quick-btn-icon">📓</span>
            Diário
          </a>
          <a href="/app/avaliacao" class="quick-btn">
            <span class="quick-btn-icon">📊</span>
            PHQ-9
          </a>
          <a href="/app/agenda" class="quick-btn">
            <span class="quick-btn-icon">📅</span>
            Agenda
          </a>
        </div>
      </div>

      <!-- HUMOR DO DIA -->
      <div class="card">
        <div class="section-title">😊 Como você está agora?</div>
        <div class="humor-grid" id="humor-grid">
          <div class="humor-btn" onclick="registrarHumor('otimo', this)">
            <span>😄</span><span>Ótimo</span>
          </div>
          <div class="humor-btn" onclick="registrarHumor('bem', this)">
            <span>🙂</span><span>Bem</span>
          </div>
          <div class="humor-btn" onclick="registrarHumor('neutro', this)">
            <span>😐</span><span>Neutro</span>
          </div>
          <div class="humor-btn" onclick="registrarHumor('mal', this)">
            <span>😔</span><span>Mal</span>
          </div>
          <div class="humor-btn" onclick="registrarHumor('pessimo', this)">
            <span>😞</span><span>Péssimo</span>
          </div>
        </div>
        <div id="humor-msg" style="display:none;margin-top:0.75rem"></div>
      </div>
    </div>

    <div class="grid-2">
      <!-- PROGRESSO XP -->
      <div class="card">
        <div class="section-title">🎮 Seu progresso</div>
        <div class="streak-display">
          <span class="streak-fire">🔥</span>
          <div>
            <div class="streak-num" id="streak-num">0</div>
            <div class="streak-label">dias consecutivos</div>
          </div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem">
          <span style="font-size:0.85rem;font-weight:600" id="xp-atual">0 XP</span>
          <span style="font-size:0.85rem;color:var(--text3)" id="xp-proximo">500 XP para próximo nível</span>
        </div>
        <div class="xp-bar-container">
          <div class="xp-bar" id="xp-bar" style="width:0%"></div>
        </div>
        <div style="font-size:0.8rem;color:var(--text3);margin-top:0.5rem" id="nivel-label">
          Nível: Iniciante
        </div>
      </div>

      <!-- PRÓXIMAS SESSÕES -->
      <div class="card">
        <div class="section-title">📅 Próximas sessões</div>
        <div id="proximas-sessoes">
          <div style="text-align:center;padding:2rem;color:var(--text3)">
            <div style="font-size:2rem;margin-bottom:0.5rem">📅</div>
            <div style="font-size:0.9rem">Nenhuma sessão agendada</div>
            <a href="/app/agenda" class="btn btn-outline" style="margin-top:1rem;font-size:0.8rem">
              Agendar sessão
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- AVALIAÇÕES RECENTES -->
    <div class="card">
      <div class="section-title">📊 Suas avaliações</div>
      <div id="avaliacoes-recentes" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-top:0.5rem">
        <div style="background:var(--bg);border-radius:12px;padding:1.25rem;text-align:center;cursor:pointer" onclick="window.location='/app/avaliacao'">
          <div style="font-size:1.5rem;margin-bottom:0.5rem">😔</div>
          <div style="font-weight:700;font-size:1rem">PHQ-9</div>
          <div style="font-size:0.8rem;color:var(--text3)">Depressão</div>
          <a href="/app/avaliacao" class="btn btn-outline" style="margin-top:1rem;font-size:0.75rem;padding:0.4rem 1rem">
            Fazer agora
          </a>
        </div>
        <div style="background:var(--bg);border-radius:12px;padding:1.25rem;text-align:center;cursor:pointer">
          <div style="font-size:1.5rem;margin-bottom:0.5rem">😰</div>
          <div style="font-weight:700;font-size:1rem">GAD-7</div>
          <div style="font-size:0.8rem;color:var(--text3)">Ansiedade</div>
          <a href="/app/avaliacao" class="btn btn-outline" style="margin-top:1rem;font-size:0.75rem;padding:0.4rem 1rem">
            Fazer agora
          </a>
        </div>
        <div style="background:var(--bg);border-radius:12px;padding:1.25rem;text-align:center;cursor:pointer">
          <div style="font-size:1.5rem;margin-bottom:0.5rem">😤</div>
          <div style="font-weight:700;font-size:1rem">PSS-10</div>
          <div style="font-size:0.8rem;color:var(--text3)">Estresse</div>
          <a href="/app/avaliacao" class="btn btn-outline" style="margin-top:1rem;font-size:0.75rem;padding:0.4rem 1rem">
            Fazer agora
          </a>
        </div>
        <div style="background:var(--bg);border-radius:12px;padding:1.25rem;text-align:center;cursor:pointer">
          <div style="font-size:1.5rem;margin-bottom:0.5rem">🌟</div>
          <div style="font-weight:700;font-size:1rem">Big Five</div>
          <div style="font-size:0.8rem;color:var(--text3)">Personalidade</div>
          <a href="/app/avaliacao" class="btn btn-outline" style="margin-top:1rem;font-size:0.75rem;padding:0.4rem 1rem">
            Fazer agora
          </a>
        </div>
      </div>
    </div>
  </div>
</main>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const NOME = localStorage.getItem('emotion_user_nome') || 'Usuário';
const PLANO = localStorage.getItem('emotion_user_plano') || 'free';
const USER_ID = localStorage.getItem('emotion_userid') || 'user';

if (!TOKEN) window.location.href = '/app/login';

// Saudação
const hora = new Date().getHours();
const saudacao = hora < 12 ? 'Bom dia' : hora < 18 ? 'Boa tarde' : 'Boa noite';
document.getElementById('greeting').textContent = saudacao + ', ' + NOME.split(' ')[0] + '! 👋';
document.getElementById('greeting-sub').textContent = new Date().toLocaleDateString('pt-BR', {{weekday:'long', day:'numeric', month:'long'}});

// Avatar
document.getElementById('avatar-inicial').textContent = NOME[0].toUpperCase();
document.getElementById('user-nome').textContent = NOME;
document.getElementById('user-plano').textContent = 'Plano ' + PLANO.charAt(0).toUpperCase() + PLANO.slice(1);

// Carregar XP
async function carregarXP() {{
  try {{
    const r = await fetch('/api/v1/xp/' + USER_ID, {{headers: {{'Authorization': 'Bearer ' + TOKEN}}}});
    if (r.ok) {{
      const d = await r.json();
      const xp = d.xp || 0;
      const nivel = d.nivel || 'Iniciante';
      const streak = d.streak || 0;
      document.getElementById('stat-xp').textContent = xp;
      document.getElementById('stat-nivel').textContent = nivel;
      document.getElementById('stat-streak').textContent = streak;
      document.getElementById('streak-num').textContent = streak;
      document.getElementById('xp-atual').textContent = xp + ' XP';
      document.getElementById('nivel-label').textContent = 'Nível: ' + nivel;
      const pct = Math.min((xp % 500) / 500 * 100, 100);
      document.getElementById('xp-bar').style.width = pct + '%';
    }}
  }} catch(e) {{}}
}}

carregarXP();

async function registrarHumor(humor, el) {{
  document.querySelectorAll('.humor-btn').forEach(b => b.classList.remove('selected'));
  el.classList.add('selected');
  const msg = document.getElementById('humor-msg');
  msg.className = 'alert alert-success';
  msg.textContent = '✅ Humor registrado! Continue assim.';
  msg.style.display = 'block';
  try {{
    await fetch('/api/v1/xp/ganhar?user_id=' + USER_ID + '&acao=registro_humor&xp=5', {{
      method: 'POST', headers: {{'Authorization': 'Bearer ' + TOKEN}}
    }});
  }} catch(e) {{}}
  setTimeout(() => {{ msg.style.display = 'none'; }}, 3000);
}}

function sair() {{
  localStorage.clear();
  window.location.href = '/app/login';
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 3. CHAT_IA.HTML
# ══════════════════════════════════════════════════
chat_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Chat com IA</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
{CSS_BASE}
body {{ display: flex; height: 100vh; overflow: hidden; background: var(--bg); }}
.sidebar {{
  width: 240px; background: white;
  border-right: 1px solid var(--border);
  display: flex; flex-direction: column;
  padding: 1rem 0;
}}
.sidebar-top {{ padding: 0 1rem 1rem; border-bottom: 1px solid var(--border); }}
.sidebar-brand {{
  font-size: 1.1rem; font-weight: 800;
  background: var(--gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-decoration: none; display: block;
  margin-bottom: 0.75rem;
}}
.chat-list {{ flex: 1; overflow-y: auto; padding: 0.5rem; }}
.chat-list-item {{
  padding: 0.75rem; border-radius: 10px;
  cursor: pointer; font-size: 0.85rem;
  color: var(--text2); transition: all 0.2s;
  white-space: nowrap; overflow: hidden;
  text-overflow: ellipsis;
}}
.chat-list-item:hover {{ background: var(--bg); }}
.chat-list-item.active {{
  background: rgba(102,126,234,0.1); color: var(--primary);
}}
.chat-main {{
  flex: 1; display: flex; flex-direction: column;
  min-width: 0;
}}
.chat-header {{
  background: white; border-bottom: 1px solid var(--border);
  padding: 1rem 1.5rem;
  display: flex; align-items: center; gap: 1rem;
}}
.ai-avatar {{
  width: 42px; height: 42px;
  background: var(--gradient); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1.25rem;
}}
.ai-name {{ font-weight: 700; font-size: 0.95rem; }}
.ai-status {{
  font-size: 0.8rem; color: var(--accent);
  display: flex; align-items: center; gap: 0.3rem;
}}
.ai-status::before {{
  content: ''; width: 6px; height: 6px;
  background: var(--accent); border-radius: 50%;
}}
.chat-messages {{
  flex: 1; overflow-y: auto;
  padding: 1.5rem; display: flex;
  flex-direction: column; gap: 1.25rem;
}}
.msg {{
  display: flex; gap: 0.75rem;
  max-width: 80%; animation: fadeUp 0.3s ease;
}}
.msg.user {{ margin-left: auto; flex-direction: row-reverse; }}
.msg-avatar {{
  width: 36px; height: 36px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem; flex-shrink: 0;
}}
.msg-avatar.ai {{ background: var(--gradient); color: white; }}
.msg-avatar.user {{ background: var(--border); }}
.msg-bubble {{
  padding: 0.875rem 1.125rem;
  border-radius: 18px; font-size: 0.9rem;
  line-height: 1.6; max-width: 100%;
}}
.msg.ai .msg-bubble {{
  background: white; border: 1px solid var(--border);
  border-top-left-radius: 4px;
}}
.msg.user .msg-bubble {{
  background: var(--gradient); color: white;
  border-top-right-radius: 4px;
}}
.msg-time {{
  font-size: 0.7rem; color: var(--text3);
  margin-top: 0.35rem;
  text-align: right;
}}
.typing-indicator {{
  display: flex; gap: 4px; padding: 0.75rem;
}}
.typing-dot {{
  width: 8px; height: 8px;
  background: var(--text3); border-radius: 50%;
  animation: typing 1.2s infinite;
}}
.typing-dot:nth-child(2) {{ animation-delay: 0.2s; }}
.typing-dot:nth-child(3) {{ animation-delay: 0.4s; }}
@keyframes typing {{
  0%, 100% {{ transform: translateY(0); opacity: 0.5; }}
  50% {{ transform: translateY(-4px); opacity: 1; }}
}}
.suggestions {{
  display: flex; gap: 0.5rem; flex-wrap: wrap;
  padding: 0 1.5rem 1rem;
}}
.suggestion-btn {{
  padding: 0.5rem 1rem; border-radius: 20px;
  border: 1px solid var(--border);
  background: white; font-size: 0.8rem;
  cursor: pointer; color: var(--text2);
  transition: all 0.2s; white-space: nowrap;
}}
.suggestion-btn:hover {{
  border-color: var(--primary); color: var(--primary);
  background: rgba(102,126,234,0.05);
}}
.chat-input-area {{
  background: white; border-top: 1px solid var(--border);
  padding: 1rem 1.5rem;
}}
.chat-input-box {{
  display: flex; gap: 0.75rem; align-items: flex-end;
}}
.chat-input {{
  flex: 1; border: 1.5px solid var(--border);
  border-radius: 24px; padding: 0.75rem 1.25rem;
  font-size: 0.9rem; resize: none;
  max-height: 120px; min-height: 48px;
  line-height: 1.5;
}}
.chat-input:focus {{
  outline: none; border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(102,126,234,0.1);
}}
.send-btn {{
  width: 48px; height: 48px;
  background: var(--gradient); border: none;
  border-radius: 50%; cursor: pointer;
  color: white; font-size: 1.1rem;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; transition: all 0.2s;
  box-shadow: 0 4px 12px rgba(102,126,234,0.35);
}}
.send-btn:hover {{ transform: scale(1.05); }}
.send-btn:disabled {{ opacity: 0.5; cursor: not-allowed; transform: none; }}
.crise-banner {{
  background: #fff5f5; border-top: 1px solid #fed7d7;
  padding: 0.5rem 1.5rem;
  display: flex; align-items: center; gap: 0.5rem;
  font-size: 0.8rem; color: var(--danger);
}}
@media (max-width: 768px) {{
  .sidebar {{ display: none; }}
  .msg {{ max-width: 90%; }}
}}
</style>
</head>
<body>

<!-- SIDEBAR -->
<div class="sidebar">
  <div class="sidebar-top">
    <a href="/app/dashboard" class="sidebar-brand">🧠 EmotionAI</a>
    <button class="btn btn-primary" style="width:100%;justify-content:center;font-size:0.85rem" onclick="novoChat()">
      + Nova conversa
    </button>
  </div>
  <div class="chat-list">
    <div class="chat-list-item active">💬 Conversa atual</div>
    <div style="padding:1rem;text-align:center;color:var(--text3);font-size:0.8rem">
      Histórico de conversas em breve
    </div>
  </div>
  <div style="padding:1rem;border-top:1px solid var(--border)">
    <a href="/app/dashboard" style="font-size:0.85rem;color:var(--text2);text-decoration:none">
      ← Voltar ao dashboard
    </a>
  </div>
</div>

<!-- CHAT MAIN -->
<div class="chat-main">
  <!-- HEADER -->
  <div class="chat-header">
    <div class="ai-avatar">🧠</div>
    <div>
      <div class="ai-name">Sofia — IA de Saúde Mental</div>
      <div class="ai-status">Online agora</div>
    </div>
    <div style="margin-left:auto">
      <a href="/app/avaliacao" class="btn btn-outline" style="font-size:0.8rem;padding:0.5rem 1rem">
        📊 Fazer avaliação
      </a>
    </div>
  </div>

  <!-- MESSAGES -->
  <div class="chat-messages" id="chat-messages">
    <div class="msg ai">
      <div class="msg-avatar ai">🧠</div>
      <div>
        <div class="msg-bubble">
          Olá! Sou a Sofia, sua assistente de saúde mental com IA. 💙<br><br>
          Estou aqui para te ouvir, ajudar a entender suas emoções e oferecer
          técnicas de bem-estar. Como você está se sentindo hoje?
        </div>
        <div class="msg-time">Agora</div>
      </div>
    </div>
  </div>

  <!-- SUGGESTIONS -->
  <div class="suggestions" id="suggestions">
    <button class="suggestion-btn" onclick="usarSugestao(this)">😰 Estou ansioso</button>
    <button class="suggestion-btn" onclick="usarSugestao(this)">😔 Me sinto triste</button>
    <button class="suggestion-btn" onclick="usarSugestao(this)">🧘 Técnica de respiração</button>
    <button class="suggestion-btn" onclick="usarSugestao(this)">💤 Problemas para dormir</button>
    <button class="suggestion-btn" onclick="usarSugestao(this)">💪 Como melhorar meu humor</button>
  </div>

  <!-- INPUT -->
  <div class="chat-input-area">
    <div class="chat-input-box">
      <textarea
        id="chat-input"
        class="chat-input"
        placeholder="Digite sua mensagem... (Enter para enviar, Shift+Enter para nova linha)"
        rows="1"
      ></textarea>
      <button class="send-btn" id="send-btn" onclick="enviarMensagem()">➤</button>
    </div>
  </div>

  <!-- CRISE -->
  <div class="crise-banner">
    🆘 Em crise? Ligue para o CVV:
    <strong><a href="tel:188" style="color:var(--danger)">188</a></strong>
    (24h, gratuito) ou acesse
    <a href="https://cvv.org.br" target="_blank" style="color:var(--danger)">cvv.org.br</a>
  </div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const NOME = localStorage.getItem('emotion_user_nome') || 'Usuário';
if (!TOKEN) window.location.href = '/app/login';

const messagesEl = document.getElementById('chat-messages');
const inputEl = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
let enviando = false;

function agora() {{
  return new Date().toLocaleTimeString('pt-BR', {{hour:'2-digit', minute:'2-digit'}});
}}

function adicionarMsg(texto, tipo) {{
  const isUser = tipo === 'user';
  const div = document.createElement('div');
  div.className = 'msg ' + tipo;
  div.innerHTML = `
    <div class="msg-avatar ${{tipo}}">${{isUser ? NOME[0].toUpperCase() : '🧠'}}</div>
    <div>
      <div class="msg-bubble">${{texto.replace(/\\n/g, '<br>')}}</div>
      <div class="msg-time">${{agora()}}</div>
    </div>
  `;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
  return div;
}}

function mostrarTyping() {{
  const div = document.createElement('div');
  div.className = 'msg ai';
  div.id = 'typing';
  div.innerHTML = `
    <div class="msg-avatar ai">🧠</div>
    <div class="msg-bubble">
      <div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
      </div>
    </div>
  `;
  messagesEl.appendChild(div);
  messagesEl.scrollTop = messagesEl.scrollHeight;
}}

function removerTyping() {{
  const t = document.getElementById('typing');
  if (t) t.remove();
}}

async function enviarMensagem() {{
  const msg = inputEl.value.trim();
  if (!msg || enviando) return;

  // Esconder sugestões
  document.getElementById('suggestions').style.display = 'none';

  enviando = true;
  sendBtn.disabled = true;
  inputEl.value = '';
  inputEl.style.height = 'auto';

  adicionarMsg(msg, 'user');
  mostrarTyping();

  try {{
    const r = await fetch('/api/v1/chat/enviar', {{
      method: 'POST',
      headers: {{
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + TOKEN
      }},
      body: JSON.stringify({{mensagem: msg}})
    }});
    const data = await r.json();
    removerTyping();
    const resposta = data.resposta || data.response || data.message || 'Desculpe, tente novamente.';
    adicionarMsg(resposta, 'ai');
  }} catch(e) {{
    removerTyping();
    adicionarMsg('Erro de conexão. Verifique sua internet e tente novamente.', 'ai');
  }}

  enviando = false;
  sendBtn.disabled = false;
  inputEl.focus();
}}

function usarSugestao(btn) {{
  inputEl.value = btn.textContent.trim().split(' ').slice(1).join(' ');
  enviarMensagem();
}}

function novoChat() {{
  messagesEl.innerHTML = `
    <div class="msg ai">
      <div class="msg-avatar ai">🧠</div>
      <div>
        <div class="msg-bubble">
          Olá! Sou a Sofia. Como posso te ajudar hoje? 💙
        </div>
        <div class="msg-time">Agora</div>
      </div>
    </div>
  `;
  document.getElementById('suggestions').style.display = 'flex';
}}

// Auto-resize textarea
inputEl.addEventListener('input', function() {{
  this.style.height = 'auto';
  this.style.height = Math.min(this.scrollHeight, 120) + 'px';
}});

// Enter para enviar
inputEl.addEventListener('keydown', function(e) {{
  if (e.key === 'Enter' && !e.shiftKey) {{
    e.preventDefault();
    enviarMensagem();
  }}
}});
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 4. DIARIO.HTML
# ══════════════════════════════════════════════════
diario_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Diário Emocional</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
{CSS_BASE}
body {{ background: var(--bg); }}
.topbar {{
  background: white; border-bottom: 1px solid var(--border);
  padding: 1rem 2rem;
  display: flex; align-items: center; gap: 1rem;
  position: sticky; top: 0; z-index: 40;
}}
.topbar a {{
  color: var(--text2); text-decoration: none;
  font-size: 0.9rem;
}}
.topbar-title {{
  font-size: 1.1rem; font-weight: 700;
  margin-left: 0.5rem;
}}
.content {{ max-width: 700px; margin: 0 auto; padding: 2rem; }}
.emocoes-grid {{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0.75rem; margin-bottom: 1.5rem;
}}
.emocao-btn {{
  display: flex; flex-direction: column;
  align-items: center; gap: 0.4rem;
  padding: 1rem 0.5rem;
  border: 2px solid var(--border);
  border-radius: 14px; cursor: pointer;
  background: white; transition: all 0.2s;
  font-size: 0.8rem; color: var(--text2);
  font-weight: 600;
}}
.emocao-btn:hover {{
  border-color: var(--primary);
  transform: translateY(-2px);
  box-shadow: var(--shadow);
}}
.emocao-btn.selected {{
  border-color: var(--primary);
  background: rgba(102,126,234,0.05);
  color: var(--primary);
}}
.emocao-emoji {{ font-size: 2rem; }}
.intensidade-container {{ margin-bottom: 1.5rem; }}
.intensidade-label {{
  display: flex; justify-content: space-between;
  font-size: 0.8rem; color: var(--text3);
  margin-top: 0.5rem;
}}
input[type=range] {{
  width: 100%; height: 6px;
  border-radius: 50px; border: none;
  background: linear-gradient(to right, #667eea var(--val, 50%), #e2e8f0 var(--val, 50%));
  cursor: pointer;
}}
.entrada-card {{
  background: white; border: 1px solid var(--border);
  border-radius: var(--radius); padding: 1.25rem;
  margin-bottom: 1rem; cursor: pointer;
  transition: all 0.2s;
}}
.entrada-card:hover {{
  border-color: rgba(102,126,234,0.3);
  box-shadow: var(--shadow);
}}
.entrada-header {{
  display: flex; justify-content: space-between;
  align-items: flex-start; margin-bottom: 0.5rem;
}}
.entrada-emocao {{
  display: flex; align-items: center; gap: 0.5rem;
  font-weight: 700; font-size: 0.95rem;
}}
.entrada-data {{
  font-size: 0.8rem; color: var(--text3);
}}
.entrada-texto {{
  font-size: 0.9rem; color: var(--text2);
  line-height: 1.6;
}}
.entrada-intensidade {{
  display: flex; align-items: center; gap: 0.5rem;
  margin-top: 0.5rem;
}}
.int-bar {{
  flex: 1; height: 4px; background: var(--border);
  border-radius: 50px; overflow: hidden;
}}
.int-fill {{
  height: 100%; background: var(--gradient);
  border-radius: 50px;
}}
.streak-mini {{
  display: flex; align-items: center; gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: rgba(246,173,85,0.1);
  border: 1px solid rgba(246,173,85,0.3);
  border-radius: 12px; margin-bottom: 1.5rem;
  font-size: 0.9rem; font-weight: 600;
  color: #d69e2e;
}}
</style>
</head>
<body>
<div class="topbar">
  <a href="/app/dashboard">← Dashboard</a>
  <span class="topbar-title">📓 Diário Emocional</span>
</div>

<div class="content" id="main-content">
  <!-- STREAK -->
  <div class="streak-mini" id="streak-display">
    🔥 <span id="streak-num">0</span> dias consecutivos — Continue assim!
  </div>

  <!-- NOVA ENTRADA -->
  <div class="card" style="margin-bottom:2rem">
    <h2 style="font-size:1.1rem;font-weight:700;margin-bottom:1.25rem">
      ✍️ Como você está agora?
    </h2>

    <!-- EMOÇÕES -->
    <div style="font-size:0.85rem;font-weight:600;color:var(--text2);margin-bottom:0.75rem">
      Selecione sua emoção principal:
    </div>
    <div class="emocoes-grid">
      <div class="emocao-btn" onclick="selecionarEmocao('alegria', this)">
        <span class="emocao-emoji">😄</span>Alegria
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('gratidao', this)">
        <span class="emocao-emoji">🙏</span>Gratidão
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('neutro', this)">
        <span class="emocao-emoji">😐</span>Neutro
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('ansiedade', this)">
        <span class="emocao-emoji">😰</span>Ansiedade
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('tristeza', this)">
        <span class="emocao-emoji">😔</span>Tristeza
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('raiva', this)">
        <span class="emocao-emoji">😤</span>Raiva
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('medo', this)">
        <span class="emocao-emoji">😨</span>Medo
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('serenidade', this)">
        <span class="emocao-emoji">😌</span>Calma
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('esperanca', this)">
        <span class="emocao-emoji">🌟</span>Esperança
      </div>
      <div class="emocao-btn" onclick="selecionarEmocao('cansaco', this)">
        <span class="emocao-emoji">😴</span>Cansaço
      </div>
    </div>

    <!-- INTENSIDADE -->
    <div class="intensidade-container">
      <label>Intensidade: <strong id="intensidade-valor">5</strong>/10</label>
      <input type="range" id="intensidade" min="1" max="10" value="5"
             oninput="atualizarIntensidade(this)">
      <div class="intensidade-label">
        <span>Leve</span><span>Moderado</span><span>Intenso</span>
      </div>
    </div>

    <!-- TEXTO -->
    <div class="form-group">
      <label>O que está acontecendo? (opcional)</label>
      <textarea id="texto-entrada" rows="3"
                placeholder="Descreva como você está se sentindo, o que aconteceu, pensamentos..."></textarea>
    </div>

    <!-- HUMOR GERAL -->
    <div class="form-group">
      <label>Humor geral hoje: <strong id="humor-valor">5</strong>/10</label>
      <input type="range" id="humor-geral" min="1" max="10" value="5"
             oninput="document.getElementById('humor-valor').textContent=this.value">
    </div>

    <button class="btn btn-primary btn-lg" style="width:100%;justify-content:center" onclick="salvarEntrada()">
      💾 Salvar entrada
    </button>
    <div id="save-msg" style="display:none;margin-top:1rem"></div>
  </div>

  <!-- HISTÓRICO -->
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem">
    <h2 style="font-size:1.1rem;font-weight:700">📅 Histórico</h2>
    <span id="total-entradas" style="font-size:0.85rem;color:var(--text3)"></span>
  </div>
  <div id="historico"></div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const USER_ID = localStorage.getItem('emotion_userid') || 'user';
if (!TOKEN) window.location.href = '/app/login';

let emocaoSelecionada = 'neutro';

const emocaoEmojis = {{
  alegria:'😄', gratidao:'🙏', neutro:'😐', ansiedade:'😰',
  tristeza:'😔', raiva:'😤', medo:'😨', serenidade:'😌',
  esperanca:'🌟', cansaco:'😴'
}};

function selecionarEmocao(emocao, el) {{
  emocaoSelecionada = emocao;
  document.querySelectorAll('.emocao-btn').forEach(b => b.classList.remove('selected'));
  el.classList.add('selected');
}}

function atualizarIntensidade(input) {{
  document.getElementById('intensidade-valor').textContent = input.value;
  const pct = ((input.value - 1) / 9 * 100) + '%';
  input.style.setProperty('--val', pct);
}}

async function salvarEntrada() {{
  const intensidade = document.getElementById('intensidade').value;
  const texto = document.getElementById('texto-entrada').value;
  const humor = document.getElementById('humor-geral').value;
  const msg = document.getElementById('save-msg');

  try {{
    const r = await fetch(
      `/api/v1/diario-emocional/entrada?user_id=${{USER_ID}}&emocao_principal=${{emocaoSelecionada}}&intensidade=${{intensidade}}&humor_geral=${{humor}}&texto=${{encodeURIComponent(texto || 'Sem texto')}}`,
      {{ method: 'POST', headers: {{ 'Authorization': 'Bearer ' + TOKEN }} }}
    );
    if (r.ok) {{
      msg.className = 'alert alert-success';
      msg.textContent = '✅ Entrada salva! +10 XP ganhos.';
      msg.style.display = 'block';
      document.getElementById('texto-entrada').value = '';
      document.querySelectorAll('.emocao-btn').forEach(b => b.classList.remove('selected'));
      emocaoSelecionada = 'neutro';
      setTimeout(() => {{ msg.style.display = 'none'; carregarHistorico(); }}, 2000);

      // Ganhar XP
      fetch(`/api/v1/xp/ganhar?user_id=${{USER_ID}}&acao=diario&xp=10`, {{
        method: 'POST', headers: {{ 'Authorization': 'Bearer ' + TOKEN }}
      }});
    }} else {{
      msg.className = 'alert alert-danger';
      msg.textContent = 'Erro ao salvar. Tente novamente.';
      msg.style.display = 'block';
    }}
  }} catch(e) {{
    msg.className = 'alert alert-danger';
    msg.textContent = 'Erro de conexão.';
    msg.style.display = 'block';
  }}
}}

async function carregarHistorico() {{
  try {{
    const r = await fetch(`/api/v1/diario-emocional/historico/${{USER_ID}}`, {{
      headers: {{ 'Authorization': 'Bearer ' + TOKEN }}
    }});
    if (!r.ok) return;
    const d = await r.json();
    const entradas = d.entradas || [];
    document.getElementById('total-entradas').textContent = entradas.length + ' entradas';

    const hist = document.getElementById('historico');
    if (entradas.length === 0) {{
      hist.innerHTML = '<div style="text-align:center;padding:2rem;color:var(--text3)"><div style="font-size:2rem;margin-bottom:0.5rem">📓</div><div>Nenhuma entrada ainda.<br>Comece agora!</div></div>';
      return;
    }}

    hist.innerHTML = entradas.map(e => `
      <div class="entrada-card">
        <div class="entrada-header">
          <div class="entrada-emocao">
            ${{emocaoEmojis[e.emocao_principal] || '😐'}}
            ${{(e.emocao_principal || 'neutro').charAt(0).toUpperCase() + (e.emocao_principal || '').slice(1)}}
          </div>
          <div class="entrada-data">${{new Date(e.criado_em || Date.now()).toLocaleDateString('pt-BR')}}</div>
        </div>
        ${{e.texto ? `<div class="entrada-texto">${{e.texto}}</div>` : ''}}
        <div class="entrada-intensidade">
          <span style="font-size:0.75rem;color:var(--text3)">Intensidade:</span>
          <div class="int-bar"><div class="int-fill" style="width:${{(e.intensidade||5)*10}}%"></div></div>
          <span style="font-size:0.75rem;color:var(--text3)">${{e.intensidade||5}}/10</span>
        </div>
      </div>
    `).join('');
  }} catch(e) {{}}
}}

carregarHistorico();
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 5. PLANOS.HTML
# ══════════════════════════════════════════════════
planos_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Planos e Preços</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
{CSS_BASE}
body {{ min-height: 100vh; }}
.topbar {{
  background: white; border-bottom: 1px solid var(--border);
  padding: 1rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}}
.topbar a {{ text-decoration: none; }}
.content {{ max-width: 1000px; margin: 0 auto; padding: 3rem 2rem; }}
.hero {{
  text-align: center; margin-bottom: 3rem;
}}
.hero h1 {{
  font-size: clamp(2rem, 5vw, 3rem);
  font-weight: 900; line-height: 1.2;
  margin-bottom: 1rem;
}}
.hero p {{
  font-size: 1.1rem; color: var(--text2);
  max-width: 500px; margin: 0 auto;
}}
.toggle-container {{
  display: flex; align-items: center; gap: 1rem;
  justify-content: center; margin-bottom: 3rem;
}}
.toggle {{
  position: relative; width: 52px; height: 28px;
  background: var(--border); border-radius: 50px;
  cursor: pointer; transition: background 0.3s;
}}
.toggle.on {{ background: var(--gradient); }}
.toggle-knob {{
  position: absolute; top: 3px; left: 3px;
  width: 22px; height: 22px; background: white;
  border-radius: 50%; transition: left 0.3s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
}}
.toggle.on .toggle-knob {{ left: 27px; }}
.toggle-label {{ font-size: 0.9rem; font-weight: 600; }}
.desconto-badge {{
  background: rgba(56,161,105,0.1); color: var(--accent);
  padding: 0.2rem 0.6rem; border-radius: 50px;
  font-size: 0.75rem; font-weight: 700;
}}
.plans-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem; align-items: start;
}}
.plan-card {{
  background: white; border: 2px solid var(--border);
  border-radius: 24px; padding: 2rem;
  position: relative; transition: all 0.2s;
}}
.plan-card:hover {{ box-shadow: var(--shadow-lg); transform: translateY(-4px); }}
.plan-card.popular {{
  border-color: var(--primary);
  box-shadow: var(--shadow-lg);
}}
.popular-tag {{
  position: absolute; top: -14px; left: 50%;
  transform: translateX(-50%);
  background: var(--gradient); color: white;
  padding: 0.3rem 1.5rem; border-radius: 50px;
  font-size: 0.75rem; font-weight: 700;
}}
.plan-name {{
  font-size: 1rem; font-weight: 700;
  color: var(--text2); margin-bottom: 0.5rem;
}}
.plan-price {{
  font-size: 3rem; font-weight: 900;
  line-height: 1; letter-spacing: -0.02em;
}}
.plan-price.gradient {{
  background: var(--gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.plan-period {{ font-size: 1rem; font-weight: 400; color: var(--text3); }}
.plan-desc {{
  font-size: 0.85rem; color: var(--text3);
  margin: 0.5rem 0 1.5rem;
}}
.plan-features {{ list-style: none; margin-bottom: 2rem; }}
.plan-features li {{
  display: flex; align-items: flex-start; gap: 0.6rem;
  padding: 0.5rem 0; font-size: 0.9rem;
  color: var(--text2); border-bottom: 1px solid var(--bg);
}}
.plan-features li:last-child {{ border: none; }}
.check-green {{ color: var(--accent); font-weight: 700; flex-shrink: 0; }}
.check-gray {{ color: var(--text3); flex-shrink: 0; }}
.guarantee {{
  text-align: center; margin-top: 3rem;
  padding: 2rem; background: white;
  border-radius: var(--radius);
  border: 1px solid var(--border);
}}
.guarantee h3 {{ font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }}
.guarantee p {{ color: var(--text2); font-size: 0.9rem; }}
.cupom-area {{
  text-align: center; margin-top: 2rem;
  padding: 1.5rem; background: rgba(102,126,234,0.05);
  border-radius: var(--radius);
  border: 1px dashed rgba(102,126,234,0.3);
}}
.cupom-input {{
  display: flex; gap: 0.5rem; max-width: 350px; margin: 0.75rem auto 0;
}}
.faq-mini {{ margin-top: 3rem; }}
.faq-mini h2 {{
  font-size: 1.5rem; font-weight: 800;
  text-align: center; margin-bottom: 1.5rem;
}}
.faq-mini-item {{
  background: white; border: 1px solid var(--border);
  border-radius: 12px; margin-bottom: 0.75rem; overflow: hidden;
}}
.faq-mini-q {{
  padding: 1rem 1.25rem; font-weight: 600;
  cursor: pointer; display: flex;
  justify-content: space-between; align-items: center;
  font-size: 0.95rem;
}}
.faq-mini-a {{
  padding: 0 1.25rem 1rem;
  font-size: 0.9rem; color: var(--text2);
  display: none; line-height: 1.6;
}}
.faq-mini-item.open .faq-mini-a {{ display: block; }}
</style>
</head>
<body>
<div class="topbar">
  <a href="/" style="font-size:1.2rem;font-weight:800;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent">
    🧠 EmotionAI
  </a>
  <div style="display:flex;gap:0.75rem">
    <a href="/app/login" class="btn btn-outline">Entrar</a>
    <a href="/app/login" class="btn btn-primary">Começar grátis</a>
  </div>
</div>

<div class="content" id="main-content">
  <div class="hero">
    <span style="display:inline-block;background:rgba(102,126,234,0.1);color:var(--primary);padding:0.3rem 1rem;border-radius:50px;font-size:0.8rem;font-weight:700;margin-bottom:1rem">
      💰 Preços simples e transparentes
    </span>
    <h1>Invista na sua<br><span style="background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent">prática clínica</span></h1>
    <p>Comece grátis. Faça upgrade quando precisar. Sem surpresas.</p>
  </div>

  <!-- TOGGLE MENSAL/ANUAL -->
  <div class="toggle-container">
    <span class="toggle-label">Mensal</span>
    <div class="toggle" id="toggle" onclick="togglePeriodo()">
      <div class="toggle-knob"></div>
    </div>
    <span class="toggle-label">
      Anual <span class="desconto-badge">-30% OFF</span>
    </span>
  </div>

  <!-- PLANOS -->
  <div class="plans-grid">
    <!-- FREE -->
    <div class="plan-card">
      <div class="plan-name">Gratuito</div>
      <div class="plan-price">R$ 0</div>
      <div class="plan-desc">Para experimentar a plataforma</div>
      <ul class="plan-features">
        <li><span class="check-green">✓</span> 5 avaliações por mês</li>
        <li><span class="check-green">✓</span> 20 mensagens de IA por mês</li>
        <li><span class="check-green">✓</span> Diário emocional</li>
        <li><span class="check-green">✓</span> Dashboard básico</li>
        <li><span class="check-green">✓</span> 1 paciente ativo</li>
        <li><span class="check-gray">–</span> Prontuário completo</li>
        <li><span class="check-gray">–</span> Agendamento online</li>
        <li><span class="check-gray">–</span> Relatórios PDF</li>
      </ul>
      <a href="/app/login" class="btn btn-outline" style="width:100%;justify-content:center">
        Começar grátis
      </a>
    </div>

    <!-- PRO -->
    <div class="plan-card popular">
      <div class="popular-tag">⭐ Mais popular</div>
      <div class="plan-name">Pro</div>
      <div class="plan-price gradient" id="price-pro">R$ 29,90</div>
      <div class="plan-period">/mês <span id="period-pro" style="font-size:0.8rem;color:var(--text3)"></span></div>
      <div class="plan-desc">Para psicólogos ativos e produtivos</div>
      <ul class="plan-features">
        <li><span class="check-green">✓</span> <strong>Avaliações ilimitadas</strong></li>
        <li><span class="check-green">✓</span> <strong>Chat IA ilimitado</strong></li>
        <li><span class="check-green">✓</span> Prontuário digital completo</li>
        <li><span class="check-green">✓</span> Agendamento online</li>
        <li><span class="check-green">✓</span> Relatórios PDF</li>
        <li><span class="check-green">✓</span> Pacientes ilimitados</li>
        <li><span class="check-green">✓</span> Suporte prioritário</li>
        <li><span class="check-green">✓</span> Exportação de dados</li>
      </ul>
      <a href="/checkout" class="btn btn-primary" style="width:100%;justify-content:center">
        Assinar Pro →
      </a>
    </div>

    <!-- CLINICA -->
    <div class="plan-card">
      <div class="plan-name">Clínica</div>
      <div class="plan-price" id="price-clinica">R$ 99,90</div>
      <div class="plan-period">/mês <span id="period-clinica"></span></div>
      <div class="plan-desc">Para clínicas e equipes de saúde</div>
      <ul class="plan-features">
        <li><span class="check-green">✓</span> Tudo do Pro</li>
        <li><span class="check-green">✓</span> <strong>Até 10 terapeutas</strong></li>
        <li><span class="check-green">✓</span> Gestão multi-clínica</li>
        <li><span class="check-green">✓</span> API completa</li>
        <li><span class="check-green">✓</span> White label</li>
        <li><span class="check-green">✓</span> Suporte 24/7</li>
        <li><span class="check-green">✓</span> Onboarding dedicado</li>
        <li><span class="check-green">✓</span> SLA garantido</li>
      </ul>
      <a href="/contato" class="btn btn-outline" style="width:100%;justify-content:center">
        Falar com vendas
      </a>
    </div>
  </div>

  <!-- CUPOM -->
  <div class="cupom-area">
    <div style="font-size:0.9rem;font-weight:600">🎟️ Tem um cupom de desconto?</div>
    <div class="cupom-input">
      <input type="text" id="cupom-input" placeholder="BEMVINDO" style="border-radius:12px">
      <button class="btn btn-primary" onclick="aplicarCupom()">Aplicar</button>
    </div>
    <div id="cupom-msg" style="margin-top:0.5rem;font-size:0.85rem"></div>
    <div style="margin-top:0.75rem;font-size:0.8rem;color:var(--text3)">
      Cupons: BEMVINDO (50% off) · PSICOLOGO (30% off) · ALBERT10 (R$10 off)
    </div>
  </div>

  <!-- GARANTIA -->
  <div class="guarantee">
    <div style="font-size:2rem;margin-bottom:0.5rem">🛡️</div>
    <h3>Garantia de 30 dias</h3>
    <p>Se não ficar satisfeito nos primeiros 30 dias, devolvemos 100% do valor pago. Sem perguntas, sem burocracia.</p>
  </div>

  <!-- FAQ MINI -->
  <div class="faq-mini">
    <h2>Dúvidas sobre os planos</h2>
    <div class="faq-mini-item">
      <div class="faq-mini-q" onclick="this.parentElement.classList.toggle('open')">
        Posso mudar de plano a qualquer momento? <span>+</span>
      </div>
      <div class="faq-mini-a">
        Sim! Faça upgrade ou downgrade quando quiser pelo painel de configurações.
        A diferença de valor é calculada proporcionalmente.
      </div>
    </div>
    <div class="faq-mini-item">
      <div class="faq-mini-q" onclick="this.parentElement.classList.toggle('open')">
        Quais formas de pagamento são aceitas? <span>+</span>
      </div>
      <div class="faq-mini-a">
        Cartão de crédito (Visa, Mastercard, Elo), PIX e boleto bancário.
        Todos os pagamentos são processados com segurança via Stripe.
      </div>
    </div>
    <div class="faq-mini-item">
      <div class="faq-mini-q" onclick="this.parentElement.classList.toggle('open')">
        O plano gratuito tem limite de tempo? <span>+</span>
      </div>
      <div class="faq-mini-a">
        Não! O plano gratuito é para sempre. Sem trials, sem pegadinhas.
        Você só faz upgrade quando precisar de mais recursos.
      </div>
    </div>
  </div>
</div>

<script>
let isAnual = false;

function togglePeriodo() {{
  isAnual = !isAnual;
  const toggle = document.getElementById('toggle');
  toggle.classList.toggle('on', isAnual);

  if (isAnual) {{
    document.getElementById('price-pro').textContent = 'R$ 20,90';
    document.getElementById('period-pro').textContent = '· cobrado anualmente';
    document.getElementById('price-clinica').textContent = 'R$ 69,90';
    document.getElementById('period-clinica').textContent = '· cobrado anualmente';
  }} else {{
    document.getElementById('price-pro').textContent = 'R$ 29,90';
    document.getElementById('period-pro').textContent = '';
    document.getElementById('price-clinica').textContent = 'R$ 99,90';
    document.getElementById('period-clinica').textContent = '';
  }}
}}

async function aplicarCupom() {{
  const codigo = document.getElementById('cupom-input').value.trim().toUpperCase();
  if (!codigo) return;
  const msg = document.getElementById('cupom-msg');
  const TOKEN = localStorage.getItem('emotion_token');
  try {{
    const r = await fetch('/api/v1/cupons/usar/' + codigo, {{
      method: 'POST',
      headers: {{'Content-Type':'application/json','Authorization':'Bearer '+TOKEN}}
    }});
    const d = await r.json();
    if (r.ok && d.ok) {{
      msg.style.color = 'var(--accent)';
      msg.textContent = '✅ Cupom aplicado! ' + d.desconto_aplicado + (d.tipo==='percentual'?'% de desconto':' reais de desconto');
    }} else {{
      msg.style.color = 'var(--danger)';
      msg.textContent = '❌ Cupom inválido ou expirado';
    }}
  }} catch(e) {{
    msg.style.color = 'var(--danger)';
    msg.textContent = 'Erro ao aplicar cupom';
  }}
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# 6. AVALIACAO.HTML
# ══════════════════════════════════════════════════
avaliacao_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI — Avaliações Psicológicas</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
{CSS_BASE}
.topbar {{
  background: white; border-bottom: 1px solid var(--border);
  padding: 1rem 2rem;
  display: flex; align-items: center; gap: 1rem;
  position: sticky; top: 0; z-index: 40;
}}
.topbar a {{ color: var(--text2); text-decoration: none; font-size: 0.9rem; }}
.content {{ max-width: 720px; margin: 0 auto; padding: 2rem; }}
.escalas-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem; margin-bottom: 2rem;
}}
.escala-card {{
  background: white; border: 2px solid var(--border);
  border-radius: 20px; padding: 1.5rem;
  cursor: pointer; transition: all 0.2s;
  text-align: center;
}}
.escala-card:hover {{
  border-color: var(--primary);
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}}
.escala-card.active {{
  border-color: var(--primary);
  background: rgba(102,126,234,0.03);
}}
.escala-emoji {{ font-size: 2.5rem; margin-bottom: 0.75rem; }}
.escala-nome {{ font-size: 1rem; font-weight: 700; margin-bottom: 0.25rem; }}
.escala-desc {{ font-size: 0.8rem; color: var(--text3); }}
.escala-perguntas {{ font-size: 0.75rem; color: var(--primary); font-weight: 600; margin-top: 0.5rem; }}
.quiz-container {{ display: none; }}
.quiz-container.active {{ display: block; }}
.progress-container {{ margin-bottom: 2rem; }}
.progress-label {{
  display: flex; justify-content: space-between;
  font-size: 0.85rem; margin-bottom: 0.5rem;
}}
.progress-bar-container {{
  background: var(--border); border-radius: 50px;
  height: 8px; overflow: hidden;
}}
.progress-bar {{
  height: 100%; background: var(--gradient);
  border-radius: 50px; transition: width 0.4s ease;
}}
.question-card {{
  background: white; border: 1px solid var(--border);
  border-radius: 20px; padding: 2rem;
  margin-bottom: 1.5rem;
}}
.question-num {{
  font-size: 0.8rem; font-weight: 700;
  color: var(--primary); margin-bottom: 0.75rem;
}}
.question-text {{
  font-size: 1.1rem; font-weight: 600;
  line-height: 1.5; margin-bottom: 1.5rem;
}}
.opcoes-grid {{
  display: grid; grid-template-columns: 1fr;
  gap: 0.5rem;
}}
.opcao-btn {{
  padding: 0.875rem 1.25rem;
  border: 2px solid var(--border); border-radius: 12px;
  background: white; cursor: pointer;
  text-align: left; font-size: 0.9rem;
  color: var(--text2); transition: all 0.2s;
  display: flex; align-items: center; gap: 0.75rem;
}}
.opcao-btn:hover {{
  border-color: var(--primary);
  background: rgba(102,126,234,0.05);
}}
.opcao-btn.selected {{
  border-color: var(--primary);
  background: rgba(102,126,234,0.1);
  color: var(--primary); font-weight: 600;
}}
.opcao-num {{
  width: 28px; height: 28px; border-radius: 50%;
  background: var(--border); display: flex;
  align-items: center; justify-content: center;
  font-size: 0.8rem; font-weight: 700; flex-shrink: 0;
  transition: all 0.2s;
}}
.opcao-btn.selected .opcao-num {{
  background: var(--primary); color: white;
}}
.resultado-card {{
  display: none; background: white;
  border: 1px solid var(--border);
  border-radius: 20px; padding: 2rem;
  text-align: center;
}}
.resultado-card.show {{ display: block; animation: fadeUp 0.5s ease; }}
.resultado-score {{
  font-size: 4rem; font-weight: 900;
  background: var(--gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1;
}}
.resultado-nivel {{
  font-size: 1.3rem; font-weight: 700;
  margin: 0.5rem 0;
}}
.resultado-desc {{
  font-size: 0.95rem; color: var(--text2);
  max-width: 400px; margin: 1rem auto;
  line-height: 1.6;
}}
.nivel-indicator {{
  display: flex; gap: 0.3rem; justify-content: center;
  margin: 1.5rem 0;
}}
.nivel-dot {{
  width: 12px; height: 12px; border-radius: 50%;
  background: var(--border);
}}
.nivel-dot.active {{ background: var(--gradient); }}
</style>
</head>
<body>
<div class="topbar">
  <a href="/app/dashboard">← Dashboard</a>
  <span style="font-size:1.1rem;font-weight:700;margin-left:0.5rem">📊 Avaliações Psicológicas</span>
</div>

<div class="content" id="main-content">
  <!-- SELEÇÃO DE ESCALA -->
  <div id="selecao">
    <div style="margin-bottom:1.5rem">
      <h2 style="font-size:1.3rem;font-weight:800;margin-bottom:0.25rem">
        Escolha uma avaliação
      </h2>
      <p style="color:var(--text3);font-size:0.9rem">
        Escalas psicológicas validadas cientificamente
      </p>
    </div>
    <div class="escalas-grid">
      <div class="escala-card" onclick="iniciarEscala('phq9')">
        <div class="escala-emoji">😔</div>
        <div class="escala-nome">PHQ-9</div>
        <div class="escala-desc">Avaliação de depressão</div>
        <div class="escala-perguntas">9 perguntas · ~3 min</div>
      </div>
      <div class="escala-card" onclick="iniciarEscala('gad7')">
        <div class="escala-emoji">😰</div>
        <div class="escala-nome">GAD-7</div>
        <div class="escala-desc">Avaliação de ansiedade</div>
        <div class="escala-perguntas">7 perguntas · ~2 min</div>
      </div>
      <div class="escala-card" onclick="iniciarEscala('pss')">
        <div class="escala-emoji">😤</div>
        <div class="escala-nome">PSS-10</div>
        <div class="escala-desc">Nível de estresse</div>
        <div class="escala-perguntas">10 perguntas · ~3 min</div>
      </div>
      <div class="escala-card" onclick="iniciarEscala('bigfive')">
        <div class="escala-emoji">🌟</div>
        <div class="escala-nome">Big Five</div>
        <div class="escala-desc">Traços de personalidade</div>
        <div class="escala-perguntas">15 perguntas · ~5 min</div>
      </div>
    </div>
  </div>

  <!-- QUIZ -->
  <div class="quiz-container" id="quiz">
    <div class="progress-container">
      <div class="progress-label">
        <span id="q-label">Pergunta 1 de 9</span>
        <span id="q-escala" style="color:var(--primary);font-weight:600">PHQ-9</span>
      </div>
      <div class="progress-bar-container">
        <div class="progress-bar" id="progress-bar" style="width:0%"></div>
      </div>
    </div>

    <div id="pergunta-container"></div>

    <div style="display:flex;gap:0.75rem;margin-top:1rem">
      <button class="btn btn-outline" id="btn-anterior" onclick="anterior()" style="display:none">
        ← Anterior
      </button>
      <button class="btn btn-primary" id="btn-proximo" onclick="proximo()" style="margin-left:auto" disabled>
        Próxima →
      </button>
    </div>
  </div>

  <!-- RESULTADO -->
  <div class="resultado-card" id="resultado">
    <div style="font-size:3rem;margin-bottom:1rem" id="resultado-emoji">📊</div>
    <div style="font-size:0.85rem;color:var(--text3);margin-bottom:0.5rem" id="resultado-escala">PHQ-9</div>
    <div class="resultado-score" id="resultado-score">0</div>
    <div class="resultado-nivel" id="resultado-nivel">Carregando...</div>
    <div class="nivel-indicator" id="nivel-dots"></div>
    <div class="resultado-desc" id="resultado-desc"></div>
    <div style="display:flex;gap:0.75rem;justify-content:center;margin-top:2rem;flex-wrap:wrap">
      <button class="btn btn-outline" onclick="reiniciar()">
        🔄 Fazer outra avaliação
      </button>
      <a href="/app/chat" class="btn btn-primary">
        💬 Falar com IA sobre resultado
      </a>
    </div>
    <div style="margin-top:1.5rem;padding:1rem;background:var(--bg);border-radius:12px;font-size:0.8rem;color:var(--text3)">
      ⚠️ Esta avaliação é apenas informativa e não substitui diagnóstico profissional.
      Consulte um psicólogo ou psiquiatra.
    </div>
  </div>
</div>

<script>
const TOKEN = localStorage.getItem('emotion_token');
const USER_ID = localStorage.getItem('emotion_userid') || 'user';
if (!TOKEN) window.location.href = '/app/login';

const ESCALAS = {{
  phq9: {{
    nome: 'PHQ-9', emoji: '😔',
    instrucao: 'Nas últimas 2 semanas, com que frequência você foi incomodado pelos seguintes problemas?',
    opcoes: ['Nenhuma vez (0)', 'Menos de 1 semana (1)', 'Mais da metade dos dias (2)', 'Quase todos os dias (3)'],
    perguntas: [
      'Pouco interesse ou prazer em fazer as coisas',
      'Se sentiu para baixo, deprimido ou sem esperança',
      'Dificuldade para adormecer ou continuar dormindo, ou dormiu demais',
      'Se sentiu cansado ou com pouca energia',
      'Falta de apetite ou comeu demais',
      'Se sentiu mal consigo mesmo — ou achou que é um fracasso ou que decepcionou sua família ou a você mesmo',
      'Dificuldade para se concentrar nas coisas',
      'Se moveu ou falou tão devagar que outras pessoas poderiam ter notado; ou ao contrário, ficou tão agitado ou inquieto que você ficava andando de um lado para outro',
      'Pensou em se machucar ou que seria melhor estar morto'
    ],
    calcular: (respostas) => {{
      const score = respostas.reduce((a, b) => a + b, 0);
      const niveis = [
        [0, 4, 'Sem depressão significativa', '😊', 'Seu resultado indica ausência de sintomas depressivos significativos. Continue cuidando da sua saúde mental!'],
        [5, 9, 'Depressão leve', '😐', 'Sintomas leves de depressão detectados. Pratique autocuidado e considere conversar com um profissional.'],
        [10, 14, 'Depressão moderada', '😔', 'Sintomas moderados de depressão. Recomendamos consultar um psicólogo ou psiquiatra.'],
        [15, 19, 'Depressão moderadamente grave', '😟', 'Sintomas significativos de depressão. É importante buscar ajuda profissional em breve.'],
        [20, 27, 'Depressão grave', '😢', 'Sintomas graves de depressão. Procure ajuda profissional o mais rápido possível. CVV: 188']
      ];
      const nivel = niveis.find(n => score >= n[0] && score <= n[1]) || niveis[0];
      return {{ score, max: 27, nivel: nivel[2], emoji: nivel[3], desc: nivel[4], dots: 5, dotAtivo: niveis.indexOf(nivel) }};
    }}
  }},
  gad7: {{
    nome: 'GAD-7', emoji: '😰',
    instrucao: 'Nas últimas 2 semanas, com que frequência você foi incomodado pelos seguintes problemas?',
    opcoes: ['Nunca (0)', 'Vários dias (1)', 'Mais da metade dos dias (2)', 'Quase todos os dias (3)'],
    perguntas: [
      'Sentir-se nervoso, ansioso ou muito tenso',
      'Não ser capaz de impedir ou de controlar as preocupações',
      'Preocupar-se muito com diversas coisas',
      'Dificuldade para relaxar',
      'Ficar tão agitado que se torna difícil permanecer sentado quieto',
      'Ficar facilmente aborrecido ou irritável',
      'Sentir medo como se algo horrível fosse acontecer'
    ],
    calcular: (respostas) => {{
      const score = respostas.reduce((a, b) => a + b, 0);
      const niveis = [
        [0, 4, 'Ansiedade mínima', '😊', 'Sem ansiedade significativa. Continue praticando técnicas de relaxamento para manter esse equilíbrio!'],
        [5, 9, 'Ansiedade leve', '😐', 'Ansiedade leve detectada. Técnicas de respiração e meditação podem ajudar.'],
        [10, 14, 'Ansiedade moderada', '😰', 'Ansiedade moderada. Considere buscar apoio psicológico para lidar com esses sintomas.'],
        [15, 21, 'Ansiedade grave', '😨', 'Ansiedade grave. É importante buscar ajuda profissional em breve. CVV: 188']
      ];
      const nivel = niveis.find(n => score >= n[0] && score <= n[1]) || niveis[0];
      return {{ score, max: 21, nivel: nivel[2], emoji: nivel[3], desc: nivel[4], dots: 4, dotAtivo: niveis.indexOf(nivel) }};
    }}
  }},
  pss: {{
    nome: 'PSS-10', emoji: '😤',
    instrucao: 'No último mês, com que frequência você...',
    opcoes: ['Nunca (0)', 'Quase nunca (1)', 'Às vezes (2)', 'Com alguma frequência (3)', 'Muito frequente (4)'],
    perguntas: [
      'Ficou chateado por algo inesperado?',
      'Sentiu dificuldade de controlar coisas importantes?',
      'Se sentiu nervoso e estressado?',
      'Sentiu confiança de lidar com problemas pessoais? (invertida)',
      'As coisas correram como queria? (invertida)',
      'Sentiu que não aguentava tudo que tinha que fazer?',
      'Conseguiu controlar as irritações da vida? (invertida)',
      'Sentiu estar por cima das dificuldades? (invertida)',
      'Ficou bravo por coisas fora do seu controle?',
      'Sentiu que dificuldades se acumulavam a ponto de não conseguir superá-las?'
    ],
    calcular: (respostas) => {{
      const reversos = new Set([3, 4, 6, 7]);
      const score = respostas.reduce((acc, v, i) => acc + (reversos.has(i) ? 4 - v : v), 0);
      const niveis = [
        [0, 13, 'Estresse baixo', '😊', 'Nível saudável de estresse. Continue praticando hábitos de autocuidado!'],
        [14, 26, 'Estresse moderado', '😐', 'Estresse moderado detectado. Considere técnicas de manejo do estresse.'],
        [27, 40, 'Estresse alto', '😤', 'Nível alto de estresse. Busque apoio profissional e pratique técnicas de relaxamento.']
      ];
      const nivel = niveis.find(n => score >= n[0] && score <= n[1]) || niveis[0];
      return {{ score, max: 40, nivel: nivel[2], emoji: nivel[3], desc: nivel[4], dots: 3, dotAtivo: niveis.indexOf(nivel) }};
    }}
  }},
  bigfive: {{
    nome: 'Big Five', emoji: '🌟',
    instrucao: 'Indique o quanto cada afirmação descreve você:',
    opcoes: ['Discordo totalmente (1)', 'Discordo (2)', 'Neutro (3)', 'Concordo (4)', 'Concordo totalmente (5)'],
    perguntas: [
      'Gosto de conhecer pessoas novas e fazer amigos',
      'Costumo me organizar e planejar antes de agir',
      'Fico ansioso ou nervoso facilmente',
      'Tenho uma imaginação ativa e criativa',
      'Sou geralmente gentil e prestativo',
      'Prefiro ambientes movimentados e sociais',
      'Sou muito caprichoso e detalhista no meu trabalho',
      'Meu humor muda com frequência',
      'Aprecio arte, música ou literatura',
      'Evito conflitos e procuro harmonia',
      'Gosto de ser o centro das atenções',
      'Cumpro prazos e responsabilidades',
      'Me estresso facilmente',
      'Gosto de aprender coisas novas',
      'Me preocupo com o bem-estar dos outros'
    ],
    calcular: (respostas) => {{
      const ext = (respostas[0] + respostas[5] + respostas[10]) / 3;
      const con = (respostas[1] + respostas[6] + respostas[11]) / 3;
      const neu = (respostas[2] + respostas[7] + respostas[12]) / 3;
      const abe = (respostas[3] + respostas[8] + respostas[13]) / 3;
      const ama = (respostas[4] + respostas[9] + respostas[14]) / 3;
      const maior = Math.max(ext, con, neu, abe, ama);
      const nomes = {{ [ext]:'Extroversão', [con]:'Conscienciosidade', [neu]:'Neuroticismo', [abe]:'Abertura', [ama]:'Amabilidade' }};
      return {{
        score: Math.round(maior * 20),
        max: 100,
        nivel: 'Traço dominante: ' + (nomes[maior] || 'Equilibrado'),
        emoji: '🌟',
        desc: `Extroversão: ${{ext.toFixed(1)}}/5 · Conscienciosidade: ${{con.toFixed(1)}}/5 · Neuroticismo: ${{neu.toFixed(1)}}/5 · Abertura: ${{abe.toFixed(1)}}/5 · Amabilidade: ${{ama.toFixed(1)}}/5`,
        dots: 5,
        dotAtivo: 2
      }};
    }}
  }}
}};

let escalaSelecionada = null;
let perguntaAtual = 0;
let respostas = [];

function iniciarEscala(nome) {{
  escalaSelecionada = ESCALAS[nome];
  perguntaAtual = 0;
  respostas = new Array(escalaSelecionada.perguntas.length).fill(-1);
  document.getElementById('selecao').style.display = 'none';
  document.getElementById('quiz').classList.add('active');
  document.getElementById('resultado').classList.remove('show');
  document.getElementById('q-escala').textContent = escalaSelecionada.nome;
  mostrarPergunta();
}}

function mostrarPergunta() {{
  const total = escalaSelecionada.perguntas.length;
  const pct = ((perguntaAtual + 1) / total * 100);
  document.getElementById('progress-bar').style.width = pct + '%';
  document.getElementById('q-label').textContent = `Pergunta ${{perguntaAtual + 1}} de ${{total}}`;
  document.getElementById('btn-anterior').style.display = perguntaAtual > 0 ? 'block' : 'none';
  document.getElementById('btn-proximo').disabled = respostas[perguntaAtual] === -1;

  const container = document.getElementById('pergunta-container');
  const letras = 'ABCDE';
  container.innerHTML = `
    <div class="question-card">
      <div class="question-num">PERGUNTA ${{perguntaAtual + 1}}</div>
      <div class="question-text">${{escalaSelecionada.instrucao}}<br><br>${{escalaSelecionada.perguntas[perguntaAtual]}}</div>
      <div class="opcoes-grid">
        ${{escalaSelecionada.opcoes.map((op, i) => `
          <button class="opcao-btn ${{respostas[perguntaAtual] === i ? 'selected' : ''}}"
                  onclick="selecionarOpcao(${{i}})">
            <div class="opcao-num">${{letras[i]}}</div>
            ${{op}}
          </button>
        `).join('')}}
      </div>
    </div>
  `;

  const isUltima = perguntaAtual === total - 1;
  document.getElementById('btn-proximo').textContent = isUltima ? '✅ Ver resultado' : 'Próxima →';
}}

function selecionarOpcao(i) {{
  respostas[perguntaAtual] = i;
  document.getElementById('btn-proximo').disabled = false;
  mostrarPergunta();
}}

function proximo() {{
  if (perguntaAtual < escalaSelecionada.perguntas.length - 1) {{
    perguntaAtual++;
    mostrarPergunta();
  }} else {{
    mostrarResultado();
  }}
}}

function anterior() {{
  if (perguntaAtual > 0) {{
    perguntaAtual--;
    mostrarPergunta();
  }}
}}

async function mostrarResultado() {{
  const resultado = escalaSelecionada.calcular(respostas);
  document.getElementById('quiz').classList.remove('active');
  const card = document.getElementById('resultado');
  card.classList.add('show');

  document.getElementById('resultado-emoji').textContent = resultado.emoji;
  document.getElementById('resultado-escala').textContent = escalaSelecionada.nome;
  document.getElementById('resultado-score').textContent = resultado.score + '/' + resultado.max;
  document.getElementById('resultado-nivel').textContent = resultado.nivel;
  document.getElementById('resultado-desc').textContent = resultado.desc;

  // Dots
  const dots = document.getElementById('nivel-dots');
  dots.innerHTML = Array(resultado.dots).fill(0).map((_, i) =>
    `<div class="nivel-dot ${{i === resultado.dotAtivo ? 'active' : ''}}"></div>`
  ).join('');

  // Salvar via API
  try {{
    const endpoint = escalaSelecionada.nome === 'PHQ-9' ? '/api/v1/phq9/calcular' :
                     escalaSelecionada.nome === 'GAD-7' ? '/api/v1/gad7/calcular' :
                     escalaSelecionada.nome === 'PSS-10' ? '/api/v1/pss/calcular' : null;
    if (endpoint) {{
      await fetch(endpoint, {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + TOKEN }},
        body: JSON.stringify(respostas)
      }});
    }}
    // XP
    await fetch(`/api/v1/xp/ganhar?user_id=${{USER_ID}}&acao=avaliacao&xp=20`, {{
      method: 'POST', headers: {{ 'Authorization': 'Bearer ' + TOKEN }}
    }});
  }} catch(e) {{}}
}}

function reiniciar() {{
  document.getElementById('selecao').style.display = 'block';
  document.getElementById('quiz').classList.remove('active');
  document.getElementById('resultado').classList.remove('show');
  escalaSelecionada = null;
  perguntaAtual = 0;
  respostas = [];
}}
</script>
</body>
</html>"""

# ══════════════════════════════════════════════════
# SALVAR TODOS OS ARQUIVOS
# ══════════════════════════════════════════════════
arquivos = {
    "templates/login.html": login_html,
    "templates/dashboard.html": dashboard_html,
    "templates/chat_ia.html": chat_html,
    "templates/diario.html": diario_html,
    "templates/planos.html": planos_html,
    "templates/avaliacao.html": avaliacao_html,
}

print("Criando páginas...")
for path, content in arquivos.items():
    Path(path).write_text(content, encoding="utf-8")
    kb = len(content) / 1024
    print(f"  ✅ {path}: {kb:.0f}KB")

print(f"\n✅ {len(arquivos)} páginas criadas com sucesso!")
print("Próximo: git add . && git commit && git push")
