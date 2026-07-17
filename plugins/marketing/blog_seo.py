#!/usr/bin/env python3
"""Blog com SEO para saude mental"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/blog", tags=["Blog"])

ARTIGOS = [
    {
        "slug": "o-que-e-phq9",
        "titulo": "O que é PHQ-9? Guia completo para psicólogos",
        "descricao": "Entenda como usar o PHQ-9 na prática clínica para avaliar depressão",
        "categoria": "Instrumentos",
        "data": "17/07/2026",
        "tempo_leitura": "5 min",
        "conteudo": """
        <h2>O que é o PHQ-9?</h2>
        <p>O PHQ-9 (Patient Health Questionnaire-9) é um instrumento de rastreio
        de depressão amplamente utilizado na prática clínica e em pesquisas.
        É composto por 9 itens baseados nos critérios diagnósticos do DSM-5.</p>
        <h2>Como interpretar os resultados?</h2>
        <ul>
            <li><strong>0-4:</strong> Sem depressão significativa</li>
            <li><strong>5-9:</strong> Depressão leve</li>
            <li><strong>10-14:</strong> Depressão moderada</li>
            <li><strong>15-19:</strong> Depressão moderadamente grave</li>
            <li><strong>20-27:</strong> Depressão grave</li>
        </ul>
        <h2>Validação brasileira</h2>
        <p>O PHQ-9 foi validado para a população brasileira por Santos et al. (2013),
        demonstrando excelente sensibilidade (88%) e especificidade (88%).</p>
        """
    },
    {
        "slug": "gad7-ansiedade-clinica",
        "titulo": "GAD-7: Como usar na avaliação de ansiedade",
        "descricao": "Guia prático do GAD-7 para psicólogos e profissionais de saúde mental",
        "categoria": "Instrumentos",
        "data": "16/07/2026",
        "tempo_leitura": "4 min",
        "conteudo": """
        <h2>O GAD-7 na prática</h2>
        <p>O Generalized Anxiety Disorder 7-item (GAD-7) é uma escala de auto-relato
        desenvolvida para rastrear e medir a gravidade do transtorno de ansiedade generalizada.</p>
        <h2>Pontuação e interpretação</h2>
        <ul>
            <li><strong>0-4:</strong> Ansiedade mínima</li>
            <li><strong>5-9:</strong> Ansiedade leve</li>
            <li><strong>10-14:</strong> Ansiedade moderada</li>
            <li><strong>15-21:</strong> Ansiedade grave</li>
        </ul>
        """
    },
    {
        "slug": "ia-saude-mental-futuro",
        "titulo": "IA na saúde mental: o futuro da psicologia digital",
        "descricao": "Como a inteligência artificial está transformando o cuidado em saúde mental",
        "categoria": "Tecnologia",
        "data": "15/07/2026",
        "tempo_leitura": "7 min",
        "conteudo": """
        <h2>IA e Psicologia: Uma parceria promissora</h2>
        <p>A inteligência artificial está revolucionando a forma como psicólogos
        avaliam, monitoram e tratam seus pacientes. Ferramentas como o Emotion
        Intelligence Platform combinam IA com instrumentos validados cientificamente.</p>
        <h2>Benefícios para psicólogos</h2>
        <ul>
            <li>Avaliações padronizadas e objetivas</li>
            <li>Monitoramento contínuo entre sessões</li>
            <li>Relatórios automáticos para evolução</li>
            <li>Alertas de risco em tempo real</li>
        </ul>
        """
    }
]

def card_artigo(a):
    return f"""
    <article style="background:white;border-radius:16px;padding:24px;
                    margin-bottom:16px;box-shadow:0 2px 8px rgba(0,0,0,0.08);
                    transition:transform 0.2s;cursor:pointer"
             onclick="location.href='/blog/{a['slug']}'">
        <div style="display:flex;justify-content:space-between;margin-bottom:8px">
            <span style="background:#e8f0fe;color:#667eea;padding:4px 12px;
                         border-radius:20px;font-size:13px">{a['categoria']}</span>
            <span style="color:#888;font-size:13px">{a['tempo_leitura']} leitura</span>
        </div>
        <h2 style="color:#333;font-size:20px;margin:8px 0">{a['titulo']}</h2>
        <p style="color:#666;line-height:1.6">{a['descricao']}</p>
        <div style="color:#888;font-size:13px;margin-top:12px">{a['data']}</div>
    </article>"""

@router.get("", response_class=HTMLResponse)
async def lista_blog():
    cards = "".join(card_artigo(a) for a in ARTIGOS)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog — Emotion Platform | Saúde Mental com IA</title>
    <meta name="description" content="Artigos sobre saúde mental, psicologia digital e uso de IA na prática clínica">
    <meta property="og:title" content="Blog Emotion Platform">
    <meta property="og:type" content="website">
    <style>
        body {{ font-family: sans-serif; background: #f8f9fa; margin: 0; padding: 20px; }}
        .container {{ max-width: 700px; margin: 0 auto; }}
        h1 {{ color: #333; }}
        article:hover {{ transform: translateY(-2px); }}
    </style>
</head>
<body>
<div class="container">
    <a href="/" style="color:#667eea;text-decoration:none">← Voltar</a>
    <h1 style="margin:16px 0 8px">📝 Blog — Saúde Mental com IA</h1>
    <p style="color:#888;margin-bottom:24px">Artigos para psicólogos e profissionais de saúde mental</p>
    {cards}
</div>
</body>
</html>""")

