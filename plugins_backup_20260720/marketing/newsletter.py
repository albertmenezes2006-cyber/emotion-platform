#!/usr/bin/env python3
"""Newsletter para captura de leads"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/newsletter", tags=["Newsletter"])
ARQUIVO = Path("newsletter_leads.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/inscrever")
async def inscrever(request: Request):
    dados = await request.json()
    email = dados.get("email", "").strip().lower()
    nome = dados.get("nome", "").strip()
    if not email or "@" not in email:
        return JSONResponse({"erro": "Email invalido"}, status_code=400)
    leads = carregar()
    if any(l["email"] == email for l in leads):
        return JSONResponse({"ok": True, "msg": "Ja inscrito"})
    leads.append({
        "email": email, "nome": nome,
        "origem": dados.get("origem", "site"),
        "timestamp": datetime.utcnow().isoformat()
    })
    ARQUIVO.write_text(json.dumps(leads, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "total": len(leads),
                         "msg": f"Inscrito! Total: {len(leads)} leads"})

@router.get("/total")
async def total_leads():
    leads = carregar()
    return JSONResponse({"total": len(leads), "leads": leads[-5:]})

@router.get("/widget", response_class=HTMLResponse)
async def widget_newsletter():
    return HTMLResponse("""
<div style="background:linear-gradient(135deg,#667eea,#764ba2);
            border-radius:16px;padding:32px;color:white;text-align:center;
            font-family:sans-serif;max-width:500px;margin:0 auto">
    <h2 style="margin:0 0 8px">📧 Receba dicas de saúde mental</h2>
    <p style="opacity:0.9;margin:0 0 20px">1x por semana. Sem spam. Cancele quando quiser.</p>
    <div style="display:flex;gap:8px;flex-wrap:wrap;justify-content:center">
        <input id="nl-nome" type="text" placeholder="Seu nome"
            style="flex:1;min-width:140px;padding:12px;border-radius:8px;
                   border:none;font-size:14px">
        <input id="nl-email" type="email" placeholder="seu@email.com"
            style="flex:2;min-width:200px;padding:12px;border-radius:8px;
                   border:none;font-size:14px">
        <button onclick="inscrever()"
            style="background:white;color:#667eea;border:none;border-radius:8px;
                   padding:12px 20px;font-weight:700;cursor:pointer;font-size:14px">
            Inscrever ✓
        </button>
    </div>
    <div id="nl-msg" style="margin-top:12px;font-size:14px"></div>
</div>
<script>
function inscrever() {
    var email = document.getElementById('nl-email').value;
    var nome = document.getElementById('nl-nome').value;
    if (!email) { alert('Digite seu email'); return; }
    fetch('/api/v1/newsletter/inscrever', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email: email, nome: nome, origem: 'widget'})
    }).then(r => r.json()).then(d => {
        document.getElementById('nl-msg').textContent = '✅ Inscrito com sucesso!';
        document.getElementById('nl-email').value = '';
        document.getElementById('nl-nome').value = '';
    });
}
</script>""")

class NewsletterPlugin(PluginBase):
    name = "newsletter_leads"
    def setup(self, app):
        app.include_router(router)

plugin = NewsletterPlugin()
