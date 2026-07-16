"""
Plugin: Reacoes e Thread de Mensagens
Categoria: comunicacao
"""
VERSAO = "1.0"
NOME = "reacoes_mensagens"
DESCRICAO = "Sistema de reacoes emoji e threads em mensagens"
CATEGORIA = "comunicacao"

from datetime import datetime
from collections import defaultdict

_reacoes = defaultdict(lambda: defaultdict(set))
_threads = {}
_mensagens_thread = defaultdict(list)

EMOJIS_EMOCAO = {
    "alegria": ["😊","😄","🌟","❤️","🎉"],
    "apoio": ["🤗","💙","🫂","💪","🙏"],
    "tristeza": ["😢","💔","🥺","😞","☁️"],
    "reflexao": ["🤔","💭","🌱","✨","🔍"],
    "gratidao": ["🙏","💝","⭐","🌸","💫"],
    "neutro": ["👍","✅","💬","📝","🔔"],
}

REACOES_PERMITIDAS = ["❤️","😊","🤗","💙","👍","🙏","💪","🌟","😢","🤔"]

def reagir_mensagem(mensagem_id: str, usuario_id: int, emoji: str) -> dict:
    if emoji not in REACOES_PERMITIDAS:
        return {"erro": f"Reacao nao permitida. Use: {REACOES_PERMITIDAS}"}
    if usuario_id in _reacoes[mensagem_id][emoji]:
        _reacoes[mensagem_id][emoji].discard(usuario_id)
        return {"acao": "removida", "emoji": emoji, "total": len(_reacoes[mensagem_id][emoji])}
    _reacoes[mensagem_id][emoji].add(usuario_id)
    return {"acao": "adicionada", "emoji": emoji, "total": len(_reacoes[mensagem_id][emoji])}

def obter_reacoes_mensagem(mensagem_id: str) -> dict:
    resultado = {}
    for emoji, usuarios in _reacoes[mensagem_id].items():
        if usuarios:
            resultado[emoji] = len(usuarios)
    return resultado

def criar_thread(mensagem_id: str, titulo: str = "") -> dict:
    import secrets
    thread_id = secrets.token_hex(6)
    _threads[thread_id] = {
        "id": thread_id,
        "mensagem_id": mensagem_id,
        "titulo": titulo[:100],
        "criado_em": datetime.now().isoformat(),
        "respostas": 0
    }
    return _threads[thread_id]

def responder_thread(thread_id: str, usuario_id: int, nome: str, conteudo: str) -> dict:
    if thread_id not in _threads:
        return {"erro": "Thread nao encontrada"}
    resposta = {
        "usuario_id": usuario_id,
        "nome": nome,
        "conteudo": conteudo[:500],
        "ts": datetime.now().isoformat(),
        "reacoes": {}
    }
    _mensagens_thread[thread_id].append(resposta)
    _threads[thread_id]["respostas"] += 1
    return {"ok": True, "resposta": resposta}

def obter_thread(thread_id: str) -> dict:
    if thread_id not in _threads:
        return {"erro": "Thread nao encontrada"}
    return {
        "thread": _threads[thread_id],
        "mensagens": _mensagens_thread.get(thread_id, [])
    }

def emojis_por_emocao(emocao: str) -> list:
    return EMOJIS_EMOCAO.get(emocao, EMOJIS_EMOCAO["neutro"])

def stats_reacoes() -> dict:
    return {
        "mensagens_com_reacoes": len(_reacoes),
        "threads_ativas": len(_threads),
        "reacoes_permitidas": REACOES_PERMITIDAS,
        "plugin": "reacoes_mensagens v1.0"
    }
