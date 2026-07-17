#!/usr/bin/env python3
"""Sistema de metas pessoais"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/metas", tags=["Metas"])
ARQUIVO = Path("metas_pessoais.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/criar")
async def criar_meta(request: Request):
    d = await request.json()
    metas = carregar()
    meta = {
        "id": len(metas) + 1,
        "titulo": d.get("titulo", ""),
        "descricao": d.get("descricao", ""),
        "prazo": d.get("prazo", ""),
        "categoria": d.get("categoria", "saude"),
        "progresso": 0,
        "status": "ativa",
        "criada_em": datetime.utcnow().isoformat()
    }
    metas.append(meta)
    ARQUIVO.write_text(json.dumps(metas, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "meta": meta})

@router.put("/progresso/{meta_id}")
async def atualizar_progresso(meta_id: int, request: Request):
    d = await request.json()
    metas = carregar()
    for m in metas:
        if m["id"] == meta_id:
            m["progresso"] = min(100, max(0, d.get("progresso", m["progresso"])))
            if m["progresso"] >= 100:
                m["status"] = "concluida"
    ARQUIVO.write_text(json.dumps(metas, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True})

@router.get("/listar")
async def listar_metas(status: str = "ativa"):
    metas = carregar()
    if status:
        metas = [m for m in metas if m["status"] == status]
    return JSONResponse({"metas": metas, "total": len(metas)})

@router.get("/pagina", response_class=HTMLResponse)
async def pagina_metas():
    metas = [m for m in carregar() if m["status"] == "ativa"]
    cards = ""
    for m in metas:
        cat_cores = {"saude": "#38a169", "trabalho": "#667eea",
                     "relacionamentos": "#e91e8c", "pessoal": "#f59e0b"}
        cor = cat_cores.get(m["categoria"], "#667eea")
        cards += f"""
        <div style="background:white;border-radius:16px;padding:24px;margin-bottom:16px;
                    box-shadow:0 4px 20px rgba(0,0,0,0.08)">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
            <h3 style="margin:0;color:#333">{m['titulo']}</h3>
            <span style="background:{cor};color:white;padding:3px 10px;
                         border-radius:20px;font-size:12px">{m['categoria']}</span>
          </div>
          <p style="color:#666;font-size:14px;margin:0 0 12px">{m['descricao']}</p>
          <div style="background:#f0f0f0;border-radius:20px;height:10px;overflow:hidden">
            <div style="background:{cor};height:100%;width:{m['progresso']}%;
                        border-radius:20px;transition:width 0.5s"></div>
          </div>
          <div style="display:flex;justify-content:space-between;margin-top:6px;
                      font-size:13px;color:#888">
            <span>Prazo: {m.get('prazo','Sem prazo')}</span>
            <span>{m['progresso']}% concluído</span>
          </div>
          <input type="range" min="0" max="100" value="{m['progresso']}"
            onchange="atualizar({m['id']},this.value)"
            style="width:100%;margin-top:12px">
        </div>"""
    if not cards:
        cards = "<p style='color:#888;text-align:center'>Nenhuma meta ativa. Crie sua primeira meta!</p>"
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Metas Pessoais — Emotion Platform</title>
<style>body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.container{{max-width:700px;margin:0 auto}}
.form{{background:white;border-radius:16px;padding:24px;margin-bottom:24px;
       box-shadow:0 4px 20px rgba(0,0,0,0.08)}}
input,select,textarea{{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;
  margin-bottom:8px;font-size:14px;box-sizing:border-box;font-family:inherit}}
input:focus,select:focus,textarea:focus{{border-color:#667eea;outline:none}}
button{{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;
  border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}}
</style></head><body>
<div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">🎯 Metas Pessoais</h1>
<div class="form">
  <h2 style="margin:0 0 16px;color:#333">Nova Meta</h2>
  <input type="text" id="titulo" placeholder="Ex: Reduzir ansiedade em 30 dias">
  <textarea id="descricao" placeholder="Descreva sua meta..." rows="3"></textarea>
  <select id="categoria">
    <option value="saude">Saúde Mental</option>
    <option value="trabalho">Trabalho</option>
    <option value="relacionamentos">Relacionamentos</option>
    <option value="pessoal">Desenvolvimento Pessoal</option>
  </select>
  <input type="date" id="prazo" placeholder="Prazo (opcional)">
  <button onclick="criar()">🎯 Criar meta</button>
</div>
<h2 style="color:#333;margin-bottom:16px">Minhas Metas</h2>
{cards}
</div>
<script>
function criar(){{
  var d={{titulo:document.getElementById("titulo").value,
    descricao:document.getElementById("descricao").value,
    categoria:document.getElementById("categoria").value,
    prazo:document.getElementById("prazo").value}};
  if(!d.titulo){{alert("Digite o título da meta");return;}}
  fetch("/api/v1/metas/criar",{{method:"POST",
    headers:{{"Content-Type":"application/json"}},
    body:JSON.stringify(d)}}).then(()=>location.reload());
}}
function atualizar(id,prog){{
  fetch("/api/v1/metas/progresso/"+id,{{method:"PUT",
    headers:{{"Content-Type":"application/json"}},
    body:JSON.stringify({{progresso:parseInt(prog)}})
  }}).then(()=>{{if(parseInt(prog)>=100)location.reload();}});
}}
</script></body></html>""")

class MetasPlugin(PluginBase):
    name = "metas_pessoais"
    def setup(self, app): app.include_router(router)
plugin = MetasPlugin()