@router.get("/{slug}", response_class=HTMLResponse)
async def artigo_blog(slug: str):
    artigo = next((a for a in ARTIGOS if a["slug"] == slug), None)
    if not artigo:
        return HTMLResponse("<h1>Artigo não encontrado</h1>", status_code=404)
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{artigo['titulo']} — Emotion Platform</title>
    <meta name="description" content="{artigo['descricao']}">
    <meta property="og:title" content="{artigo['titulo']}">
    <meta property="og:description" content="{artigo['descricao']}">
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{artigo['titulo']}",
        "description": "{artigo['descricao']}",
        "datePublished": "{artigo['data']}",
        "publisher": {{
            "@type": "Organization",
            "name": "Emotion Intelligence Platform"
        }}
    }}
    </script>
    <style>
        body {{ font-family: sans-serif; background: #f8f9fa; margin: 0; padding: 20px; }}
        .container {{ max-width: 700px; margin: 0 auto; background: white;
                     border-radius: 16px; padding: 40px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        h1 {{ color: #333; font-size: 28px; line-height: 1.3; }}
        h2 {{ color: #444; margin-top: 28px; }}
        p, li {{ color: #555; line-height: 1.8; }}
        .meta {{ color: #888; font-size: 14px; margin: 12px 0 24px; }}
        .cta {{ background: linear-gradient(135deg, #667eea, #764ba2);
               color: white; padding: 20px; border-radius: 12px;
               text-align: center; margin-top: 32px; }}
        .cta a {{ color: white; font-weight: 700; font-size: 16px; }}
    </style>
</head>
<body>
<div style="max-width:700px;margin:0 auto;padding:20px">
    <a href="/blog" style="color:#667eea;text-decoration:none">← Blog</a>
</div>
<div class="container">
    <span style="background:#e8f0fe;color:#667eea;padding:4px 12px;
                 border-radius:20px;font-size:13px">{artigo['categoria']}</span>
    <h1 style="margin-top:12px">{artigo['titulo']}</h1>
    <div class="meta">{artigo['data']} · {artigo['tempo_leitura']} de leitura</div>
    {artigo['conteudo']}
    <div class="cta">
        <p style="color:white;margin:0 0 12px">Experimente grátis no Emotion Platform</p>
        <a href="/app/avaliacao">🚀 Fazer avaliação PHQ-9 agora →</a>
    </div>
</div>
</body>
</html>""")

class BlogPlugin(PluginBase):
    name = "blog_seo"
    def setup(self, app):
        app.include_router(router)

plugin = BlogPlugin()
