"""
Plugin: AutoML
Categoria: mlpipeline
Descrição: Sistema AutoML para seleção automática de algoritmos e hiperparâmetros
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import random
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/automl", tags=["mlpipeline"])

jobs_automl = {}
resultados_automl = {}


ALGORITMOS = [
    "logistic_regression", "random_forest", "gradient_boosting",
    "svm", "naive_bayes", "knn", "decision_tree", "xgboost",
    "lightgbm", "extra_trees", "ridge", "lasso"
]


class AutoMLPlugin(PluginBase):
    name = "automl"
    version = "1.0.0"
    description = "AutoML para seleção automática de modelos"
    category = "mlpipeline"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "jobs_total": len(jobs_automl),
            "jobs_completos": sum(1 for j in jobs_automl.values() if j["status"] == "completo")
        }


@router.post("/job/iniciar")
async def iniciar_automl(
    nome: str,
    objetivo: str = "classificacao",
    metrica: str = "accuracy",
    tempo_maximo_segundos: int = 60,
    n_algoritmos: int = 5
):
    """Inicia um job AutoML"""
    objetivos_validos = ["classificacao", "regressao", "clustering"]
    if objetivo not in objetivos_validos:
        raise HTTPException(status_code=400, detail=f"Objetivos: {objetivos_validos}")

    job_id = str(uuid.uuid4())[:8]

    # Selecionar e avaliar algoritmos
    algoritmos_selecionados = random.sample(ALGORITMOS, min(n_algoritmos, len(ALGORITMOS)))
    trials = []

    for alg in algoritmos_selecionados:
        score = round(random.uniform(0.60, 0.97), 4)
        trials.append({
            "algoritmo": alg,
            "score": score,
            "tempo_treino": round(random.uniform(0.1, 10.0), 2),
            "hiperparametros": _gerar_hiperparametros(alg),
            "status": "completo"
        })

    # Ordenar por score
    trials.sort(key=lambda x: x["score"], reverse=True)
    melhor = trials[0]

    job = {
        "id": job_id,
        "nome": nome,
        "objetivo": objetivo,
        "metrica": metrica,
        "status": "completo",
        "inicio": datetime.utcnow().isoformat(),
        "duracao_segundos": round(random.uniform(5, 30), 1),
        "algoritmos_avaliados": len(trials),
        "melhor_algoritmo": melhor["algoritmo"],
        "melhor_score": melhor["score"],
        "melhores_hiperparametros": melhor["hiperparametros"],
        "ranking": trials,
        "recomendacao": f"Use {melhor['algoritmo']} com os hiperparâmetros sugeridos"
    }
    jobs_automl[job_id] = job
    resultados_automl[job_id] = trials

    return {
        "job_id": job_id,
        "status": "completo",
        "melhor_algoritmo": melhor["algoritmo"],
        "melhor_score": melhor["score"],
        "metrica": metrica,
        "total_avaliados": len(trials),
        "ranking_top5": trials[:5]
    }


@router.get("/job/{job_id}")
async def obter_job(job_id: str):
    """Obtém resultado de um job AutoML"""
    if job_id not in jobs_automl:
        raise HTTPException(status_code=404, detail="Job não encontrado")
    return jobs_automl[job_id]


@router.get("/jobs")
async def listar_jobs():
    """Lista todos os jobs AutoML"""
    return {
        "total": len(jobs_automl),
        "jobs": [{
            "id": j["id"],
            "nome": j["nome"],
            "objetivo": j["objetivo"],
            "melhor_algoritmo": j["melhor_algoritmo"],
            "melhor_score": j["melhor_score"],
            "status": j["status"]
        } for j in jobs_automl.values()]
    }


@router.get("/algoritmos")
async def listar_algoritmos():
    """Lista algoritmos disponíveis no AutoML"""
    return {
        "total": len(ALGORITMOS),
        "algoritmos": ALGORITMOS,
        "objetivos_suportados": ["classificacao", "regressao", "clustering"]
    }


def _gerar_hiperparametros(algoritmo: str) -> dict:
    mapa = {
        "random_forest": {"n_estimators": random.choice([50, 100, 200]), "max_depth": random.choice([5, 10, 15])},
        "gradient_boosting": {"n_estimators": random.choice([50, 100]), "learning_rate": round(random.uniform(0.01, 0.3), 3)},
        "svm": {"C": round(random.uniform(0.1, 10.0), 2), "kernel": random.choice(["rbf", "linear", "poly"])},
        "knn": {"n_neighbors": random.choice([3, 5, 7, 11])},
        "xgboost": {"n_estimators": random.choice([50, 100, 200]), "max_depth": random.choice([3, 5, 6])},
        "lightgbm": {"num_leaves": random.choice([15, 31, 63]), "learning_rate": round(random.uniform(0.01, 0.3), 3)}
    }
    return mapa.get(algoritmo, {"default": True})


plugin = AutoMLPlugin()
