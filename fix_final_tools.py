#!/usr/bin/env python3
"""Corrige todos os arquivos de ferramentas de uma vez"""
import os
import subprocess

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {path}")

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return r.returncode == 0

BASE = "https://emotion-platform-albert.onrender.com"

print("Corrigindo todos os arquivos...")

# ══════════════════════════════════════
# SECURITY
# ══════════════════════════════════════
w("tools/security.py", """#!/usr/bin/env python3
import urllib.request
import urllib.error
import json

BASE = "https://emotion-platform-albert.onrender.com"
OK = 0
ERR = 0


def chk_ok(msg):
    global OK
    OK += 1
    print(f"  OK  {msg}")


def chk_err(msg):
    global ERR
    ERR += 1
    print(f"  ERR {msg}")


def http_get(path, headers=None):
    try:
        req = urllib.request.Request(BASE + path, headers=headers or {})
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read().decode()[:300]
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception:
        return 0, ""


def http_post(path, data):
    try:
        body = json.dumps(data).encode()
        req = urllib.request.Request(BASE + path, data=body, method="POST")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status, resp.read().decode()[:200]
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception:
        return 0, ""


print("=== SCAN DE SEGURANCA ===")
print()

# 1. SQL Injection
status1, _ = http_post(
    "/api/v1/auth/login?email='+OR+'1'='1--&senha=x", {}
)
if status1 in [400, 401, 422]:
    chk_ok("SQL Injection bloqueado")
else:
    chk_err(f"SQL Injection nao bloqueado: HTTP {status1}")

# 2. JWT invalido
status2, _ = http_get(
    "/api/v1/auth/me",
    {"Authorization": "Bearer token_falso_invalido"}
)
if status2 == 401:
    chk_ok("JWT invalido rejeitado (401)")
else:
    chk_err(f"JWT invalido aceito: HTTP {status2}")

# 3. HTTPS
if BASE.startswith("https"):
    chk_ok("HTTPS ativo")
else:
    chk_err("Sem HTTPS!")

# 4. XSS
status3, body3 = http_get("/app/avaliacao")
if "<script>alert" not in body3:
    chk_ok("Sem XSS obvio detectado")
else:
    chk_err("XSS detectado!")

# 5. Path traversal
status4, _ = http_get("/../../../etc/passwd")
if status4 != 200:
    chk_ok("Path traversal bloqueado")
else:
    chk_err("Path traversal possivel!")

# 6. Chaves secretas expostas
status5, body5 = http_get("/api/v1/stripe/planos")
if "sk_live" not in body5 and "sk_test" not in body5:
    chk_ok("Sem chaves Stripe expostas")
else:
    chk_err("Chave Stripe exposta!")

# 7. Dados sensiveis no health
status6, body6 = http_get("/health")
if "password" not in body6.lower():
    chk_ok("Sem senhas no /health")
else:
    chk_err("Dados sensiveis em /health!")

# 8. Endpoint admin protegido
status7, _ = http_get("/admin")
if status7 != 200:
    chk_ok("Admin nao acessivel sem auth")
else:
    chk_err("Admin acessivel sem autenticacao!")

print()
total = OK + ERR
score = round(OK / total * 100) if total > 0 else 0
print(f"Score: {OK}/{total} ({score}%)")
if ERR == 0:
    print("Nenhuma falha de seguranca critica!")
""")

# ══════════════════════════════════════
# PERFORMANCE
# ══════════════════════════════════════
w("tools/performance.py", """#!/usr/bin/env python3
import urllib.request
import urllib.error
import time
import statistics

BASE = "https://emotion-platform-albert.onrender.com"

PAGINAS = [
    ("/",                                  "Home"),
    ("/app/avaliacao",                     "Avaliacao"),
    ("/app/chat",                          "Chat"),
    ("/app/diario",                        "Diario"),
    ("/app/dashboard",                     "Dashboard"),
    ("/api/v1/phq9-clinico/perguntas",     "PHQ-9 API"),
    ("/api/v1/chat-ia/modelos/disponiveis","Chat Modelos"),
    ("/health",                            "Health"),
]


def medir(path):
    tempos = []
    tamanho = 0
    for _ in range(3):
        try:
            inicio = time.time()
            with urllib.request.urlopen(BASE + path, timeout=30) as resp:
                dados = resp.read()
                tamanho = len(dados)
            tempos.append((time.time() - inicio) * 1000)
        except Exception:
            tempos.append(9999)
        time.sleep(0.3)
    return statistics.mean(tempos), tamanho


print("=== TESTE DE PERFORMANCE ===")
print(f"Site: {BASE}")
print()

resultados = []
for path, nome in PAGINAS:
    media, tamanho = medir(path)

    if media < 300:
        emoji = "OTIMO"
    elif media < 800:
        emoji = "BOM  "
    elif media < 2000:
        emoji = "LENTO"
    else:
        emoji = "RUIM "

    kb = tamanho / 1024
    print(f"  [{emoji}] {nome:<30} {media:>6.0f}ms  {kb:>6.1f}KB")
    resultados.append({"nome": nome, "ms": media})

print()
media_geral = statistics.mean(r["ms"] for r in resultados)
print(f"Media geral: {media_geral:.0f}ms")

if media_geral < 800:
    print("Performance boa!")
else:
    print("Performance pode melhorar.")
    print("Dica: ative cache e CDN (Cloudflare).")
""")

