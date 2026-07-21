#!/usr/bin/env python3
"""Formulacao de caso clinico estruturada"""
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json
from pathlib import Path

router = APIRouter(prefix="/api/v1/formulacao-caso", tags=["Clínico"])
ARQUIVO = Path("formulacoes_caso.json")

def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text())
    return []

@router.post("/salvar")
async def salvar_formulacao(request: Request):
    d = await request.json()
    formulacoes = carregar()
    formulacoes.append({**d, "id": len(formulacoes)+1,
                        "criado_em": datetime.utcnow().isoformat()})
    ARQUIVO.write_text(json.dumps(formulacoes, ensure_ascii=False, indent=2))
    return JSONResponse({"ok": True, "id": len(formulacoes)})

@router.get("/listar")
async def listar_formulacoes():
    return JSONResponse({"formulacoes": carregar(), "total": len(carregar())})

@router.get("", response_class=HTMLResponse)
async def pagina_formulacao():
    return HTMLResponse("""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Formulação de Caso — Emotion Platform</title>
<style>
body{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}
.container{max-width:800px;margin:0 auto}
.secao{background:white;border-radius:16px;padding:24px;margin-bottom:16px;
       box-shadow:0 4px 20px rgba(0,0,0,0.08)}
.secao h2{color:#667eea;margin:0 0 16px;font-size:18px;
          border-bottom:2px solid #e8f0fe;padding-bottom:8px}
textarea{width:100%;padding:12px;border-radius:8px;border:2px solid #e0e0e0;
  font-size:14px;resize:vertical;box-sizing:border-box;font-family:inherit;min-height:80px}
textarea:focus{border-color:#667eea;outline:none}
input{width:100%;padding:10px;border-radius:8px;border:2px solid #e0e0e0;
  font-size:14px;box-sizing:border-box}
input:focus{border-color:#667eea;outline:none}
button{background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;
  border-radius:12px;padding:14px;font-size:16px;font-weight:700;width:100%;cursor:pointer}
label{display:block;font-weight:600;color:#444;margin:12px 0 4px;font-size:14px}
</style></head><body>
<div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">📋 Formulação de Caso Clínico</h1>
<p style="color:#888;margin-bottom:24px">Modelo estruturado baseado em TCC para compreensão do paciente</p>

<div class="secao">
  <h2>1. Identificação</h2>
  <label>Nome (iniciais ou fictício)</label><input type="text" id="nome" placeholder="Ex: M.S.">
  <label>Idade</label><input type="text" id="idade" placeholder="Ex: 34 anos">
  <label>Encaminhamento / Demanda inicial</label>
  <textarea id="demanda" placeholder="Por que o paciente procurou atendimento?"></textarea>
</div>

<div class="secao">
  <h2>2. Problemas Apresentados</h2>
  <label>Queixas principais</label>
  <textarea id="queixas" placeholder="Quais são os problemas principais relatados pelo paciente?"></textarea>
  <label>Comportamentos problemáticos</label>
  <textarea id="comportamentos" placeholder="Quais comportamentos estão mantendo ou agravando os problemas?"></textarea>
</div>

<div class="secao">
  <h2>3. História de Desenvolvimento</h2>
  <label>Eventos relevantes da história de vida</label>
  <textarea id="historia" placeholder="Infância, relacionamentos, perdas, traumas, conquistas..."></textarea>
  <label>História familiar</label>
  <textarea id="familia" placeholder="Dinâmica familiar, saúde mental na família..."></textarea>
</div>

<div class="secao">
  <h2>4. Fatores Predisponentes / Precipitantes / Mantenedores</h2>
  <label>Predisponentes (vulnerabilidades)</label>
  <textarea id="pred" placeholder="O que tornou o paciente vulnerável? Biológico, psicológico, social..."></textarea>
  <label>Precipitantes (desencadeadores)</label>
  <textarea id="prec" placeholder="O que desencadeou o problema atual?"></textarea>
  <label>Mantenedores (o que mantém o problema)</label>
  <textarea id="mant" placeholder="Evitação, reforços, crenças, sistema de apoio..."></textarea>
</div>

<div class="secao">
  <h2>5. Crenças Centrais e Intermediárias</h2>
  <label>Crenças centrais identificadas</label>
  <textarea id="crencas_centrais" placeholder="Ex: 'Sou incapaz', 'Não sou amável', 'O mundo é perigoso'"></textarea>
  <label>Regras e suposições</label>
  <textarea id="regras" placeholder="Ex: 'Se eu falhar, serei rejeitado'"></textarea>
</div>

<div class="secao">
  <h2>6. Hipótese Diagnóstica</h2>
  <label>Diagnóstico(s) provável(is)</label>
  <input type="text" id="diagnostico" placeholder="Ex: F32.1 Episódio Depressivo Moderado (CID-10)">
  <label>Diagnósticos diferenciais</label>
  <textarea id="diferenciais" placeholder="Quais outros diagnósticos considerar?"></textarea>
</div>

<div class="secao">
  <h2>7. Plano Terapêutico</h2>
  <label>Objetivos terapêuticos</label>
  <textarea id="objetivos" placeholder="O que se pretende alcançar com o tratamento?"></textarea>
  <label>Intervenções planejadas</label>
  <textarea id="intervencoes" placeholder="Técnicas, abordagens, frequência de sessões..."></textarea>
  <label>Indicadores de progresso</label>
  <textarea id="indicadores" placeholder="Como saberemos que houve melhora?"></textarea>
</div>

<button onclick="salvar()">💾 Salvar Formulação</button>
</div>
<script>
function salvar(){
  var campos=['nome','idade','demanda','queixas','comportamentos','historia',
    'familia','pred','prec','mant','crencas_centrais','regras',
    'diagnostico','diferenciais','objetivos','intervencoes','indicadores'];
  var d={};
  campos.forEach(function(c){
    var el=document.getElementById(c);
    d[c]=el?el.value:"";
  });
  if(!d.nome){alert("Informe a identificação do paciente");return;}
  fetch("/api/v1/formulacao-caso/salvar",{method:"POST",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(d)})
  .then(r=>r.json()).then(function(r){
    alert("✅ Formulação salva! ID: "+r.id);
  });
}
</script></body></html>""")

class FormulacaoPlugin(PluginBase):
    name = "formulacao_caso_clinico"
    def setup(self, app): app.include_router(router)
plugin = FormulacaoPlugin()
