#!/usr/bin/env python3
"""FAQ inteligente com busca"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/faq", tags=["FAQ"])

PERGUNTAS = [
    {"q": "O que é o PHQ-9?", "r": "O PHQ-9 é um questionário de 9 itens para rastrear depressão, baseado nos critérios do DSM-5. Scores: 0-4 sem depressão, 5-9 leve, 10-14 moderada, 15-19 moderadamente grave, 20-27 grave.", "cat": "Instrumentos"},
    {"q": "O que é o GAD-7?", "r": "O GAD-7 avalia ansiedade generalizada em 7 questões. Scores: 0-4 mínima, 5-9 leve, 10-14 moderada, 15-21 grave.", "cat": "Instrumentos"},
    {"q": "É seguro usar a plataforma?", "r": "Sim! Usamos criptografia, HTTPS, conformidade com LGPD e servidores seguros. Seus dados são protegidos.", "cat": "Segurança"},
    {"q": "Posso usar gratuitamente?", "r": "Sim! O plano Free permite avaliações ilimitadas, chat com IA e diário emocional sem custo.", "cat": "Planos"},
    {"q": "Como funciona o chat com IA?", "r": "Nossa IA usa modelos avançados (Mistral, Groq, Gemini) treinados para suporte emocional em português.", "cat": "IA"},
    {"q": "O que é o plano Clínica?", "r": "R$ 99,90/mês. Inclui prontuário completo, múltiplos pacientes, relatórios PDF e suporte prioritário.", "cat": "Planos"},
    {"q": "Como adiciono o widget no meu site?", "r": "Cole uma linha de código HTML no seu site. Veja /widget/demo para instruções.", "cat": "Widget"},
    {"q": "Como cancelo minha assinatura?", "r": "Acesse Configurações > Assinatura > Cancelar. Você mantém acesso até o fim do período pago.", "cat": "Planos"},
    {"q": "Funciona no celular?", "r": "Sim! É um PWA (Progressive Web App). Você pode instalar no celular como um app nativo.", "cat": "Mobile"},
    {"q": "Como exportar dados dos pacientes?", "r": "No dashboard do psicólogo, clique em Exportar > CSV ou PDF para baixar todos os dados.", "cat": "Dados"},
]

@router.get("", response_class=HTMLResponse)
async def pagina_faq():
    itens = ""
    for p in PERGUNTAS:
        itens += f"""
        <div class="faq-item" data-q="{p['q'].lower()}" data-r="{p['r'].lower()}">
            <div class="faq-q" onclick="toggle(this)">
                <span class="cat">{p['cat']}</span>
                {p['q']}
                <span class="arrow">▼</span>
            </div>
            <div class="faq-r">{p['r']}</div>
        </div>"""
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FAQ — Emotion Platform</title>
<meta name="description" content="Perguntas frequentes sobre o Emotion Intelligence Platform">
<style>
body{{font-family:sans-serif;background:#f8f9fa;margin:0;padding:20px}}
.container{{max-width:700px;margin:0 auto}}
h1{{color:#333}} input{{width:100%;padding:14px;border-radius:12px;border:2px solid #e0e0e0;
font-size:16px;margin-bottom:20px;box-sizing:border-box;outline:none}}
input:focus{{border-color:#667eea}}
.faq-item{{background:white;border-radius:12px;margin-bottom:12px;overflow:hidden;
           box-shadow:0 2px 8px rgba(0,0,0,0.06)}}
.faq-q{{padding:20px;cursor:pointer;display:flex;align-items:center;gap:12px;font-weight:600}}
.faq-q:hover{{background:#f8f9fa}}
.faq-r{{padding:0 20px;max-height:0;overflow:hidden;transition:all 0.3s;color:#555;line-height:1.6}}
.faq-r.open{{padding:0 20px 20px;max-height:200px}}
.arrow{{margin-left:auto;transition:transform 0.3s;font-size:12px}}
.arrow.open{{transform:rotate(180deg)}}
.cat{{background:#e8f0fe;color:#667eea;padding:2px 10px;border-radius:20px;font-size:12px;white-space:nowrap}}
.hidden{{display:none}}
</style></head><body>
<div class="container">
<a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
<h1>❓ Perguntas Frequentes</h1>
<input type="text" placeholder="🔍 Buscar pergunta..." oninput="buscar(this.value)">
{itens}
</div>
<script>
function toggle(el){{
  var r=el.nextElementSibling,a=el.querySelector(".arrow");
  r.classList.toggle("open");a.classList.toggle("open");
}}
function buscar(q){{
  q=q.toLowerCase();
  document.querySelectorAll(".faq-item").forEach(function(i){{
    i.classList.toggle("hidden",q&&!i.dataset.q.includes(q)&&!i.dataset.r.includes(q));
  }});
}}
</script></body></html>""")

@router.get("/json")
async def faq_json():
    return JSONResponse(PERGUNTAS)

class FAQPlugin(PluginBase):
    name = "faq_inteligente"
    def setup(self, app): app.include_router(router)
plugin = FAQPlugin()
