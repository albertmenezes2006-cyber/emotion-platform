"""
Plugin: S7-S8 Sessoes e Logs
Categoria: seguranca
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "sessoes"
DESCRICAO = "S7-S8 Sessoes e Logs"
CATEGORIA = "seguranca"

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S6/18 — UPLOADS E ARQUIVOS (12 implementações)
# ═══════════════════════════════════════════════════════════════════════

UPLOAD_CONFIG = {
    "tamanho_max_mb": 10,
    "extensoes_permitidas": {
        "imagem": [".jpg",".jpeg",".png",".gif",".webp"],
        "audio":  [".mp3",".wav",".ogg",".m4a",".webm"],
        "doc":    [".pdf",".txt"],
    },
    "mimes_permitidos": {
        "image/jpeg","image/png","image/gif","image/webp",
        "audio/mpeg","audio/wav","audio/ogg","audio/mp4",
        "audio/webm","application/pdf","text/plain",
    },
    "chars_proibidos_nome": ["/","\\",":","*","?",'"',"<",">","|","\x00"],
}

def validar_extensao_arquivo(nome: str, tipo: str = "imagem") -> dict:
    import os
    if not nome:
        return {"valida": False, "erro": "Nome vazio"}
    ext = os.path.splitext(nome)[1].lower()
    permitidas = UPLOAD_CONFIG["extensoes_permitidas"].get(tipo, [])
    if ext not in permitidas:
        return {"valida": False, "erro": f"Extensao {ext} nao permitida", "permitidas": permitidas}
    return {"valida": True, "extensao": ext}

def validar_tamanho_arquivo(tamanho_bytes: int) -> dict:
    max_bytes = UPLOAD_CONFIG["tamanho_max_mb"] * 1024 * 1024
    if tamanho_bytes > max_bytes:
        return {"valido": False, "erro": f"Arquivo muito grande (max {UPLOAD_CONFIG['tamanho_max_mb']}MB)"}
    return {"valido": True, "tamanho_mb": round(tamanho_bytes/1024/1024, 2)}

def sanitizar_nome_upload(nome: str) -> str:
    import re
    import os
    if not nome:
        return "arquivo"
    for char in UPLOAD_CONFIG["chars_proibidos_nome"]:
        nome = nome.replace(char, "_")
    nome = re.sub(r"\.{2,}", ".", nome)
    base, ext = os.path.splitext(nome)
    base = re.sub(r"[^\w\-]", "_", base)[:50]
    return f"{base}{ext.lower()}"

def gerar_nome_seguro_upload(nome_original: str) -> str:
    import secrets
    import os
    ext = os.path.splitext(nome_original)[1].lower()
    return f"{secrets.token_hex(16)}{ext}"

def verificar_mime_upload(content_type: str) -> bool:
    return content_type.split(";")[0].strip() in UPLOAD_CONFIG["mimes_permitidos"]

def verificar_magic_bytes(conteudo: bytes, extensao: str) -> bool:
    magic = {
        ".jpg":  [b"\xff\xd8\xff"],
        ".jpeg": [b"\xff\xd8\xff"],
        ".png":  [b"\x89PNG"],
        ".gif":  [b"GIF87a", b"GIF89a"],
        ".pdf":  [b"%PDF"],
        ".mp3":  [b"ID3", b"\xff\xfb"],
        ".wav":  [b"RIFF"],
    }
    esperados = magic.get(extensao.lower(), [])
    if not esperados:
        return True
    return any(conteudo.startswith(m) for m in esperados)

def verificar_zip_bomb(conteudo: bytes, max_ratio: int = 100) -> bool:
    if not conteudo[:4] == b"PK\x03\x04":
        return False
    try:
        import zipfile
        import io
        with zipfile.ZipFile(io.BytesIO(conteudo)) as z:
            total = sum(i.file_size for i in z.infolist())
            return total > len(conteudo) * max_ratio
    except Exception:
        return False

def remover_metadata_exif(conteudo: bytes, extensao: str) -> bytes:
    if extensao.lower() not in (".jpg", ".jpeg"):
        return conteudo
    try:
        from PIL import Image
        import io
        img = Image.open(io.BytesIO(conteudo))
        saida = io.BytesIO()
        img_sem_exif = Image.new(img.mode, img.size)
        img_sem_exif.putdata(list(img.getdata()))
        img_sem_exif.save(saida, format="JPEG", quality=95)
        return saida.getvalue()
    except Exception:
        return conteudo

def validar_upload_completo(nome: str, conteudo: bytes, content_type: str, tipo: str = "imagem") -> dict:
    import os
    erros = []
    ext = os.path.splitext(nome)[1].lower()
    v_ext = validar_extensao_arquivo(nome, tipo)
    if not v_ext["valida"]:
        erros.append(v_ext["erro"])
    v_tam = validar_tamanho_arquivo(len(conteudo))
    if not v_tam["valido"]:
        erros.append(v_tam["erro"])
    if not verificar_mime_upload(content_type):
        erros.append(f"MIME type nao permitido: {content_type}")
    if conteudo and not verificar_magic_bytes(conteudo, ext):
        erros.append("Conteudo do arquivo nao corresponde a extensao")
    if verificar_zip_bomb(conteudo):
        erros.append("Arquivo suspeito detectado")
    return {
        "valido": len(erros) == 0,
        "erros": erros,
        "nome_seguro": gerar_nome_seguro_upload(nome),
        "tamanho_mb": round(len(conteudo)/1024/1024, 2)
    }

# ═══════════════════════════════════════════════════════════════════════
# SEGURANÇA S7/18 — SESSOES E TOKENS (16 implementações)
# ═══════════════════════════════════════════════════════════════════════


_sessoes_db_s7: dict = {}
_refresh_tokens_s7: dict = {}
_token_familias_s7: dict = {}

SESSION_CONFIG = {
    "access_token_minutos": 60,
    "refresh_token_dias": 30,
    "max_sessoes_user": 5,
    "inatividade_minutos": 120,
}

def gerar_access_token_s7(usuario_id: int, fingerprint: str) -> str:
    token = _secrets_s7.token_urlsafe(32)
    _sessoes_db_s7[token] = {
        "usuario_id": usuario_id,
        "fingerprint": fingerprint,
        "criado_em": _datetime_s7.now().isoformat(),
        "ultimo_acesso": _datetime_s7.now().isoformat(),
        "ativo": True
    }
    return token

def gerar_refresh_token_s7(usuario_id: int, familia: str = None) -> str:
    if not familia:
        familia = _secrets_s7.token_hex(16)
    token = _secrets_s7.token_urlsafe(48)
    _refresh_tokens_s7[token] = {
        "usuario_id": usuario_id,
        "familia": familia,
        "criado_em": _datetime_s7.now().isoformat(),
        "usado": False
    }
    if familia not in _token_familias_s7:
        _token_familias_s7[familia] = []
    _token_familias_s7[familia].append(token)
    return token

def validar_sessao_s7(token: str, fingerprint: str) -> dict:
    from datetime import timedelta
    if token not in _sessoes_db_s7:
        return {"valida": False, "erro": "Sessao nao encontrada"}
    sessao = _sessoes_db_s7[token]
    if not sessao.get("ativo"):
        return {"valida": False, "erro": "Sessao inativa"}
    ultimo = _datetime_s7.fromisoformat(sessao["ultimo_acesso"])
    if _datetime_s7.now() > ultimo + timedelta(minutes=SESSION_CONFIG["inatividade_minutos"]):
        sessao["ativo"] = False
        return {"valida": False, "erro": "Sessao expirada por inatividade"}
    if sessao.get("fingerprint") != fingerprint:
        sessao["ativo"] = False
        return {"valida": False, "erro": "Dispositivo diferente detectado", "alerta": True}
    sessao["ultimo_acesso"] = _datetime_s7.now().isoformat()
    return {"valida": True, "usuario_id": sessao["usuario_id"]}

def revogar_sessao_s7(token: str):
    if token in _sessoes_db_s7:
        _sessoes_db_s7[token]["ativo"] = False

def revogar_todas_sessoes_s7(usuario_id: int):
    for token, sessao in _sessoes_db_s7.items():
        if sessao.get("usuario_id") == usuario_id:
            sessao["ativo"] = False

def detectar_token_theft_s7(refresh_token: str) -> bool:
    if refresh_token not in _refresh_tokens_s7:
        return False
    dados = _refresh_tokens_s7[refresh_token]
    if dados.get("usado"):
        familia = dados.get("familia")
        if familia and familia in _token_familias_s7:
            for t in _token_familias_s7[familia]:
                if t in _refresh_tokens_s7:
                    _refresh_tokens_s7[t]["usado"] = True
        return True
    return False

def limitar_sessoes_simultaneas_s7(usuario_id: int):
    sessoes_user = [
        (token, s) for token, s in _sessoes_db_s7.items()
        if s.get("usuario_id") == usuario_id and s.get("ativo")
    ]
    if len(sessoes_user) >= SESSION_CONFIG["max_sessoes_user"]:
        sessoes_user.sort(key=lambda x: x[1].get("ultimo_acesso",""))
        token_antigo = sessoes_user[0][0]
        _sessoes_db_s7[token_antigo]["ativo"] = False

def gerar_session_id_seguro() -> str:
    return _secrets_s7.token_urlsafe(64)

def cookie_seguro_config() -> dict:
    return {
        "httponly": True,
        "secure": True,
        "samesite": "strict",
        "max_age": SESSION_CONFIG["access_token_minutos"] * 60,
        "path": "/",
    }

def stats_sessoes_s7() -> dict:
    ativas = sum(1 for s in _sessoes_db_s7.values() if s.get("ativo"))
    total = len(_sessoes_db_s7)
    return {
        "sessoes_ativas": ativas,
        "sessoes_total": total,
        "refresh_tokens": len(_refresh_tokens_s7),
        "familias": len(_token_familias_s7),
        "config": SESSION_CONFIG
    }

@app.get("/api/sessoes-status")
async def sessoes_status_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    sessoes_user = [
        {"ultimo_acesso": s.get("ultimo_acesso"), "ativo": s.get("ativo")}
        for s in _sessoes_db_s7.values()
        if s.get("usuario_id") == usuario.get("id")
    ]
    return JSONResponse({
        "sessoes": sessoes_user,
        "total": len(sessoes_user),
        "config": SESSION_CONFIG,
        "seguranca": "S7/18 — 16 protecoes de sessao"
    })

@app.post("/api/revogar-todas-sessoes")
async def revogar_todas_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    revogar_todas_sessoes_s7(usuario.get("id"))
    return JSONResponse({"ok": True, "msg": "Todas as sessoes foram revogadas"})

# ═══ FIM S5+S6+S7/18 ════════════════════════════════════════════════




