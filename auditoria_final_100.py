#!/usr/bin/env python3
"""
Auditoria Final 100% — Emotion Intelligence Platform
Testa TUDO que é possível automatizar
"""
import urllib.request
import urllib.error
import urllib.parse
import json
import time
import random
import string
import os

VERDE   = "\033[92m"
AMARELO = "\033[93m"
VERMELHO= "\033[91m"
AZUL    = "\033[94m"
RESET   = "\033[0m"
NEGRITO = "\033[1m"

BASE  = "https://emotion-platform-albert.onrender.com"
TOKEN = None
EMAIL = f"audit_{''.join(random.choices(string.ascii_lowercase, k=6))}@teste.com"
SENHA = "senha123"
USER_ID = "test123"

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

def req(method, path, body=None, token=None, timeout=30):
    url = BASE + path
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body else None
    inicio = time.time()
    try:
        r = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            tempo = round((time.time() - inicio) * 1000)
            try:
                return resp.status, json.loads(resp.read()), tempo
            except Exception:
                return resp.status, {}, tempo
    except urllib.error.HTTPError as e:
        tempo = round((time.time() - inicio) * 1000)
        try:
            return e.code, json.loads(e.read()), tempo
        except Exception:
            return e.code, {}, tempo
    except Exception as ex:
        return 0, {"erro": str(ex)}, 0

# Setup
status, data, _ = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Auditoria Final",
    "email": EMAIL,
    "senha": SENHA,
    "tipo": "psicologo"
})
if status in [200, 201]:
    TOKEN = data.get("token") or data.get("access_token")
    USER_ID = data.get("user_id", USER_ID)
    print(f"{VERDE}✅ Usuario criado: {EMAIL}{RESET}")

# ══════════════════════════════════════════════════
secao("1. PERFORMANCE — Tempo de resposta")
# ══════════════════════════════════════════════════

rotas_perf = ["/health", "/", "/app/login", "/app/dashboard",
              "/api/v1/stripe/planos", "/sitemap.xml"]

tempos = []
for rota in rotas_perf:
    s, d, t = req("GET", rota)
    tempos.append(t)
    if s == 200 and t < 2000:
        log_ok(f"{rota} → {t}ms")
    elif s == 200 and t < 5000:
        log_warn(f"{rota} → {t}ms (lento)")
    elif s in [200, 301, 302]:
        log_warn(f"{rota} → {t}ms (muito lento)")
    else:
        log_warn(f"{rota} → {s} ({t}ms)")

media = round(sum(tempos) / len(tempos))
if media < 2000:
    log_ok(f"Tempo médio: {media}ms ✅")
elif media < 5000:
    log_warn(f"Tempo médio: {media}ms (aceitável)")
else:
    log_erro(f"Tempo médio: {media}ms (muito lento!)")

# ══════════════════════════════════════════════════
secao("2. MOBILE — User-Agent simulado")
# ══════════════════════════════════════════════════

mobile_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15"
paginas_mobile = ["/", "/app/login", "/app/dashboard", "/app/chat"]

for rota in paginas_mobile:
    try:
        r = urllib.request.Request(BASE + rota,
            headers={"User-Agent": mobile_ua})
        with urllib.request.urlopen(r, timeout=15) as resp:
            html = resp.read().decode(errors="ignore")
            tem_viewport = "viewport" in html
            tem_responsive = "max-width" in html or "width:100%" in html
            if tem_viewport and tem_responsive:
                log_ok(f"Mobile {rota} — viewport ✅ responsive ✅")
            elif tem_viewport:
                log_warn(f"Mobile {rota} — viewport ✅ responsive ⚠️")
            else:
                log_erro(f"Mobile {rota} — sem viewport!")
    except Exception as e:
        log_warn(f"Mobile {rota}: {e}")

# ══════════════════════════════════════════════════
secao("3. JAVASCRIPT — Verificar erros nos HTMLs")
# ══════════════════════════════════════════════════

import re
paginas_js = ["/app/login", "/app/dashboard", "/app/chat",
              "/app/diario", "/app/avaliacao"]

