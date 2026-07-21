#!/usr/bin/env python3
"""
Teste Fase 3 — 35% restantes
Admin, Agendamento, Prontuário, Escalas, Cupons, Afiliados, PDF
"""
import urllib.request
import urllib.error
import json
import random
import string

VERDE   = "\033[92m"
AMARELO = "\033[93m"
VERMELHO= "\033[91m"
AZUL    = "\033[94m"
RESET   = "\033[0m"
NEGRITO = "\033[1m"

BASE  = "https://emotion-platform-albert.onrender.com"
TOKEN = None
EMAIL = f"fase3_{''.join(random.choices(string.ascii_lowercase, k=6))}@teste.com"
SENHA = "senha123"

ok = 0; warn = 0; erro = 0
resultados = []

def log_ok(msg):
    global ok; ok += 1
    print(f"  {VERDE}✅ {msg}{RESET}")
    resultados.append(f"OK: {msg}")

def log_warn(msg):
    global warn; warn += 1
    print(f"  {AMARELO}⚠️  {msg}{RESET}")
    resultados.append(f"WARN: {msg}")

def log_erro(msg):
    global erro; erro += 1
    print(f"  {VERMELHO}❌ {msg}{RESET}")
    resultados.append(f"ERRO: {msg}")

def secao(titulo):
    print(f"\n{NEGRITO}{AZUL}{'='*55}{RESET}")
    print(f"{NEGRITO}{AZUL}  {titulo}{RESET}")
    print(f"{NEGRITO}{AZUL}{'='*55}{RESET}")

def req(method, path, body=None, token=None):
    url = BASE + path
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body else None
    try:
        r = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(r, timeout=30) as resp:
            try:
                return resp.status, json.loads(resp.read())
            except Exception:
                return resp.status, {}
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except Exception:
            return e.code, {}
    except Exception as ex:
        return 0, {"erro": str(ex)}

# Setup — criar usuario
status, data = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Teste Fase3",
    "email": EMAIL,
    "senha": SENHA,
    "tipo": "psicologo"
})
if status in [200, 201]:
    TOKEN = data.get("token") or data.get("access_token")
    print(f"{VERDE}✅ Usuario criado: {EMAIL}{RESET}")
else:
    print(f"{VERMELHO}❌ Erro ao criar usuario: {status}{RESET}")

# ══════════════════════════════════════════════════
# 1. PSS CORRIGIDO
# ══════════════════════════════════════════════════
secao("1. PSS — ESCALA ESTRESSE")
status, data = req("POST", "/api/v1/pss/calcular", [1,0,1,0,1,0,1,0,1,0])
if status == 200:
    log_ok(f"PSS OK — score={data.get('score')} nivel={data.get('nivel')}")
else:
    status2, data2 = req("POST", "/api/v1/pss/calcular",
                         {"respostas": [1,0,1,0,1,0,1,0,1,0]}, token=TOKEN)
    if status2 == 200:
        log_ok(f"PSS OK (com body) — score={data2.get('score')}")
    else:
        log_erro(f"PSS: {status} | body: {status2}")

# ══════════════════════════════════════════════════
# 2. ESCALAS COMPLETAS
# ══════════════════════════════════════════════════
secao("2. ESCALAS COMPLETAS")

# GAD-7
status, data = req("GET", "/api/v1/gad7")
if status == 200:
    log_ok("GAD-7 pagina OK")
else:
    log_warn(f"GAD-7 GET: {status}")

status, data = req("POST", "/api/v1/gad7/calcular",
                   {"respostas": [1,0,1,0,1,0,1]}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"GAD-7 calcular OK — {data}")
else:
    log_warn(f"GAD-7 calcular: {status}")

# WHOQOL
status, data = req("GET", "/api/v1/whoqol")
if status == 200:
    log_ok("WHOQOL pagina OK")
else:
    log_warn(f"WHOQOL: {status}")

# PHQ-9 avaliacao
status, data = req("POST", "/api/v1/phq9/avaliacao",
                   {"respostas": [1,0,1,0,1,0,1,0,0]}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"PHQ-9 avaliacao OK — {data}")
else:
    log_warn(f"PHQ-9 avaliacao: {status}")

# Rosenberg
status, data = req("GET", "/api/v1/rosenberg")
if status == 200:
    log_ok("Rosenberg OK")
else:
    log_warn(f"Rosenberg: {status}")

# ══════════════════════════════════════════════════
# 3. ADMIN
# ══════════════════════════════════════════════════
secao("3. ADMIN PANEL")

status, data = req("GET", "/admin")
if status in [200, 401, 403]:
    log_ok(f"Admin acessivel ({status})")
else:
    log_warn(f"Admin: {status}")

status, data = req("GET", "/api/v1/auth/stats/usuarios")
if status == 200:
    log_ok(f"Stats usuarios OK — total={data.get('total_usuarios')}")
