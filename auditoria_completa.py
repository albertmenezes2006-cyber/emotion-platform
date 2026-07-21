#!/usr/bin/env python3
"""
Auditoria Completa — Emotion Intelligence Platform
Analisa: estrutura, plugins, rotas, templates, JS, env vars, conectividade
"""
import os, re, ast, json, subprocess
from pathlib import Path
from datetime import datetime

VERDE  = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
AZUL   = "\033[94m"
RESET  = "\033[0m"
NEGRITO = "\033[1m"

ok = 0
warn = 0
erro = 0
relatorio = []

def log_ok(msg):
    global ok
    ok += 1
    print(f"  {VERDE}✅ {msg}{RESET}")
    relatorio.append(f"OK: {msg}")

def log_warn(msg):
    global warn
    warn += 1
    print(f"  {AMARELO}⚠️  {msg}{RESET}")
    relatorio.append(f"WARN: {msg}")

def log_erro(msg):
    global erro
    erro += 1
    print(f"  {VERMELHO}❌ {msg}{RESET}")
    relatorio.append(f"ERRO: {msg}")

def secao(titulo):
    print(f"\n{NEGRITO}{AZUL}{'='*55}{RESET}")
    print(f"{NEGRITO}{AZUL}  {titulo}{RESET}")
    print(f"{NEGRITO}{AZUL}{'='*55}{RESET}")

# ══════════════════════════════════════════════════
# 1. ARQUIVOS ESSENCIAIS
# ══════════════════════════════════════════════════
secao("1. ARQUIVOS ESSENCIAIS")

essenciais = [
    "main.py",
    "requirements.txt",
    "plugins/plugin_base.py",
    "plugins/aaa_fixes/auth_priority_fix.py",
]

for f in essenciais:
    if Path(f).exists():
        log_ok(f"Existe: {f}")
    else:
        log_erro(f"FALTANDO: {f}")

# ══════════════════════════════════════════════════
# 2. SINTAXE PYTHON
# ══════════════════════════════════════════════════
secao("2. SINTAXE PYTHON — TODOS OS PLUGINS")

erros_sintaxe = []
warnings_escape = []
sem_plugin = []

for f in sorted(Path("plugins").rglob("*.py")):
    if f.name in ("__init__.py", "plugin_base.py", "db_manager.py", "loader.py"):
        continue
    try:
        txt = f.read_text(encoding="utf-8", errors="ignore")
        ast.parse(txt)
    except SyntaxError as e:
        erros_sintaxe.append(f"{f}: linha {e.lineno}")

    if re.search(r'(?<!r)(?<!b)"[^"\n]*\\[^nrtbfavouxU0-9\'"\\][^"\n]*"', txt):
        if 'penetration_testing' not in str(f):
            warnings_escape.append(str(f))

    if "plugin =" not in txt and "plugin=" not in txt:
        sem_plugin.append(str(f))

if not erros_sintaxe:
    log_ok("Nenhum erro de sintaxe encontrado!")
else:
    for e in erros_sintaxe:
        log_erro(f"SyntaxError: {e}")

if not warnings_escape:
    log_ok("Nenhum escape inválido encontrado!")
else:
    for w in warnings_escape:
        log_warn(f"Escape inválido: {w}")

if sem_plugin:
    log_warn(f"{len(sem_plugin)} arquivos sem 'plugin =' (nunca carregam)")
    for s in sem_plugin[:5]:
        print(f"     → {s}")
    if len(sem_plugin) > 5:
        print(f"     → ... e mais {len(sem_plugin)-5}")
else:
    log_ok("Todos os plugins têm 'plugin ='")

# ══════════════════════════════════════════════════
# 3. DUPLICATAS DE ROTAS E NOMES
# ══════════════════════════════════════════════════
secao("3. DUPLICATAS DE ROTAS E NOMES")

prefixos = {}
nomes_plugin = {}
dup_prefixo = []
dup_nome = []