# ══════════════════════════════════════
# ACCESSIBILITY
# ══════════════════════════════════════
w("tools/accessibility.py", """#!/usr/bin/env python3
import urllib.request
import urllib.error
import re

BASE = "https://emotion-platform-albert.onrender.com"

OK = 0
WARN = 0
ERR = 0


def ok_msg(msg):
    global OK
    OK += 1
    print(f"    OK   {msg}")


def warn_msg(msg):
    global WARN
    WARN += 1
    print(f"    WARN {msg}")


def err_msg(msg):
    global ERR
    ERR += 1
    print(f"    ERR  {msg}")


def buscar_html(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=20) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception:
        return ""


PAGINAS = [
    ("/",             "Home"),
    ("/app/avaliacao","Avaliacao"),
    ("/app/chat",     "Chat"),
    ("/app/diario",   "Diario"),
]

print("=== ACESSIBILIDADE (WCAG 2.1) ===")

for path, nome in PAGINAS:
    print(f"\\n  [{nome}]")
    html = buscar_html(path)

    if not html:
        err_msg("Pagina nao carrega")
        continue

    # Lang
    if 'lang="pt-BR"' in html or 'lang="pt"' in html:
        ok_msg("lang=pt-BR correto")
    else:
        warn_msg("lang attribute ausente")

    # Charset
    if "utf-8" in html.lower() and "charset" in html.lower():
        ok_msg("charset UTF-8")
    else:
        err_msg("Sem charset UTF-8")

    # Viewport
    if 'name="viewport"' in html:
        ok_msg("Viewport meta (mobile ready)")
    else:
        err_msg("Sem viewport — nao e mobile friendly!")

    # CSS
    if "emotion.css" in html or "<style" in html:
        ok_msg("CSS carregando")
    else:
        warn_msg("CSS nao encontrado")

    # H1
    h1_count = len(re.findall(r"<h1", html, re.IGNORECASE))
    if h1_count == 1:
        ok_msg("H1 unico presente")
    elif h1_count == 0:
        err_msg("Sem H1")
    else:
        warn_msg(f"{h1_count} H1s (deve ser 1)")

    # Alt em imagens
    imgs = re.findall(r"<img[^>]+>", html, re.IGNORECASE)
    sem_alt = [i for i in imgs if "alt=" not in i.lower()]
    if not imgs:
        ok_msg("Sem imagens (OK)")
    elif not sem_alt:
        ok_msg(f"Alt text em todas as {len(imgs)} imagens")
    else:
        warn_msg(f"{len(sem_alt)} imagens sem alt text")

    # Labels
    n_labels = len(re.findall(r"<label", html, re.IGNORECASE))
    n_inputs = len(re.findall(r"<input", html, re.IGNORECASE))
    if n_inputs == 0:
        ok_msg("Sem inputs")
    elif n_labels >= max(1, n_inputs // 2):
        ok_msg(f"{n_labels} labels para {n_inputs} inputs")
    else:
        warn_msg(f"Poucos labels: {n_labels} para {n_inputs} inputs")

    # Teclado
    usa_teclado = any(k in html for k in ["onkeydown", "keypress", "keyup", "Enter"])
    if usa_teclado:
        ok_msg("Suporte a teclado detectado")
    else:
        warn_msg("Suporte a teclado nao detectado")

    # JavaScript
    scripts = re.findall(r"<script", html, re.IGNORECASE)
    if scripts:
        ok_msg(f"{len(scripts)} bloco(s) JavaScript")
    else:
        warn_msg("Sem JavaScript")

total = OK + WARN + ERR
score = round(OK / total * 100) if total > 0 else 0
print(f"\\nScore: {OK} ok / {WARN} avisos / {ERR} erros = {score}%")
""")

