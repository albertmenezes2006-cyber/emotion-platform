#!/usr/bin/env python3
"""Termos de uso atualizados e completos"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/termos-uso", tags=["Jurídico"])

@router.get("", response_class=HTMLResponse)
async def termos():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Termos de Uso — Emotion Platform</title>
<style>
body{font-family:sans-serif;max-width:800px;margin:0 auto;padding:40px 20px;color:#333;line-height:1.8}
h1{color:#667eea;border-bottom:3px solid #667eea;padding-bottom:12px}
h2{color:#444;margin-top:32px} p{color:#555;margin-bottom:12px}
.update{background:#f0f4ff;border-radius:8px;padding:12px;color:#667eea;font-size:14px;margin-bottom:24px}
.highlight{background:#fff3cd;border-left:4px solid #f59e0b;padding:12px;border-radius:4px;margin:16px 0}
</style></head><body>
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1>📋 Termos de Uso</h1>
<div class="update">Última atualização: 17/07/2026 · Versão 2.0</div>
<h2>1. Aceitação dos Termos</h2>
<p>Ao acessar o Emotion Intelligence Platform, você concorda com estes Termos de Uso.
Se não concordar, não utilize o serviço.</p>
<h2>2. Descrição do Serviço</h2>
<p>O Emotion Platform é uma plataforma de apoio à saúde mental que oferece instrumentos
de avaliação psicológica (PHQ-9, GAD-7), chat com IA e ferramentas para psicólogos.
<strong>Não substitui atendimento psicológico ou psiquiátrico profissional.</strong></p>
<div class="highlight">⚠️ Em caso de emergência ou crise, ligue 188 (CVV) ou 192 (SAMU) imediatamente.</div>
<h2>3. Uso Adequado</h2>
<p>É proibido usar a plataforma para fins ilegais, difamar terceiros, transmitir conteúdo
prejudicial ou tentar acessar sistemas não autorizados.</p>
<h2>4. Privacidade e LGPD</h2>
<p>Tratamos seus dados conforme a Lei 13.709/2018 (LGPD). Você tem direito de acessar,
corrigir e deletar seus dados. Veja nossa <a href="/privacidade" style="color:#667eea">Política de Privacidade</a>.</p>
<h2>5. Propriedade Intelectual</h2>
<p>Todo conteúdo da plataforma é protegido por direitos autorais. Os instrumentos
PHQ-9 e GAD-7 são de domínio público e validados para uso clínico.</p>
<h2>6. Limitação de Responsabilidade</h2>
<p>A plataforma é fornecida "como está". Não nos responsabilizamos por danos
indiretos, incidentais ou consequenciais decorrentes do uso.</p>
<h2>7. Modificações</h2>
<p>Podemos modificar estes termos a qualquer momento. Usuários serão notificados
por email sobre mudanças significativas.</p>
<h2>8. Contato</h2>
<p>Dúvidas: <a href="mailto:albertmenezes2006@gmail.com" style="color:#667eea">albertmenezes2006@gmail.com</a></p>
<p style="color:#aaa;margin-top:40px;font-size:14px">Emotion Intelligence Platform · CNPJ em processo · São Paulo, Brasil</p>
</body></html>""")

class TermosPlugin(PluginBase):
    name = "termos_atualizados"
    def setup(self, app): app.include_router(router)
plugin = TermosPlugin()
