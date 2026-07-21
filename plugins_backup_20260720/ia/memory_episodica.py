"""
Plugin: Memória Episódica
Categoria: ia
Descrição: Sistema de memória episódica para IA com contexto emocional de longo prazo
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/memoria-episodica", tags=["ia"])

memorias_db = {}
indices_usuario = {}
resumos_db = {}


class MemoriaEpisodicaPlugin(PluginBase):
    name = "memory_episodica"
    version = "1.0.0"
    description = "Memória episódica com contexto emocional de longo prazo"
    category = "ia"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "total_memorias": len(memorias_db),
            "usuarios_com_memorias": len(indices_usuario)
        }


@router.post("/registrar")
async def registrar_memoria(
    user_id: str,
    tipo: str = "conversacao",
    conteudo: str = "",
    emocao: str = "neutro",
    importancia: float = 0.5,
    contexto: str = ""
):
    """Registra uma memória episódica"""
    tipos_validos = [
        "conversacao", "insight", "evento_emocional", "conquista",
        "desafio", "reflexao", "objetivo", "gatilho", "coping"
    ]
    if tipo not in tipos_validos:
        raise HTTPException(status_code=400, detail=f"Tipos válidos: {tipos_validos}")

    memoria_id = str(uuid.uuid4())[:8]
    memoria = {
        "id": memoria_id,
        "user_id": user_id,
        "tipo": tipo,
        "conteudo": conteudo[:1000],
        "emocao": emocao,
        "importancia": min(max(importancia, 0.0), 1.0),
        "contexto": contexto,
        "timestamp": datetime.utcnow().isoformat(),
        "acessos": 0,
        "ultimo_acesso": None,
        "consolidada": False,
        "tags": _extrair_tags(conteudo),
        "embedding_emocional": {
            "valencia": _emocao_para_valencia(emocao),
            "ativacao": _emocao_para_ativacao(emocao),
            "dominancia": 0.5
        }
    }
    memorias_db[memoria_id] = memoria

    # Indexar por usuário
    if user_id not in indices_usuario:
        indices_usuario[user_id] = []
    indices_usuario[user_id].append(memoria_id)

    # Manter apenas últimas 500 memórias por usuário
    if len(indices_usuario[user_id]) > 500:
        id_antigo = indices_usuario[user_id].pop(0)
        if id_antigo in memorias_db:
            del memorias_db[id_antigo]

    return {"memoria_id": memoria_id, "status": "memória registrada", "memoria": memoria}


@router.get("/buscar/{user_id}")
async def buscar_memorias(
    user_id: str,
    tipo: str = None,
    emocao: str = None,
    limite: int = 20,
    min_importancia: float = 0.0
):
    """Busca memórias de um usuário"""
    ids = indices_usuario.get(user_id, [])
    memorias = [memorias_db[mid] for mid in ids if mid in memorias_db]

    # Filtrar
    if tipo:
        memorias = [m for m in memorias if m["tipo"] == tipo]
    if emocao:
        memorias = [m for m in memorias if m["emocao"] == emocao]
    if min_importancia > 0:
        memorias = [m for m in memorias if m["importancia"] >= min_importancia]

    # Ordenar por importância e recência
    memorias.sort(key=lambda x: (x["importancia"], x["timestamp"]), reverse=True)

    # Atualizar acessos
    for m in memorias[:limite]:
        m["acessos"] += 1
        m["ultimo_acesso"] = datetime.utcnow().isoformat()

    return {
        "user_id": user_id,
        "total": len(memorias),
        "memorias": memorias[:limite]
    }


@router.get("/contexto/{user_id}")
async def obter_contexto_emocional(user_id: str, ultimas: int = 10):
    """Obtém contexto emocional do usuário baseado em memórias recentes"""
    ids = indices_usuario.get(user_id, [])
    memorias = [memorias_db[mid] for mid in ids if mid in memorias_db]
    memorias.sort(key=lambda x: x["timestamp"], reverse=True)
    recentes = memorias[:ultimas]

    if not recentes:
        return {"user_id": user_id, "contexto": "sem memórias registradas"}

    # Analisar padrão emocional
    emocoes = [m["emocao"] for m in recentes]
    emocoes_count = {}
    for e in emocoes:
        emocoes_count[e] = emocoes_count.get(e, 0) + 1

    valencias = [m["embedding_emocional"]["valencia"] for m in recentes]
    media_valencia = sum(valencias) / len(valencias)

    emocao_predominante = max(emocoes_count, key=emocoes_count.get) if emocoes_count else "neutro"

    return {
        "user_id": user_id,
        "emocao_predominante": emocao_predominante,
        "distribuicao_emocoes": emocoes_count,
        "valencia_media": round(media_valencia, 3),
        "estado_geral": "positivo" if media_valencia > 0.6 else "negativo" if media_valencia < 0.4 else "neutro",
        "memorias_analisadas": len(recentes),
        "insights": _gerar_insights(recentes, emocao_predominante)
    }


@router.post("/consolidar/{user_id}")
async def consolidar_memorias(user_id: str):
    """Consolida memórias (simula processo de consolidação de memória)"""
    ids = indices_usuario.get(user_id, [])
    memorias = [memorias_db[mid] for mid in ids if mid in memorias_db]

    if len(memorias) < 5:
        return {"status": "poucas memórias para consolidar"}

    # Agrupar por tipo
    por_tipo = {}
    for m in memorias:
        tipo = m["tipo"]
        if tipo not in por_tipo:
            por_tipo[tipo] = []
        por_tipo[tipo].append(m)

    resumo_id = str(uuid.uuid4())[:8]
    resumo = {
        "id": resumo_id,
        "user_id": user_id,
        "total_memorias": len(memorias),
        "por_tipo": {t: len(ms) for t, ms in por_tipo.items()},
        "periodo": {
            "inicio": memorias[-1]["timestamp"] if memorias else None,
            "fim": memorias[0]["timestamp"] if memorias else None
        },
        "consolidado_em": datetime.utcnow().isoformat()
    }
    resumos_db[resumo_id] = resumo

    # Marcar como consolidadas
    for m in memorias:
        m["consolidada"] = True

    return {"status": "memórias consolidadas", "resumo": resumo}


@router.get("/stats/{user_id}")
async def stats_memorias(user_id: str):
    """Estatísticas de memórias do usuário"""
    ids = indices_usuario.get(user_id, [])
    memorias = [memorias_db[mid] for mid in ids if mid in memorias_db]

    if not memorias:
        return {"user_id": user_id, "total": 0, "status": "sem memórias"}

    return {
        "user_id": user_id,
        "total": len(memorias),
        "por_tipo": _contar_por_campo(memorias, "tipo"),
        "por_emocao": _contar_por_campo(memorias, "emocao"),
        "importancia_media": sum(m["importancia"] for m in memorias) / len(memorias),
        "consolidadas": sum(1 for m in memorias if m["consolidada"]),
        "mais_acessadas": sorted(memorias, key=lambda x: x["acessos"], reverse=True)[:5]
    }


def _extrair_tags(texto: str) -> list:
    palavras_chave = [
        "ansiedade", "depressao", "alegria", "medo", "raiva", "tristeza",
        "esperanca", "gratidao", "amor", "paz", "estresse", "calma",
        "conquista", "desafio", "superacao", "crescimento"
    ]
    return [p for p in palavras_chave if p in texto.lower()]


def _emocao_para_valencia(emocao: str) -> float:
    mapa = {
        "feliz": 0.9, "alegre": 0.85, "grato": 0.8, "calmo": 0.7,
        "esperancoso": 0.75, "neutro": 0.5, "ansioso": 0.3,
        "triste": 0.2, "raiva": 0.15, "medo": 0.1, "desespero": 0.05
    }
    return mapa.get(emocao.lower(), 0.5)


def _emocao_para_ativacao(emocao: str) -> float:
    mapa = {
        "feliz": 0.7, "alegre": 0.8, "raiva": 0.9, "medo": 0.85,
        "ansioso": 0.8, "triste": 0.2, "calmo": 0.3, "neutro": 0.5
    }
    return mapa.get(emocao.lower(), 0.5)


def _contar_por_campo(memorias: list, campo: str) -> dict:
    contagem = {}
    for m in memorias:
        valor = m.get(campo, "desconhecido")
        contagem[valor] = contagem.get(valor, 0) + 1
    return contagem


def _gerar_insights(memorias: list, emocao_predominante: str) -> list:
    insights = []
    if emocao_predominante in ["triste", "ansioso", "medo"]:
        insights.append("Padrão de emoções negativas detectado. Considere técnicas de regulação emocional.")
    if emocao_predominante in ["feliz", "grato", "calmo"]:
        insights.append("Momento emocional positivo. Continue cultivando essas emoções.")

    tipos = [m["tipo"] for m in memorias]
    if tipos.count("gatilho") > 2:
        insights.append("Múltiplos gatilhos identificados. Trabalhar estratégias de coping pode ajudar.")
    if tipos.count("conquista") > 0:
        insights.append("Conquistas recentes registradas. Reconheça seu progresso!")

    return insights if insights else ["Continue registrando suas experiências para insights mais precisos."]


plugin = MemoriaEpisodicaPlugin()
