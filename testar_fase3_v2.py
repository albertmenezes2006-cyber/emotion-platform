#!/usr/bin/env python3
"""Teste Fase 3 v2 — rotas reais corrigidas"""
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
EMAIL = f"fase3b_{''.join(random.choices(string.ascii_lowercase, k=6))}@teste.com"
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

# Setup
status, data = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Teste Fase3b",
    "email": EMAIL,
    "senha": SENHA,
    "tipo": "psicologo"
})
if status in [200, 201]:
    TOKEN = data.get("token") or data.get("access_token")
    USER_ID = data.get("user_id", "test123")
    print(f"{VERDE}✅ Usuario: {EMAIL}{RESET}")
else:
    USER_ID = "test123"
    print(f"{AMARELO}⚠️  Usando user_id padrao{RESET}")

# ══════════════════════════════════════════════════
secao("1. DIÁRIO — ROTAS REAIS")
# ══════════════════════════════════════════════════

status, data = req("POST", "/api/v1/diario-emocional/entrada", {
    "emocao": "ansioso",
    "intensidade": 6,
    "texto": "Testando diário emocional"
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"Diario entrada OK — {data}")
else:
    log_warn(f"Diario entrada: {status}")

status, data = req("GET", f"/api/v1/diario-emocional/historico/{USER_ID}", token=TOKEN)
if status == 200:
    log_ok(f"Diario historico OK")
else:
    log_warn(f"Diario historico: {status}")

status, data = req("GET", "/api/v1/diario-emocional/emocoes/disponiveis")
if status == 200:
    log_ok(f"Emocoes disponiveis OK — {list(data.keys())[:3] if isinstance(data, dict) else data}")
else:
    log_warn(f"Emocoes: {status}")

# ══════════════════════════════════════════════════
secao("2. GAD-7 — ROTA REAL")
# ══════════════════════════════════════════════════

# GAD não existe como /gad7 — vamos verificar
status, data = req("GET", "/api/v1/gad7")
if status == 200:
    log_ok("GAD-7 OK")
else:
    log_warn(f"GAD-7 /api/v1/gad7: {status} — escala pode não existir")
    # Tentar alternativas
    for rota in ["/api/v1/gad-7", "/api/v1/escalas/gad7", "/gad7"]:
        s, d = req("GET", rota)
        if s == 200:
            log_ok(f"GAD-7 encontrado em {rota}")
            break

# ══════════════════════════════════════════════════
secao("3. STREAK — ROTAS REAIS")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/streak-habitos/status")
if status == 200:
    log_ok(f"Streak habitos OK — {data}")
else:
    log_warn(f"Streak: {status}")

status, data = req("GET", "/api/v1/streak-meditacao/status")
if status == 200:
    log_ok(f"Streak meditacao OK")
else:
    log_warn(f"Streak meditacao: {status}")

status, data = req("GET", "/api/v1/streak-mental")
if status == 200:
    log_ok(f"Streak mental OK")
else:
    log_warn(f"Streak mental: {status}")

# ══════════════════════════════════════════════════
secao("4. LGPD — ROTAS REAIS")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/lgpd-avancado/status")
if status == 200:
    log_ok(f"LGPD avancado OK — {data}")
else:
    log_warn(f"LGPD avancado: {status}")

status, data = req("POST", "/api/v1/compliance-lgpd/consentimento/registrar", {
    "user_id": USER_ID,
    "tipo": "termos_uso",
    "aceito": True
}, token=TOKEN)
if status in [200, 201]:
    log_ok("LGPD consentimento OK")
else:
    log_warn(f"LGPD consentimento: {status}")

# ══════════════════════════════════════════════════
secao("5. RECUPERAR SENHA — ROTA REAL")
# ══════════════════════════════════════════════════

status, data = req("POST", "/api/v1/auth-jwt/recuperar-senha", {"email": EMAIL})
if status in [200, 201]:
    log_ok(f"Recuperar senha JWT OK — {data}")
else:
    log_warn(f"Recuperar senha JWT: {status} — {data}")

# ══════════════════════════════════════════════════
secao("6. AFILIADOS — ROTAS REAIS")
# ══════════════════════════════════════════════════

status, data = req("POST", "/api/v1/afiliados/cadastrar", {
    "nome": "Afiliado Teste",
    "email": EMAIL,
    "codigo": "ALBERT30"
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"Afiliado cadastrado OK — {data}")
    codigo = data.get("codigo", "ALBERT30")
else:
    log_warn(f"Afiliado cadastrar: {status} — {data}")
    codigo = "ALBERT30"

status, data = req("GET", f"/api/v1/afiliados/dashboard/{codigo}")
if status == 200:
    log_ok(f"Dashboard afiliado OK")
else:
    log_warn(f"Dashboard afiliado: {status}")

# ══════════════════════════════════════════════════
secao("7. AGENDA — ROTAS REAIS")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/agenda-grupo/status")
if status == 200:
    log_ok(f"Agenda grupo OK")
else:
    log_warn(f"Agenda grupo: {status}")

status, data = req("POST", "/api/v1/agenda-real/sessao/agendar", {
    "psicologo_id": "psi001",
    "paciente_nome": "Paciente Teste",
    "data_hora": "2026-08-01T14:00:00",
    "tipo": "online",
    "duracao": 50
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"Sessao agendada OK — {data}")
else:
    log_warn(f"Agendar sessao: {status} — {data}")

status, data = req("GET", "/api/v1/agendamento-online/status")
if status == 200:
    log_ok("Agendamento online OK")
else:
    log_warn(f"Agendamento online: {status}")

# ══════════════════════════════════════════════════
secao("8. PRONTUÁRIO — ROTAS REAIS")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/prontuario-eletronico/status")
if status == 200:
    log_ok(f"Prontuario eletronico OK")
else:
    log_warn(f"Prontuario eletronico: {status}")

status, data = req("POST", "/api/v1/prontuario-real/paciente/cadastrar", {
    "nome": "Paciente Silva",
    "data_nascimento": "1990-01-01",
    "queixa": "Ansiedade generalizada",
    "psicologo_id": "psi001"
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"Prontuario paciente OK — {data}")
else:
    log_warn(f"Prontuario paciente: {status} — {data}")

# ══════════════════════════════════════════════════
secao("9. PDF E EXPORTAÇÃO")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/export-pdf/status")
if status == 200:
    log_ok(f"Export PDF status OK — {data}")
else:
    log_warn(f"Export PDF: {status}")

status, data = req("POST", "/api/v1/relatorio-pdf/gerar", {
    "user_id": USER_ID,
    "tipo": "progresso",
    "periodo": "mensal"
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"PDF gerado OK — {data}")
else:
    log_warn(f"PDF gerar: {status} — {data}")

# ══════════════════════════════════════════════════
secao("10. KO-FI E MONETIZAÇÃO EXTRA")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/tip/kofi")
if status == 200:
    log_ok(f"Ko-fi OK — {data}")
elif status == 403:
    log_warn("Ko-fi 403 — pode precisar de auth")
    status2, data2 = req("GET", "/api/v1/tip/kofi", token=TOKEN)
    if status2 == 200:
        log_ok(f"Ko-fi com token OK")
    else:
        log_warn(f"Ko-fi com token: {status2}")
else:
    log_warn(f"Ko-fi: {status}")

status, data = req("GET", "/api/v1/tip/bmc")
if status == 200:
    log_ok(f"BMC OK")
else:
    log_warn(f"BMC: {status}")

status, data = req("GET", "/api/v1/tip/patreon")
if status == 200:
    log_ok(f"Patreon OK")
else:
    log_warn(f"Patreon: {status}")

# ══════════════════════════════════════════════════
secao("11. ESCALAS EXTRAS")
# ══════════════════════════════════════════════════

# PSS com rotas corretas
status, data = req("POST", "/api/v1/pss/calcular", [2,1,2,1,2,1,2,1,2,1])
if status == 200:
    log_ok(f"PSS lista OK — score={data.get('score')} nivel={data.get('nivel')}")
else:
    log_warn(f"PSS lista: {status}")

# WHOQOL
status, data = req("GET", "/api/v1/whoqol")
if status == 200:
    log_ok("WHOQOL pagina OK")
else:
    log_warn(f"WHOQOL: {status}")

# Rosenberg
status, data = req("GET", "/api/v1/rosenberg")
if status == 200:
    log_ok("Rosenberg OK")
else:
    log_warn(f"Rosenberg: {status}")

# PHQ9
status, data = req("POST", "/api/v1/phq9/calcular", {
    "respostas": [2,1,2,0,1,0,2,1,0]
}, token=TOKEN)
if status == 200:
    log_ok(f"PHQ-9 calcular OK — score={data.get('score')}")
else:
    log_warn(f"PHQ-9: {status}")

# ══════════════════════════════════════════════════
secao("12. CUPONS COMPLETO")
# ══════════════════════════════════════════════════

for cupom in ["BEMVINDO", "PSICOLOGO", "LAUNCH", "ALBERT10"]:
    status, data = req("POST", f"/api/v1/cupons/usar/{cupom}", {}, token=TOKEN)
    if status in [200, 201]:
        log_ok(f"Cupom {cupom} — desconto={data.get('desconto_aplicado')}")
    else:
        log_warn(f"Cupom {cupom}: {status}")

# ══════════════════════════════════════════════════
secao("13. GAMIFICAÇÃO COMPLETA")
# ══════════════════════════════════════════════════

status, data = req("POST", "/api/v1/xp/ganhar", {
    "user_id": USER_ID,
    "acao": "teste_completo",
    "xp": 50
}, token=TOKEN)
if status in [200, 201]:
    log_ok(f"XP ganhar OK — {data}")
else:
    log_warn(f"XP ganhar: {status}")

status, data = req("GET", "/api/v1/xp/ranking/top")
if status == 200:
    log_ok("Ranking top OK")
else:
    log_warn(f"Ranking: {status}")

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

status, data = req("GET", "/api/v1/missoes-semanais/status")
if status == 200:
    log_ok("Missoes semanais OK")
else:
    log_warn(f"Missoes: {status}")

# ══════════════════════════════════════════════════
secao("14. NOTIFICAÇÕES COMPLETAS")
# ══════════════════════════════════════════════════

status, data = req("GET", "/api/v1/telegram/setup")
if status == 200:
    log_ok(f"Telegram setup OK")
else:
    log_warn(f"Telegram: {status}")

status, data = req("GET", "/api/v1/alertas-humor/status")
if status == 200:
    log_ok("Alertas humor OK")
else:
    log_warn(f"Alertas humor: {status}")

status, data = req("GET", "/api/v1/lembretes-sessao/status")
if status == 200:
    log_ok("Lembretes sessao OK")
else:
    log_warn(f"Lembretes: {status}")

# ══════════════════════════════════════════════════
secao("15. ADMIN COMPLETO")
# ══════════════════════════════════════════════════

status, data = req("GET", "/admin")
if status == 200:
    log_ok("Admin panel OK")
else:
    log_warn(f"Admin: {status}")

status, data = req("GET", "/api/v1/auth/stats/usuarios")
if status == 200:
    log_ok(f"Stats OK — usuarios={data.get('total_usuarios')}")
else:
    log_warn(f"Stats: {status}")

status, data = req("GET", "/api/v1/feature-flags/status")
if status == 200:
    log_ok("Feature flags OK")
else:
    log_warn(f"Feature flags: {status}")

status, data = req("GET", "/api/v1/sistema/backup/status")
if status == 200:
    log_ok("Backup sistema OK")
else:
    log_warn(f"Backup: {status}")

# ══════════════════════════════════════════════════
secao("RESUMO FASE 3 v2")
# ══════════════════════════════════════════════════

total = ok + warn + erro
pct_ok   = (ok   / total * 100) if total else 0
pct_warn = (warn / total * 100) if total else 0
pct_erro = (erro / total * 100) if total else 0

print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

score = int(pct_ok)
print(f"\n  {NEGRITO}📊 Score Fase 3 v2: {score}%{RESET}")

if score >= 90:
    print(f"  {VERDE}{NEGRITO}🚀 Excelente!{RESET}")
elif score >= 70:
    print(f"  {AMARELO}{NEGRITO}⚡ Bom! Pequenos ajustes.{RESET}")
else:
    print(f"  {VERMELHO}{NEGRITO}🔧 Precisa atenção.{RESET}")

with open("teste_fase3_v2_resultado.txt", "w") as f:
    f.write(f"Score: {score}%\n\n")
    for r in resultados:
        f.write(r + "\n")

print(f"  📄 Salvo em: teste_fase3_v2_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