for rota in paginas_js:
    try:
        r = urllib.request.Request(BASE + rota)
        with urllib.request.urlopen(r, timeout=15) as resp:
            html = resp.read().decode(errors="ignore")
            erros_js = []
            if "data.user.id" in html:
                erros_js.append("data.user.id (bug login)")
            if "undefined" in html and "localStorage" in html:
                erros_js.append("possível undefined")
            if "console.error" in html:
                erros_js.append("console.error encontrado")
            fetch_calls = re.findall(r"fetch\(['\"]([^'\"]+)['\"]", html)

            if not erros_js:
                log_ok(f"JS {rota} — {len(fetch_calls)} fetches, sem erros")
            else:
                log_warn(f"JS {rota} — {erros_js}")
    except Exception as e:
        log_warn(f"JS {rota}: {e}")

# ══════════════════════════════════════════════════
secao("4. BANCO DE DADOS — Verificar operações")
# ══════════════════════════════════════════════════

# Testar CRUD completo
# Criar
s, d, t = req("POST", f"/api/v1/diario-emocional/entrada?user_id={USER_ID}&emocao_principal=alegria&intensidade=8&humor_geral=9&texto=Teste+banco", token=TOKEN)
if s in [200, 201]:
    log_ok(f"Banco CREATE OK ({t}ms)")
else:
    log_erro(f"Banco CREATE: {s}")

# Ler
s, d, t = req("GET", f"/api/v1/diario-emocional/historico/{USER_ID}", token=TOKEN)
if s == 200:
    total = d.get("total_entradas", 0)
    log_ok(f"Banco READ OK — {total} registros ({t}ms)")
else:
    log_erro(f"Banco READ: {s}")

# Testar prontuário
s, d, t = req("POST", f"/api/v1/prontuario-real/paciente/cadastrar?nome=Paciente+DB+Test&data_nascimento=1990-01-01&terapeuta_id={USER_ID}", token=TOKEN)
if s in [200, 201]:
    pac_id = d.get("paciente_id", "")
    log_ok(f"Banco prontuario OK — id={pac_id} ({t}ms)")
else:
    log_warn(f"Banco prontuario: {s}")

# Testar agenda
s, d, t = req("POST", f"/api/v1/agenda-real/sessao/agendar?paciente_id=pac_db&terapeuta_id={USER_ID}&data_hora=2026-09-01T10:00:00&tipo=online", token=TOKEN)
if s in [200, 201]:
    log_ok(f"Banco agenda OK ({t}ms)")
else:
    log_warn(f"Banco agenda: {s}")

# ══════════════════════════════════════════════════
secao("5. EMAIL — Verificar configuração")
# ══════════════════════════════════════════════════

s, d, t = req("POST", f"/api/v1/auth-jwt/recuperar-senha?email={EMAIL}")
if s in [200, 201]:
    nota = d.get("nota", "")
    if "SendGrid" in nota:
        log_warn(f"Email: configurado mas sem SendGrid real — {nota}")
    else:
        log_ok(f"Email OK — {d.get('status')}")
else:
    log_erro(f"Email: {s}")

s, d, t = req("GET", "/api/v1/telegram/setup")
if s == 200:
    token_ok = d.get("token_configurado", False)
    chat_ok = d.get("chat_id_configurado", False)
    if token_ok and chat_ok:
        log_ok("Telegram configurado ✅")
    else:
        log_warn(f"Telegram parcial: token={token_ok} chat={chat_ok}")
else:
    log_warn(f"Telegram: {s}")

# ══════════════════════════════════════════════════
secao("6. STRIPE — Verificar configuração")
# ══════════════════════════════════════════════════

s, d, t = req("GET", "/api/v1/stripe/planos")
if s == 200:
    planos = list(d.get("planos", {}).keys())
    log_ok(f"Stripe planos: {planos}")
else:
    log_erro(f"Stripe planos: {s}")

s, d, t = req("GET", "/api/v1/stripe-setup/status")
if s == 200:
    log_ok(f"Stripe setup OK — {d}")
else:
    log_warn(f"Stripe setup: {s}")

s, d, t = req("GET", "/api/v1/stripe-checkout/configuracao")
if s == 200:
    log_ok("Stripe checkout config OK")
else:
    log_warn(f"Stripe checkout: {s}")

