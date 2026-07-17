#!/usr/bin/env python3
"""Tracker de medicamentos psiquiatricos"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/medicamentos", tags=["Medicamentos"])
ARQUIVO = Path("medicamentos_tracker.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return {"medicamentos": [], "registros": []}

@router.post("/adicionar")
async def adicionar_med(request: Request):
    d = await request.json()
    dados = carregar()
    med = {"id": len(dados["medicamentos"])+1, "nome": d.get("nome",""),
           "dose": d.get("dose",""), "horarios": d.get("horarios",[]),
           "ativo": True, "inicio": datetime.utcnow().strftime("%d/%m/%Y")}
    dados["medicamentos"].append(med)
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "id": med["id"]})

@router.post("/tomar/{med_id}")
async def registrar_tomada(med_id: int):
    dados = carregar()
    dados["registros"].append({"med_id": med_id, "timestamp": datetime.utcnow().isoformat(),
                               "data": datetime.utcnow().strftime("%d/%m/%Y %H:%M")})
    ARQUIVO.write_text(json.dumps(dados, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "msg": "Medicamento registrado"})

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_medicamentos():
    dados = carregar()
    meds_html = ""
    for m in dados["medicamentos"]:
        if m.get("ativo"):
            horarios = " | ".join(m.get("horarios",[]))
            meds_html += f"""
            <div style="background:white;border-radius:14px;padding:20px;margin-bottom:12px;
                        box-shadow:0 2px 8px rgba(0,0,0,0.06);border-left:4px solid #667eea">
              <div style="display:flex;justify-content:space-between;align-items:center">
                <div>
                  <div style="font-weight:700;color:#333;font-size:16px">💊 {m['nome']}</div>
                  <div style="color:#888;font-size:13px">Dose: {m['dose']} · Horários: {horarios}</div>
                </div>
                <button onclick="tomar({m['id']})" style="background:#667eea;color:white;border:none;
                  border-radius:8px;padding:10px 16px;cursor:pointer;font-weight:700">✓ Tomei</button>
              </div>
            </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Medicamentos — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f0f4ff;padding:20px;margin:0}}
.container{{max-width:600px;margin:0 auto}}
.form{{background:white;border-radius:16px;padding:24px;margin-bottom:20px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}}
input{{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;margin-bottom:8px;font-size:14px;box-sizing:border-box}}
input:focus{{border-color:#667eea;outline:none}}
button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:12px;padding:12px;font-size:15px;font-weight:700;width:100%;cursor:pointer}}
.aviso{{background:#fff3cd;border-left:4px solid #f59e0b;padding:12px;border-radius:8px;margin-bottom:16px;font-size:13px;color:#854d0e}}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">💊 Controle de Medicamentos</h1>
<div class="aviso">⚠️ Este tracker é apenas um lembrete. Nunca altere doses sem orientação médica.</div>
<div class="form">
  <h2 style="margin:0 0 16px;color:#333">Adicionar Medicamento</h2>
  <input type="text" id="nome" placeholder="Nome do medicamento">
  <input type="text" id="dose" placeholder="Dose (ex: 20mg)">
  <input type="text" id="horarios" placeholder="Horários (ex: 08:00, 20:00)">
  <button onclick="adicionar()">+ Adicionar medicamento</button>
</div>
<h2 style="color:#333;margin-bottom:14px">Meus Medicamentos</h2>
{meds_html if meds_html else "<p style='color:#888'>Nenhum medicamento cadastrado.</p>"}
</div><script>
function adicionar(){{
  var n=document.getElementById("nome").value;
  var d=document.getElementById("dose").value;
  var h=document.getElementById("horarios").value.split(",").map(s=>s.trim());
  if(!n){{alert("Digite o nome");return;}}
  fetch("/api/v1/medicamentos/adicionar",{{method:"POST",
    headers:{{"Content-Type":"application/json"}},
    body:JSON.stringify({{nome:n,dose:d,horarios:h}})}}).then(()=>location.reload());
}}
function tomar(id){{
  fetch("/api/v1/medicamentos/tomar/"+id,{{method:"POST"}})
  .then(r=>r.json()).then(function(d){{alert("✅ "+d.msg);location.reload();}});
}}
</script></body></html>""")

class MedicamentoPlugin(PluginBase):
    name = "medicamento_tracker"
    def setup(self, app): app.include_router(router)
plugin = MedicamentoPlugin()
