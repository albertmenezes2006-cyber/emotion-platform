#!/usr/bin/env python3
"""Feedback rapido dos usuarios"""
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, HTMLResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/feedback", tags=["Feedback"])

ARQUIVO = Path("feedback_usuarios.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

def salvar(dados):
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))

@router.post("/enviar")
async def enviar_feedback(request: Request):
    dados = await request.json()
    feedbacks = carregar()
    feedbacks.append({
        "id": len(feedbacks) + 1,
        "nota": dados.get("nota", 0),
        "mensagem": dados.get("mensagem", ""),
        "pagina": dados.get("pagina", ""),
        "timestamp": datetime.utcnow().isoformat()
    })
    salvar(feedbacks)
    return JSONResponse({"ok": True, "total": len(feedbacks)})

@router.get("/listar")
async def listar_feedbacks():
    feedbacks = carregar()
    media = sum(f["nota"] for f in feedbacks) / len(feedbacks) if feedbacks else 0
    return JSONResponse({
        "total": len(feedbacks),
        "media": round(media, 1),
        "feedbacks": feedbacks[-10:]
    })

@router.get("/widget", response_class=HTMLResponse)
async def widget_feedback():
    return HTMLResponse("""
<div id="feedback-widget" style="position:fixed;bottom:80px;right:20px;
     background:white;border-radius:16px;padding:20px;
     box-shadow:0 4px 20px rgba(0,0,0,0.15);width:280px;
     font-family:sans-serif;display:none;z-index:9998">
    <h3 style="margin:0 0 12px;color:#333">Como foi sua experiência?</h3>
    <div style="display:flex;gap:8px;justify-content:center;margin:12px 0">
        <span onclick="votar(1)" style="font-size:28px;cursor:pointer">😢</span>
        <span onclick="votar(2)" style="font-size:28px;cursor:pointer">😐</span>
        <span onclick="votar(3)" style="font-size:28px;cursor:pointer">🙂</span>
        <span onclick="votar(4)" style="font-size:28px;cursor:pointer">😊</span>
        <span onclick="votar(5)" style="font-size:28px;cursor:pointer">🤩</span>
    </div>
    <textarea id="fb-msg" placeholder="Algum comentário? (opcional)"
        style="width:100%;border:1px solid #eee;border-radius:8px;
               padding:8px;font-size:13px;resize:none;height:60px"></textarea>
    <button onclick="enviarFeedback()"
        style="width:100%;background:#667eea;color:white;border:none;
               border-radius:8px;padding:10px;margin-top:8px;cursor:pointer;
               font-weight:700">Enviar</button>
</div>
<button onclick="toggleFeedback()"
    style="position:fixed;bottom:20px;right:20px;
           background:#667eea;color:white;border:none;
           border-radius:50px;padding:10px 16px;cursor:pointer;
           font-family:sans-serif;font-size:13px;font-weight:700;
           box-shadow:0 4px 15px rgba(102,126,234,0.4);z-index:9997">
    ⭐ Feedback
</button>
<script>
var notaSelecionada = 0;
function toggleFeedback() {
    var w = document.getElementById('feedback-widget');
    w.style.display = w.style.display === 'none' ? 'block' : 'none';
}
function votar(n) {
    notaSelecionada = n;
    var spans = document.querySelectorAll('#feedback-widget span');
    spans.forEach(function(s, i) {
        s.style.transform = i < n ? 'scale(1.3)' : 'scale(1)';
    });
}
function enviarFeedback() {
    if (!notaSelecionada) { alert('Selecione uma nota!'); return; }
    fetch('/api/v1/feedback/enviar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            nota: notaSelecionada,
            mensagem: document.getElementById('fb-msg').value,
            pagina: window.location.pathname
        })
    }).then(function() {
        document.getElementById('feedback-widget').innerHTML =
            '<p style="text-align:center;color:#38a169;font-weight:700">✅ Obrigado pelo feedback!</p>';
        setTimeout(function() {
            document.getElementById('feedback-widget').style.display = 'none';
        }, 2000);
    });
}
</script>""")

class FeedbackPlugin(PluginBase):
    name = "feedback_rapido"
    def setup(self, app):
        app.include_router(router)

plugin = FeedbackPlugin()
