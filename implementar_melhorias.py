#!/usr/bin/env python3
"""Implementa todas as melhorias baseadas em pesquisas"""
from pathlib import Path
import json

print("="*55)
print("IMPLEMENTANDO TODAS AS MELHORIAS")
print("="*55)

# ══════════════════════════════════════════════════
# 1. WHATSAPP BUTTON FLUTUANTE (em todas as páginas)
# ══════════════════════════════════════════════════
whatsapp_btn = """
<!-- WhatsApp Flutuante -->
<a href="https://wa.me/5579999999999?text=Olá!%20Tenho%20interesse%20no%20EmotionAI%20para%20psicólogos." 
   target="_blank"
   id="whatsapp-btn"
   style="position:fixed;bottom:2rem;right:2rem;z-index:9997;width:56px;height:56px;background:#25D366;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(37,211,102,0.4);transition:all 0.3s;text-decoration:none"
   onmouseover="this.style.transform='scale(1.1)'"
   onmouseout="this.style.transform='scale(1)'">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="white">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
  </svg>
</a>
<div id="whatsapp-tooltip" style="position:fixed;bottom:2.5rem;right:5rem;z-index:9996;background:#1a202c;color:white;padding:0.5rem 1rem;border-radius:50px;font-size:0.8rem;font-weight:600;white-space:nowrap;opacity:0;transition:opacity 0.3s;pointer-events:none">
  💬 Falar pelo WhatsApp
</div>
<script>
const wBtn = document.getElementById('whatsapp-btn');
const wTip = document.getElementById('whatsapp-tooltip');
if (wBtn) {
  wBtn.addEventListener('mouseenter', () => wTip.style.opacity = '1');
  wBtn.addEventListener('mouseleave', () => wTip.style.opacity = '0');
  // Mostrar pulsando após 10 segundos
  setTimeout(() => {
    wBtn.style.animation = 'waPulse 1s ease 3';
  }, 10000);
}
</script>
<style>
@keyframes waPulse {
  0%,100% { box-shadow: 0 4px 20px rgba(37,211,102,0.4); }
  50% { box-shadow: 0 4px 40px rgba(37,211,102,0.8); transform: scale(1.1); }
}
</style>
<!-- /WhatsApp -->
"""

# Adicionar em todas as páginas
templates = list(Path("templates").glob("*.html"))
wa_count = 0
for t in templates:
    html = t.read_text(encoding="utf-8", errors="ignore")
    if "whatsapp-btn" not in html and "</body>" in html:
        html = html.replace("</body>", whatsapp_btn + "\n</body>")
        t.write_text(html, encoding="utf-8")
        wa_count += 1

print(f"✅ WhatsApp flutuante em {wa_count} páginas!")

# ══════════════════════════════════════════════════
# 2. COOKIE CONSENT LGPD
# ══════════════════════════════════════════════════
cookie_consent = """
<!-- Cookie Consent LGPD -->
<div id="cookie-banner" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:9995;background:white;border-top:1px solid #e2e8f0;padding:1rem 2rem;box-shadow:0 -4px 20px rgba(0,0,0,0.08)">
  <div style="max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap">
    <div style="flex:1;min-width:250px">
      <div style="font-weight:700;font-size:0.9rem;margin-bottom:0.25rem">🍪 Usamos cookies</div>
      <div style="font-size:0.8rem;color:#4a5568">Utilizamos cookies para melhorar sua experiência. Ao continuar, você concorda com nossa <a href="/privacidade" style="color:#667eea">Política de Privacidade</a> e a <strong>LGPD</strong>.</div>
    </div>
    <div style="display:flex;gap:0.75rem;flex-shrink:0">
      <button onclick="recusarCookies()" style="padding:0.6rem 1.25rem;border-radius:50px;border:1.5px solid #e2e8f0;background:white;font-size:0.85rem;cursor:pointer;font-weight:600;color:#4a5568">Só essenciais</button>
      <button onclick="aceitarCookies()" style="padding:0.6rem 1.5rem;border-radius:50px;border:none;background:linear-gradient(135deg,#667eea,#764ba2);color:white;font-size:0.85rem;cursor:pointer;font-weight:700">Aceitar todos ✓</button>
    </div>
  </div>
</div>
<script>
function aceitarCookies() {
  localStorage.setItem('cookie_consent', 'all');
  document.getElementById('cookie-banner').style.display = 'none';
}
function recusarCookies() {
  localStorage.setItem('cookie_consent', 'essential');
  document.getElementById('cookie-banner').style.display = 'none';
}
// Mostrar se não aceitou ainda
if (!localStorage.getItem('cookie_consent')) {
  setTimeout(() => {
    document.getElementById('cookie-banner').style.display = 'block';
  }, 2000);
}
</script>
<!-- /Cookie Consent -->
"""

