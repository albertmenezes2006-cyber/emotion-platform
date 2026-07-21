#!/usr/bin/env python3
"""Pricing page otimizada para conversao"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/precos", tags=["Pricing"])

@router.get("", response_class=HTMLResponse)
async def pagina_precos():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Planos e Preços — Emotion Platform</title>
<meta name="description" content="Planos acessíveis para psicólogos brasileiros. Comece grátis hoje.">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Product",
"name":"Emotion Intelligence Platform","offers":[
{"@type":"Offer","price":"0","priceCurrency":"BRL","name":"Free"},
{"@type":"Offer","price":"29.90","priceCurrency":"BRL","name":"Pro"},
{"@type":"Offer","price":"99.90","priceCurrency":"BRL","name":"Clinica"}]}</script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:#f8f9fa;padding:40px 20px}
h1{text-align:center;color:#333;font-size:36px;margin-bottom:8px}
.sub{text-align:center;color:#888;margin-bottom:40px;font-size:18px}
.toggle{display:flex;justify-content:center;gap:0;margin-bottom:40px}
.toggle button{padding:10px 24px;border:2px solid #667eea;background:white;
  color:#667eea;cursor:pointer;font-size:14px;font-weight:700}
.toggle button:first-child{border-radius:12px 0 0 12px}
.toggle button:last-child{border-radius:0 12px 12px 0}
.toggle button.ativo{background:#667eea;color:white}
.planos{display:flex;gap:20px;max-width:900px;margin:0 auto;flex-wrap:wrap;justify-content:center}
.plano{background:white;border-radius:20px;padding:32px;flex:1;min-width:240px;
  box-shadow:0 4px 20px rgba(0,0,0,0.08);position:relative;transition:transform 0.2s}
.plano:hover{transform:translateY(-4px)}
.plano.popular{border:3px solid #667eea;transform:scale(1.05)}
.badge{background:#667eea;color:white;padding:4px 16px;border-radius:20px;
  font-size:12px;font-weight:700;position:absolute;top:-12px;left:50%;transform:translateX(-50%)}
.preco{font-size:48px;font-weight:800;color:#333;margin:16px 0 4px}
.preco span{font-size:16px;font-weight:400;color:#888}
ul{list-style:none;margin:20px 0;padding:0}
li{padding:8px 0;color:#555;display:flex;align-items:center;gap:8px;font-size:14px}
li::before{content:"✓";color:#38a169;font-weight:700}
li.nao{color:#bbb} li.nao::before{content:"✗";color:#bbb}
.btn{display:block;text-align:center;padding:14px;border-radius:12px;
  font-weight:700;text-decoration:none;margin-top:20px;font-size:16px}
.btn-free{background:#f0f4ff;color:#667eea}
.btn-pro{background:linear-gradient(135deg,#667eea,#764ba2);color:white}
.btn-clinica{background:linear-gradient(135deg,#667eea,#764ba2);color:white}
.garantia{text-align:center;margin-top:32px;color:#888;font-size:14px}
</style></head><body>
<h1>Planos simples e transparentes</h1>
<p class="sub">Sem surpresas. Cancele quando quiser.</p>
<div class="toggle">
  <button class="ativo" onclick="setPlano('mensal',this)">Mensal</button>
  <button onclick="setPlano('anual',this)">Anual (2 meses grátis)</button>
</div>
<div class="planos">
  <div class="plano">
    <h2 style="color:#333">Free</h2>
    <div class="preco">R$0<span>/mês</span></div>
    <p style="color:#888;font-size:14px">Para começar</p>
    <ul>
      <li>PHQ-9 e GAD-7 ilimitados</li>
      <li>Chat com IA (10/dia)</li>
      <li>Diário emocional</li>
      <li>Dashboard básico</li>
      <li class="nao">Prontuário completo</li>
      <li class="nao">Relatórios PDF</li>
      <li class="nao">Múltiplos pacientes</li>
    </ul>
    <a href="/app/login" class="btn btn-free">Começar grátis →</a>
  </div>
  <div class="plano popular">
    <div class="badge">⭐ MAIS POPULAR</div>
    <h2 style="color:#333">Pro</h2>
    <div class="preco" id="preco-pro">R$29,90<span>/mês</span></div>
    <p style="color:#888;font-size:14px">Para psicólogos autônomos</p>
    <ul>
      <li>Tudo do Free</li>
      <li>Chat com IA ilimitado</li>
      <li>Prontuário básico</li>
      <li>10 pacientes ativos</li>
      <li>Relatórios PDF</li>
      <li>Suporte por email</li>
      <li class="nao">Multi-terapeuta</li>
    </ul>
    <a href="/api/v1/stripe-checkout/planos" class="btn btn-pro">Assinar Pro →</a>
  </div>
  <div class="plano">
    <h2 style="color:#333">Clínica</h2>
    <div class="preco" id="preco-clinica">R$99,90<span>/mês</span></div>
    <p style="color:#888;font-size:14px">Para clínicas e equipes</p>
    <ul>
      <li>Tudo do Pro</li>
      <li>Pacientes ilimitados</li>
      <li>Prontuário completo</li>
      <li>Multi-terapeuta (5)</li>
      <li>Analytics avançado</li>
      <li>White-label básico</li>
      <li>Suporte prioritário</li>
    </ul>
    <a href="/api/v1/stripe-checkout/planos" class="btn btn-clinica">Assinar Clínica →</a>
  </div>
</div>
<p class="garantia">🔒 Pagamento seguro via Stripe e PIX · 7 dias de garantia · Cancele quando quiser</p>
<script>
function setPlano(tipo,btn){
  document.querySelectorAll(".toggle button").forEach(b=>b.classList.remove("ativo"));
  btn.classList.add("ativo");
  if(tipo==="anual"){
    document.getElementById("preco-pro").innerHTML="R$24,90<span>/mês</span>";
    document.getElementById("preco-clinica").innerHTML="R$79,90<span>/mês</span>";
  } else {
    document.getElementById("preco-pro").innerHTML="R$29,90<span>/mês</span>";
    document.getElementById("preco-clinica").innerHTML="R$99,90<span>/mês</span>";
  }
}
</script></body></html>""")

class PricingPlugin(PluginBase):
    name = "pricing_otimizado"
    def setup(self, app): app.include_router(router)
plugin = PricingPlugin()
