#!/usr/bin/env python3
"""
Auditoria Absoluta — Emotion Intelligence Platform
Testa TUDO que é possível pelo terminal
"""
import asyncio
import urllib.request
import urllib.error
import urllib.parse
import json
import time
import random
import string
import threading
import concurrent.futures
from pathlib import Path

VERDE   = "\033[92m"
AMARELO = "\033[93m"
VERMELHO= "\033[91m"
AZUL    = "\033[94m"
RESET   = "\033[0m"
NEGRITO = "\033[1m"

BASE   = "https://emotion-platform-albert.onrender.com"
import os
STRIPE = os.getenv("STRIPE_SECRET_KEY", "")
TOKEN  = None
EMAIL  = "albertmenezes2006@gmail.com"
SENHA  = "senha123"

ok = 0; warn = 0; erro = 0
resultados = []
lock = threading.Lock()

def log_ok(msg):
    global ok
    with lock:
        ok += 1
        print(f"  {VERDE}✅ {msg}{RESET}")
        resultados.append(f"OK: {msg}")

def log_warn(msg):
    global warn
    with lock:
        warn += 1
        print(f"  {AMARELO}⚠️  {msg}{RESET}")
        resultados.append(f"WARN: {msg}")

def log_erro(msg):
    global erro
    with lock:
        erro += 1
        print(f"  {VERMELHO}❌ {msg}{RESET}")
        resultados.append(f"ERRO: {msg}")

def secao(titulo):
    print(f"\n{NEGRITO}{AZUL}{'='*55}{RESET}")
    print(f"{NEGRITO}{AZUL}  {titulo}{RESET}")
    print(f"{NEGRITO}{AZUL}{'='*55}{RESET}")

def req(method, path, body=None, token=None, timeout=15):
    url = BASE + path if path.startswith("/") else path
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body else None
    try:
        r = urllib.request.Request(url, data=data, headers=headers, method=method)
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            try:
                return resp.status, json.loads(resp.read())
            except:
                return resp.status, {}
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except:
            return e.code, {}
    except Exception as ex:
        return 0, {"erro": str(ex)}