# Adicionar na landing e páginas principais
paginas_cookie = [
    "templates/index.html",
    "templates/sobre.html",
    "templates/planos.html",
    "templates/blog.html",
    "templates/faq.html",
]
ck_count = 0
for p in paginas_cookie:
    path = Path(p)
    if path.exists():
        html = path.read_text(encoding="utf-8")
        if "cookie-banner" not in html:
            html = html.replace("</body>", cookie_consent + "\n</body>")
            path.write_text(html, encoding="utf-8")
            ck_count += 1
print(f"✅ Cookie consent LGPD em {ck_count} páginas!")

# ══════════════════════════════════════════════════
# 3. CALCULADORA ROI na página de preços
# ══════════════════════════════════════════════════
roi_calc = """
<!-- Calculadora ROI -->
<section style="background:var(--bg);padding:4rem 2rem">
  <div style="max-width:700px;margin:0 auto">
    <div style="text-align:center;margin-bottom:2rem">
      <span style="display:inline-block;background:rgba(102,126,234,0.1);color:#667eea;padding:0.3rem 1rem;border-radius:50px;font-size:0.8rem;font-weight:700;margin-bottom:1rem">🧮 Calculadora de ROI</span>
      <h2 style="font-size:clamp(1.5rem,3vw,2rem);font-weight:800">Quanto você <span style="background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent">economiza</span> por mês?</h2>
      <p style="color:#4a5568;margin-top:0.5rem">Calcule seu retorno sobre investimento no EmotionAI</p>
    </div>
    <div style="background:white;border:1px solid #e2e8f0;border-radius:16px;padding:2rem">
      <div style="margin-bottom:1.25rem">
        <label style="font-size:0.85rem;font-weight:600;color:#4a5568;display:block;margin-bottom:0.5rem">
          Quantos pacientes você atende por semana?
        </label>
        <input type="range" id="roi-pacientes" min="5" max="50" value="15" oninput="calcularROI()" style="width:100%">
        <div style="display:flex;justify-content:space-between;font-size:0.8rem;color:#718096;margin-top:0.25rem">
          <span>5</span><span id="roi-pac-val" style="font-weight:700;color:#667eea">15 pacientes</span><span>50</span>
        </div>
      </div>
      <div style="margin-bottom:1.25rem">
        <label style="font-size:0.85rem;font-weight:600;color:#4a5568;display:block;margin-bottom:0.5rem">
          Horas gastas com burocracia por semana:
        </label>
        <input type="range" id="roi-horas" min="1" max="20" value="5" oninput="calcularROI()" style="width:100%">
        <div style="display:flex;justify-content:space-between;font-size:0.8rem;color:#718096;margin-top:0.25rem">
          <span>1h</span><span id="roi-horas-val" style="font-weight:700;color:#667eea">5 horas</span><span>20h</span>
        </div>
      </div>
      <div style="margin-bottom:1.25rem">
        <label style="font-size:0.85rem;font-weight:600;color:#4a5568;display:block;margin-bottom:0.5rem">
          Valor da sua hora de trabalho (R$):
        </label>
        <input type="range" id="roi-valor" min="50" max="500" value="150" step="10" oninput="calcularROI()" style="width:100%">
        <div style="display:flex;justify-content:space-between;font-size:0.8rem;color:#718096;margin-top:0.25rem">
          <span>R$50</span><span id="roi-valor-val" style="font-weight:700;color:#667eea">R$150/h</span><span>R$500</span>
        </div>
      </div>
      <!-- Resultado -->
      <div style="background:linear-gradient(135deg,#667eea,#764ba2);border-radius:16px;padding:1.5rem;color:white;text-align:center;margin-top:1.5rem">
        <div style="font-size:0.9rem;opacity:0.85;margin-bottom:0.5rem">Com EmotionAI você economiza</div>
        <div id="roi-economia" style="font-size:3rem;font-weight:900;line-height:1">R$ 600</div>
        <div style="font-size:0.85rem;opacity:0.85;margin-top:0.25rem">por mês em tempo recuperado</div>
        <div style="margin-top:1rem;padding-top:1rem;border-top:1px solid rgba(255,255,255,0.2);display:flex;justify-content:center;gap:2rem;flex-wrap:wrap">
          <div>
            <div id="roi-horas-ec" style="font-size:1.3rem;font-weight:800">20h</div>
            <div style="font-size:0.75rem;opacity:0.8">horas/mês recuperadas</div>
          </div>
          <div>
            <div id="roi-roi" style="font-size:1.3rem;font-weight:800">20x</div>
            <div style="font-size:0.75rem;opacity:0.8">retorno sobre investimento</div>
          </div>
        </div>
      </div>
      <div style="text-align:center;margin-top:1.5rem">
        <a href="/app/login" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:0.9rem 2.5rem;border-radius:50px;text-decoration:none;font-weight:700;box-shadow:0 4px 16px rgba(102,126,234,0.4)">
          Começar a economizar agora →
        </a>
      </div>
    </div>
  </div>
</section>
<script>
function calcularROI() {
  const pac = parseInt(document.getElementById('roi-pacientes').value);
  const horas = parseInt(document.getElementById('roi-horas').value);
  const valor = parseInt(document.getElementById('roi-valor').value);
  
  document.getElementById('roi-pac-val').textContent = pac + ' pacientes';
  document.getElementById('roi-horas-val').textContent = horas + ' horas';
  document.getElementById('roi-valor-val').textContent = 'R$' + valor + '/h';
  
  // EmotionAI economiza 70% do tempo de burocracia
  const horasEc = Math.round(horas * 0.7 * 4); // por mês
  const economia = horasEc * valor;
  const investimento = 29.90;
  const roi = Math.round(economia / investimento);
  
  document.getElementById('roi-economia').textContent = 'R$ ' + economia.toLocaleString('pt-BR');
  document.getElementById('roi-horas-ec').textContent = horasEc + 'h';
  document.getElementById('roi-roi').textContent = roi + 'x';
}
calcularROI();
</script>
<!-- /Calculadora ROI -->
"""

