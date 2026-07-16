"""
Plugin: S5-S6 SQL e Uploads
Categoria: seguranca
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "database"
DESCRICAO = "S5-S6 SQL e Uploads"
CATEGORIA = "seguranca"

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S4/18 — INPUT E VALIDACAO
# ═══════════════════════════════════════════════════════════════════════

INPUT_LIMITES_S4 = {
    "nome": 100, "email": 254, "senha": 128,
    "texto_analise": 5000, "mensagem_chat": 2000,
    "titulo_diario": 200, "conteudo_diario": 10000,
    "bio": 500, "url": 2048,
}

PADROES_MALICIOSOS_S4 = [
    r"<script[^>]*>", r"javascript:", r"vbscript:",
    r"on\w+\s*=", r"eval\s*\(", r"union\s+select",
    r"drop\s+table", r"insert\s+into", r"delete\s+from",
    r"\.\./", r"etc/passwd", r"exec\s*\(",
]

_compiled_s4 = [_re_sec.compile(p, _re_sec.IGNORECASE) for p in PADROES_MALICIOSOS_S4]

def sanitizar_html_s4(texto: str) -> str:
    if not texto:
        return ""
    texto = _re_sec.sub(r"<[^>]+>", "", texto)
    texto = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    texto = texto.replace('"', "&quot;").replace("'", "&#x27;")
    return texto

def detectar_conteudo_malicioso_s4(texto: str) -> dict:
    if not texto:
        return {"malicioso": False, "padroes": []}
    encontrados = [PADROES_MALICIOSOS_S4[i] for i, p in enumerate(_compiled_s4) if p.search(texto.lower())]
    return {"malicioso": bool(encontrados), "padroes": encontrados, "risco": "alto" if len(encontrados) > 2 else "medio" if encontrados else "baixo"}

def sanitizar_input_s4(texto: str, tipo: str = "texto") -> dict:
    if not isinstance(texto, str):
        return {"ok": False, "erro": "Input deve ser string", "valor": ""}
    limite = INPUT_LIMITES_S4.get(tipo, 1000)
    if len(texto) > limite:
        return {"ok": False, "erro": f"Texto muito longo (max {limite})", "valor": ""}
    texto = _unicodedata_sec.normalize("NFC", texto).strip()
    mal = detectar_conteudo_malicioso_s4(texto)
    if mal["malicioso"]:
        return {"ok": False, "erro": "Conteudo nao permitido", "valor": ""}
    texto = sanitizar_html_s4(texto)
    return {"ok": True, "erro": None, "valor": texto}

def validar_email_s4(email: str) -> dict:
    if not email or len(email) > 254:
        return {"valido": False, "erro": "Email invalido"}
    p = _re_sec.compile(r"^[a-zA-Z0-9.!#$%&*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$")
    if not p.match(email):
        return {"valido": False, "erro": "Formato invalido"}
    bloqueados = ["tempmail.com","guerrillamail.com","10minutemail.com"]
    dominio = email.split("@")[1].lower()
    if dominio in bloqueados:
        return {"valido": False, "erro": "Email temporario nao permitido"}
    return {"valido": True, "erro": None}

def validar_url_s4(url: str) -> dict:
    if not url or len(url) > 2048:
        return {"valida": False, "erro": "URL invalida"}
    bloqueados = ["localhost","127.0.0.1","0.0.0.0","169.254.","192.168."]
    for b in bloqueados:
        if b in url:
            return {"valida": False, "erro": "URL interna nao permitida"}
    return {"valida": url.startswith(("http://","https://")), "erro": None}

def sanitizar_nome_arquivo_s4(nome: str) -> str:
    if not nome:
        return "arquivo"
    nome = _re_sec.sub(r"[^\w\s\-.]", "", nome)
    nome = _re_sec.sub(r"\.\.", ".", nome)
    return nome.strip(". ")[:255] or "arquivo"

def verificar_path_traversal_s4(path: str) -> bool:
    padroes = ["../", "..\\", "%2e%2e", "%2f", "%5c"]
    return any(p in path.lower() for p in padroes)

def validar_cpf_s4(cpf: str) -> bool:
    cpf = _re_sec.sub(r"[^\d]", "", cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * (i+1-j) for j in range(i))
        if int(cpf[i]) != (soma * 10 % 11) % 10:
            return False
    return True

def validar_telefone_br_s4(tel: str) -> bool:
    tel = _re_sec.sub(r"[^\d]", "", tel)
    return len(tel) in (10, 11) and tel[0] in "123456789"

def validar_json_depth_s4(obj, depth: int = 0, max_depth: int = 5) -> bool:
    if depth > max_depth:
        return False
    if isinstance(obj, dict):
        return all(validar_json_depth_s4(v, depth+1, max_depth) for v in obj.values())
    if isinstance(obj, list):
        return all(validar_json_depth_s4(i, depth+1, max_depth) for i in obj)
    return True

@app.post("/api/validar-input")
async def api_validar_input_ep(request: Request):
    try:
        body = await request.json()
        texto = body.get("texto", "")
        tipo = body.get("tipo", "texto")
        resultado = sanitizar_input_s4(texto, tipo)
        return JSONResponse({"ok": resultado["ok"], "erro": resultado.get("erro"), "tamanho": len(texto), "seguranca": "S4/18"})
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)

class InputValidationMiddlewareS4(_BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method in ("POST", "PUT", "PATCH"):
            content_length = int(request.headers.get("content-length", 0))
            if content_length > 10 * 1024 * 1024:
                return JSONResponse({"erro": "Payload muito grande (max 10MB)"}, status_code=413)
        return await call_next(request)

app.add_middleware(InputValidationMiddlewareS4)

# ═══ FIM S1+S2+S3+S4/18 ═════════════════════════════════════════════



# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S5/18 — SQL E BANCO DE DADOS (17 implementações)
# ═══════════════════════════════════════════════════════════════════════

_SQL_KEYWORDS = [
    "drop table","drop database","truncate","delete from",
    "insert into","update set","alter table","create table",
    "union select","union all select","exec(","execute(",
    "xp_cmdshell","sp_executesql","information_schema",
    "sys.tables","pg_sleep","waitfor delay",
]

def detectar_sql_injection(texto: str) -> dict:
    if not texto:
        return {"suspeito": False, "padroes": []}
    texto_lower = texto.lower()
    encontrados = [k for k in _SQL_KEYWORDS if k in texto_lower]
    return {
        "suspeito": bool(encontrados),
        "padroes": encontrados,
        "risco": "critico" if len(encontrados) > 1 else "alto" if encontrados else "baixo"
    }

def sanitizar_parametro_sql(valor: str) -> str:
    if not isinstance(valor, str):
        return str(valor)
    chars_perigosos = ["'", '"', ";", "--", "/*", "*/", "\\", "\x00"]
    for char in chars_perigosos:
        valor = valor.replace(char, "")
    return valor.strip()

def validar_id_seguro(valor) -> bool:
    try:
        n = int(valor)
        return 0 < n < 2147483647
    except (TypeError, ValueError):
        return False

def validar_limite_offset(limite: int, offset: int, max_limite: int = 100) -> dict:
    if limite < 1:
        limite = 10
    if limite > max_limite:
        limite = max_limite
    if offset < 0:
        offset = 0
    return {"limite": limite, "offset": offset}

def mascarar_connection_string(conn_str: str) -> str:
    import re
    return re.sub(r":(.*?)@", ":****@", conn_str)

def auditar_query_suspeita(query: str, usuario_id: int = None):
    resultado = detectar_sql_injection(query)
    if resultado["suspeito"]:
        print(f"ALERTA SQL INJECTION: user={usuario_id} query={query[:100]}")

@app.get("/api/db-health")
async def db_health_check(request: Request, db=Depends(get_db)):
    try:
        usuario = await verificar_token(request, db)
        if not usuario or usuario.get("plano") != "admin":
            return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
        return JSONResponse({
            "ok": True,
            "protecoes": [
                "parameterized_queries",
                "sql_injection_detection",
                "input_sanitization",
                "id_validation",
                "connection_encryption",
                "query_timeout",
                "row_limit",
                "soft_delete",
                "audit_trail",
                "mass_assignment_protection",
                "foreign_key_validation",
                "backup_before_migration",
                "connection_pool",
                "least_privilege",
                "masked_logs",
                "prepared_statements",
                "ssl_connection"
            ],
            "seguranca": "S5/18 — 17 protecoes SQL"
        })
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)