# ══════════════════════════════════════════════════
secao("7. ACESSIBILIDADE — Verificar básico")
# ══════════════════════════════════════════════════

try:
    r = urllib.request.Request(BASE + "/")
    with urllib.request.urlopen(r, timeout=15) as resp:
        html = resp.read().decode(errors="ignore")

        checks = {
            "lang=": "lang attribute",
            "alt=": "image alt",
            "aria-": "ARIA labels",
            "role=": "ARIA roles",
            "<title>": "page title",
            "meta name=\"description\"": "meta description",
        }

        for check, nome in checks.items():
            if check in html:
                log_ok(f"Acessibilidade: {nome} ✅")
            else:
                log_warn(f"Acessibilidade: {nome} ausente")
except Exception as e:
    log_warn(f"Acessibilidade: {e}")

# ══════════════════════════════════════════════════
secao("8. SEO COMPLETO")
# ══════════════════════════════════════════════════

s, d, t = req("GET", "/sitemap.xml")
if s == 200:
    log_ok(f"Sitemap OK ({t}ms)")
else:
    log_erro(f"Sitemap: {s}")

s, d, t = req("GET", "/robots.txt")
if s == 200:
    log_ok(f"Robots.txt OK ({t}ms)")
else:
    log_erro(f"Robots: {s}")

s, d, t = req("GET", "/api/v1/seo-check")
if s == 200:
    log_ok(f"SEO check OK — {d}")
else:
    log_warn(f"SEO check: {s}")

# Open Graph
try:
    r = urllib.request.Request(BASE + "/")
    with urllib.request.urlopen(r, timeout=15) as resp:
        html = resp.read().decode(errors="ignore")
        og_checks = ["og:title", "og:description", "og:image", "twitter:card"]
        for og in og_checks:
            if og in html:
                log_ok(f"SEO: {og} ✅")
            else:
                log_warn(f"SEO: {og} ausente")
except Exception:
    pass

# ══════════════════════════════════════════════════
secao("9. SEGURANÇA AVANÇADA")
# ══════════════════════════════════════════════════

# SQL Injection
s, d, t = req("POST", "/api/v1/auth/login", {
    "email": "' OR 1=1 --",
    "senha": "qualquer"
})
if s in [401, 422, 400]:
    log_ok(f"SQL Injection bloqueado ({s}) ✅")
else:
    log_erro(f"SQL Injection não bloqueado: {s}")

# XSS
s, d, t = req("POST", "/api/v1/auth/login", {
    "email": "<script>alert('xss')</script>",
    "senha": "qualquer"
})
if s in [401, 422, 400]:
    log_ok(f"XSS bloqueado ({s}) ✅")
else:
    log_warn(f"XSS: {s}")

# Rate limit
s, d, t = req("GET", "/api/v1/rate-limit/status")
if s == 200:
    log_ok(f"Rate limit ativo — {d}")
else:
    log_warn(f"Rate limit: {s}")

# Headers de segurança
s, d, t = req("GET", "/api/v1/security-headers/check")
if s == 200:
    headers = d.get("headers_ativos", [])
    log_ok(f"Security headers: {len(headers)} ativos")
else:
    log_warn(f"Security headers: {s}")

# ══════════════════════════════════════════════════
secao("10. ESCALAS COMPLETAS")
# ══════════════════════════════════════════════════

# PHQ-9
s, d, t = req("POST", "/api/v1/phq9/calcular",
              {"respostas": [2,1,2,0,1,0,2,1,0]}, token=TOKEN)
if s == 200:
    log_ok(f"PHQ-9 OK — score={d.get('score')} nivel={d.get('nivel')}")
else:
    log_erro(f"PHQ-9: {s}")

# GAD-7
s, d, t = req("POST", "/api/v1/gad7/calcular",
              [1,2,1,0,1,2,1])
if s == 200:
    log_ok(f"GAD-7 OK — score={d.get('score')} nivel={d.get('nivel')}")
else:
    log_erro(f"GAD-7: {s}")

# PSS
s, d, t = req("POST", "/api/v1/pss/calcular",
              [1,0,1,0,1,0,1,0,1,0])
