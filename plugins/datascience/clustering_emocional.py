"""
Plugin: Clustering Emocional
Categoria: datascience
Descrição: Algoritmos de clustering para segmentar perfis emocionais de usuários
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import math
import random
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/clustering", tags=["datascience"])

clusters_db = {}
perfis_db = {}
modelos_db = {}


class ClusteringEmocionalPlugin(PluginBase):
    name = "clustering_emocional"
    version = "1.0.0"
    description = "Clustering de perfis emocionais com K-Means e DBSCAN simulados"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "modelos_treinados": len(modelos_db),
            "perfis_analisados": len(perfis_db)
        }


@router.post("/perfil/adicionar")
async def adicionar_perfil(
    user_id: str,
    valencia: float = 0.5,
    ativacao: float = 0.5,
    ansiedade: float = 0.3,
    depressao: float = 0.2,
    estresse: float = 0.4,
    bem_estar: float = 0.6
):
    """Adiciona perfil emocional para clustering"""
    perfis_db[user_id] = {
        "user_id": user_id,
        "features": {
            "valencia": min(max(valencia, 0.0), 1.0),
            "ativacao": min(max(ativacao, 0.0), 1.0),
            "ansiedade": min(max(ansiedade, 0.0), 1.0),
            "depressao": min(max(depressao, 0.0), 1.0),
            "estresse": min(max(estresse, 0.0), 1.0),
            "bem_estar": min(max(bem_estar, 0.0), 1.0)
        },
        "cluster_id": None,
        "adicionado_em": datetime.utcnow().isoformat()
    }
    return {"status": "perfil adicionado", "user_id": user_id}


@router.post("/treinar/kmeans")
async def treinar_kmeans(k: int = 4, max_iteracoes: int = 100):
    """Executa K-Means clustering nos perfis"""
    if len(perfis_db) < k:
        raise HTTPException(
            status_code=400,
            detail=f"Mínimo {k} perfis necessários. Atual: {len(perfis_db)}"
        )

    perfis = list(perfis_db.values())
    features_keys = list(perfis[0]["features"].keys())

    # Inicializar centroides aleatoriamente
    centroides = []
    indices_iniciais = random.sample(range(len(perfis)), k)
    for idx in indices_iniciais:
        centroides.append(dict(perfis[idx]["features"]))

    assignments = {}
    for _ in range(max_iteracoes):
        # Atribuir cada ponto ao centroide mais próximo
        novos_assignments = {}
        for p in perfis:
            distancias = [_distancia_euclidiana(p["features"], c, features_keys) for c in centroides]
            cluster = distancias.index(min(distancias))
            novos_assignments[p["user_id"]] = cluster

        # Verificar convergência
        if novos_assignments == assignments:
            break
        assignments = novos_assignments

        # Atualizar centroides
        for c_idx in range(k):
            membros = [p for p in perfis if assignments.get(p["user_id"]) == c_idx]
            if membros:
                for feat in features_keys:
                    centroides[c_idx][feat] = sum(m["features"][feat] for m in membros) / len(membros)

    # Atualizar perfis com cluster
    for user_id, cluster_id in assignments.items():
        if user_id in perfis_db:
            perfis_db[user_id]["cluster_id"] = cluster_id

    # Salvar modelo
    modelo_id = str(uuid.uuid4())[:8]
    modelos_db[modelo_id] = {
        "id": modelo_id,
        "algoritmo": "kmeans",
        "k": k,
        "centroides": centroides,
        "assignments": assignments,
        "treinado_em": datetime.utcnow().isoformat(),
        "total_perfis": len(perfis)
    }

    # Gerar descrições dos clusters
    descricoes = _descrever_clusters(centroides, assignments, perfis_db)

    # Salvar clusters
    clusters_db[modelo_id] = descricoes

    return {
        "modelo_id": modelo_id,
        "k": k,
        "total_perfis": len(perfis),
        "clusters": descricoes
    }


@router.get("/clusters/{modelo_id}")
async def ver_clusters(modelo_id: str):
    """Visualiza clusters de um modelo"""
    if modelo_id not in modelos_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")

    modelo = modelos_db[modelo_id]
    clusters = clusters_db.get(modelo_id, [])

    return {
        "modelo_id": modelo_id,
        "algoritmo": modelo["algoritmo"],
        "k": modelo["k"],
        "total_perfis": modelo["total_perfis"],
        "clusters": clusters
    }


@router.post("/classificar")
async def classificar_novo_perfil(
    modelo_id: str,
    valencia: float = 0.5,
    ativacao: float = 0.5,
    ansiedade: float = 0.3,
    depressao: float = 0.2,
    estresse: float = 0.4,
    bem_estar: float = 0.6
):
    """Classifica um novo perfil em um cluster existente"""
    if modelo_id not in modelos_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")

    modelo = modelos_db[modelo_id]
    features = {
        "valencia": valencia, "ativacao": ativacao,
        "ansiedade": ansiedade, "depressao": depressao,
        "estresse": estresse, "bem_estar": bem_estar
    }
    features_keys = list(features.keys())

    distancias = [
        _distancia_euclidiana(features, c, features_keys)
        for c in modelo["centroides"]
    ]
    cluster_id = distancias.index(min(distancias))
    distancia_min = min(distancias)

    clusters = clusters_db.get(modelo_id, [])
    cluster_info = next((c for c in clusters if c["id"] == cluster_id), {})

    return {
        "cluster_id": cluster_id,
        "cluster_nome": cluster_info.get("nome", f"Cluster {cluster_id}"),
        "descricao": cluster_info.get("descricao", ""),
        "distancia_centroide": round(distancia_min, 4),
        "confianca": round(1 / (1 + distancia_min), 4)
    }


@router.get("/stats")
async def stats_clustering():
    """Estatísticas de clustering"""
    return {
        "total_perfis": len(perfis_db),
        "modelos_treinados": len(modelos_db),
        "perfis_classificados": sum(1 for p in perfis_db.values() if p["cluster_id"] is not None)
    }


def _distancia_euclidiana(p1: dict, p2: dict, keys: list) -> float:
    return math.sqrt(sum((p1.get(k, 0) - p2.get(k, 0)) ** 2 for k in keys))


def _descrever_clusters(centroides, assignments, perfis_db):
    descricoes = []
    nomes = [
        "Resiliente Positivo", "Ansioso em Busca", "Equilibrado Estável",
        "Alto Risco Emocional", "Em Crescimento", "Mindful Ativo"
    ]
    for i, centroide in enumerate(centroides):
        membros = [uid for uid, cid in assignments.items() if cid == i]
        bem_estar_medio = centroide.get("bem_estar", 0.5)
        descricao = (
            "Perfil com alto bem-estar e boa regulação emocional." if bem_estar_medio >= 0.6
            else "Perfil com desafios emocionais moderados." if bem_estar_medio >= 0.4
            else "Perfil necessita atenção e suporte especializado."
        )
        descricoes.append({
            "id": i,
            "nome": nomes[i % len(nomes)],
            "descricao": descricao,
            "total_membros": len(membros),
            "centroide": {k: round(v, 3) for k, v in centroide.items()},
            "bem_estar_medio": round(bem_estar_medio, 3)
        })
    return descricoes


plugin = ClusteringEmocionalPlugin()