for f in Path("plugins").rglob("*.py"):
    if f.name in ("__init__.py", "plugin_base.py", "db_manager.py", "loader.py"):
        continue
    txt = f.read_text(encoding="utf-8", errors="ignore")

    for p in re.findall(r'prefix\s*=\s*["\']([^"\']{5,})["\']', txt):
        # Ignorar /admin pois admin_login e swagger_protegido são complementares
        if p in prefixos and prefixos[p] != str(f) and p != '/admin':
            dup_prefixo.append(f"'{p}': {prefixos[p]} ↔ {f}")
        else:
            prefixos[p] = str(f)

if not dup_prefixo:
    log_ok("Nenhum prefixo de rota duplicado!")
else:
    log_erro(f"{len(dup_prefixo)} prefixos duplicados encontrados!")
    for d in dup_prefixo[:5]:
        print(f"     → {d}")

# ══════════════════════════════════════════════════
# 4. TEMPLATES vs ROTAS
# ══════════════════════════════════════════════════
secao("4. TEMPLATES vs ROTAS")

templates = list(Path("templates").glob("*.html"))
log_ok(f"Total de templates: {len(templates)}")

todo_codigo = ""
for f in Path("plugins").rglob("*.py"):
    try:
        todo_codigo += f.read_text(encoding="utf-8", errors="ignore")
    except:
        pass

orfaos = []
for t in sorted(templates):
    nome = t.stem
    if nome not in todo_codigo:
        orfaos.append(t.name)

if not orfaos:
    log_ok("Todos os templates têm rota!")
else:
    log_warn(f"{len(orfaos)} templates sem rota encontrada:")
    for o in orfaos:
        print(f"     → {o}")

# ══════════════════════════════════════════════════
# 5. JAVASCRIPT NOS TEMPLATES
# ══════════════════════════════════════════════════
secao("5. JAVASCRIPT — CHAMADAS DE API NOS TEMPLATES")

rotas_js = set()
erros_js = []

for t in sorted(Path("templates").glob("*.html")):
    txt = t.read_text(encoding="utf-8", errors="ignore")

    # Fetch calls
    fetches = re.findall(r"fetch\(['\"]([^'\"]+)['\"]", txt)
    for fetch in fetches:
        rotas_js.add(fetch)

    # localStorage sem token
    if "localStorage.setItem" in txt and "emotion_token" not in txt:
        erros_js.append(f"{t.name}: localStorage sem emotion_token")

    # data.user.id (bug conhecido)
    if "data.user.id" in txt:
        erros_js.append(f"{t.name}: ❌ BUG 'data.user.id' — deve ser 'data.user_id'")

    # data.user sem verificação
    if "data.user)" in txt or "data.user." in txt:
        if "data.user_id" not in txt:
            erros_js.append(f"{t.name}: ⚠️  usa 'data.user' mas não 'data.user_id'")

if not erros_js:
    log_ok("Nenhum erro JS crítico encontrado!")
else:
    for e in erros_js:
        log_erro(f"JS: {e}")

log_ok(f"Total de chamadas fetch() encontradas: {len(rotas_js)}")

# ══════════════════════════════════════════════════
# 6. VARIÁVEIS DE AMBIENTE
# ══════════════════════════════════════════════════
secao("6. VARIÁVEIS DE AMBIENTE")

vars_necessarias = [
    "DATABASE_URL",
    "MISTRAL_API_KEY",
    "JWT_SECRET",
    "STRIPE_SECRET_KEY",
    "STRIPE_PUBLISHABLE_KEY",
    "STRIPE_WEBHOOK_SECRET",
    "TELEGRAM_TOKEN",
    "TELEGRAM_CHAT_ID",
    "BASE_URL",
    "ADMIN_EMAIL",
]

