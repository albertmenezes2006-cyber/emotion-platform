#!/usr/bin/env python3
"""Sistema de agendamento de sessoes"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime, timedelta
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/agenda", tags=["Agenda"])
ARQUIVO = Path("agenda_sessoes.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/criar")
async def criar_sessao(request: Request):
    d = await request.json()
    sessoes = carregar()
    sessao = {
        "id": len(sessoes) + 1,
        "paciente": d.get("paciente", ""),
        "psicologo": d.get("psicologo", ""),
        "data": d.get("data", ""),
        "hora": d.get("hora", ""),
        "tipo": d.get("tipo", "presencial"),
        "status": "agendado",
        "link_video": d.get("link_video", ""),
        "notas": d.get("notas", ""),
        "criado_em": datetime.utcnow().isoformat()
    }
    sessoes.append(sessao)
    ARQUIVO.write_text(json.dumps(sessoes, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "sessao_id": sessao["id"]})

@router.get("/listar")
async def listar_sessoes(psicologo: str = ""):
    sessoes = carregar()
    if psicologo:
        sessoes = [s for s in sessoes if s["psicologo"] == psicologo]
    return JSONResponse({"sessoes": sessoes, "total": len(sessoes)})

@router.put("/status/{sessao_id}")
async def atualizar_status(sessao_id: int, request: Request):
    d = await request.json()
    sessoes = carregar()
    for s in sessoes:
        if s["id"] == sessao_id:
            s["status"] = d.get("status", s["status"])
    ARQUIVO.write_text(json.dumps(sessoes, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True})

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_agenda():
    sessoes = carregar()
    itens = ""
    for s in sessoes[-10:]:
        cor = {"agendado": "#667eea", "realizado": "#38a169",
               "cancelado": "#e53e3e"}.get(s["status"], "#888")
        itens += f"""
        <div style="background:white;border-radius:12px;padding:20px;
                    margin-bottom:12px;border-left:4px solid {cor};
                    box-shadow:0 2px 8px rgba(0,0,0,0.06)">
          <div style="display:flex;justify-content:space-between">
            <strong style="color:#333">{s.get('paciente','N/A')}</strong>
            <span style="background:{cor};color:white;padding:2px 10px;
                         border-radius:20px;font-size:12px">{s['status']}</span>
          </div>
          <div style="color:#888;font-size:14px;margin-top:4px">
            📅 {s.get('data','')} às {s.get('hora','')} · {s.get('tipo','presencial')}
          </div>
        </div>"""
    if not itens:
        itens = "<p style='color:#888;text-align:center'>Nenhuma sessão agendada ainda</p>"
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Agenda — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
h1{{color:#333}} input,select{{width:100%;padding:10px;border-radius:8px;
  border:2px solid #e0e0e0;margin-bottom:8px;font-size:14px;box-sizing:border-box}}
input:focus,select:focus{{border-color:#667eea;outline:none}}
button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;
  border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
.form{{background:white;border-radius:16px;padding:24px;margin-bottom:24px;
       box-shadow:0 4px 20px rgba(0,0,0,0.08)}}
</style></head><body>
<div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="margin:16px 0">📅 Agenda de Sessões</h1>
<div class="form">
  <h2 style="margin:0 0 16px;color:#333">Nova Sessão</h2>
  <input type="text" id="paciente" placeholder="Nome do paciente">
  <input type="text" id="psicologo" placeholder="Psicólogo responsável">
  <input type="date" id="data">
  <input type="time" id="hora">
  <select id="tipo">
    <option value="presencial">Presencial</option>
    <option value="online">Online</option>
    <option value="telefone">Telefone</option>
  </select>
  <input type="text" id="link" placeholder="Link da videochamada (opcional)">
  <button onclick="agendar()">📅 Agendar sessão</button>
</div>
<h2 style="color:#333;margin-bottom:16px">Próximas sessões</h2>
{itens}
</div>
<script>
function agendar(){{
  var dados={{
    paciente:document.getElementById("paciente").value,
    psicologo:document.getElementById("psicologo").value,
    data:document.getElementById("data").value,
    hora:document.getElementById("hora").value,
    tipo:document.getElementById("tipo").value,
    link_video:document.getElementById("link").value
  }};
  if(!dados.paciente||!dados.data){{alert("Preencha paciente e data");return;}}
  fetch("/api/v1/agenda/criar",{{method:"POST",
    headers:{{"Content-Type":"application/json"}},
    body:JSON.stringify(dados)}}).then(r=>r.json()).then(d=>{{
    alert("✅ Sessão agendada! ID: "+d.sessao_id);
    location.reload();
  }});
}}
</script></body></html>""")

class AgendaPlugin(PluginBase):
    name = "sistema_agenda"
    def setup(self, app): app.include_router(router)
plugin = AgendaPlugin()