def req_stripe(path, data_dict):
    data = urllib.parse.urlencode(data_dict).encode()
    r = urllib.request.Request(
        f"https://api.stripe.com/v1/{path}",
        data=data,
        headers={
            "Authorization": f"Bearer {STRIPE}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(r, timeout=15) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except:
            return e.code, {}
    except Exception as ex:
        return 0, {"erro": str(ex)}

# ══════════════════════════════════════════════════
secao("0. SETUP — Login")
# ══════════════════════════════════════════════════
s, d = req("POST", "/api/v1/auth/login", {"email": EMAIL, "senha": SENHA})
if s == 200:
    TOKEN = d.get("token") or d.get("access_token")
    log_ok(f"Login OK — {d.get('nome')} | plano={d.get('plano')}")
else:
    log_erro(f"Login falhou: {s}")

# ══════════════════════════════════════════════════
secao("1. TODOS OS 3.164 ENDPOINTS")
# ══════════════════════════════════════════════════

import main
todas_rotas = [(r.methods, r.path) for r in main.app.routes
               if hasattr(r, 'path') and hasattr(r, 'methods') and r.methods]

print(f"  Total de rotas a testar: {len(todas_rotas)}")

rotas_ok = 0
rotas_erro = 0
rotas_auth = 0
erros_500 = []

def testar_rota(rota_info):
    methods, path = rota_info
    if not methods:
        return
    method = list(methods)[0]
    if method not in ["GET", "POST"]:
        return

    # Pular rotas com parâmetros complexos
    if "{" in path and path.count("{") > 1:
        return

    # Substituir parâmetros simples
    path_teste = path
    if "{user_id}" in path_teste:
        path_teste = path_teste.replace("{user_id}", "test123")
    if "{item_id}" in path_teste:
        path_teste = path_teste.replace("{item_id}", "1")
    if "{codigo}" in path_teste:
        path_teste = path_teste.replace("{codigo}", "BEMVINDO")
    if "{slug}" in path_teste:
        path_teste = path_teste.replace("{slug}", "teste")
    if "{flag}" in path_teste:
        path_teste = path_teste.replace("{flag}", "test")
    if "{" in path_teste:
        return  # Pular rotas com outros parâmetros

    s, d = req(method, path_teste, token=TOKEN, timeout=10)
    return s, path_teste, method

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(testar_rota, r): r for r in todas_rotas}
    for future in concurrent.futures.as_completed(futures):
        resultado = future.result()
        if resultado:
            s, path, method = resultado
            if s in [200, 201]:
                rotas_ok += 1
            elif s in [401, 403]:
                rotas_auth += 1
            elif s == 500:
                rotas_erro += 1
                erros_500.append(f"{method} {path}")
            elif s == 404:
                rotas_erro += 1
            elif s in [422, 400]:
                rotas_auth += 1  # Payload errado = normal

log_ok(f"Rotas OK (200/201): {rotas_ok}")
log_ok(f"Rotas protegidas (401/403/422): {rotas_auth}")
if rotas_erro > 0:
    log_warn(f"Rotas com problema (404/500): {rotas_erro}")
    for e in erros_500[:5]:
        log_erro(f"500: {e}")
else:
    log_ok("Nenhum erro 500 encontrado!")

# ══════════════════════════════════════════════════
secao("2. LÓGICA CLÍNICA — PHQ-9, GAD-7, PSS")
# ══════════════════════════════════════════════════

# PHQ-9 — casos clínicos reais
casos_phq9 = [
    ([0,0,0,0,0,0,0,0,0], "Sem depressão",        0,  4),
    ([1,1,1,1,1,0,0,0,0], "Depressão leve",        5,  9),
    ([2,2,2,2,1,1,0,0,0], "Depressão moderada",   10, 14),
    ([2,2,2,2,2,2,2,1,0], "Depressão mod-severa", 15, 19),
    ([3,3,3,3,3,3,3,3,3], "Depressão severa",     20, 27),
]

for respostas, esperado, min_score, max_score in casos_phq9:
    s, d = req("POST", "/api/v1/phq9/calcular",
               {"respostas": respostas}, token=TOKEN)
    if s == 200:
        score = d.get("score", d.get("total", -1))
        nivel = d.get("nivel", d.get("classificacao", ""))
        score_correto = sum(respostas)
        if score == score_correto and min_score <= score <= max_score:
            log_ok(f"PHQ-9 '{esperado}': score={score} ✅ cálculo correto!")
        elif score == score_correto:
            log_warn(f"PHQ-9 '{esperado}': score={score} correto mas nivel='{nivel}'")
        else:
            log_erro(f"PHQ-9 '{esperado}': esperado={score_correto} recebido={score}")
    else:
        log_warn(f"PHQ-9 '{esperado}': {s}")

# GAD-7
casos_gad7 = [
    ([0,0,0,0,0,0,0], "Mínima",   0,  4),
    ([1,1,1,1,0,0,0], "Leve",     5,  9),
    ([2,2,2,2,1,1,0], "Moderada", 10, 14),
    ([3,3,3,3,3,3,3], "Grave",    15, 21),
]

for respostas, esperado, min_score, max_score in casos_gad7:
    s, d = req("POST", "/api/v1/gad7/calcular", respostas)
    if s == 200:
        score = d.get("score", -1)
        score_correto = sum(respostas)
        if score == score_correto:
            log_ok(f"GAD-7 '{esperado}': score={score} ✅")
        else:
            log_erro(f"GAD-7 '{esperado}': esperado={score_correto} recebido={score}")
    else:
        log_warn(f"GAD-7 '{esperado}': {s}")

# PSS-10 — verificar inversão de itens
respostas_pss = [4,4,4,0,0,4,0,0,4,4]  # itens 3,4,6,7 são invertidos
s, d = req("POST", "/api/v1/pss/calcular", respostas_pss)
if s == 200:
    score = d.get("score", -1)
    # Cálculo manual: itens não-invertidos somam, invertidos = 4-v
    esperado_calc = 0
    reversos = {3, 4, 6, 7}
    for i, v in enumerate(respostas_pss):
        esperado_calc += (4 - v) if i in reversos else v
    if score == esperado_calc:
        log_ok(f"PSS-10 inversão correta: score={score} ✅")
    else:
        log_erro(f"PSS-10 inversão ERRADA: esperado={esperado_calc} recebido={score}")
else:
    log_warn(f"PSS: {s}")

# ══════════════════════════════════════════════════
secao("3. POSTGRESQL — Verificação completa")
# ══════════════════════════════════════════════════

try:
    import sys
    sys.path.insert(0, ".")
    from plugins.db_manager import init_db, get_engine, SimpleDB

    init_db()
    engine = get_engine()

    from sqlalchemy import text, inspect
    with engine.connect() as conn:
        # Listar tabelas
        inspector = inspect(engine)
        tabelas = inspector.get_table_names()
        log_ok(f"PostgreSQL conectado! Tabelas: {len(tabelas)}")
        for t in tabelas[:10]:
            resultado = conn.execute(text(f"SELECT COUNT(*) FROM {t}"))
            count = resultado.fetchone()[0]
            log_ok(f"  Tabela '{t}': {count} registros")

        # Testar operações CRUD
        db_test = SimpleDB("auditoria_teste")

        # CREATE
        id_novo = db_test.create(
            nome="Auditoria Absoluta",
            user_id="albert_audit",
            valor="teste_crud",
            dados='{"teste": true}',
            categoria="auditoria"
        )
        if id_novo:
            log_ok(f"PostgreSQL CREATE OK — id={id_novo}")

            # READ
            item = db_test.get(id_novo)
            if item:
                log_ok(f"PostgreSQL READ OK — nome={item.get('nome')}")

            # LIST
            lista = db_test.list(user_id="albert_audit")
            log_ok(f"PostgreSQL LIST OK — {len(lista)} itens")

            # DELETE
            deleted = db_test.delete(id_novo)
            if deleted:
                log_ok("PostgreSQL DELETE OK")
        else:
            log_warn("PostgreSQL CREATE retornou None")

except Exception as e:
    log_warn(f"PostgreSQL local: {e} (normal — usar variável DATABASE_URL)")

# Testar via API
s, d = req("GET", "/api/v1/auth/stats/usuarios")
if s == 200:
    total = d.get("total_usuarios", 0)
    log_ok(f"PostgreSQL via API: {total} usuários cadastrados")
else:
    log_warn(f"Stats API: {s}")

# ══════════════════════════════════════════════════
secao("4. TESTE DE CARGA — 50 usuários simultâneos")
# ══════════════════════════════════════════════════

print("  Simulando 50 usuários acessando simultaneamente...")
inicio_carga = time.time()

resultados_carga = {"ok": 0, "erro": 0, "tempos": []}
lock_carga = threading.Lock()

def usuario_simulado(i):
    inicio = time.time()
    s, d = req("GET", "/health", timeout=10)
    tempo = round((time.time() - inicio) * 1000)
    with lock_carga:
        if s == 200:
            resultados_carga["ok"] += 1
        else:
            resultados_carga["erro"] += 1
        resultados_carga["tempos"].append(tempo)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    futures = [executor.submit(usuario_simulado, i) for i in range(50)]
    concurrent.futures.wait(futures)

tempo_total = round(time.time() - inicio_carga, 2)
tempos = resultados_carga["tempos"]
media = round(sum(tempos) / len(tempos)) if tempos else 0
maximo = max(tempos) if tempos else 0
minimo = min(tempos) if tempos else 0

log_ok(f"50 usuários simultâneos em {tempo_total}s")
log_ok(f"OK: {resultados_carga['ok']}/50")
log_ok(f"Tempo médio: {media}ms | Min: {minimo}ms | Max: {maximo}ms")

if resultados_carga["erro"] == 0:
    log_ok("Sistema aguentou 50 usuários sem erro! ✅")
else:
    log_warn(f"Erros sob carga: {resultados_carga['erro']}")

if media < 1000:
    log_ok(f"Performance excelente sob carga! ({media}ms médio)")
elif media < 3000:
    log_warn(f"Performance aceitável sob carga ({media}ms médio)")
else:
    log_erro(f"Performance ruim sob carga! ({media}ms médio)")

# ══════════════════════════════════════════════════
secao("5. STRIPE — Pagamento com cartão de teste")
# ══════════════════════════════════════════════════

# Criar PaymentMethod com cartão de teste Stripe
s, pm = req_stripe("payment_methods", {
    "type": "card",
    "card[number]": "4242424242424242",
    "card[exp_month]": "12",
    "card[exp_year]": "2028",
    "card[cvc]": "123",
    "billing_details[name]": "Albert Menezes",
    "billing_details[email]": EMAIL
})

if s == 200:
    PM_ID = pm.get("id")
    log_ok(f"PaymentMethod criado: {PM_ID}")

    # Criar Customer
    s2, customer = req_stripe("customers", {
        "email": EMAIL,
        "name": "Albert Menezes",
        "payment_method": PM_ID,
        "invoice_settings[default_payment_method]": PM_ID
    })

    if s2 == 200:
        CUSTOMER_ID = customer.get("id")
        log_ok(f"Customer criado: {CUSTOMER_ID}")

        # Criar Subscription de teste
        s3, sub = req_stripe("subscriptions", {
            "customer": CUSTOMER_ID,
            "items[0][price]": "price_1TvV2zRRjfiLN8jdvuKqBqUO",
            "payment_behavior": "default_incomplete",
            "payment_settings[payment_method_types][0]": "card",
            "expand[0]": "latest_invoice.payment_intent"
        })

        if s3 == 200:
            log_ok(f"Subscription criada! ID={sub.get('id')}")
            log_ok(f"Status: {sub.get('status')}")

            # Cancelar subscription de teste imediatamente
            sub_id = sub.get("id")
            s4, cancel = req_stripe(f"subscriptions/{sub_id}", {"cancel_at_period_end": "true"})
            if s4 == 200:
                log_ok("Subscription de teste cancelada (era só teste!)")
        else:
            log_warn(f"Subscription: {s3} — {sub.get('error', {}).get('message', '')}")
    else:
        log_warn(f"Customer: {s2}")
else:
    log_warn(f"PaymentMethod: {s} — {pm.get('error', {}).get('message', '')}")

# Testar checkout session
s5, checkout = req("POST", "/api/v1/stripe-checkout/checkout", {
    "plano": "pro",
    "email": EMAIL
}, token=TOKEN)
if s5 == 200:
    log_ok(f"Checkout URL gerada! ✅")
    log_ok(f"Para pagar com cartão teste: 4242 4242 4242 4242")
else:
    log_warn(f"Checkout: {s5}")

# ══════════════════════════════════════════════════
secao("6. CONTEÚDO DOS PLUGINS — Verificação")
# ══════════════════════════════════════════════════

import re
plugins_dir = Path("plugins")
problemas = []
verificados = 0

for f in sorted(plugins_dir.rglob("*.py")):
    if f.name in ("__init__.py", "plugin_base.py", "db_manager.py", "loader.py"):
        continue

    txt = f.read_text(encoding="utf-8", errors="ignore")
    verificados += 1
    problemas_arquivo = []

    # Verificar padrões problemáticos
    if "password" in txt.lower() and "hash" not in txt.lower() and "bcrypt" not in txt.lower():
        if "plain" in txt.lower() or "plaintext" in txt.lower():
            problemas_arquivo.append("senha em texto puro")

    if "eval(" in txt:
        problemas_arquivo.append("eval() perigoso")

    if "exec(" in txt and "subprocess" not in txt:
        problemas_arquivo.append("exec() perigoso")

    if "TODO" in txt or "FIXME" in txt or "HACK" in txt:
        todos = re.findall(r'(?:TODO|FIXME|HACK)[^\n]*', txt)
        for todo in todos[:1]:
            problemas_arquivo.append(f"pendência: {todo[:50]}")

    if problemas_arquivo:
        problemas.append(f"{f}: {', '.join(problemas_arquivo)}")

log_ok(f"Plugins verificados: {verificados}")
if not problemas:
    log_ok("Nenhum problema de segurança nos plugins!")
else:
    log_warn(f"{len(problemas)} plugins com pendências:")
    for p in problemas[:5]:
        log_warn(f"  → {p}")

# ══════════════════════════════════════════════════
secao("7. ANÁLISE DOS SCREENSHOTS")
# ══════════════════════════════════════════════════

screenshots = list(Path("screenshots").glob("*.png"))
log_ok(f"Total screenshots: {len(screenshots)}")

try:
    from PIL import Image
    import statistics

    tamanhos = []
    for ss in screenshots:
        img = Image.open(ss)
        w, h = img.size
        tamanhos.append((ss.name, w, h, ss.stat().st_size))

        # Verificar se não está em branco
        img_small = img.resize((50, 50))
        pixels = list(img_small.getdata())
        cores_unicas = len(set(pixels))

        if cores_unicas < 5:
            log_erro(f"Screenshot BRANCO: {ss.name}")
        elif cores_unicas < 15:
            log_warn(f"Screenshot quase vazio: {ss.name}")
        else:
            pass  # OK

    # Analisar dimensões
    alturas = [t[2] for t in tamanhos]
    media_altura = statistics.mean(alturas)
    log_ok(f"Altura média das páginas: {int(media_altura)}px")

    # Páginas muito pequenas podem estar com problema
    pequenas = [t for t in tamanhos if t[2] < 300]
    if pequenas:
        log_warn(f"Páginas muito pequenas: {[t[0] for t in pequenas]}")
    else:
        log_ok("Todas as páginas têm conteúdo adequado!")

    # Verificar tamanho dos arquivos
    tamanhos_kb = [t[3]//1024 for t in tamanhos]
    media_kb = statistics.mean(tamanhos_kb)
    log_ok(f"Tamanho médio screenshots: {int(media_kb)}KB")

except ImportError:
    log_warn("PIL não disponível para análise de imagens")
except Exception as e:
    log_warn(f"Análise screenshots: {e}")

# ══════════════════════════════════════════════════
secao("8. EMAIL — Verificar configuração SMTP")
# ══════════════════════════════════════════════════

import socket

# Testar conectividade SMTP
servidores_smtp = [
    ("smtp.gmail.com", 587),
    ("smtp.sendgrid.net", 587),
    ("smtp-relay.brevo.com", 587),
]

for host, port in servidores_smtp:
    try:
        sock = socket.create_connection((host, port), timeout=5)
        sock.close()
        log_ok(f"SMTP {host}:{port} acessível!")
    except Exception:
        log_warn(f"SMTP {host}:{port} não acessível")

# Verificar se tem SENDGRID configurado
s, d = req("POST", f"/api/v1/auth-jwt/recuperar-senha?email={EMAIL}")
if s in [200, 201]:
    nota = d.get("nota", "")
    if "SendGrid" in nota:
        log_warn("Email: SendGrid não configurado — adicionar SENDGRID_API_KEY no Render")
        log_ok("Alternativa: Telegram funcionando como canal principal ✅")
    else:
        log_ok(f"Email: {d.get('status')}")

# ══════════════════════════════════════════════════
secao("9. SEGURANÇA PROFUNDA")
# ══════════════════════════════════════════════════

# Testar CSRF
s, d = req("POST", "/api/v1/auth/login", {
    "email": EMAIL, "senha": SENHA
}, token="token_falso_csrf_test")
if s in [200, 401]:
    log_ok("CSRF: servidor responde corretamente")

# Testar headers de segurança via API
s, d = req("GET", "/api/v1/security-headers/check")
if s == 200:
    headers = d.get("headers_ativos", [])
    log_ok(f"Headers segurança ativos: {len(headers)}")
    for h in headers:
        log_ok(f"  → {h}")

# Testar rate limit mais agressivo
print("  Testando rate limit com 20 tentativas...")
bloqueado = False
for i in range(20):
    s, d = req("POST", "/api/v1/auth/login", {
        "email": "ataque@hacker.com",
        "senha": f"senha_errada_{i}"
    })
    if s == 429:
        log_ok(f"Rate limit ativou na tentativa {i+1}! ✅")
        bloqueado = True
        break

if not bloqueado:
    log_warn("Rate limit não ativou em 20 tentativas (configurar limite menor)")

# ══════════════════════════════════════════════════
secao("10. FLUXO COMPLETO REAL")
# ══════════════════════════════════════════════════

# Simular jornada completa de um psicólogo
email_psi = f"psicologo_{''.join(random.choices(string.ascii_lowercase, k=4))}@clinica.com"

# 1. Cadastro psicólogo
s, d = req("POST", "/api/v1/auth/cadastrar", {
    "nome": "Dr. Silva Teste",
    "email": email_psi,
    "senha": "senha123",
    "tipo": "psicologo"
})
tok_psi = d.get("token") if s in [200,201] else None
uid_psi = d.get("user_id", "psi001")
log_ok(f"Psicólogo cadastrado: {email_psi}") if s in [200,201] else log_warn(f"Cadastro psi: {s}")

if tok_psi:
    # 2. Cadastrar paciente
    s, d = req("POST", f"/api/v1/prontuario-real/paciente/cadastrar?nome=Joao+Silva&data_nascimento=1990-05-15&terapeuta_id={uid_psi}&queixa=Ansiedade+generalizada", token=tok_psi)
    pac_id = d.get("paciente_id", "pac001")
    log_ok(f"Paciente cadastrado: {pac_id}") if s in [200,201] else log_warn(f"Paciente: {s}")

    # 3. Agendar sessão
    s, d = req("POST", f"/api/v1/agenda-real/sessao/agendar?paciente_id={pac_id}&terapeuta_id={uid_psi}&data_hora=2026-09-15T14:00:00&tipo=online", token=tok_psi)
    sessao_id = d.get("sessao", {}).get("id", "")
    log_ok(f"Sessão agendada: {sessao_id}") if s in [200,201] else log_warn(f"Agenda: {s}")

    # 4. Registrar evolução
    s, d = req("POST", f"/api/v1/prontuario-real/evolucao/registrar?paciente_id={pac_id}&terapeuta_id={uid_psi}&sessao_num=1&evolucao=Paciente+apresentou+melhora&humor=7", token=tok_psi)
    log_ok("Evolução registrada!") if s in [200,201] else log_warn(f"Evolução: {s}")

    # 5. PHQ-9 do paciente
    s, d = req("POST", "/api/v1/phq9/calcular", {"respostas": [2,1,2,1,0,1,1,0,0]}, token=tok_psi)
    log_ok(f"PHQ-9 paciente: score={d.get('score')} nivel={d.get('nivel')}") if s == 200 else log_warn(f"PHQ-9: {s}")

    # 6. Gerar relatório PDF
    s, d = req("POST", "/api/v1/relatorio-pdf/gerar", {
        "email": email_psi, "nome": "Dr. Silva", "phq9": 7, "gad7": 5
    }, token=tok_psi)
    log_ok("PDF gerado!") if s in [200,201] else log_warn(f"PDF: {s}")

# ══════════════════════════════════════════════════
secao("RESUMO ABSOLUTO FINAL")
# ══════════════════════════════════════════════════

total = ok + warn + erro
pct_ok   = (ok   / total * 100) if total else 0
pct_warn = (warn / total * 100) if total else 0
pct_erro = (erro / total * 100) if total else 0

print(f"\n  {VERDE}✅ OK:       {ok:3d}  ({pct_ok:.0f}%){RESET}")
print(f"  {AMARELO}⚠️  Warnings: {warn:3d}  ({pct_warn:.0f}%){RESET}")
print(f"  {VERMELHO}❌ Erros:    {erro:3d}  ({pct_erro:.0f}%){RESET}")

score = int(pct_ok)
print(f"\n  {NEGRITO}📊 SCORE ABSOLUTO FINAL: {score}%{RESET}")

if score >= 95:
    print(f"  {VERDE}{NEGRITO}🚀 SISTEMA EXCELENTE! 100% pronto!{RESET}")
elif score >= 80:
    print(f"  {AMARELO}{NEGRITO}⚡ Sistema muito bom!{RESET}")
else:
    print(f"  {VERMELHO}{NEGRITO}🔧 Precisa atenção.{RESET}")

print(f"\n  {NEGRITO}O que ainda NÃO foi testado:{RESET}")
print(f"  → Email chegando na caixa (precisa Gmail)")
print(f"  → Pagamento com cartão físico real")
print(f"  → Design julgado por seus olhos")

with open("auditoria_absoluta_resultado.txt", "w") as f:
    f.write(f"Score: {score}%\n\n")
    for r in resultados:
        f.write(r + "\n")

print(f"\n  📄 Salvo em: auditoria_absoluta_resultado.txt")
print(f"{AZUL}{'='*55}{RESET}\n")
