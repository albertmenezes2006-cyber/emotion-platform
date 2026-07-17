#!/usr/bin/env python3
"""Glossario completo de saude mental"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/glossario", tags=["Educação"])

TERMOS = {
    "Ansiedade": "Estado de apreensão, tensão e preocupação excessiva. Pode ser adaptativa (normal) ou patológica (GAD, fobia, pânico).",
    "Depressão": "Transtorno do humor caracterizado por tristeza persistente, perda de interesse e alterações no sono, apetite e energia.",
    "PHQ-9": "Patient Health Questionnaire-9. Instrumento de 9 itens para rastrear e medir a gravidade da depressão.",
    "GAD-7": "Generalized Anxiety Disorder 7. Escala de 7 itens para avaliar ansiedade generalizada.",
    "CBT": "Terapia Cognitivo-Comportamental. Abordagem baseada em evidências que conecta pensamentos, emoções e comportamentos.",
    "DBT": "Terapia Comportamental Dialética. Desenvolvida por Linehan para regulação emocional e tolerância ao mal-estar.",
    "ACT": "Terapia de Aceitação e Compromisso. Foca em aceitar experiências difíceis e agir de acordo com valores.",
    "EMDR": "Eye Movement Desensitization and Reprocessing. Terapia para trauma usando movimentos oculares bilaterais.",
    "Mindfulness": "Atenção plena ao momento presente, sem julgamento. Base de várias abordagens terapêuticas.",
    "Burnout": "Síndrome de esgotamento profissional com exaustão emocional, despersonalização e baixa realização.",
    "PTSD": "Transtorno de Estresse Pós-Traumático. Resposta psicológica prolongada após evento traumático.",
    "TOC": "Transtorno Obsessivo-Compulsivo. Caracterizado por obsessões (pensamentos) e compulsões (comportamentos).",
    "TDAH": "Transtorno do Déficit de Atenção e Hiperatividade. Dificuldade de atenção, impulsividade e hiperatividade.",
    "TEA": "Transtorno do Espectro Autista. Condição do neurodesenvolvimento com variações na comunicação e interação social.",
    "Psicofarmacologia": "Estudo dos efeitos de medicamentos sobre a mente, humor e comportamento.",
    "TCC": "Terapia Cognitivo-Comportamental. Versão em português do CBT.",
    "Aliança Terapêutica": "Relação de colaboração e confiança entre terapeuta e paciente. Preditor de sucesso terapêutico.",
    "Formulação de Caso": "Hipótese clínica que explica os problemas do paciente e guia o tratamento.",
    "Psicoeducação": "Processo de ensinar ao paciente sobre seu diagnóstico, tratamento e estratégias de manejo.",
    "Regulação Emocional": "Capacidade de reconhecer, compreender e gerenciar emoções de forma adaptativa.",
    "LGPD": "Lei Geral de Proteção de Dados (Lei 13.709/2018). Regula o uso de dados pessoais no Brasil.",
    "CRP": "Conselho Regional de Psicologia. Órgão regulador da profissão de psicólogo no Brasil.",
    "CFP": "Conselho Federal de Psicologia. Órgão máximo de regulação da psicologia no Brasil.",
    "CVV": "Centro de Valorização da Vida. Liga 188, disponível 24h para suporte emocional.",
    "CAPS": "Centro de Atenção Psicossocial. Serviço público de saúde mental no SUS.",
}

@router.get("", response_class=HTMLResponse)
async def pagina_glossario():
    letras = {}
    for termo, def_ in sorted(TERMOS.items()):
        l = termo[0].upper()
        if l not in letras:
            letras[l] = []
        letras[l].append((termo, def_))
    secoes = ""
    nav = ""
    for letra, itens in sorted(letras.items()):
        nav += f'<a href="#letra-{letra}" style="color:#667eea;text-decoration:none;padding:4px 8px;background:#e8f0fe;border-radius:6px;font-weight:700">{letra}</a>'
        cards = ""
        for termo, def_ in itens:
            cards += f"""
            <div style="border-bottom:1px solid #f0f0f0;padding:16px 0" id="termo-{termo.lower().replace(' ','-')}">
              <h3 style="color:#667eea;margin:0 0 6px;font-size:16px">{termo}</h3>
              <p style="color:#555;margin:0;line-height:1.6;font-size:14px">{def_}</p>
            </div>"""
        secoes += f'<div id="letra-{letra}" style="margin-bottom:32px"><h2 style="color:#333;border-bottom:2px solid #667eea;padding-bottom:8px">{letra}</h2>{cards}</div>'
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Glossário de Saúde Mental — Emotion Platform</title>
<meta name="description" content="Glossário completo de termos de saúde mental em português">
<style>
body{{font-family:sans-serif;background:#f8f9fa;padding:20px;margin:0}}
.container{{max-width:800px;margin:0 auto}}
.nav{{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0;padding:16px;
      background:white;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}}
.search{{width:100%;padding:14px;border-radius:12px;border:2px solid #e0e0e0;
  font-size:16px;box-sizing:border-box;outline:none;margin-bottom:20px}}
.search:focus{{border-color:#667eea}}
.content{{background:white;border-radius:16px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.08)}}
</style></head><body><div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1 style="color:#333;margin:16px 0">📚 Glossário de Saúde Mental</h1>
<p style="color:#888;margin-bottom:20px">{len(TERMOS)} termos explicados em português</p>
<input type="text" class="search" placeholder="🔍 Buscar termo..." oninput="buscar(this.value)">
<div class="nav">{nav}</div>
<div class="content" id="conteudo">{secoes}</div>
</div><script>
function buscar(q){{
  q=q.toLowerCase();
  document.querySelectorAll("[id^='termo-']").forEach(function(el){{
    var txt=el.textContent.toLowerCase();
    el.style.display=(!q||txt.includes(q))?"block":"none";
  }});
}}
</script></body></html>""")

@router.get("/json")
async def glossario_json():
    return JSONResponse([{"termo": k, "definicao": v} for k, v in sorted(TERMOS.items())])

class GlossarioPlugin(PluginBase):
    name = "glossario_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = GlossarioPlugin()