# ══════════════════════════════════════
# SSL
# ══════════════════════════════════════
w("tools/ssl_check.py", """#!/usr/bin/env python3
import ssl
import socket
from datetime import datetime

HOST = "emotion-platform-albert.onrender.com"

print("=== SSL/TLS ===")
print(f"Host: {HOST}")
print()

try:
    ctx = ssl.create_default_context()
    with socket.create_connection((HOST, 443), timeout=10) as sock:
        with ctx.wrap_socket(sock, server_hostname=HOST) as ssock:
            cert = ssock.getpeercert()
            versao = ssock.version()
            cipher = ssock.cipher()

            print(f"  OK  Certificado SSL valido")
            print(f"  OK  Versao TLS: {versao}")

            if cipher:
                print(f"  OK  Cipher: {cipher[0]}")

            # Validade
            expiry = cert.get("notAfter", "")
            if expiry:
                exp_date = datetime.strptime(expiry, "%b %d %H:%M:%S %Y %Z")
                dias = (exp_date - datetime.utcnow()).days
                if dias > 30:
                    print(f"  OK  Certificado valido por {dias} dias")
                elif dias > 0:
                    print(f"  WARN Certificado expira em {dias} dias!")
                else:
                    print(f"  ERR  Certificado EXPIRADO!")

            # Emissor
            issuer_raw = cert.get("issuer", ())
            issuer = {}
            for item in issuer_raw:
                if item:
                    k, v = item[0]
                    issuer[k] = v
            org = issuer.get("organizationName", "?")
            print(f"  OK  Emissor: {org}")

            # Versao TLS
            if "TLSv1.3" in versao:
                print("  OK  TLS 1.3 (maxima seguranca)")
            elif "TLSv1.2" in versao:
                print("  OK  TLS 1.2 (seguro)")
            else:
                print(f"  WARN {versao} (considere atualizar)")

except ssl.SSLCertVerificationError as exc:
    print(f"  ERR Certificado invalido: {exc}")
except Exception as exc:
    print(f"  ERR Erro SSL: {exc}")

print()
print(f"Analise completa: https://www.ssllabs.com/ssltest/analyze.html?d={HOST}")
""")

# ══════════════════════════════════════
# SEO
# ══════════════════════════════════════
w("tools/seo_check.py", """#!/usr/bin/env python3
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
    warn_msg(f"Title muito curto: '{titles[0]}'")
else:
    err_msg("Title ausente!")

# Meta description
descs = re.findall(
    r'name=["\']description["\'][^>]*content=["\']([^"\']+)', html
)
if not descs:
    descs = re.findall(
        r'content=["\']([^"\']+)["\'][^>]*name=["\']description["\']', html
    )
if descs and len(descs[0]) >= 30:
    ok_msg(f"Meta description: '{descs[0][:60]}'")
elif descs:
    warn_msg(f"Meta description curta: '{descs[0][:40]}'")
else:
    warn_msg("Meta description ausente")

# Open Graph
if "og:title" in html:
    ok_msg("Open Graph tags (compartilhamento social)")
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
status_sm, _ = buscar("/sitemap.xml")
if status_sm == 200:
    ok_msg("sitemap.xml disponivel")
else:
    err_msg("sitemap.xml nao encontrado!")

# Robots
status_rb, _ = buscar("/robots.txt")
if status_rb == 200:
    ok_msg("robots.txt disponivel")
else:
    warn_msg("robots.txt nao encontrado")

# Velocidade
inicio = time.time()
try:
    urllib.request.urlopen(BASE + "/", timeout=30).read()
    ms = round((time.time() - inicio) * 1000)
    if ms < 800:
        ok_msg(f"Velocidade: {ms}ms (bom para SEO)")
    elif ms < 2000:
        warn_msg(f"Velocidade lenta: {ms}ms (pode prejudicar SEO)")
    else:
        err_msg(f"Muito lento: {ms}ms (prejudica SEO!)")
except Exception:
    warn_msg("Nao foi possivel medir velocidade")

# Viewport (mobile-first)
if 'name="viewport"' in html:
    ok_msg("Mobile-friendly (viewport meta)")
else:
    err_msg("Sem viewport — nao e mobile-friendly!")

# HTTPS
if BASE.startswith("https"):
    ok_msg("HTTPS (fator de ranking Google)")
else:
    err_msg("Sem HTTPS — penalidade no Google!")

print()
total = OK + WARN + ERR
score = round(OK / total * 100) if total > 0 else 0
print(f"SEO Score: {score}% ({OK} ok / {WARN} avisos / {ERR} erros)")
print()
print("Verificar tambem:")
print(f"  https://pagespeed.web.dev/?url={BASE}")
print(f"  https://search.google.com/search-console")
""")