else:
    log_warn(f"Stats: {status}")

status, data = req("GET", "/api/v1/metricas-sistema/status")
if status == 200:
    log_ok("Metricas sistema OK")
else:
    log_warn(f"Metricas: {status}")

status, data = req("GET", "/api/v1/logs-sistema/status")
if status == 200:
    log_ok("Logs sistema OK")
else:
    log_warn(f"Logs: {status}")

# ══════════════════════════════════════════════════
# 4. AGENDAMENTO
# ══════════════════════════════════════════════════
secao("4. AGENDAMENTO")

if TOKEN:
    status, data = req("POST", "/api/v1/agenda-real/sessao/agendar", {
        "psicologo_id": "psi001",
        "paciente_id": "pac001",
        "data": "2026-08-01",
        "hora": "14:00",
        "tipo": "online"
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"Sessao agendada! — {data}")
    else:
        log_warn(f"Agendar sessao: {status}")

    status, data = req("GET", "/api/v1/agenda/listar", token=TOKEN)
    if status == 200:
        log_ok("Listar agenda OK")
    else:
        log_warn(f"Listar agenda: {status}")

    status, data = req("GET", "/api/v1/agendamento-online/status")
    if status == 200:
        log_ok("Agendamento online OK")
    else:
        log_warn(f"Agendamento online: {status}")

# ══════════════════════════════════════════════════
# 5. PRONTUÁRIO
# ══════════════════════════════════════════════════
secao("5. PRONTUARIO")

if TOKEN:
    status, data = req("POST", "/api/v1/prontuario-real/paciente/cadastrar", {
        "nome": "Paciente Teste",
        "email": "paciente@teste.com",
        "data_nascimento": "1990-01-01",
        "queixa_principal": "Ansiedade"
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"Prontuario criado! — {data}")
    else:
        log_warn(f"Prontuario: {status}")

    status, data = req("POST", "/api/v1/prontuario-real/evolucao/registrar", {
        "paciente_id": "pac001",
        "sessao": 1,
        "evolucao": "Paciente apresentou melhora significativa"
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok("Evolucao registrada!")
    else:
        log_warn(f"Evolucao: {status}")

    status, data = req("GET", "/api/v1/prontuario-completo/status")
    if status == 200:
        log_ok("Prontuario completo OK")
    else:
        log_warn(f"Prontuario completo: {status}")

# ══════════════════════════════════════════════════
# 6. CUPONS
# ══════════════════════════════════════════════════
secao("6. CUPONS")

for cupom in ["BEMVINDO", "PSICOLOGO", "ALBERT10"]:
    status, data = req("POST", f"/api/v1/cupons/usar/{cupom}", {}, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"Cupom {cupom} OK — {data}")
    elif status == 404:
        log_warn(f"Cupom {cupom}: rota nao encontrada")
    else:
        log_warn(f"Cupom {cupom}: {status} — {data}")

# ══════════════════════════════════════════════════
# 7. AFILIADOS
# ══════════════════════════════════════════════════
secao("7. AFILIADOS")

status, data = req("POST", "/api/v1/afiliados/cadastrar", {
    "nome": "Afiliado Teste",
    "email": EMAIL,
    "codigo": "ALBERT30"
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"Afiliado cadastrado! — {data}")
else:
    log_warn(f"Afiliados: {status}")

status, data = req("GET", "/afiliado")
if status == 200:
    log_ok("Pagina afiliado OK")
else:
    log_erro(f"Pagina afiliado: {status}")

# ══════════════════════════════════════════════════
# 8. RELATÓRIO PDF
# ══════════════════════════════════════════════════
secao("8. RELATORIO PDF")

if TOKEN:
    status, data = req("POST", "/api/v1/relatorio-pdf/gerar", {
        "tipo": "mensal",
        "user_id": "teste123"
    }, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"PDF gerado! — {data}")
    else:
        log_warn(f"PDF: {status}")

# ══════════════════════════════════════════════════
# 9. RECUPERAÇÃO DE SENHA
# ══════════════════════════════════════════════════
secao("9. RECUPERACAO DE SENHA")

status, data = req("POST", "/api/v1/auth/recuperar-senha",
                   {"email": EMAIL})
if status in [200, 201]:
    log_ok(f"Recuperar senha OK — {data}")
else:
    log_warn(f"Recuperar senha: {status}")

status, data = req("POST", "/api/v1/auth-jwt/recuperar-senha",
                   {"email": EMAIL})
if status in [200, 201]:
    log_ok(f"Recuperar senha JWT OK")
else:
    log_warn(f"Recuperar senha JWT: {status}")

# ══════════════════════════════════════════════════
# 10. DIÁRIO COMPLETO
# ══════════════════════════════════════════════════
secao("10. DIARIO COMPLETO")

if TOKEN:
    status, data = req("GET", "/api/v1/diario/listar", token=TOKEN)
    if status == 200:
        log_ok(f"Diario listar OK — {data}")
    else:
        log_warn(f"Diario listar: {status}")

    status, data = req("GET", "/api/v1/diario-emocional/listar", token=TOKEN)
    if status == 200:
        log_ok(f"Diario emocional listar OK")
    else:
        log_warn(f"Diario emocional listar: {status}")

# ══════════════════════════════════════════════════
# 11. GAMIFICAÇÃO COMPLETA
# ══════════════════════════════════════════════════
secao("11. GAMIFICACAO COMPLETA")

if TOKEN:
    status, data = req("GET", "/api/v1/xp/ranking/top")
    if status == 200:
        log_ok(f"Ranking top OK")
    else:
        log_warn(f"Ranking: {status}")

    status, data = req("GET", "/api/v1/streak/status", token=TOKEN)
    if status == 200:
        log_ok(f"Streak OK — {data}")
    else:
        log_warn(f"Streak: {status}")

    status, data = req("GET", "/api/v1/conquistas/status")
    if status == 200:
        log_ok("Conquistas OK")
    else:
        log_warn(f"Conquistas: {status}")

    status, data = req("GET", "/api/v1/desafios-diarios/status")
    if status == 200:
        log_ok("Desafios diarios OK")
    else:
        log_warn(f"Desafios: {status}")

# ══════════════════════════════════════════════════
# 12. NOTIFICAÇÕES
# ══════════════════════════════════════════════════
secao("12. NOTIFICACOES")

status, data = req("GET", "/api/v1/telegram/setup")
if status == 200:
    log_ok(f"Telegram OK — {data}")
else:
    log_warn(f"Telegram: {status}")

status, data = req("GET", "/api/v1/notificacao-conquista/status")
if status == 200:
    log_ok("Notificacao conquista OK")
else:
    log_warn(f"Notificacao: {status}")

# ══════════════════════════════════════════════════
# 13. SEO E SITEMAP
# ══════════════════════════════════════════════════
secao("13. SEO E SITEMAP")

for rota in ["/sitemap.xml", "/robots.txt", "/api/v1/seo", "/api/v1/seo-check"]:
    status, _ = req("GET", rota)
    if status == 200:
        log_ok(f"{rota} OK")
    else:
        log_warn(f"{rota}: {status}")

# ══════════════════════════════════════════════════
# 14. MONETIZAÇÃO COMPLETA
# ══════════════════════════════════════════════════
secao("14. MONETIZACAO COMPLETA")

status, data = req("GET", "/api/v1/stripe/planos")
if status == 200:
    log_ok(f"Stripe planos OK")
else:
    log_warn(f"Stripe: {status}")

status, data = req("GET", "/api/v1/stripe-checkout/configuracao")
if status == 200:
    log_ok("Stripe checkout config OK")
else:
    log_warn(f"Stripe checkout: {status}")

status, data = req("GET", "/api/v1/tip/status")
if status == 200:
    log_ok(f"Tip/doacao OK — {data}")
else:
    log_warn(f"Tip: {status}")

status, data = req("GET", "/api/v1/tip/kofi")
if status == 200:
    log_ok("Ko-fi OK")
else:
    log_warn(f"Ko-fi: {status}")

# ══════════════════════════════════════════════════
# 15. SEGURANÇA AVANÇADA
# ══════════════════════════════════════════════════
secao("15. SEGURANCA AVANCADA")

status, data = req("GET", "/api/v1/security-headers/check")
if status == 200:
    log_ok(f"Security headers OK — {data}")
else:
    log_warn(f"Security headers: {status}")

status, data = req("GET", "/api/v1/xss/check")
if status == 200:
    log_ok("XSS check OK")
else:
    log_warn(f"XSS: {status}")

status, data = req("GET", "/api/v1/rate-limit/status")
if status == 200:
    log_ok("Rate limit OK")
else:
    log_warn(f"Rate limit: {status}")

status, data = req("GET", "/api/v1/compliance-lgpd/status")
if status == 200:
    log_ok("LGPD compliance OK")
else:
    log_warn(f"LGPD: {status}")

# ══════════════════════════════════════════════════
# RESUMO FINAL
# ══════════════════════════════════════════════════
secao("RESUMO FASE 3")
total = ok + warn + erro
pct_ok   = (ok   / total * 100) if total else 0
pct_warn = (warn / total * 100) if total else 0
pct_erro = (erro / total * 100) if total else 0

print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

score = int(pct_ok)
print(f"\n  {NEGRITO}📊 Score Fase 3: {score}%{RESET}")

with open("teste_fase3_resultado.txt", "w") as f:
    f.write(f"Score Fase 3: {score}%\n\n")
    for r in resultados:
        f.write(r + "\n")

print(f"\n  📄 Salvo em: teste_fase3_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
