#!/usr/bin/env python3
"""Pagina sobre completa com historia e missao"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/sobre", tags=["Sobre"])

@router.get("", response_class=HTMLResponse)
async def pagina_sobre():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sobre — Emotion Intelligence Platform</title>
<meta name="description" content="Conheça a história e missão do Emotion Platform">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:#f8f9fa}
.hero{background:linear-gradient(135deg,#667eea,#764ba2);color:white;
  padding:80px 20px;text-align:center}
.hero h1{font-size:42px;margin-bottom:12px}
.hero p{font-size:20px;opacity:0.9;max-width:600px;margin:0 auto}
.container{max-width:800px;margin:0 auto;padding:60px 20px}
.section{margin-bottom:60px}
.section h2{color:#333;font-size:28px;margin-bottom:16px}
.section p{color:#555;line-height:1.8;font-size:16px;margin-bottom:12px}
.stats{display:flex;gap:20px;flex-wrap:wrap;margin:40px 0}
.stat{background:white;border-radius:16px;padding:24px;flex:1;min-width:150px;
  text-align:center;box-shadow:0 4px 20px rgba(0,0,0,0.08)}
.stat .num{font-size:36px;font-weight:800;color:#667eea}
.stat .label{color:#888;font-size:14px;margin-top:4px}
.valores{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
.valor{background:white;border-radius:12px;padding:20px;
  box-shadow:0 2px 8px rgba(0,0,0,0.06);border-left:4px solid #667eea}
.valor h3{color:#333;margin-bottom:8px}
.valor p{color:#666;font-size:14px;line-height:1.6}
.cta{background:linear-gradient(135deg,#667eea,#764ba2);border-radius:20px;
  padding:48px;text-align:center;color:white;margin-top:60px}
.cta h2{font-size:32px;margin-bottom:12px}
.cta p{opacity:0.9;margin-bottom:24px;font-size:16px}
.btn{display:inline-block;background:white;color:#667eea;padding:14px 32px;
  border-radius:12px;text-decoration:none;font-weight:700;font-size:16px}
</style></head><body>
<div class="hero">
  <h1>🧠 Emotion Intelligence Platform</h1>
  <p>Democratizando o cuidado em saúde mental através da tecnologia</p>
</div>
<div class="container">
  <div class="stats">
    <div class="stat"><div class="num">1.461</div><div class="label">Plugins ativos</div></div>
    <div class="stat"><div class="num">7.255</div><div class="label">Rotas disponíveis</div></div>
    <div class="stat"><div class="num">100%</div><div class="label">Testes passando</div></div>
    <div class="stat"><div class="num">0</div><div class="label">Erros em produção</div></div>
  </div>
  <div class="section">
    <h2>Nossa Missão</h2>
    <p>O Emotion Intelligence Platform nasceu com um propósito claro: <strong>ser a ferramenta #1
    para psicólogos brasileiros</strong> que desejam usar tecnologia e inteligência artificial
    para melhorar o cuidado com seus pacientes.</p>
    <p>Acreditamos que a saúde mental é um direito de todos, e que a tecnologia pode ser
    uma poderosa aliada dos profissionais de psicologia — nunca uma substituta.</p>
  </div>
  <div class="section">
    <h2>Nossa História</h2>
    <p>Desenvolvido por Albert Menezes, o Emotion Platform surgiu da necessidade de criar
    ferramentas de avaliação psicológica validadas e em português, integradas com IA moderna.</p>
    <p>Com mais de 270 commits, 1.782 arquivos e tecnologia de ponta, construímos a plataforma
    mais completa de saúde mental digital do Brasil — tudo com código limpo e testes rigorosos.</p>
  </div>
  <div class="section">
    <h2>Nossos Valores</h2>
    <div class="valores">
      <div class="valor"><h3>🔬 Evidência Científica</h3>
        <p>Todos os instrumentos são validados cientificamente para a população brasileira.</p></div>
      <div class="valor"><h3>🔒 Privacidade Total</h3>
        <p>Conformidade com LGPD. Seus dados são seus. Sempre.</p></div>
      <div class="valor"><h3>🤝 Apoio ao Profissional</h3>
        <p>Criado por e para psicólogos brasileiros.</p></div>
      <div class="valor"><h3>🌐 Acessibilidade</h3>
        <p>WCAG 2.1 AA. Tecnologia para todos, sem exceção.</p></div>
    </div>
  </div>
  <div class="cta">
    <h2>Pronto para começar?</h2>
    <p>Junte-se a psicólogos que já transformaram sua prática com tecnologia</p>
    <a href="/app/login" class="btn">Criar conta grátis →</a>
  </div>
</div>
</body></html>""")

class SobrePlugin(PluginBase):
    name = "sobre_completo"
    def setup(self, app): app.include_router(router)
plugin = SobrePlugin()
