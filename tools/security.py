#!/usr/bin/env python3
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
