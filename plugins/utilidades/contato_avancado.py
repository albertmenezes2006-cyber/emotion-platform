#!/usr/bin/env python3
"""Pagina de contato avancada"""
from fastapi import APIRouter, Request, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/contato", tags=["Contato"])
ARQUIVO = Path("mensagens_contato.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/enviar")
async def enviar_contato(request: Request):
    d = await request.json()
    msgs = carregar()
    msgs.append({**d, "timestamp": datetime.utcnow().isoformat(), "lido": False})
    ARQUIVO.write_text(json.dumps(msgs, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "msg": "Mensagem recebida! Respondemos em até 24h."})

@router.get("/mensagens")
async def listar_mensagens():
    return JSONResponse(carregar())

@router.get("", response_class=HTMLResponse)
async def pagina_contato():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Contato — Emotion Platform</title>
<style>
body{font-family:sans-serif;background:#f8f9fa;margin:0;padding:20px}
.container{max-width:600px;margin:0 auto}
.card{background:white;border-radius:16px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}
h1{color:#333;margin-bottom:4px} label{display:block;margin:16px 0 6px;font-weight:600;color:#444}
input,select,textarea{width:100%;padding:12px;border-radius:8px;border:2px solid #e0e0e0;
  font-size:14px;box-sizing:border-box;font-family:inherit;outline:none}
input:focus,select:focus,textarea:focus{border-color:#667eea}
textarea{height:120px;resize:vertical}
button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;
  border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;
  cursor:pointer;margin-top:8px}
.info{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:24px}
.info-item{background:#f0f4ff;border-radius:12px;padding:16px;flex:1;min-width:140px;text-align:center}
</style></head><body>
<div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<br><br>
<div class="info">
  <div class="info-item"><div style="font-size:24px">📧</div><div style="font-size:12px;color:#888;margin-top:4px">Email</div>
    <div style="font-size:13px;font-weight:700">albertmenezes2006@gmail.com</div></div>
  <div class="info-item"><div style="font-size:24px">⚡</div><div style="font-size:12px;color:#888;margin-top:4px">Resposta</div>
    <div style="font-size:13px;font-weight:700">Em até 24 horas</div></div>
  <div class="info-item"><div style="font-size:24px">🌐</div><div style="font-size:12px;color:#888;margin-top:4px">Suporte</div>
    <div style="font-size:13px;font-weight:700">24/7 via chat</div></div>
</div>
<div class="card">
<h1>💬 Fale Conosco</h1>
<p style="color:#888">Dúvidas, sugestões ou parcerias? Estamos aqui!</p>
<label>Nome</label><input id="nome" type="text" placeholder="Seu nome completo">
<label>Email</label><input id="email" type="email" placeholder="seu@email.com">
<label>Assunto</label>
<select id="assunto">
  <option>Dúvida técnica</option>
  <option>Parceria</option>
  <option>Sugestão de melhoria</option>
  <option>Planos e preços</option>
  <option>Outro</option>
</select>
<label>Mensagem</label>
<textarea id="msg" placeholder="Descreva sua mensagem..."></textarea>
<button onclick="enviar()">Enviar mensagem ✉️</button>
<div id="ok" style="display:none;margin-top:16px;background:#e8f5e9;
  border-radius:8px;padding:12px;color:#2e7d32;text-align:center;font-weight:700">
  ✅ Mensagem enviada! Respondemos em até 24h.
</div>
</div></div>
<script>
function enviar(){
  var dados={nome:document.getElementById("nome").value,
    email:document.getElementById("email").value,
    assunto:document.getElementById("assunto").value,
    mensagem:document.getElementById("msg").value};
  if(!dados.nome||!dados.email){alert("Preencha nome e email");return;}
  fetch("/contato/enviar",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify(dados)}).then(()=>{
    document.getElementById("ok").style.display="block";
    document.getElementById("msg").value="";
  });
}
</script></body></html>""")

class ContatoPlugin(PluginBase):
    name = "contato_avancado"
    def setup(self, app): app.include_router(router)
plugin = ContatoPlugin()
