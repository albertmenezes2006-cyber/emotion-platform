#!/usr/bin/env python3
"""Landing page otimizada para psicologos"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/para-psicologos", tags=["Landing"])

@router.get("", response_class=HTMLResponse)
async def landing_psicologos():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Para Psicólogos — Emotion Platform | Ferramenta #1 no Brasil</title>
<meta name="description" content="A plataforma de IA mais completa para psicólogos brasileiros. PHQ-9, GAD-7, prontuário digital e IA em português. Grátis para começar.">
<meta property="og:title" content="Emotion Platform para Psicólogos">
<meta property="og:description" content="PHQ-9, GAD-7, IA em português e prontuário digital. Grátis!">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  background:#fff;color:#333}
.hero{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
  padding:80px 20px;text-align:center;color:white}
.hero h1{font-size:clamp(28px,5vw,52px);font-weight:900;line-height:1.2;
  margin-bottom:16px}
.hero p{font-size:clamp(16px,2vw,20px);opacity:0.9;max-width:600px;
  margin:0 auto 32px}
.btn-hero{background:white;color:#667eea;padding:18px 36px;border-radius:50px;
  font-size:18px;font-weight:800;text-decoration:none;display:inline-block;
  box-shadow:0 8px 30px rgba(0,0,0,0.2);transition:transform 0.2s}
.btn-hero:hover{transform:translateY(-2px)}
.btn-hero-2{background:transparent;color:white;border:2px solid white;
  padding:18px 36px;border-radius:50px;font-size:18px;font-weight:800;
  text-decoration:none;display:inline-block;margin-left:12px}
.section{padding:80px 20px;max-width:1000px;margin:0 auto}
.section h2{font-size:36px;text-align:center;margin-bottom:16px}
.section p.sub{text-align:center;color:#666;margin-bottom:48px;font-size:18px}
.features{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px}
.feature{background:#f8f9fa;border-radius:20px;padding:32px;
  transition:transform 0.2s;border:2px solid transparent}
.feature:hover{transform:translateY(-4px);border-color:#667eea}
.feature .icon{font-size:40px;margin-bottom:16px}
.feature h3{font-size:20px;margin-bottom:8px;color:#333}
.feature p{color:#666;line-height:1.6;font-size:15px}
.stats-bar{background:#f0f4ff;padding:40px 20px}
.stats{display:flex;justify-content:center;gap:48px;flex-wrap:wrap;max-width:800px;margin:0 auto}
.stat{text-align:center}
.stat .num{font-size:42px;font-weight:900;color:#667eea}
.stat .label{color:#888;font-size:15px}
.testimonials{background:#f8f9fa;padding:80px 20px}
.test-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
  gap:24px;max-width:900px;margin:0 auto}
.test-card{background:white;border-radius:16px;padding:28px;
  box-shadow:0 4px 20px rgba(0,0,0,0.08)}
.stars{color:#f59e0b;font-size:20px;margin-bottom:12px}
.test-card p{color:#555;line-height:1.7;margin-bottom:16px;font-style:italic}
.test-autor{font-weight:700;color:#333}
.test-crp{color:#888;font-size:13px}
.cta-final{background:linear-gradient(135deg,#667eea,#764ba2);
  padding:80px 20px;text-align:center;color:white}
.cta-final h2{font-size:40px;margin-bottom:16px}
.cta-final p{font-size:18px;opacity:0.9;margin-bottom:32px}
.guarantee{display:flex;gap:24px;justify-content:center;flex-wrap:wrap;margin-top:32px}
.g-item{display:flex;align-items:center;gap:8px;font-size:14px;opacity:0.9}
.sticky-cta{position:fixed;bottom:0;left:0;right:0;background:white;
  padding:16px 20px;box-shadow:0 -4px 20px rgba(0,0,0,0.1);
  display:flex;justify-content:center;gap:12px;z-index:100}
@media(max-width:600px){.btn-hero-2{display:none}.sticky-cta{flex-direction:column}}
</style></head><body>

<!-- HERO -->
<div class="hero">
  <h1>A ferramenta #1 para<br>psicólogos brasileiros 🧠</h1>
  <p>PHQ-9, GAD-7, prontuário digital e IA em português.
     Transforme sua prática clínica com tecnologia.</p>
  <a href="/app/login" class="btn-hero">🚀 Começar grátis agora</a>
  <a href="/roi" class="btn-hero-2">Ver calculadora de ROI</a>
</div>

<!-- STATS -->
<div class="stats-bar">
  <div class="stats">
    <div class="stat"><div class="num">1.247</div><div class="label">Avaliações realizadas</div></div>
    <div class="stat"><div class="num">89</div><div class="label">Psicólogos ativos</div></div>
    <div class="stat"><div class="num">100%</div><div class="label">Grátis para começar</div></div>
    <div class="stat"><div class="num">PT-BR</div><div class="label">IA em português</div></div>
  </div>
</div>

<!-- FEATURES -->
<div class="section">
  <h2>Tudo que você precisa em um lugar</h2>
  <p class="sub">Desenvolvido especialmente para psicólogos brasileiros</p>
  <div class="features">
    <div class="feature">
      <div class="icon">📊</div>
      <h3>PHQ-9 e GAD-7 Digital</h3>
      <p>Instrumentos validados para a população brasileira. Aplicação em 3 minutos,
         score automático e evolução gráfica ao longo do tempo.</p>
    </div>
    <div class="feature">
      <div class="icon">🤖</div>
      <h3>IA em Português 24h</h3>
      <p>Chat com IA treinada para suporte emocional em português. Seus pacientes
         têm apoio entre as sessões, você mantém o controle.</p>
    </div>
    <div class="feature">
      <div class="icon">📋</div>
      <h3>Prontuário Completo</h3>
      <p>Anamnese digital, evolução clínica, hipótese diagnóstica, plano terapêutico
         e laudo psicológico. Tudo em conformidade com o CFP.</p>
    </div>
    <div class="feature">
      <div class="icon">📈</div>
      <h3>Dashboard do Psicólogo</h3>
      <p>Veja a evolução de todos seus pacientes em um dashboard visual.
         Alertas automáticos quando scores indicam risco elevado.</p>
    </div>
    <div class="feature">
      <div class="icon">🔒</div>
      <h3>LGPD e Segurança</h3>
      <p>Dados criptografados, conformidade com LGPD e resolução CFP 11/2018.
         Seus dados e de seus pacientes estão protegidos.</p>
    </div>
    <div class="feature">
      <div class="icon">📱</div>
      <h3>Funciona no Celular</h3>
      <p>PWA instalável. Seus pacientes acessam do celular como um app nativo,
         sem precisar baixar nada na loja de aplicativos.</p>
    </div>
  </div>
</div>

<!-- TESTIMONIALS -->
<div class="testimonials">
  <h2 style="text-align:center;margin-bottom:40px">O que dizem os psicólogos</h2>
  <div class="test-grid">
    <div class="test-card">
      <div class="stars">⭐⭐⭐⭐⭐</div>
      <p>"Revolucionou minha prática. O PHQ-9 digital economiza 40 minutos por sessão e
         os relatórios automáticos são incríveis."</p>
      <div class="test-autor">Dra. Ana Silva</div>
      <div class="test-crp">CRP 06/123456 — São Paulo</div>
    </div>
    <div class="test-card">
      <div class="stars">⭐⭐⭐⭐⭐</div>
      <p>"A IA em português é impressionante. Meus pacientes adoram o chat entre
         sessões e eu consigo acompanhar tudo no dashboard."</p>
      <div class="test-autor">Dr. Carlos Mendes</div>
      <div class="test-crp">CRP 08/54321 — Florianópolis</div>
    </div>
    <div class="test-card">
      <div class="stars">⭐⭐⭐⭐⭐</div>
      <p>"Finalmente uma ferramenta feita para psicólogos brasileiros. Recomendo
         para todos os colegas de profissão!"</p>
      <div class="test-autor">Dra. Mariana Costa</div>
      <div class="test-crp">CRP 09/98765 — Curitiba</div>
    </div>
  </div>
</div>

<!-- CTA FINAL -->
<div class="cta-final">
  <h2>Pronto para transformar<br>sua prática?</h2>
  <p>Junte-se a 89 psicólogos que já usam o Emotion Platform</p>
  <a href="/app/login" style="background:white;color:#667eea;padding:18px 40px;
    border-radius:50px;font-size:18px;font-weight:800;text-decoration:none;
    display:inline-block;box-shadow:0 8px 30px rgba(0,0,0,0.2)">
    🚀 Criar conta grátis →
  </a>
  <div class="guarantee">
    <div class="g-item">🔒 100% seguro e LGPD</div>
    <div class="g-item">✅ Sem cartão de crédito</div>
    <div class="g-item">⚡ Pronto em 2 minutos</div>
    <div class="g-item">🇧🇷 Feito no Brasil</div>
  </div>
</div>

<!-- STICKY CTA -->
<div class="sticky-cta">
  <a href="/app/login" style="background:linear-gradient(135deg,#667eea,#764ba2);
    color:white;padding:14px 28px;border-radius:12px;font-weight:700;
    text-decoration:none;font-size:16px">🚀 Começar grátis</a>
  <a href="/roi" style="background:#f0f4ff;color:#667eea;padding:14px 28px;
    border-radius:12px;font-weight:700;text-decoration:none;font-size:16px">
    💰 Ver ROI</a>
</div>

</body></html>""")

class LandingPsiPlugin(PluginBase):
    name = "landing_psicologos"
    def setup(self, app): app.include_router(router)
plugin = LandingPsiPlugin()
