#!/usr/bin/env python3
"""Sitemap dinâmico com artigos do blog"""
from fastapi import APIRouter
from fastapi.responses import Response
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(tags=["SEO"])

BASE = "https://emotion-platform-albert.onrender.com"

URLS = [
    ("/", "1.0", "daily"),
    ("/planos", "0.9", "weekly"),
    ("/sobre", "0.8", "monthly"),
    ("/faq", "0.8", "weekly"),
    ("/contato", "0.7", "monthly"),
    ("/psicologos", "0.9", "weekly"),
    ("/terapia", "0.8", "weekly"),
    ("/blog", "0.9", "daily"),
    ("/blog/phq9-guia", "0.8", "monthly"),
    ("/blog/gad7-guia", "0.8", "monthly"),
    ("/blog/telepsicologia", "0.8", "monthly"),
    ("/comparativo", "0.9", "weekly"),
    ("/afiliado", "0.7", "monthly"),
    ("/privacidade", "0.5", "monthly"),
    ("/termos", "0.5", "monthly"),
]

@router.get("/sitemap.xml")
async def sitemap():
    hoje = datetime.now().strftime("%Y-%m-%d")
    urls_xml = ""
    for url, priority, freq in URLS:
        urls_xml += f"""
  <url>
    <loc>{BASE}{url}</loc>
    <lastmod>{hoje}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
    
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}
</urlset>'''
    return Response(xml, media_type="application/xml")

class SitemapDinamicoPlugin(PluginBase):
    name = "sitemap_dinamico_v2"
    def setup(self, app):
        app.include_router(router)

plugin = SitemapDinamicoPlugin()