if s == 200:
    log_ok(f"PSS OK — score={d.get('score')} nivel={d.get('nivel')}")
else:
    log_erro(f"PSS: {s}")

# WHOQOL
s, d, t = req("GET", "/api/v1/whoqol")
if s == 200:
    log_ok("WHOQOL OK")
else:
    log_warn(f"WHOQOL: {s}")

# Big Five
s, d, t = req("POST", "/api/v1/bigfive/calcular",
              [3,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2])
if s == 200:
    log_ok(f"Big Five OK — {d}")
else:
    log_erro(f"Big Five: {s}")

# Rosenberg
s, d, t = req("GET", "/api/v1/rosenberg")
if s == 200:
    log_ok("Rosenberg OK")
else:
    log_warn(f"Rosenberg: {s}")

# ══════════════════════════════════════════════════
secao("11. TODAS AS PÁGINAS HTML")
# ══════════════════════════════════════════════════

todas_paginas = [
    "/", "/app/login", "/app/cadastro", "/app/dashboard",
    "/app/chat", "/app/diario", "/app/avaliacao", "/app/gamificacao",
    "/app/ranking", "/app/perfil", "/app/configuracoes", "/app/analises",
    "/app/carteira", "/app/score-ie", "/app/planos",
    "/sobre", "/blog", "/faq", "/contato", "/privacidade", "/termos",
    "/planos", "/premium", "/psicologos", "/terapia", "/afiliado",
    "/whitelabel", "/para-psicologos", "/para-clinicas",
    "/checkout/anual", "/checkout/creditos",
    "/nova-senha", "/recuperar-senha",
    "/presente", "/presente/sucesso", "/obrigado", "/sucesso",
    "/offline", "/sitemap.xml", "/robots.txt",
    "/manifest.json", "/sw.js",
    "/meditacao", "/respiracao", "/gratidao", "/grounding",
]

pag_ok = 0; pag_err = 0
for rota in todas_paginas:
    s, d, t = req("GET", rota)
    if s == 200:
        pag_ok += 1
    elif s in [301, 302]:
        pag_ok += 1
    elif s in [401, 403]:
        pag_ok += 1
    else:
        log_warn(f"Pagina {rota}: {s}")
        pag_err += 1

log_ok(f"Paginas OK: {pag_ok}/{len(todas_paginas)}")
if pag_err > 0:
    log_warn(f"Paginas com problema: {pag_err}")

# ══════════════════════════════════════════════════
secao("12. FLUXO COMPLETO DO USUÁRIO")
# ══════════════════════════════════════════════════

# Simular jornada completa: cadastro → login → chat → diario → escala → xp
print(f"\n  Simulando jornada completa do usuario...")

# 1. Cadastro
email_jornada = f"jornada_{''.join(random.choices(string.ascii_lowercase, k=4))}@teste.com"
s, d, t = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Jornada Teste", "email": email_jornada,
    "senha": "senha123", "tipo": "paciente"
})
tok_j = d.get("token") or d.get("access_token") if s in [200,201] else None
uid_j = d.get("user_id", "j001") if s in [200,201] else "j001"
if tok_j:
    log_ok(f"Jornada 1/6: Cadastro OK")
else:
    log_erro("Jornada 1/6: Cadastro falhou")

# 2. Login
s, d, t = req("POST", "/api/v1/auth/login",
              {"email": email_jornada, "senha": "senha123"})
if s == 200:
    log_ok("Jornada 2/6: Login OK")
else:
    log_erro("Jornada 2/6: Login falhou")

# 3. Chat
s, d, t = req("POST", "/api/v1/chat/enviar",
              {"mensagem": "Olá, preciso de ajuda com ansiedade"}, token=tok_j)
if s == 200:
    log_ok(f"Jornada 3/6: Chat OK")
else:
    log_warn(f"Jornada 3/6: Chat {s}")

# 4. Diário
s, d, t = req("POST", f"/api/v1/diario-emocional/entrada?user_id={uid_j}&emocao_principal=ansioso&intensidade=6&humor_geral=5&texto=Me+sentindo+ansioso", token=tok_j)
if s in [200,201]:
    log_ok("Jornada 4/6: Diario OK")
else:
    log_warn(f"Jornada 4/6: Diario {s}")

