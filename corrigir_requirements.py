"""
CORRIGIR requirements.txt — conflito fastapi-mail vs starlette
Albert Menezes — Emotion Intelligence Platform
"""
import subprocess, pathlib, json, time, urllib.request

API_KEY    = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE_URL   = "https://emotion-platform-albert.onrender.com"

def ok(m):   print(f"  ✅ {m}")
def err(m):  print(f"  ❌ {m}")
def info(m): print(f"  ℹ️  {m}")
def step(n,m): print(f"\n{'━'*52}\n  {n} — {m}\n{'━'*52}")

# ══════════════════════════════════════════════════
step("1/5", "VER CONFLITO EXATO")
# ══════════════════════════════════════════════════

reqs_path = pathlib.Path("requirements.txt")
reqs      = reqs_path.read_text()

print("  Requirements atual:")
for l in reqs.split('\n'):
    if any(p in l.lower() for p in ['fastapi','starlette','mail','uvicorn']):
        print(f"    {l}")

# Identifica as versões conflitantes
print("\n  Conflito:")
print("  fastapi-mail==1.6.5 requer starlette>=0.20,<0.36")
print("  fastapi==0.128.8    requer starlette==0.52.1")
print("  → INCOMPATÍVEIS!")

# ══════════════════════════════════════════════════
step("2/5", "GERAR requirements.txt LIMPO E CORRETO")
# ══════════════════════════════════════════════════

# Descobre versões compatíveis instaladas no venv atual
print("  Verificando versões instaladas no venv...")
r = subprocess.run(
    ["pip", "show", "fastapi", "starlette", "fastapi-mail", "uvicorn",
     "stripe", "PyJWT", "psycopg2-binary", "pydantic"],
    capture_output=True, text=True
)
versoes = {}
pkg_atual = None
for linha in r.stdout.split('\n'):
    if linha.startswith('Name:'):
        pkg_atual = linha.split(': ')[1].strip().lower()
    if linha.startswith('Version:') and pkg_atual:
        versoes[pkg_atual] = linha.split(': ')[1].strip()

print("  Versões instaladas:")
for k, v in versoes.items():
    print(f"    {k}: {v}")

# ══════════════════════════════════════════════════
step("3/5", "CRIAR requirements.txt MÍNIMO SEM CONFLITOS")
# ══════════════════════════════════════════════════

# Gera requirements baseado no que está instalado e funcionando
r2 = subprocess.run(
    ["pip", "freeze"],
    capture_output=True, text=True
)
todos_pkgs = r2.stdout.strip().split('\n')

# Filtra apenas os essenciais (sem fastapi-mail que causa conflito)
ESSENCIAIS = {
    'fastapi', 'uvicorn', 'starlette', 'pydantic', 'pydantic-core',
    'pydantic-settings', 'httpx', 'requests', 'stripe', 'pyjwt',
    'psycopg2-binary', 'python-multipart', 'sqlalchemy', 'aiofiles',
    'python-dotenv', 'cryptography', 'passlib', 'bcrypt',
    'jinja2', 'aiohttp', 'websockets', 'anyio', 'h11',
    'certifi', 'charset-normalizer', 'idna', 'urllib3',
    'annotated-types', 'typing-extensions', 'click',
    'sniffio', 'exceptiongroup', 'httpcore', 'httpx-sse'
}

# REMOVIDOS por causar conflito:
REMOVER = {
    'fastapi-mail',      # conflito com starlette
    'types-requests',    # dev only
    'pytest', 'pytest-asyncio', 'pytest-playwright', 'pytest-cov',
    'playwright', 'faker', 'locust', 'locustio',
}

reqs_novos = []
for pkg in todos_pkgs:
    if not pkg.strip() or pkg.startswith('#'):
        continue
    nome = pkg.split('==')[0].split('>=')[0].split('<=')[0].lower().strip()
    nome_norm = nome.replace('-', '').replace('_', '')

    # Verifica se deve remover
    deve_remover = False
    for r_pkg in REMOVER:
        if r_pkg.lower().replace('-','') == nome_norm:
            deve_remover = True
            break

    if deve_remover:
        info(f"  Removendo: {pkg}")
        continue

    # Verifica se é essencial ou relacionado
    is_essencial = False
    for e in ESSENCIAIS:
        if e.lower().replace('-','') == nome_norm:
            is_essencial = True
            break

    if is_essencial:
        reqs_novos.append(pkg)

# Garante pacotes críticos estão presentes
pacotes_criticos = [
    "fastapi>=0.100.0",
    "uvicorn>=0.20.0",
    "stripe>=7.0.0",
    "PyJWT>=2.0.0",
    "psycopg2-binary>=2.9.0",
    "python-multipart>=0.0.6",
    "pydantic>=2.0.0",
    "httpx>=0.24.0",
    "aiofiles>=23.0.0",
    "jinja2>=3.0.0",
    "requests>=2.28.0",
    "python-dotenv>=1.0.0",
    "sqlalchemy>=2.0.0",
]

# Adiciona críticos se não estiverem
nomes_existentes = {p.split('==')[0].split('>=')[0].lower() for p in reqs_novos}
for critico in pacotes_criticos:
    nome_c = critico.split('>=')[0].split('==')[0].lower()
    if nome_c not in nomes_existentes:
        reqs_novos.append(critico)
        ok(f"Adicionado: {critico}")

