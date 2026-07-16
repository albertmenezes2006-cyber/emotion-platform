"""
Plugin: Correlação Emocional
Categoria: datascience
Descrição: Análise de correlação entre variáveis emocionais e comportamentais
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import statistics
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/correlacao", tags=["datascience"])

dados_correlacao = {}
resultados_db = {}


class CorrelacaoEmocionalPlugin(PluginBase):
    name = "correlacao_emocional"
    version = "1.0.0"
    description = "Análise de correlação entre variáveis emocionais"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "datasets": len(dados_correlacao),
            "analises": len(resultados_db)
        }


@router.post("/dataset/adicionar")
async def adicionar_dados(user_id: str, dados: dict):
    """Adiciona dados para análise de correlação"""
    if user_id not in dados_correlacao:
        dados_correlacao[user_id] = []

    dados["timestamp"] = datetime.utcnow().isoformat()
    dados_correlacao[user_id].append(dados)

    if len(dados_correlacao[user_id]) > 365:
        dados_correlacao[user_id] = dados_correlacao[user_id][-365:]

    return {"status": "dados adicionados", "total": len(dados_correlacao[user_id])}


@router.post("/analisar/{user_id}")
async def analisar_correlacoes(user_id: str):
    """Analisa correlações entre variáveis do usuário"""
    if user_id not in dados_correlacao or len(dados_correlacao[user_id]) < 5:
        raise HTTPException(status_code=400, detail="Mínimo 5 pontos de dados necessários")

    dados = dados_correlacao[user_id]
    # Identificar variáveis numéricas
    variaveis = set()
    for d in dados:
        for k, v in d.items():
            if isinstance(v, (int, float)) and k != "timestamp":
                variaveis.add(k)

    variaveis = list(variaveis)
    correlacoes = []

    for i in range(len(variaveis)):
        for j in range(i + 1, len(variaveis)):
            v1, v2 = variaveis[i], variaveis[j]
            pares = [(d.get(v1), d.get(v2)) for d in dados if d.get(v1) is not None and d.get(v2) is not None]
            if len(pares) >= 3:
                x = [p[0] for p in pares]
                y = [p[1] for p in pares]
                r = _pearson(x, y)
                correlacoes.append({
                    "var1": v1,
                    "var2": v2,
                    "pearson_r": round(r, 4),
                    "forca": _classificar_correlacao(r),
                    "direcao": "positiva" if r > 0 else "negativa",
                    "n_amostras": len(pares)
                })

    correlacoes.sort(key=lambda x: abs(x["pearson_r"]), reverse=True)

    analise_id = str(uuid.uuid4())[:8]
    resultado = {
        "id": analise_id,
        "user_id": user_id,
        "total_pontos": len(dados),
        "variaveis_analisadas": variaveis,
        "correlacoes": correlacoes,
        "top_correlacoes": correlacoes[:5],
        "analisado_em": datetime.utcnow().isoformat()
    }
    resultados_db[analise_id] = resultado

    return resultado


@router.get("/matriz/{user_id}")
async def matriz_correlacao(user_id: str):
    """Gera matriz de correlação"""
    if user_id not in dados_correlacao or len(dados_correlacao[user_id]) < 5:
        raise HTTPException(status_code=400, detail="Mínimo 5 pontos necessários")

    dados = dados_correlacao[user_id]
    variaveis = set()
    for d in dados:
        for k, v in d.items():
            if isinstance(v, (int, float)) and k != "timestamp":
                variaveis.add(k)
    variaveis = sorted(list(variaveis))

    matriz = {}
    for v1 in variaveis:
        matriz[v1] = {}
        for v2 in variaveis:
            if v1 == v2:
                matriz[v1][v2] = 1.0
            else:
                pares = [(d.get(v1), d.get(v2)) for d in dados if d.get(v1) is not None and d.get(v2) is not None]
                if len(pares) >= 3:
                    x = [p[0] for p in pares]
                    y = [p[1] for p in pares]
                    matriz[v1][v2] = round(_pearson(x, y), 4)
                else:
                    matriz[v1][v2] = None

    return {"variaveis": variaveis, "matriz": matriz}


def _pearson(x: list, y: list) -> float:
    """Calcula correlação de Pearson"""
    n = len(x)
    if n < 2:
        return 0.0
    try:
        mx = statistics.mean(x)
        my = statistics.mean(y)
        num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
        den_x = math.sqrt(sum((xi - mx) ** 2 for xi in x))
        den_y = math.sqrt(sum((yi - my) ** 2 for yi in y))
        if den_x == 0 or den_y == 0:
            return 0.0
        return num / (den_x * den_y)
    except Exception:
        return 0.0


import math

def _classificar_correlacao(r: float) -> str:
    ar = abs(r)
    if ar >= 0.8:
        return "muito_forte"
    elif ar >= 0.6:
        return "forte"
    elif ar >= 0.4:
        return "moderada"
    elif ar >= 0.2:
        return "fraca"
    else:
        return "muito_fraca"


plugin = CorrelacaoEmocionalPlugin()
