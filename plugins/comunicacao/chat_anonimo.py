"""
Plugin: Chat Anonimo Seguro
Categoria: comunicacao
"""
VERSAO = "1.0"
NOME = "chat_anonimo"
DESCRICAO = "Chat anonimo seguro para usuarios que precisam de apoio sem identificacao"
CATEGORIA = "comunicacao"

import hashlib
import os
from datetime import datetime
from collections import defaultdict

_salas_anonimas = {}
_mensagens_anonimas = defaultdict(list)
_usuarios_anonimos = {}

def gerar_identidade_anonima(seed: str = "") -> dict:
    import secrets
    token = secrets.token_hex(16)
    apelidos = ["Borboleta","Estrela","Lua","Sol","Nuvem","Rio","Vento","Flor","Monte","Mar"]
    cores = ["Azul","Verde","Dourado","Prateado","Roxo","Rosa","Laranja","Turquesa"]
    import random
    r = random.Random(token)
    apelido = r.choice(apelidos) + r.choice(cores)
    avatar = f"https://api.dicebear.com/7.x/bottts/svg?seed={token[:8]}"
    identidade = {
        "token": token,
        "apelido": apelido,
        "avatar": avatar,
        "criado_em": datetime.now().isoformat(),
        "ativo": True
    }
    _usuarios_anonimos[token] = identidade
    return identidade

def criar_sala_anonima(topico: str = "apoio_emocional", max_usuarios: int = 2) -> dict:
    import secrets
    sala_id = secrets.token_hex(8)
    _salas_anonimas[sala_id] = {
        "id": sala_id,
        "topico": topico,
        "max_usuarios": max_usuarios,
        "usuarios": [],
        "criado_em": datetime.now().isoformat(),
        "ativa": True,
        "mensagens_count": 0
    }
    return _salas_anonimas[sala_id]

def entrar_sala_anonima(sala_id: str, token_usuario: str) -> dict:
    if sala_id not in _salas_anonimas:
        return {"erro": "Sala nao encontrada"}
    sala = _salas_anonimas[sala_id]
    if not sala["ativa"]:
        return {"erro": "Sala encerrada"}
    if len(sala["usuarios"]) >= sala["max_usuarios"]:
        return {"erro": "Sala cheia"}
    if token_usuario not in sala["usuarios"]:
        sala["usuarios"].append(token_usuario)
    identidade = _usuarios_anonimos.get(token_usuario, {})
    return {"ok": True, "sala": sala_id, "apelido": identidade.get("apelido","Anonimo"), "usuarios_na_sala": len(sala["usuarios"])}

def enviar_mensagem_anonima(sala_id: str, token_usuario: str, mensagem: str) -> dict:
    if sala_id not in _salas_anonimas:
        return {"erro": "Sala nao encontrada"}
    if token_usuario not in _salas_anonimas[sala_id]["usuarios"]:
        return {"erro": "Nao esta na sala"}
    identidade = _usuarios_anonimos.get(token_usuario, {"apelido": "Anonimo"})
    msg = {
        "apelido": identidade["apelido"],
        "mensagem": mensagem[:500],
        "ts": datetime.now().isoformat(),
        "hash_autor": hashlib.sha256(token_usuario.encode()).hexdigest()[:8]
    }
    _mensagens_anonimas[sala_id].append(msg)
    _salas_anonimas[sala_id]["mensagens_count"] += 1
    return {"ok": True, "mensagem": msg}

def obter_mensagens_sala(sala_id: str, limite: int = 50) -> list:
    return _mensagens_anonimas.get(sala_id, [])[-limite:]

def encerrar_sala(sala_id: str):
    if sala_id in _salas_anonimas:
        _salas_anonimas[sala_id]["ativa"] = False

def stats_chat_anonimo() -> dict:
    return {
        "salas_ativas": sum(1 for s in _salas_anonimas.values() if s["ativa"]),
        "total_salas": len(_salas_anonimas),
        "usuarios_anonimos": len(_usuarios_anonimos),
        "plugin": "chat_anonimo v1.0"
    }
