"""
Plugin: S1-S2 Senhas e Headers
Categoria: seguranca
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "auth"
DESCRICAO = "S1-S2 Senhas e Headers"
CATEGORIA = "seguranca"

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S1/18 — SENHAS E AUTENTICAÇÃO
# ═══════════════════════════════════════════════════════════════════════


BCRYPT_ROUNDS = 12
SENHA_MIN_CHARS = 8
MAX_TENTATIVAS_LOGIN = 5
BLOQUEIO_MINUTOS = 30
MAX_SESSOES_SIMULTANEAS = 5
TOKEN_EXPIRACAO_MINUTOS = 15
HISTORICO_SENHAS = 5

_tentativas_login_sec = {}
_contas_bloqueadas_sec = {}
_historico_senhas_sec = {}
_sessoes_ativas_sec = {}
_dispositivos_conhecidos_sec = {}
_tokens_invalidados_sec = set()

def validar_forca_senha(senha: str) -> dict:
    erros = []
    score = 0
    if len(senha) < SENHA_MIN_CHARS:
        erros.append(f"Minimo {SENHA_MIN_CHARS} caracteres")
    else:
        score += 1
    if not _re_sec.search(r"[A-Z]", senha):
        erros.append("Pelo menos 1 maiuscula")
    else:
        score += 1
    if not _re_sec.search(r"[a-z]", senha):
        erros.append("Pelo menos 1 minuscula")
    else:
        score += 1
    if not _re_sec.search(r"\d", senha):
        erros.append("Pelo menos 1 numero")
    else:
        score += 1
    if not _re_sec.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("Pelo menos 1 especial")
    else:
        score += 1
    if len(senha) >= 12:
        score += 1
    if len(senha) >= 16:
        score += 1
    niveis = {0:"Muito fraca",1:"Muito fraca",2:"Fraca",3:"Media",4:"Boa",5:"Forte",6:"Muito forte",7:"Excelente"}
    return {"valida": len(erros)==0, "score": score, "nivel": niveis.get(score,"Fraca"), "erros": erros}

def hash_senha_seguro(senha: str) -> str:
    try:
        import bcrypt
        salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
        return bcrypt.hashpw(senha.encode(), salt).decode()
    except ImportError:
        import hashlib
        import os
        salt = os.urandom(32).hex()
        h = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt.encode(), 310000)
        return f"pbkdf2:{salt}:{h.hex()}"

def verificar_senha_segura(senha: str, hash_armazenado: str) -> bool:
    try:
        if hash_armazenado.startswith("pbkdf2:"):
            import hashlib
            _, salt, h = hash_armazenado.split(":")
            novo_h = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt.encode(), 310000)
            return _hmac_sec.compare_digest(h, novo_h.hex())
        import bcrypt
        return bcrypt.checkpw(senha.encode(), hash_armazenado.encode())
    except Exception:
        return False

def conta_bloqueada_sec(identificador: str) -> bool:
    from datetime import datetime
    if identificador not in _contas_bloqueadas_sec:
        return False
    if datetime.now() > _contas_bloqueadas_sec[identificador]:
        del _contas_bloqueadas_sec[identificador]
        _tentativas_login_sec.pop(identificador, None)
        return False
    return True

def registrar_tentativa_login_sec(identificador: str, sucesso: bool) -> dict:
    from datetime import datetime
    agora = datetime.now()
    janela = agora - _timedelta_sec(minutes=BLOQUEIO_MINUTOS)
    if identificador not in _tentativas_login_sec:
        _tentativas_login_sec[identificador] = []
    _tentativas_login_sec[identificador] = [
        t for t in _tentativas_login_sec[identificador] if t > janela
    ]
    if not sucesso:
        _tentativas_login_sec[identificador].append(agora)
    tentativas = len(_tentativas_login_sec[identificador])
    if tentativas >= MAX_TENTATIVAS_LOGIN:
        _contas_bloqueadas_sec[identificador] = agora + _timedelta_sec(minutes=BLOQUEIO_MINUTOS)
    return {"tentativas": tentativas, "bloqueado": tentativas >= MAX_TENTATIVAS_LOGIN, "restantes": max(0, MAX_TENTATIVAS_LOGIN - tentativas)}

def gerar_fingerprint_dispositivo_sec(request: Request) -> str:
    import hashlib
    ua = request.headers.get("user-agent", "")
    ip = request.client.host if request.client else ""
    accept = request.headers.get("accept-language", "")
    return hashlib.sha256(f"{ua}:{ip}:{accept}".encode()).hexdigest()[:32]

def gerar_token_seguro_sec(tamanho: int = 32) -> str:
    import secrets
    return secrets.token_urlsafe(tamanho)

def invalidar_token_sec(token: str):
    _tokens_invalidados_sec.add(token[:32])

def token_invalido_sec(token: str) -> bool:
    return token[:32] in _tokens_invalidados_sec

def comparacao_segura_sec(a: str, b: str) -> bool:
    return _hmac_sec.compare_digest(
        a.encode() if isinstance(a, str) else a,
        b.encode() if isinstance(b, str) else b
    )

def calcular_risco_login_sec(ip: str, fingerprint: str, usuario_id: int = None) -> dict:
    score = 0
    fatores = []
    tentativas = len(_tentativas_login_sec.get(ip, []))
    if tentativas > 0:
        score += tentativas * 10
        fatores.append(f"{tentativas} tentativas recentes")
    if usuario_id and fingerprint not in _dispositivos_conhecidos_sec.get(usuario_id, set()):
        score += 25
        fatores.append("Dispositivo desconhecido")
    nivel = "baixo" if score < 25 else "medio" if score < 50 else "alto"
    return {"score": score, "nivel": nivel, "fatores": fatores}

@app.post("/api/verificar-senha")
async def api_verificar_senha(request: Request):
    try:
        body = await request.json()
        senha = body.get("senha", "")
        resultado = validar_forca_senha(senha)
        return JSONResponse({"ok": True, "valida": resultado["valida"], "score": resultado["score"], "nivel": resultado["nivel"], "erros": resultado["erros"]})
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)


