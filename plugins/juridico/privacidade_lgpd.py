#!/usr/bin/env python3
"""Politica de privacidade LGPD completa"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/privacidade-lgpd", tags=["Jurídico"])

@router.get("", response_class=HTMLResponse)
async def privacidade():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Política de Privacidade — Emotion Platform</title>
<style>
body{font-family:sans-serif;max-width:800px;margin:0 auto;padding:40px 20px;line-height:1.8}
h1{color:#667eea;border-bottom:3px solid #667eea;padding-bottom:12px}
h2{color:#444;margin-top:32px} p,li{color:#555}
.direito{background:#f0fff4;border-left:4px solid #38a169;padding:12px;
         border-radius:4px;margin:8px 0}
table{width:100%;border-collapse:collapse;margin:16px 0}
td,th{padding:10px;border:1px solid #eee;text-align:left;font-size:14px}
th{background:#f0f4ff;font-weight:700}
</style></head><body>
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1>🔒 Política de Privacidade</h1>
<p>Última atualização: 17/07/2026 · Em conformidade com a LGPD (Lei 13.709/2018)</p>
<h2>Dados que Coletamos</h2>
<table>
<tr><th>Tipo de Dado</th><th>Finalidade</th><th>Retenção</th></tr>
<tr><td>Email e nome</td><td>Identificação e login</td><td>Enquanto conta ativa</td></tr>
<tr><td>Scores PHQ-9/GAD-7</td><td>Acompanhamento clínico</td><td>5 anos ou até solicitação</td></tr>
<tr><td>Histórico de chat</td><td>Continuidade do suporte</td><td>1 ano</td></tr>
<tr><td>Logs de acesso</td><td>Segurança e auditoria</td><td>90 dias</td></tr>
</table>
<h2>Seus Direitos (LGPD Art. 18)</h2>
<div class="direito">✅ <strong>Acesso:</strong> Solicitar cópia de todos seus dados</div>
<div class="direito">✅ <strong>Correção:</strong> Corrigir dados incorretos</div>
<div class="direito">✅ <strong>Exclusão:</strong> Deletar sua conta e dados</div>
<div class="direito">✅ <strong>Portabilidade:</strong> Exportar dados em CSV/JSON</div>
<div class="direito">✅ <strong>Oposição:</strong> Opor-se ao tratamento</div>
<div class="direito">✅ <strong>Revogação:</strong> Revogar consentimento</div>
<h2>Segurança</h2>
<p>Usamos criptografia AES-256, HTTPS/TLS, autenticação JWT e servidores em nuvem
certificados (Render.com). Dados de saúde mental são tratados como dados sensíveis.</p>
<h2>Compartilhamento</h2>
<p>Não vendemos dados. Compartilhamos apenas com: psicólogo responsável pelo paciente
(com consentimento) e fornecedores de infraestrutura (Render, PostgreSQL).</p>
<h2>Cookies</h2>
<p>Usamos cookies essenciais para funcionamento e analytics (Microsoft Clarity, GA4)
com finalidade de melhorar a plataforma. Você pode recusar cookies analíticos.</p>
<h2>Encarregado (DPO)</h2>
<p>Albert Menezes · <a href="mailto:albertmenezes2006@gmail.com" style="color:#667eea">albertmenezes2006@gmail.com</a></p>
<p>Para exercer seus direitos, envie email com assunto "LGPD — [seu direito]".</p>
</body></html>""")

class PrivacidadePlugin(PluginBase):
    name = "privacidade_lgpd"
    def setup(self, app): app.include_router(router)
plugin = PrivacidadePlugin()
