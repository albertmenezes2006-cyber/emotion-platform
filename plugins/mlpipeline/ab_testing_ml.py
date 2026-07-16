"""
Plugin: A/B Testing para Modelos ML
Categoria: mlpipeline
Descrição: A/B Testing especializado para comparação de modelos de ML em produção
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import random
import math
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/ab-ml", tags=["mlpipeline"])

experimentos_ml = {}
predicoes_log = {}


class ABTestingMLPlugin(PluginBase):
    name = "ab_testing_ml"
    version = "1.0.0"
    description = "A/B Testing para modelos ML em produção"
    category = "mlpipeline"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "experimentos_ativos": sum(1 for e in experimentos_ml.values() if e["ativo"]),
            "predicoes_total": sum(len(p) for p in predicoes_log.values())
        }


@router.post("/experimento/criar")
async def criar_experimento_ml(
    nome: str,
    modelo_controle: str,
    modelo_tratamento: str,
    split: float = 0.5,
    metrica_primaria: str = "accuracy",
    descricao: str = ""
):
    """Cria experimento A/B para comparar modelos"""
    if not 0.1 <= split <= 0.9:
        raise HTTPException(status_code=400, detail="Split deve ser entre 0.1 e 0.9")

    exp_id = str(uuid.uuid4())[:8]
    experimentos_ml[exp_id] = {
        "id": exp_id,
        "nome": nome,
        "modelo_A": modelo_controle,
        "modelo_B": modelo_tratamento,
        "split_A": 1 - split,
        "split_B": split,
        "metrica_primaria": metrica_primaria,
        "descricao": descricao,
        "ativo": True,
        "criado_em": datetime.utcnow().isoformat(),
        "stats": {
            "A": {"predicoes": 0, "corretas": 0, "score_total": 0.0},
            "B": {"predicoes": 0, "corretas": 0, "score_total": 0.0}
        }
    }
    predicoes_log[exp_id] = []

    return {
        "experimento_id": exp_id,
        "modelo_A": modelo_controle,
        "modelo_B": modelo_tratamento,
        "split": f"{int((1-split)*100)}% / {int(split*100)}%",
        "status": "experimento criado"
    }


@router.post("/experimento/{exp_id}/predizer")
async def fazer_predicao(
    exp_id: str,
    user_id: str,
    score_real: float = None
):
    """Faz predição usando o experimento A/B"""
    if exp_id not in experimentos_ml:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    exp = experimentos_ml[exp_id]
    if not exp["ativo"]:
        raise HTTPException(status_code=400, detail="Experimento inativo")

    # Decisão A/B
    grupo = "B" if random.random() < exp["split_B"] else "A"
    modelo_usado = exp[f"modelo_{grupo}"]

    # Simular predição
    predicao_score = round(random.uniform(0.4, 0.99), 4)
    correto = predicao_score >= 0.5

    # Registrar
    registro = {
        "user_id": user_id,
        "grupo": grupo,
        "modelo": modelo_usado,
        "predicao": predicao_score,
        "score_real": score_real,
        "correto": correto,
        "timestamp": datetime.utcnow().isoformat()
    }
    predicoes_log[exp_id].append(registro)

    # Atualizar stats
    exp["stats"][grupo]["predicoes"] += 1
    exp["stats"][grupo]["score_total"] += predicao_score
    if correto:
        exp["stats"][grupo]["corretas"] += 1

    return {
        "grupo": grupo,
        "modelo": modelo_usado,
        "predicao": predicao_score,
        "experimento_id": exp_id
    }


@router.get("/experimento/{exp_id}/resultados")
async def resultados_experimento(exp_id: str):
    """Resultados e análise estatística do experimento"""
    if exp_id not in experimentos_ml:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    exp = experimentos_ml[exp_id]
    stats_A = exp["stats"]["A"]
    stats_B = exp["stats"]["B"]

    acc_A = stats_A["corretas"] / stats_A["predicoes"] if stats_A["predicoes"] > 0 else 0
    acc_B = stats_B["corretas"] / stats_B["predicoes"] if stats_B["predicoes"] > 0 else 0

    # Teste z simplificado para proporções
    p_value = _calcular_p_value(
        stats_A["corretas"], stats_A["predicoes"],
        stats_B["corretas"], stats_B["predicoes"]
    )

    significativo = p_value < 0.05
    vencedor = None
    if significativo:
        vencedor = "B" if acc_B > acc_A else "A"

    return {
        "experimento": exp["nome"],
        "total_predicoes": stats_A["predicoes"] + stats_B["predicoes"],
        "modelo_A": {
            "nome": exp["modelo_A"],
            "predicoes": stats_A["predicoes"],
            "accuracy": round(acc_A, 4),
            "score_medio": round(stats_A["score_total"] / max(stats_A["predicoes"], 1), 4)
        },
        "modelo_B": {
            "nome": exp["modelo_B"],
            "predicoes": stats_B["predicoes"],
            "accuracy": round(acc_B, 4),
            "score_medio": round(stats_B["score_total"] / max(stats_B["predicoes"], 1), 4)
        },
        "analise_estatistica": {
            "p_value": round(p_value, 4),
            "significativo": significativo,
            "nivel_confianca": "95%"
        },
        "vencedor": vencedor,
        "recomendacao": f"Adotar modelo {vencedor}" if vencedor else "Coletar mais dados"
    }


@router.post("/experimento/{exp_id}/encerrar")
async def encerrar_experimento(exp_id: str):
    """Encerra um experimento A/B"""
    if exp_id not in experimentos_ml:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")
    experimentos_ml[exp_id]["ativo"] = False
    experimentos_ml[exp_id]["encerrado_em"] = datetime.utcnow().isoformat()
    return {"status": "experimento encerrado", "exp_id": exp_id}


def _calcular_p_value(successes_A, n_A, successes_B, n_B) -> float:
    """Calcula p-value simplificado para teste de proporções"""
    if n_A == 0 or n_B == 0:
        return 1.0
    p_A = successes_A / n_A
    p_B = successes_B / n_B
    p_pool = (successes_A + successes_B) / (n_A + n_B)
    if p_pool == 0 or p_pool == 1:
        return 1.0
    se = math.sqrt(p_pool * (1 - p_pool) * (1/n_A + 1/n_B))
    if se == 0:
        return 1.0
    z = abs(p_A - p_B) / se
    # Aproximação do p-value pela distribuição normal
    p_value = 2 * (1 - _norm_cdf(z))
    return max(0.001, min(1.0, p_value))


def _norm_cdf(x: float) -> float:
    """CDF da normal padrão (aproximação)"""
    t = 1 / (1 + 0.2316419 * abs(x))
    poly = t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))))
    return 1 - (1 / math.sqrt(2 * math.pi)) * math.exp(-x**2 / 2) * poly if x >= 0 else 1 - _norm_cdf(-x)


plugin = ABTestingMLPlugin()