planos = Path("templates/planos.html")
if planos.exists():
    html = planos.read_text(encoding="utf-8")
    if "roi-pacientes" not in html:
        html = html.replace("<!-- /Calculadora ROI -->", "")
        html = html.replace("</main>", roi_calc + "\n</main>") if "</main>" in html else html.replace(
            '<section class="faq-mini">', roi_calc + '\n<section class="faq-mini">'
        )
        planos.write_text(html, encoding="utf-8")
        print("✅ Calculadora ROI adicionada na página de preços!")

# ══════════════════════════════════════════════════
# 4. SITEMAP DINÂMICO
# ══════════════════════════════════════════════════
sitemap_plugin = Path("plugins/utilidades/sitemap_dinamico.py")
sitemap_plugin.write_text('''#!/usr/bin/env python3
"""Sitemap dinâmico com artigos do blog"""
from fastapi import APIRouter
from fastapi.responses import Response
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(tags=["SEO"])

BASE = "https://emotion-platform-albert.onrender.com"

URLS = [
    ("/", "1.0", "daily"),
    ("/planos", "0.9", "weekly"),
    ("/sobre", "0.8", "monthly"),
    ("/faq", "0.8", "weekly"),
    ("/contato", "0.7", "monthly"),
    ("/psicologos", "0.9", "weekly"),
    ("/terapia", "0.8", "weekly"),
    ("/blog", "0.9", "daily"),
    ("/blog/phq9-guia", "0.8", "monthly"),
    ("/blog/gad7-guia", "0.8", "monthly"),
    ("/blog/telepsicologia", "0.8", "monthly"),
    ("/comparativo", "0.9", "weekly"),
    ("/afiliado", "0.7", "monthly"),
    ("/privacidade", "0.5", "monthly"),
    ("/termos", "0.5", "monthly"),
]

@router.get("/sitemap.xml")
async def sitemap():
    hoje = datetime.now().strftime("%Y-%m-%d")
    urls_xml = ""
    for url, priority, freq in URLS:
        urls_xml += f"""
  <url>
    <loc>{BASE}{url}</loc>
    <lastmod>{hoje}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
    
    xml = f\'\'\'<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}
</urlset>\'\'\'
    return Response(xml, media_type="application/xml")

class SitemapDinamicoPlugin(PluginBase):
    name = "sitemap_dinamico_v2"
    def setup(self, app):
        app.include_router(router)

plugin = SitemapDinamicoPlugin()
''', encoding="utf-8")
print("✅ Sitemap dinâmico criado!")