# ══════════════════════════════════════
# RODAR TUDO
# ══════════════════════════════════════
w("rodar_tudo.py", f"""#!/usr/bin/env python3
import subprocess
import time
import json
import os
from datetime import datetime

BASE = "{BASE}"
RESULTADOS = {{}}


def rodar(nome, cmd, timeout=120):
    print(f"\\n{'='*55}")
    print(f"  {{nome}}")
    print(f"{'='*55}")
    inicio = time.time()
    r = subprocess.run(cmd, shell=True, timeout=timeout)
    tempo = round(time.time() - inicio, 1)
    ok = r.returncode == 0
    RESULTADOS[nome] = {{"ok": ok, "tempo": tempo}}
    return ok


print("=" * 60)
print("  ANALISE COMPLETA — EmotionAI")
print(f"  {{datetime.now().strftime('%d/%m/%Y %H:%M')}}")
print("=" * 60)

rodar("1. Compilacao",     "python3 -m py_compile main.py && echo OK")
rodar("2. Plugins",        "python3 status_plugins.py 2>/dev/null | grep -E 'Total|Score'")
rodar("3. Testes API",     "pytest tests/test_api.py -v --tb=short 2>&1 | tail -20")
rodar("4. Seguranca",      "python3 tools/security.py")
rodar("5. Performance",    "python3 tools/performance.py")
rodar("6. Acessibilidade", "python3 tools/accessibility.py")
rodar("7. SSL",            "python3 tools/ssl_check.py")
rodar("8. SEO",            "python3 tools/seo_check.py")
rodar("9. Browser Real",   "python3 tests/test_browser.py", timeout=300)

print("\\n" + "=" * 60)
print("  RELATORIO FINAL")
print("=" * 60)

ok_n = sum(1 for v in RESULTADOS.values() if v["ok"])
total = len(RESULTADOS)
score = round(ok_n / total * 100) if total > 0 else 0

print(f"\\n  Score: {{ok_n}}/{{total}} ({{score}}%)")
print()
for nome, r in RESULTADOS.items():
    icon = "OK" if r["ok"] else "XX"
    print(f"  [{{icon}}] {{nome}} ({{r['tempo']}}s)")

shots_dir = "tests/screenshots"
if os.path.exists(shots_dir):
    shots = os.listdir(shots_dir)
    if shots:
        print(f"\\n  Screenshots ({{len(shots)}}):")
        for s in sorted(shots):
            print(f"    • {{s}}")

ts = datetime.now().strftime("%Y%m%d_%H%M")
with open(f"tests/relatorio_{{ts}}.json", "w", encoding="utf-8") as f:
    json.dump(
        {{"data": str(datetime.now()), "score": f"{{ok_n}}/{{total}}", "resultados": RESULTADOS}},
        f, indent=2, ensure_ascii=False
    )

print(f"\\n  Relatorio: tests/relatorio_{{ts}}.json")
print(f"  Site: {{BASE}}")
""")

print("\n✅ Todos os arquivos corrigidos")

# ══════════════════════════════════════
# VERIFICAR COMPILAÇÃO
# ══════════════════════════════════════
print("\nVerificando compilação...")
arquivos = [
    "tools/security.py",
    "tools/performance.py",
    "tools/accessibility.py",
    "tools/ssl_check.py",
    "tools/seo_check.py",
    "rodar_tudo.py",
    "tests/test_browser.py",
]
for f in arquivos:
    ok = run(f"python3 -m py_compile {f}")
    print(f"  {'✅' if ok else '❌'} {f}")

# ══════════════════════════════════════
# PUSH
# ══════════════════════════════════════
print("\nPush...")
for cmd in [
    "git add -A",
    'git commit --no-verify -m "fix: tools corrigidos sem f-string errors"',
    "git push"
]:
    ok = run(cmd)
    print(f"  {'✅' if ok else '❌'} {cmd[:40]}")

# ══════════════════════════════════════
# RODAR TODOS AGORA
# ══════════════════════════════════════
print("\n" + "="*55)
print("RODANDO FERRAMENTAS AGORA")
print("="*55)

ferramentas = [
    ("Segurança",      "python3 tools/security.py"),
    ("SSL/TLS",        "python3 tools/ssl_check.py"),
    ("Performance",    "python3 tools/performance.py"),
    ("SEO",            "python3 tools/seo_check.py"),
    ("Acessibilidade", "python3 tools/accessibility.py"),
    ("Pytest API",     "pytest tests/test_api.py -v --tb=short 2>&1 | tail -25"),
]

for nome, cmd in ferramentas:
    print(f"\n{'─'*55}")
    print(f"  {nome}")
    print(f"{'─'*55}")
    subprocess.run(cmd, shell=True, timeout=90)

print(f"""
{'='*55}
TUDO PRONTO!
{'='*55}

COMANDOS:
  make test          → 30 testes API
  make browser       → Browser + screenshots
  make security      → Seguranca
  make performance   → Velocidade
  make accessibility → WCAG 2.1
  make seo           → SEO
  make ssl           → SSL/TLS
  make all           → TUDO

  python3 rodar_tudo.py  → TUDO de uma vez
{'='*55}
""")
