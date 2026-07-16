"""
Plugin: Feature Engineering
Categoria: datascience
Descrição: Engenharia de features emocionais para modelos de ML
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import statistics
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/feature-eng", tags=["datascience"])

datasets_db = {}
features_db = {}


class FeatureEngineeringPlugin(PluginBase):
    name = "feature_engineering"
    version = "1.0.0"
    description = "Engenharia de features para ML emocional"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "datasets": len(datasets_db),
            "feature_sets": len(features_db)
        }


@router.post("/dataset/criar")
async def criar_dataset(nome: str, descricao: str = ""):
    """Cria um dataset para feature engineering"""
    ds_id = str(uuid.uuid4())[:8]
    datasets_db[ds_id] = {
        "id": ds_id,
        "nome": nome,
        "descricao": descricao,
        "amostras": [],
        "criado_em": datetime.utcnow().isoformat()
    }
    return {"dataset_id": ds_id, "status": "dataset criado"}


@router.post("/dataset/{ds_id}/amostra")
async def adicionar_amostra(
    ds_id: str,
    user_id: str,
    emocao: str = "neutro",
    intensidade: float = 0.5,
    hora_dia: int = 12,
    dia_semana: int = 1,
    qualidade_sono: float = 7.0,
    atividade_fisica: float = 0.5,
    interacoes_sociais: int = 3,
    label: int = 1
):
    """Adiciona amostra ao dataset"""
    if ds_id not in datasets_db:
        raise HTTPException(status_code=404, detail="Dataset não encontrado")

    amostra = {
        "user_id": user_id,
        "features_raw": {
            "emocao": emocao,
            "intensidade": intensidade,
            "hora_dia": hora_dia,
            "dia_semana": dia_semana,
            "qualidade_sono": qualidade_sono,
            "atividade_fisica": atividade_fisica,
            "interacoes_sociais": interacoes_sociais
        },
        "label": label,
        "timestamp": datetime.utcnow().isoformat()
    }
    datasets_db[ds_id]["amostras"].append(amostra)

    return {"status": "amostra adicionada", "total": len(datasets_db[ds_id]["amostras"])}


@router.post("/dataset/{ds_id}/extrair-features")
async def extrair_features(ds_id: str):
    """Extrai e transforma features do dataset"""
    if ds_id not in datasets_db:
        raise HTTPException(status_code=404, detail="Dataset não encontrado")

    amostras = datasets_db[ds_id]["amostras"]
    if len(amostras) < 2:
        raise HTTPException(status_code=400, detail="Mínimo 2 amostras necessárias")

    features_extraidas = []
    for a in amostras:
        raw = a["features_raw"]

        # Encoding de emoção
        emocao_score = {
            "feliz": 1.0, "calmo": 0.8, "neutro": 0.5,
            "ansioso": 0.3, "triste": 0.2, "raiva": 0.1
        }.get(raw["emocao"], 0.5)

        # Features derivadas
        features = {
            # Features originais normalizadas
            "emocao_score": emocao_score,
            "intensidade": raw["intensidade"],
            "qualidade_sono_norm": raw["qualidade_sono"] / 10.0,
            "atividade_fisica": raw["atividade_fisica"],
            "interacoes_norm": min(raw["interacoes_sociais"] / 10.0, 1.0),

            # Features derivadas (engenharia)
            "periodo_dia": _codificar_periodo(raw["hora_dia"]),
            "eh_fim_semana": 1.0 if raw["dia_semana"] >= 6 else 0.0,
            "score_saude_geral": (raw["qualidade_sono"] / 10 + raw["atividade_fisica"]) / 2,
            "risco_emocional": (1 - emocao_score) * raw["intensidade"],
            "bem_estar_estimado": (
                emocao_score * 0.4 +
                (raw["qualidade_sono"] / 10.0) * 0.3 +
                raw["atividade_fisica"] * 0.2 +
                min(raw["interacoes_sociais"] / 10.0, 1.0) * 0.1
            ),

            # Label
            "label": a["label"]
        }
        features_extraidas.append(features)

    feat_id = str(uuid.uuid4())[:8]
    features_db[feat_id] = {
        "id": feat_id,
        "dataset_id": ds_id,
        "total_amostras": len(features_extraidas),
        "features": features_extraidas,
        "nomes_features": [k for k in features_extraidas[0].keys() if k != "label"],
        "extraido_em": datetime.utcnow().isoformat()
    }

    # Estatísticas das features
    nomes = features_db[feat_id]["nomes_features"]
    stats = {}
    for nome in nomes:
        valores = [f[nome] for f in features_extraidas]
        stats[nome] = {
            "media": round(statistics.mean(valores), 4),
            "min": round(min(valores), 4),
            "max": round(max(valores), 4)
        }

    return {
        "feature_set_id": feat_id,
        "total_amostras": len(features_extraidas),
        "total_features": len(nomes),
        "features_disponiveis": nomes,
        "estatisticas": stats
    }


@router.get("/feature-set/{feat_id}")
async def obter_feature_set(feat_id: str):
    """Obtém um feature set"""
    if feat_id not in features_db:
        raise HTTPException(status_code=404, detail="Feature set não encontrado")
    return features_db[feat_id]


@router.get("/stats")
async def stats_feature_eng():
    """Estatísticas gerais"""
    return {
        "datasets": len(datasets_db),
        "feature_sets": len(features_db),
        "total_amostras": sum(len(d["amostras"]) for d in datasets_db.values())
    }


def _codificar_periodo(hora: int) -> float:
    """Codifica hora do dia em período (0=madrugada, 1=manhã, 2=tarde, 3=noite)"""
    if 0 <= hora < 6:
        return 0.0
    elif 6 <= hora < 12:
        return 0.33
    elif 12 <= hora < 18:
        return 0.67
    else:
        return 1.0


plugin = FeatureEngineeringPlugin()