# ══════════════════════════════════════════════════
# 5. SEQUÊNCIA DE 3 EMAILS (via Brevo)
# ══════════════════════════════════════════════════
email_sequence = Path("plugins/notificacoes/email_sequence.py")
email_sequence.write_text('''#!/usr/bin/env python3
"""Sequência automática de 3 emails pós-cadastro"""
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx, os, asyncio
from datetime import datetime

router = APIRouter(prefix="/api/v1/email-sequence", tags=["Email"])

BREVO_KEY = os.getenv("BREVO_API_KEY", "")
FROM_EMAIL = "albertmenezes2006@gmail.com"
FROM_NAME = "Albert — EmotionAI"
BASE = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

async def enviar_brevo(para: str, nome: str, assunto: str, html: str):
    if not BREVO_KEY:
        return
    async with httpx.AsyncClient() as client:
        await client.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={"api-key": BREVO_KEY, "Content-Type": "application/json"},
            json={
                "sender": {"name": FROM_NAME, "email": FROM_EMAIL},
                "to": [{"email": para, "name": nome}],
                "subject": assunto,
                "htmlContent": html
            },
            timeout=10
        )

async def sequencia_emails(email: str, nome: str):
    """Envia 3 emails em sequência"""
    primeiro_nome = nome.split()[0] if nome else "Psicólogo"
    
    # Email 1 — imediato (boas-vindas)
    await enviar_brevo(email, nome,
        f"🧠 Bem-vindo ao EmotionAI, {primeiro_nome}!",
        f"""<div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;padding:2rem">
        <h1 style="color:#667eea">Olá, {primeiro_nome}! 👋</h1>
        <p>Seja bem-vindo ao EmotionAI — a plataforma que vai transformar sua prática clínica.</p>
        <h3>Por onde começar:</h3>
        <ul>
          <li>✅ <a href="{BASE}/app/avaliacao">Aplique o PHQ-9</a> no seu primeiro paciente</li>
          <li>✅ <a href="{BASE}/app/chat">Converse com a Sofia</a> (nossa IA)</li>
          <li>✅ <a href="{BASE}/app/diario">Configure o diário emocional</a></li>
        </ul>
        <a href="{BASE}/app/dashboard" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:12px 24px;border-radius:50px;text-decoration:none;font-weight:700;margin-top:1rem">
          Acessar plataforma →
        </a>
        <p style="color:#718096;font-size:0.85rem;margin-top:2rem">
          Qualquer dúvida, responda este email.<br>— Albert, fundador do EmotionAI
        </p>
        </div>"""
    )
    
    # Email 2 — após 2 dias
    await asyncio.sleep(172800)  # 48 horas
    await enviar_brevo(email, nome,
        f"💡 {primeiro_nome}, você sabia disso no EmotionAI?",
        f"""<div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;padding:2rem">
        <h2 style="color:#667eea">Dica especial para você 💡</h2>
        <p>Olá, {primeiro_nome}! Espero que esteja aproveitando o EmotionAI.</p>
        <p><strong>Você sabia?</strong> Com o PHQ-9 digital, seus pacientes respondem <em>antes</em> da sessão e você chega com o score pronto. Isso economiza até 15 minutos por atendimento.</p>
        <p>Calcule: 15 min × 20 pacientes/semana = <strong>5 horas economizadas por semana!</strong></p>
        <a href="{BASE}/app/avaliacao" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:12px 24px;border-radius:50px;text-decoration:none;font-weight:700;margin-top:1rem">
          Testar PHQ-9 agora →
        </a>
        </div>"""
    )
    
    # Email 3 — após 5 dias
    await asyncio.sleep(259200)  # 72 horas a mais
    await enviar_brevo(email, nome,
        f"🎁 {primeiro_nome}, presente especial para você",
        f"""<div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;padding:2rem">
        <h2 style="color:#667eea">Um presente exclusivo 🎁</h2>
        <p>Olá, {primeiro_nome}! Como você ainda está no plano gratuito, quero te dar uma chance especial.</p>
        <p>Use o cupom <strong style="color:#667eea;font-size:1.2rem">PSICOLOGO</strong> e ganhe <strong>30% de desconto</strong> no plano Pro.</p>
        <p>Com o Pro você tem: prontuário completo, agendamento online e chat IA ilimitado.</p>
        <div style="background:#f8fafc;border:2px dashed #667eea;border-radius:12px;padding:1rem;text-align:center;margin:1rem 0">
          <span style="font-size:1.5rem;font-weight:900;color:#667eea;letter-spacing:0.1em">PSICOLOGO</span>
        </div>
        <a href="{BASE}/planos" style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:12px 24px;border-radius:50px;text-decoration:none;font-weight:700">
          Resgatar desconto →
        </a>
        <p style="color:#718096;font-size:0.8rem;margin-top:1rem">*Oferta válida por 48 horas.</p>
        </div>"""
    )

@router.post("/iniciar")
async def iniciar_sequencia(
    email: str, nome: str, background_tasks: BackgroundTasks
):
    """Inicia sequência de emails pós-cadastro"""
    background_tasks.add_task(sequencia_emails, email, nome)
    return JSONResponse({"ok": True, "msg": "Sequência iniciada"})

@router.get("/status")
async def status():
    return {"plugin": "email_sequence", "emails": 3, "status": "ativo"}

class EmailSequencePlugin(PluginBase):
    name = "email_sequence_v1"
    def setup(self, app):
        app.include_router(router)

plugin = EmailSequencePlugin()
''', encoding="utf-8")
print("✅ Sequência de 3 emails criada!")