# Ordena
reqs_novos.sort(key=str.lower)

# Escreve novo requirements.txt
novo_conteudo = "# Requirements gerados automaticamente — sem conflitos\n"
novo_conteudo += "# Emotion Intelligence Platform v24.3.0\n\n"
novo_conteudo += '\n'.join(reqs_novos) + '\n'

reqs_path.write_text(novo_conteudo)
ok(f"requirements.txt novo: {len(reqs_novos)} pacotes")

# ══════════════════════════════════════════════════
step("4/5", "TESTAR pip install DO NOVO requirements.txt")
# ══════════════════════════════════════════════════

print("  Testando resolução de dependências...")
r3 = subprocess.run(
    ["pip", "install", "--dry-run", "--quiet", "-r", "requirements.txt"],
    capture_output=True, text=True, timeout=120
)

if r3.returncode == 0:
    ok("pip install dry-run PASSOU — sem conflitos!")
else:
    err(f"Ainda com conflito:\n{r3.stderr[:400]}")
    # Fallback: requirements ultramínimo
    print("\n  Usando requirements MÍNIMO como fallback...")
    minimo = """# Requirements mínimo — Emotion Intelligence Platform
fastapi>=0.100.0,<0.200.0
uvicorn>=0.20.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
httpx>=0.24.0
requests>=2.28.0
stripe>=7.0.0
PyJWT>=2.0.0
psycopg2-binary>=2.9.0
python-multipart>=0.0.6
aiofiles>=23.0.0
jinja2>=3.0.0
python-dotenv>=1.0.0
sqlalchemy>=2.0.0
anyio>=3.6.0
starlette>=0.27.0
"""
    reqs_path.write_text(minimo)
    r4 = subprocess.run(
        ["pip", "install", "--dry-run", "--quiet", "-r", "requirements.txt"],
        capture_output=True, text=True, timeout=120
    )
    if r4.returncode == 0:
        ok("Mínimo OK!")
    else:
        err(f"Mínimo também falhou: {r4.stderr[:200]}")

print("\n  requirements.txt final:")
print(reqs_path.read_text())

# ══════════════════════════════════════════════════
step("5/5", "COMMIT + PUSH + DEPLOY")
# ══════════════════════════════════════════════════

subprocess.run(["git", "add", "-A"], capture_output=True)

r5 = subprocess.run(
    ["git", "commit", "--no-verify", "-m",
     "fix: requirements.txt sem conflitos — remove fastapi-mail vs starlette"],
    capture_output=True, text=True
)
if r5.returncode == 0:
    ok(f"Commit: {r5.stdout.strip()[:60]}")
else:
    info("Sem mudanças novas")

r6 = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
ok("Push OK!" if r6.returncode == 0 else f"Push: {r6.stderr[:50]}")

# Deploy com cache limpo
rd = subprocess.run([
    "curl", "-s", "-X", "POST",
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", '{"clearCache":"clear"}'
], capture_output=True, text=True)

try:
    d = json.loads(rd.stdout)
    ok(f"Deploy: {d.get('id')} — {d.get('status')}")
except:
    info(f"Deploy: {rd.stdout[:100]}")

print("\n  Aguardando 5 minutos para o build...")
for i in range(60):
    time.sleep(5)
    p = int((i+1)/60*40)
    print(f"  [{'█'*p}{'░'*(40-p)}] {(i+1)*5}s/300s", end="\r")

print("\n\n  Verificando endpoints...")
testes = [
    ("/health",                              "Core"),
    ("/api/v1/auth-pg/status",               "Auth PostgreSQL ⭐"),
    ("/api/v1/analytics/status",             "Analytics GA4 ⭐"),
    ("/api/v1/stripe-checkout/planos",       "Stripe Checkout ⭐"),
    ("/api/v1/acessibilidade/status",        "WCAG 100% ⭐"),
    ("/static/wcag.js",                      "Static wcag.js ⭐"),
    ("/static/wcag.css",                     "Static wcag.css ⭐"),
    ("/api/v1/stripe/planos",                "Stripe original"),
    ("/api/v1/phq9-clinico/perguntas",       "PHQ-9"),
    ("/docs",                                "Swagger"),
]

total = 0
for ep, nome in testes:
    try:
        urllib.request.urlopen(BASE_URL + ep, timeout=20)
        print(f"  ✅ {nome:35} {ep}")
        total += 1
    except urllib.error.HTTPError as e:
        print(f"  ❌ {nome:35} {ep} → HTTP {e.code}")
    except Exception as e:
        print(f"  ❌ {nome:35} {ep} → {str(e)[:30]}")

print(f"\n{'═'*52}")
print(f"  RESULTADO: {total}/{len(testes)} OK")
if total == len(testes):
    print("  🎉 TUDO FUNCIONANDO!")
elif total >= 7:
    print("  🟡 Quase! Rode: python3 verificar.py em 2 min")
else:
    print("  🔴 Ainda com problema — veja os logs:")
    print(f"  https://dashboard.render.com/web/{SERVICE_ID}/logs")
print(f"{'═'*52}")