# 5. PHQ-9
s, d, t = req("POST", "/api/v1/phq9/calcular",
              {"respostas": [1,0,1,0,0,0,1,0,0]}, token=tok_j)
if s == 200:
    log_ok(f"Jornada 5/6: PHQ-9 OK — score={d.get('score')}")
else:
    log_warn(f"Jornada 5/6: PHQ-9 {s}")

# 6. XP
s, d, t = req("POST", f"/api/v1/xp/ganhar?user_id={uid_j}&acao=primeira_avaliacao&xp=50")
if s in [200,201]:
    log_ok(f"Jornada 6/6: XP OK — {d.get('xp_total')} XP")
else:
    log_warn(f"Jornada 6/6: XP {s}")

# ══════════════════════════════════════════════════
secao("13. MONETIZAÇÃO COMPLETA")
# ══════════════════════════════════════════════════

# Cupons
for cupom in ["BEMVINDO", "PSICOLOGO", "LAUNCH", "ALBERT10"]:
    s, d, t = req("POST", f"/api/v1/cupons/usar/{cupom}", {}, token=TOKEN)
    if s in [200,201]:
        log_ok(f"Cupom {cupom}: {d.get('desconto_aplicado')}% desconto")
    else:
        log_warn(f"Cupom {cupom}: {s}")

# PIX
s, d, t = req("GET", "/qr/")
if s == 200:
    log_ok("PIX/QR OK")
else:
    log_warn(f"PIX: {s}")

# Afiliados
s, d, t = req("POST", "/api/v1/afiliados/cadastrar", {
    "nome": "Afiliado Audit", "email": EMAIL, "profissao": "Psicologo"
})
if s in [200,201]:
    log_ok(f"Afiliados OK — codigo={d.get('codigo')}")
else:
    log_warn(f"Afiliados: {s}")

# ══════════════════════════════════════════════════
secao("14. ADMIN E GESTÃO")
# ══════════════════════════════════════════════════

for rota in ["/admin", "/api/v1/auth/stats/usuarios",
             "/api/v1/metricas-sistema/status",
             "/api/v1/logs-sistema/status",
             "/api/v1/sistema/backup/status",
             "/api/v1/feature-flags/status"]:
    s, d, t = req("GET", rota)
    if s in [200, 401, 403]:
        log_ok(f"Admin {rota} OK ({s})")
    else:
        log_warn(f"Admin {rota}: {s}")

# ══════════════════════════════════════════════════
secao("15. PWA E OFFLINE")
# ══════════════════════════════════════════════════

for rota in ["/manifest.json", "/sw.js", "/offline"]:
    s, d, t = req("GET", rota)
    if s == 200:
        log_ok(f"PWA {rota} OK ({t}ms)")
    else:
        log_erro(f"PWA {rota}: {s}")

# ══════════════════════════════════════════════════
secao("RESUMO FINAL — AUDITORIA 100%")
# ══════════════════════════════════════════════════

total = ok + warn + erro
pct_ok   = (ok   / total * 100) if total else 0
pct_warn = (warn / total * 100) if total else 0
pct_erro = (erro / total * 100) if total else 0

print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

score = int(pct_ok)
print(f"\n  {NEGRITO}📊 SCORE FINAL: {score}%{RESET}")

if score >= 95:
    print(f"  {VERDE}{NEGRITO}🚀 SISTEMA EXCELENTE! Pronto para produção.{RESET}")
elif score >= 80:
    print(f"  {AMARELO}{NEGRITO}⚡ Sistema bom! Pequenos ajustes.{RESET}")
else:
    print(f"  {VERMELHO}{NEGRITO}🔧 Precisa atenção.{RESET}")

print(f"\n  {NEGRITO}O que um código NÃO pode testar:{RESET}")
print(f"  → Design visual (abra o browser!)")
print(f"  → Experiência real do usuário")
print(f"  → Pagamento Stripe real")
print(f"  → Email chegando na caixa")

with open("auditoria_final_resultado.txt", "w") as f:
    f.write(f"Score Final: {score}%\n\n")
    for r in resultados:
        f.write(r + "\n")

print(f"\n  📄 Salvo em: auditoria_final_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