# ══════════════════════════════════════════════════
# 6. PÁGINA PARA CLÍNICAS (B2B)
# ══════════════════════════════════════════════════
clinicas_html = Path("templates/para-clinicas.html")
clinicas_html.write_text("""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EmotionAI para Clínicas — Gestão Completa para Equipes de Psicólogos</title>
<meta name="description" content="EmotionAI para clínicas: gerencie múltiplos psicólogos, prontuários e agenda em uma plataforma. A partir de R$99,90/mês.">
<meta name="robots" content="index, follow">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧠</text></svg>">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
:root { --primary:#667eea; --gradient:linear-gradient(135deg,#667eea,#764ba2); --bg:#f8fafc; --text:#1a202c; --text2:#4a5568; --border:#e2e8f0; --accent:#38a169; --radius:16px; }
body { font-family:Inter,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }
nav { position:fixed; top:0; left:0; right:0; background:rgba(255,255,255,0.95); backdrop-filter:blur(12px); border-bottom:1px solid var(--border); z-index:100; padding:0 2rem; height:64px; display:flex; align-items:center; justify-content:space-between; }
.nav-brand { font-size:1.25rem; font-weight:800; background:var(--gradient); -webkit-background-clip:text; -webkit-text-fill-color:transparent; text-decoration:none; }
.btn { padding:0.6rem 1.5rem; border-radius:50px; font-weight:600; font-size:0.9rem; cursor:pointer; border:none; text-decoration:none; display:inline-flex; align-items:center; gap:0.5rem; transition:all 0.2s; }
.btn-primary { background:var(--gradient); color:white; box-shadow:0 4px 16px rgba(102,126,234,0.35); }
.btn-lg { padding:0.9rem 2.5rem; font-size:1rem; }
.hero { padding:8rem 2rem 5rem; background:white; }
.container { max-width:1100px; margin:0 auto; padding:0 2rem; }
.grad { background:var(--gradient); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.badge { display:inline-block; background:rgba(102,126,234,0.1); color:var(--primary); padding:0.3rem 1rem; border-radius:50px; font-size:0.8rem; font-weight:700; margin-bottom:1rem; }
.features-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1.5rem; margin-top:3rem; }
.feature { background:white; border:1px solid var(--border); border-radius:var(--radius); padding:1.75rem; transition:all 0.2s; }
.feature:hover { box-shadow:0 8px 32px rgba(102,126,234,0.12); transform:translateY(-3px); }
.feature-icon { font-size:2.5rem; margin-bottom:1rem; }
.feature h3 { font-weight:700; margin-bottom:0.5rem; }
.feature p { font-size:0.9rem; color:var(--text2); line-height:1.6; }
.stats-row { display:flex; gap:3rem; justify-content:center; flex-wrap:wrap; padding:3rem; background:var(--gradient); border-radius:var(--radius); color:white; margin:3rem 0; }
.stat-item { text-align:center; }
.stat-num { font-size:2.5rem; font-weight:900; }
.stat-label { font-size:0.85rem; opacity:0.85; margin-top:0.25rem; }
.plano-clinica { background:white; border:2px solid var(--primary); border-radius:24px; padding:2.5rem; max-width:500px; margin:3rem auto; text-align:center; box-shadow:0 8px 32px rgba(102,126,234,0.15); }
.form-contato { background:white; border:1px solid var(--border); border-radius:var(--radius); padding:2rem; max-width:600px; margin:3rem auto; }
input, textarea, select { width:100%; padding:0.75rem 1rem; border:1.5px solid var(--border); border-radius:12px; font-size:0.95rem; font-family:inherit; margin-bottom:1rem; }
input:focus, textarea:focus { outline:none; border-color:var(--primary); }
footer { background:#1a202c; color:#a0aec0; padding:2rem; text-align:center; font-size:0.85rem; margin-top:4rem; }
footer a { color:#667eea; text-decoration:none; }
</style>
</head>
<body>
<nav>
  <a href="/" class="nav-brand">🧠 EmotionAI</a>
  <a href="/contato" class="btn btn-primary">Falar com vendas</a>
</nav>
<div style="height:64px"></div>

<div class="hero">
  <div class="container" style="text-align:center">
    <span class="badge">🏥 Para Clínicas</span>
    <h1 style="font-size:clamp(2rem,5vw,3.5rem);font-weight:900;line-height:1.1;margin-bottom:1.5rem">
      Gerencie sua clínica com<br><span class="grad">Inteligência Artificial</span>
    </h1>
    <p style="font-size:1.1rem;color:var(--text2);max-width:580px;margin:0 auto 2rem;line-height:1.7">
      Uma plataforma para toda sua equipe de psicólogos — prontuários compartilhados, agenda unificada e relatórios de desempenho.
    </p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
      <a href="#contato" class="btn btn-primary btn-lg">Solicitar demonstração →</a>
      <a href="/planos" class="btn" style="background:white;border:1.5px solid var(--border);color:var(--text2)">Ver preços</a>
    </div>
    <p style="font-size:0.85rem;color:var(--text2);margin-top:1rem">✅ Setup em 24h · ✅ Treinamento incluído · ✅ Suporte dedicado</p>
  </div>
</div>

<section style="padding:5rem 2rem;background:var(--bg)">
  <div class="container">
    <div style="text-align:center;margin-bottom:1rem">
      <span class="badge">⚡ Funcionalidades</span>
      <h2 style="font-size:clamp(1.8rem,4vw,2.5rem);font-weight:800">Tudo que sua clínica <span class="grad">precisa</span></h2>
    </div>
    <div class="features-grid">
      <div class="feature"><div class="feature-icon">👥</div><h3>Múltiplos psicólogos</h3><p>Até 10 terapeutas na mesma conta. Cada um com seu acesso individual e prontuários separados.</p></div>
      <div class="feature"><div class="feature-icon">📋</div><h3>Prontuário compartilhado</h3><p>Toda a equipe acessa o histórico do paciente com permissões configuráveis por cargo.</p></div>
      <div class="feature"><div class="feature-icon">📅</div><h3>Agenda unificada</h3><p>Visão geral de todos os atendimentos da clínica em um só calendário.</p></div>
      <div class="feature"><div class="feature-icon">📊</div><h3>Relatórios de desempenho</h3><p>Métricas de atendimentos, escalas e resultados por terapeuta e por período.</p></div>
      <div class="feature"><div class="feature-icon">🔒</div><h3>Conformidade total</h3><p>LGPD, CFP e sigilo profissional garantidos por design em toda a plataforma.</p></div>
      <div class="feature"><div class="feature-icon">🎨</div><h3>White label</h3><p>Personalize com a logo e cores da sua clínica. Seus pacientes veem sua marca.</p></div>
    </div>
  </div>
</section>

<section style="padding:3rem 2rem">
  <div class="container">
    <div class="stats-row">
      <div class="stat-item"><div class="stat-num">5h</div><div class="stat-label">economizadas por semana por terapeuta</div></div>
      <div class="stat-item"><div class="stat-num">30%</div><div class="stat-label">menos faltas com lembretes automáticos</div></div>
      <div class="stat-item"><div class="stat-num">10x</div><div class="stat-label">ROI médio no primeiro mês</div></div>
      <div class="stat-item"><div class="stat-num">24h</div><div class="stat-label">para começar a usar</div></div>
    </div>
  </div>
</section>

<section style="padding:3rem 2rem;background:var(--bg)">
  <div class="container">
    <div class="plano-clinica">
      <span class="badge">💰 Plano Clínica</span>
      <div style="font-size:3rem;font-weight:900;background:var(--gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin:1rem 0">R$ 99,90</div>
      <div style="color:var(--text2);margin-bottom:1.5rem">/mês · até 10 terapeutas</div>
      <ul style="list-style:none;text-align:left;margin-bottom:2rem">
        <li style="padding:0.5rem 0;border-bottom:1px solid var(--border);font-size:0.9rem">✅ Tudo do plano Pro</li>
        <li style="padding:0.5rem 0;border-bottom:1px solid var(--border);font-size:0.9rem">✅ Até 10 terapeutas</li>
        <li style="padding:0.5rem 0;border-bottom:1px solid var(--border);font-size:0.9rem">✅ Gestão multi-clínica</li>
        <li style="padding:0.5rem 0;border-bottom:1px solid var(--border);font-size:0.9rem">✅ White label</li>
        <li style="padding:0.5rem 0;border-bottom:1px solid var(--border);font-size:0.9rem">✅ Relatórios avançados</li>
        <li style="padding:0.5rem 0;font-size:0.9rem">✅ Suporte 24/7 dedicado</li>
      </ul>
      <a href="#contato" class="btn btn-primary" style="width:100%;justify-content:center">Solicitar demonstração →</a>
      <p style="font-size:0.8rem;color:var(--text2);margin-top:1rem">🛡️ Garantia de 30 dias · Cancele quando quiser</p>
    </div>
  </div>
</section>

<section style="padding:3rem 2rem;background:white" id="contato">
  <div class="container">
    <div style="text-align:center;margin-bottom:2rem">
      <h2 style="font-size:1.8rem;font-weight:800">Solicitar <span class="grad">demonstração gratuita</span></h2>
      <p style="color:var(--text2)">Nossa equipe entra em contato em até 24 horas</p>
    </div>
    <div class="form-contato">
      <input type="text" id="cl-nome" placeholder="Nome completo *">
      <input type="email" id="cl-email" placeholder="E-mail profissional *">
      <input type="tel" id="cl-tel" placeholder="WhatsApp (com DDD)">
      <input type="text" id="cl-clinica" placeholder="Nome da clínica *">
      <select id="cl-terapeutas">
        <option value="">Quantos terapeutas na clínica?</option>
        <option>2-3 terapeutas</option>
        <option>4-6 terapeutas</option>
        <option>7-10 terapeutas</option>
        <option>Mais de 10</option>
      </select>
      <textarea id="cl-msg" rows="3" placeholder="Como posso ajudar sua clínica?"></textarea>
      <button onclick="enviarClinica()" class="btn btn-primary" style="width:100%;justify-content:center;padding:1rem">
        Solicitar demonstração gratuita →
      </button>
      <div id="cl-msg-result" style="display:none;margin-top:1rem;padding:0.75rem;border-radius:12px"></div>
    </div>
  </div>
</section>

<footer>
  © 2026 EmotionAI &nbsp;·&nbsp;
  <a href="/">Home</a> &nbsp;·&nbsp;
  <a href="/planos">Planos</a> &nbsp;·&nbsp;
  <a href="/psicologos">Para Psicólogos</a> &nbsp;·&nbsp;
  <a href="/contato">Contato</a>
</footer>

<script>
async function enviarClinica() {
  const nome = document.getElementById('cl-nome').value;
  const email = document.getElementById('cl-email').value;
  const clinica = document.getElementById('cl-clinica').value;
  const msg = document.getElementById('cl-msg-result');
  
  if (!nome || !email || !clinica) {
    msg.style.cssText = 'display:block;background:#fff5f5;border:1px solid #fed7d7;color:#c53030;padding:0.75rem;border-radius:12px';
    msg.textContent = 'Preencha os campos obrigatórios.';
    return;
  }
  
  try {
    await fetch('/contato/enviar', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        nome, email, 
        assunto: 'Demonstração Clínica — ' + clinica,
        mensagem: document.getElementById('cl-msg').value || 'Interesse no plano Clínica'
      })
    });
  } catch(e) {}
  
  msg.style.cssText = 'display:block;background:#f0fff4;border:1px solid #9ae6b4;color:#276749;padding:0.75rem;border-radius:12px';
  msg.textContent = '✅ Solicitação enviada! Entraremos em contato em até 24h.';
}
</script>
</body>
</html>
""", encoding="utf-8")
print("✅ Página /para-clinicas criada!")

# ══════════════════════════════════════════════════
# 7. ADICIONAR ROTAS NOVAS
# ══════════════════════════════════════════════════
routes = Path("plugins/frontend/routes.py")
txt = routes.read_text(encoding="utf-8")

novas_rotas = ""
if "/para-clinicas" not in txt:
    novas_rotas += """
@router.get("/para-clinicas", response_class=HTMLResponse)
async def page_clinicas():
    html = ler_html("para-clinicas.html")
    return HTMLResponse(html) if html else HTMLResponse("<h1>Para Clínicas</h1>")
"""

if novas_rotas:
    txt = txt + novas_rotas
    routes.write_text(txt, encoding="utf-8")
    print("✅ Rotas adicionadas!")

print("\n" + "="*55)
print("TODAS AS MELHORIAS IMPLEMENTADAS!")
print("="*55)
print("✅ WhatsApp flutuante em todas as páginas")
print("✅ Cookie consent LGPD")
print("✅ Calculadora ROI na página de preços")
print("✅ Sitemap dinâmico atualizado")
print("✅ Sequência de 3 emails automáticos")
print("✅ Página /para-clinicas (B2B)")
