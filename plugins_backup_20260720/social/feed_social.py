"""
Plugin: Feed Social — Posts e Interacoes
Categoria: social
"""
VERSAO = "1.0"
NOME = "feed_social"
DESCRICAO = "Feed social de bem-estar — posts, likes, comentarios e seguir usuarios"
CATEGORIA = "social"

from datetime import datetime
from collections import defaultdict

_posts = {}
_likes = defaultdict(set)
_comentarios = defaultdict(list)
_seguidores = defaultdict(set)
_seguindo = defaultdict(set)
_feed_cache = defaultdict(list)

def criar_post(usuario_id: int, nome: str, conteudo: str, emocao: str = "", tipo: str = "texto") -> dict:
    import secrets
    post_id = secrets.token_hex(8)
    post = {
        "id": post_id,
        "usuario_id": usuario_id,
        "nome": nome,
        "conteudo": conteudo[:500],
        "emocao": emocao,
        "tipo": tipo,
        "likes": 0,
        "comentarios": 0,
        "publico": True,
        "criado_em": datetime.now().isoformat(),
        "ts": datetime.now().timestamp()
    }
    _posts[post_id] = post
    return post

def curtir_post(post_id: str, usuario_id: int) -> dict:
    if post_id not in _posts:
        return {"erro": "Post nao encontrado"}
    if usuario_id in _likes[post_id]:
        _likes[post_id].discard(usuario_id)
        _posts[post_id]["likes"] -= 1
        return {"acao": "descurtido", "total": _posts[post_id]["likes"]}
    _likes[post_id].add(usuario_id)
    _posts[post_id]["likes"] += 1
    return {"acao": "curtido", "total": _posts[post_id]["likes"]}

def comentar_post(post_id: str, usuario_id: int, nome: str, comentario: str) -> dict:
    if post_id not in _posts:
        return {"erro": "Post nao encontrado"}
    c = {"usuario_id": usuario_id, "nome": nome, "comentario": comentario[:200], "ts": datetime.now().isoformat()}
    _comentarios[post_id].append(c)
    _posts[post_id]["comentarios"] += 1
    return {"ok": True, "comentario": c}

def seguir_usuario(seguidor_id: int, seguido_id: int) -> dict:
    if seguido_id in _seguidores[seguidor_id]:
        _seguidores[seguidor_id].discard(seguido_id)
        _seguindo[seguido_id].discard(seguidor_id)
        return {"acao": "deixou_de_seguir"}
    _seguidores[seguidor_id].add(seguido_id)
    _seguindo[seguido_id].add(seguidor_id)
    return {"acao": "seguindo"}

def obter_feed(usuario_id: int, limite: int = 20) -> list:
    seguindo = _seguidores.get(usuario_id, set())
    todos_posts = list(_posts.values())
    posts_feed = [p for p in todos_posts if p["usuario_id"] in seguindo or p["usuario_id"] == usuario_id]
    posts_feed.sort(key=lambda x: x["ts"], reverse=True)
    return posts_feed[:limite]

def obter_posts_publicos(limite: int = 20, emocao: str = None) -> list:
    posts = [p for p in _posts.values() if p.get("publico")]
    if emocao:
        posts = [p for p in posts if p.get("emocao") == emocao]
    posts.sort(key=lambda x: x["ts"], reverse=True)
    return posts[:limite]

def stats_social() -> dict:
    return {
        "total_posts": len(_posts),
        "total_likes": sum(len(v) for v in _likes.values()),
        "total_comentarios": sum(len(v) for v in _comentarios.values()),
        "usuarios_com_seguidores": len(_seguidores),
        "plugin": "feed_social v1.0"
    }
