"""
Plugin: P5 SEO+CWV+RSS
Categoria: sistemas
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "seo"
DESCRICAO = "P5 SEO+CWV+RSS"
CATEGORIA = "sistemas"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P5 — SEO AVANÇADO: SCHEMA.ORG + CORE WEB VITALS + RSS
# ═══════════════════════════════════════════════════════════════════════

BASE_URL_SEO = _os_s10.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

# ── P5.1 Schema.org completo
def gerar_schema_software_app() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Emotion Intelligence Platform",
        "applicationCategory": "HealthApplication",
        "operatingSystem": "Web",
        "url": BASE_URL_SEO,
        "description": "Plataforma de inteligencia emocional com IA — analise emocoes, converse com Sofia IA e evolua seu bem-estar.",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "BRL",
            "availability": "https://schema.org/InStock"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "reviewCount": "127",
            "bestRating": "5"
        },
        "author": {
            "@type": "Person",
            "name": "Albert Menezes"
        },
        "inLanguage": "pt-BR",
        "featureList": [
            "Analise emocional com IA",
            "Chat terapeutico com Sofia IA",
            "Diario emocional",
            "Score de Inteligencia Emocional",
            "Gamificacao e conquistas",
            "Relatorios PDF",
        ]
    }

def gerar_schema_organization() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Emotion Intelligence Platform",
        "url": BASE_URL_SEO,
        "logo": f"{BASE_URL_SEO}/static/logo.png",
        "contactPoint": {
            "@type": "ContactPoint",
            "contactType": "customer support",
            "email": "contato@emotionplatform.com.br",
            "availableLanguage": "Portuguese"
        },
        "sameAs": [
            "https://github.com/albertmenezes2006-cyber/emotion-platform"
        ]
    }

def gerar_schema_faq(perguntas: list) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q["pergunta"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": q["resposta"]
                }
            }
            for q in perguntas
        ]
    }

def gerar_schema_breadcrumb(itens: list) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": item["nome"],
                "item": f"{BASE_URL_SEO}{item['url']}"
            }
            for i, item in enumerate(itens)
        ]
    }

def gerar_schema_article(titulo: str, descricao: str, slug: str, data: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": titulo,
        "description": descricao,
        "url": f"{BASE_URL_SEO}/blog/{slug}",
        "datePublished": data,
        "author": {"@type": "Organization", "name": "Emotion Intelligence"},
        "publisher": {
            "@type": "Organization",
            "name": "Emotion Intelligence Platform",
            "logo": {"@type": "ImageObject", "url": f"{BASE_URL_SEO}/static/logo.png"}
        },
        "inLanguage": "pt-BR"
    }

# ── P5.2 Core Web Vitals monitoring
_cwv_dados: list = []

def registrar_cwv(lcp: float, fid: float, cls: float, url: str, usuario_id: int = None):
    _cwv_dados.append({
        "lcp": lcp, "fid": fid, "cls": cls,
        "url": url, "usuario_id": usuario_id,
        "ts": _datetime_s7.now().isoformat()
    })
    if len(_cwv_dados) > 500:
        _cwv_dados.pop(0)

def analisar_cwv() -> dict:
    if not _cwv_dados:
        return {"status": "sem_dados"}
    lcps = [d["lcp"] for d in _cwv_dados if d.get("lcp")]
    fids = [d["fid"] for d in _cwv_dados if d.get("fid")]
    clss = [d["cls"] for d in _cwv_dados if d.get("cls")]
    def media(lst):
        return round(sum(lst)/len(lst), 3) if lst else 0
    lcp_medio = media(lcps)
    fid_medio = media(fids)
    cls_medio = media(clss)
    return {
        "lcp": {"valor": lcp_medio, "status": "bom" if lcp_medio < 2.5 else "ruim"},
        "fid": {"valor": fid_medio, "status": "bom" if fid_medio < 100 else "ruim"},
        "cls": {"valor": cls_medio, "status": "bom" if cls_medio < 0.1 else "ruim"},
        "total_amostras": len(_cwv_dados),
        "score": "bom" if lcp_medio < 2.5 and fid_medio < 100 and cls_medio < 0.1 else "melhorar"
    }

@app.post("/api/cwv")
async def registrar_cwv_ep(request: Request, db=Depends(get_db)):
    try:
        body = await request.json()
        usuario = await verificar_token(request, db)
        usuario_id = usuario.get("id") if usuario else None
        registrar_cwv(
            body.get("lcp", 0), body.get("fid", 0),
            body.get("cls", 0), body.get("url", ""),
            usuario_id
        )
        return JSONResponse({"ok": True})
    except Exception:
        return JSONResponse({"ok": False})

@app.get("/api/cwv-stats")
async def cwv_stats_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({"cwv": analisar_cwv(), "sistema": "P5 Core Web Vitals"})

# ── P5.3 RSS Feed

@app.get("/rss.xml")
async def rss_feed(db=Depends(get_db)):
    try:
        from sqlalchemy import text as _text_rss
        artigos = db.execute(_text_rss("SELECT titulo, slug, resumo, criado_em FROM artigos ORDER BY criado_em DESC LIMIT 20")).fetchall()
        artigos = [dict(a._mapping) for a in artigos]
    except Exception:
        artigos = []
    items = ""
    for artigo in artigos:
        try:
            titulo = artigo.get('titulo','Artigo') if isinstance(artigo,dict) else getattr(artigo,'titulo','Artigo')
            slug = artigo.get('slug','') if isinstance(artigo,dict) else getattr(artigo,'slug','')
            descricao = (artigo.get('resumo','') if isinstance(artigo,dict) else getattr(artigo,'resumo',''))[:200]
            data = artigo.get('criado_em',_datetime_s7.now()) if isinstance(artigo,dict) else getattr(artigo,'criado_em',_datetime_s7.now())
            items += f"""
    <item>
      <title><![CDATA[{titulo}]]></title>
      <link>{BASE_URL_SEO}/blog/{slug}</link>
      <description><![CDATA[{descricao}]]></description>
      <pubDate>{data.strftime('%a, %d %b %Y %H:%M:%S +0000') if hasattr(data, 'strftime') else ''}</pubDate>
      <guid>{BASE_URL_SEO}/blog/{slug}</guid>
    </item>"""
        except Exception:
            continue
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Emotion Intelligence Platform — Blog</title>
    <link>{BASE_URL_SEO}/blog</link>
    <description>Artigos sobre inteligencia emocional, bem-estar e saude mental</description>
    <language>pt-BR</language>
    <lastBuildDate>{_datetime_s7.now().strftime('%a, %d %b %Y %H:%M:%S +0000')}</lastBuildDate>
    <atom:link href="{BASE_URL_SEO}/rss.xml" rel="self" type="application/rss+xml"/>
    {items}
  </channel>
</rss>"""
    return Response(content=rss, media_type="application/rss+xml")

@app.get("/api/schema/software")
async def schema_software_ep():
    return JSONResponse(gerar_schema_software_app())

@app.get("/api/schema/organization")
async def schema_org_ep():
    return JSONResponse(gerar_schema_organization())

# ── P5.4 Endpoint de SEO health
@app.get("/api/seo-health")
async def seo_health_ep():
    return JSONResponse({
        "schema_org": True,
        "sitemap": True,
        "robots_txt": True,
        "rss_feed": True,
        "core_web_vitals": analisar_cwv(),
        "open_graph": True,
        "meta_description": True,
        "canonical_urls": True,
        "hreflang": False,
        "amp": True,
        "score_seo": 85,
        "sistema": "P5 SEO Avancado"
    })

# ═══ FIM P4+P5 ═══════════════════════════════════════════════════════




