#!/usr/bin/env python3
"""Pagina de emergencia e crise completa"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/emergencia", tags=["Crise"])

@router.get("", response_class=HTMLResponse)
async def pagina_emergencia():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Emergência — Emotion Platform</title>
<meta name="description" content="Recursos de emergência e crise em saúde mental">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:#fff5f5;min-height:100vh;padding:20px}
.container{max-width:600px;margin:0 auto}
.alerta{background:#e53e3e;color:white;border-radius:16px;padding:28px;margin-bottom:20px;text-align:center}
.alerta h1{font-size:28px;margin-bottom:8px}
.btn-grande{display:block;border-radius:16px;padding:20px;text-align:center;
  text-decoration:none;font-size:20px;font-weight:800;margin-bottom:12px;
  transition:transform 0.2s}
.btn-grande:hover{transform:scale(1.02)}
.btn-vermelho{background:#e53e3e;color:white}
.btn-laranja{background:#dd6b20;color:white}
.btn-azul{background:#3182ce;color:white}
.btn-roxo{background:#805ad5;color:white}
.card{background:white;border-radius:16px;padding:24px;margin-bottom:16px;
      box-shadow:0 4px 20px rgba(229,62,62,0.1)}
.card h2{color:#e53e3e;margin:0 0 12px}
ul{padding-left:20px}
li{padding:6px 0;color:#555;line-height:1.6}
</style></head><body>
<div class="container">
<div class="alerta">
  <h1>🆘 Recursos de Emergência</h1>
  <p>Você não está sozinho. Ajuda está disponível agora.</p>
</div>

<a href="tel:188" class="btn-grande btn-vermelho">📞 CVV — Ligue 188<br><small style="font-size:14px;font-weight:400">24 horas, 7 dias, gratuito</small></a>
<a href="https://cvv.org.br/chat" target="_blank" class="btn-grande btn-laranja">💬 Chat CVV — cvv.org.br<br><small style="font-size:14px;font-weight:400">Conversa online gratuita</small></a>
<a href="tel:192" class="btn-grande btn-azul">🚑 SAMU — 192<br><small style="font-size:14px;font-weight:400">Emergências médicas</small></a>
<a href="tel:193" class="btn-grande btn-roxo">🚒 Bombeiros — 193<br><small style="font-size:14px;font-weight:400">Emergências gerais</small></a>

<div class="card">
  <h2>🏥 Outros Recursos</h2>
  <ul>
    <li><strong>CAPS</strong> — Centro de Atenção Psicossocial da sua cidade (SUS, gratuito)</li>
    <li><strong>UPA 24h</strong> — Unidade de Pronto Atendimento mais próxima</li>
    <li><strong>UBS</strong> — Unidade Básica de Saúde (atendimento de saúde mental)</li>
    <li><strong>NASF</strong> — Núcleo de Apoio à Saúde da Família</li>
  </ul>
</div>

<div class="card">
  <h2>💙 Enquanto espera ajuda</h2>
  <ul>
    <li>Respire fundo: inspire 4s, segure 4s, expire 4s</li>
    <li>Ligue para alguém de confiança</li>
    <li>Vá para um lugar seguro e iluminado</li>
    <li>Evite ficar sozinho(a) se possível</li>
    <li>Lembre-se: isso é temporário. Você pode passar por isso.</li>
  </ul>
</div>

<div class="card">
  <h2>🌟 Razões para continuar</h2>
  <p style="color:#555;line-height:1.7">Você chegou até aqui. Isso já mostra sua força. Há pessoas que se importam com você, mesmo quando a dor torna difícil sentir isso. Com ajuda profissional, as coisas podem melhorar. Você merece apoio.</p>
</div>

<a href="/" style="display:block;text-align:center;color:#667eea;padding:16px;text-decoration:none;font-weight:700">← Voltar à plataforma</a>
</div></body></html>""")

class EmergenciaPlugin(PluginBase):
    name = "pagina_emergencia_completa"
    def setup(self, app): app.include_router(router)
plugin = EmergenciaPlugin()
