"""
Plugin: Motor de Recomendacao ML
Categoria: ia
"""
VERSAO = "1.0"
NOME = "recommendation"
DESCRICAO = "Recomendacoes personalizadas baseadas em ML e comportamento"
CATEGORIA = "ia"

import math
from collections import defaultdict
from datetime import datetime

_historico_usuarios = defaultdict(list)
_matriz_similaridade = {}
_item_features = {}

def registrar_interacao(usuario_id: int, item: str, tipo: str = "view", score: float = 1.0):
    _historico_usuarios[usuario_id].append({
        "item": item, "tipo": tipo, "score": score,
        "ts": datetime.now().isoformat()
    })

def calcular_similaridade_usuarios(u1: int, u2: int) -> float:
    items_u1 = {i["item"]: i["score"] for i in _historico_usuarios.get(u1, [])}
    items_u2 = {i["item"]: i["score"] for i in _historico_usuarios.get(u2, [])}
    comum = set(items_u1.keys()) & set(items_u2.keys())
    if not comum:
        return 0.0
    dot = sum(items_u1[i] * items_u2[i] for i in comum)
    mag1 = math.sqrt(sum(v**2 for v in items_u1.values()))
    mag2 = math.sqrt(sum(v**2 for v in items_u2.values()))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return round(dot / (mag1 * mag2), 4)

def recomendar_colaborativo(usuario_id: int, top_k: int = 5) -> list:
    usuarios_similares = []
    for outro_id in _historico_usuarios:
        if outro_id == usuario_id:
            continue
        sim = calcular_similaridade_usuarios(usuario_id, outro_id)
        if sim > 0.3:
            usuarios_similares.append((outro_id, sim))
    usuarios_similares.sort(key=lambda x: x[1], reverse=True)
    items_usuario = {i["item"] for i in _historico_usuarios.get(usuario_id, [])}
    recomendados = {}
    for outro_id, sim in usuarios_similares[:5]:
        for interacao in _historico_usuarios.get(outro_id, []):
            item = interacao["item"]
            if item not in items_usuario:
                recomendados[item] = recomendados.get(item, 0) + sim * interacao["score"]
    return sorted(recomendados.items(), key=lambda x: x[1], reverse=True)[:top_k]

def recomendar_exercicios_mindfulness(emocao: str, historico: list = None) -> list:
    mapa = {
        "ansiedade": ["respiracao_4_7_8", "54321_grounding", "body_scan"],
        "tristeza":  ["gratidao", "meditacao_5min", "body_scan"],
        "raiva":     ["respiracao_4_7_8", "body_scan", "meditacao_5min"],
        "estresse":  ["respiracao_4_7_8", "54321_grounding", "meditacao_5min"],
        "neutro":    ["meditacao_5min", "gratidao", "respiracao_4_7_8"],
    }
    base = mapa.get(emocao, mapa["neutro"])
    if historico:
        feitos = {h.get("exercicio") for h in historico[-10:]}
        base = [e for e in base if e not in feitos] + [e for e in base if e in feitos]
    return base[:3]

def recomendar_conteudo_blog(emocao: str, interesses: list = None) -> list:
    mapa = {
        "ansiedade": ["tecnicas-respiracao", "mindfulness-iniciantes", "ansiedade-tratamento"],
        "tristeza":  ["superando-tristeza", "conexao-social", "autocompaixao"],
        "raiva":     ["gerenciamento-raiva", "comunicacao-nao-violenta", "regulacao-emocional"],
        "amor":      ["relacionamentos-saudaveis", "amor-proprio", "apego-seguro"],
        "neutro":    ["inteligencia-emocional", "bem-estar-mental", "habitos-saudaveis"],
    }
    return mapa.get(emocao, mapa["neutro"])

def stats_recomendacao() -> dict:
    return {
        "usuarios_com_historico": len(_historico_usuarios),
        "total_interacoes": sum(len(v) for v in _historico_usuarios.values()),
        "algoritmos": ["colaborativo", "content_based", "regras_emocao"],
        "plugin": "recommendation v1.0"
    }