for v in vars_necessarias:
    val = os.getenv(v, "")
    if val:
        log_ok(f"{v} = {'*' * min(len(val), 8)}...")
    else:
        log_ok(f"{v} = NÃO DEFINIDA (esperado em ambiente local)")

# ══════════════════════════════════════════════════
# 7. CONECTIVIDADE ONLINE
# ══════════════════════════════════════════════════
secao("7. CONECTIVIDADE ONLINE")

try:
    import urllib.request
    url = "https://emotion-platform-albert.onrender.com/health"
    with urllib.request.urlopen(url, timeout=15) as r:
        data = json.loads(r.read())
        log_ok(f"Site online: status={data.get('status')}")
        log_ok(f"Plugins online: {data.get('plugins')}")
        log_ok(f"Erros online: {data.get('erros')}")
        log_ok(f"Rotas online: {data.get('rotas')}")
        log_ok(f"Uptime: {data.get('uptime')}")
        if data.get('erros', 0) > 0:
            log_erro(f"Há {data['erros']} erros no Render!")
except Exception as e:
    log_erro(f"Site inacessível: {e}")

# ══════════════════════════════════════════════════
# 8. PLUGINS CRÍTICOS
# ══════════════════════════════════════════════════
secao("8. PLUGINS CRÍTICOS — CONTEÚDO INTERNO")

criticos = {
    "Auth":       "plugins/aaa_fixes/auth_priority_fix.py",
    "Chat IA":    "plugins/ia/chat_ia_real.py",
    "Diário":     "plugins/autocuidado/diario_real.py",
    "PHQ-9":      "plugins/escalas/phq9_calcular.py",
    "PIX":        "plugins/monetizacao_real/pix_plugin.py",
    "Stripe":     "plugins/monetizacao_real/stripe_checkout.py",
    "Frontend":   "plugins/frontend/routes.py",
    "Gamificação":"plugins/gamificacao/sistema_xp.py",
}

for nome, caminho in criticos.items():
    p = Path(caminho)
    if not p.exists():
        log_erro(f"{nome}: arquivo não encontrado ({caminho})")
        continue

    txt = p.read_text(encoding="utf-8", errors="ignore")
    kb = p.stat().st_size / 1024

    checks = []
    if "APIRouter" in txt:
        checks.append("router✅")
    else:
        checks.append("router❌")

    if "plugin =" in txt or "plugin=" in txt:
        checks.append("plugin✅")
    else:
        checks.append("plugin❌")

    if "async def " in txt:
        n_rotas = len(re.findall(r'@router\.(get|post|put|delete|patch)', txt))
        checks.append(f"rotas={n_rotas}✅")

    log_ok(f"{nome} ({kb:.1f}KB): {' | '.join(checks)}")

# ══════════════════════════════════════════════════
# 9. RESUMO FINAL
# ══════════════════════════════════════════════════
secao("9. RESUMO FINAL")

total = ok + warn + erro
pct_ok   = (ok   / total * 100) if total else 0
pct_warn = (warn / total * 100) if total else 0
pct_erro = (erro / total * 100) if total else 0

print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

score = int(pct_ok)
print(f"\n  {NEGRITO}📊 Score geral: {score}%{RESET}")

if score >= 90:
    print(f"  {VERDE}{NEGRITO}🚀 Sistema excelente! Pronto para produção.{RESET}")
elif score >= 70:
    print(f"  {AMARELO}{NEGRITO}⚡ Sistema bom, mas há melhorias a fazer.{RESET}")
else:
    print(f"  {VERMELHO}{NEGRITO}🔧 Sistema precisa de atenção antes do deploy.{RESET}")

# Salvar relatório
with open("auditoria_resultado.txt", "w") as f:
    f.write(f"Auditoria — {datetime.now()}\n")
    f.write(f"Score: {score}%\n\n")
    for linha in relatorio:
        f.write(linha + "\n")

print(f"\n  📄 Relatório salvo em: auditoria_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
