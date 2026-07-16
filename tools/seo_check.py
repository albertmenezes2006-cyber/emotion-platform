#!/usr/bin/env python3
import urllib.request
import urllib.error
import re
import time

BASE = "https://emotion-platform-albert.onrender.com"

OK = 0
WARN = 0
ERR = 0


def ok_msg(msg):
    global OK
    OK += 1
    print(f"  OK   {msg}")


def warn_msg(msg):
    global WARN
    WARN += 1
    print(f"  WARN {msg}")


def err_msg(msg):
    global ERR
    ERR += 1
    print(f"  ERR  {msg}")


def buscar(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=20) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception:
        return 0, ""


print("=== ANALISE SEO ===")
print(f"Site: {BASE}")
print()

status_home, html = buscar("/")
if status_home != 200:
    err_msg(f"Home nao carrega: HTTP {status_home}")
else:
    ok_msg(f"Home carrega: HTTP {status_home}")

# Title
titles = re.findall(r"<title>([^<]+)</title>", html)
if titles and len(titles[0]) >= 10:
    ok_msg(f"Title: '{titles[0][:60]}'")
elif titles:
    warn_msg(f"Title curto: '{titles[0]}'")
else:
    err_msg("Title ausente!")

# Meta description — sem aspas mistas no regex
desc_pattern = re.compile(r'name=.description.[^>]*content=.([^"'> ]{10,})', re.IGNORECASE)
descs = desc_pattern.findall(html)
if descs:
    ok_msg(f"Meta description encontrada")
else:
    warn_msg("Meta description ausente ou curta")

# Open Graph
if "og:title" in html:
    ok_msg("Open Graph tags presentes")
else:
    warn_msg("Sem Open Graph tags")

# Canonical
if "canonical" in html:
    ok_msg("Canonical URL presente")
else:
    warn_msg("Sem canonical URL")

# H1
h1s = re.findall(r"<h1[^>]*>", html, re.IGNORECASE)
if len(h1s) == 1:
    ok_msg("H1 unico presente")
elif len(h1s) == 0:
    err_msg("Sem H1!")
else:
    warn_msg(f"{len(h1s)} H1s (deve ser 1)")

# Sitemap
s_sm, _ = buscar("/sitemap.xml")
if s_sm == 200:
    ok_msg("sitemap.xml disponivel")
else:
    err_msg("sitemap.xml nao encontrado!")

# Robots
s_rb, _ = buscar("/robots.txt")
if s_rb == 200:
    ok_msg("robots.txt disponivel")
else:
    warn_msg("robots.txt nao encontrado")

# Velocidade
try:
    inicio = time.time()
    urllib.request.urlopen(BASE + "/app/avaliacao", timeout=30).read()
    ms = round((time.time() - inicio) * 1000)
    if ms < 800:
        ok_msg(f"Velocidade avaliacao: {ms}ms")
    elif ms < 2000:
        warn_msg(f"Lento: {ms}ms")
    else:
        err_msg(f"Muito lento: {ms}ms")
except Exception:
    warn_msg("Nao foi possivel medir velocidade")

# Viewport
if 'name="viewport"' in html:
    ok_msg("Mobile-friendly (viewport)")
else:
    err_msg("Sem viewport!")

# HTTPS
if BASE.startswith("https"):
    ok_msg("HTTPS ativo (fator ranking Google)")
else:
    err_msg("Sem HTTPS!")

print()
total = OK + WARN + ERR
score = round(OK / total * 100) if total > 0 else 0
print(f"SEO Score: {score}% ({OK} ok / {WARN} avisos / {ERR} erros)")
print()
print("Verificar tambem:")
print(f"  https://pagespeed.web.dev/?url={BASE}/app/avaliacao")
print(f"  https://search.google.com/search-console")
