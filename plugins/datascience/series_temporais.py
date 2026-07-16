"""
Plugin: Séries Temporais Emocionais
Categoria: datascience
Descrição: Análise de séries temporais de dados emocionais com decomposição e tendências
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta
import uuid
import statistics
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/series-temporais", tags=["datascience"])

series_db = {}
analises_db = {}


class SeriesTemporaisPlugin(PluginBase):
    name = "series_temporais"
    version = "1.0.0"
    description = "Análise de séries temporais emocionais"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "series_registradas": len(series_db),
            "analises_realizadas": len(analises_db)
        }


@router.post("/serie/criar")
async def criar_serie(user_id: str, nome: str = "serie_emocional", tipo: str = "bem_estar"):
    """Cria uma série temporal para um usuário"""
    serie_id = f"{user_id}_{tipo}"
    series_db[serie_id] = {
        "id": serie_id,
        "user_id": user_id,
        "nome": nome,
        "tipo": tipo,
        "pontos": [],
        "criado_em": datetime.utcnow().isoformat()
    }
    return {"serie_id": serie_id, "status": "série criada"}


@router.post("/serie/{serie_id}/ponto")
async def adicionar_ponto(
    serie_id: str,
    valor: float,
    timestamp: str = None,
    contexto: str = ""
):
    """Adiciona ponto à série temporal"""
    if serie_id not in series_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    ponto = {
        "valor": min(max(valor, 0.0), 10.0),
        "timestamp": timestamp or datetime.utcnow().isoformat(),
        "contexto": contexto
    }
    series_db[serie_id]["pontos"].append(ponto)

    # Manter máximo 365 dias
    if len(series_db[serie_id]["pontos"]) > 365:
        series_db[serie_id]["pontos"] = series_db[serie_id]["pontos"][-365:]

    return {"status": "ponto adicionado", "total_pontos": len(series_db[serie_id]["pontos"])}


@router.get("/serie/{serie_id}/analisar")
async def analisar_serie(serie_id: str, janela: int = 7):
    """Analisa a série temporal com decomposição STL simplificada"""
    if serie_id not in series_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    serie = series_db[serie_id]
    pontos = serie["pontos"]

    if len(pontos) < 3:
        return {"status": "poucos pontos", "minimo": 3, "atual": len(pontos)}

    valores = [p["valor"] for p in pontos]

    # Tendência (média móvel)
    tendencia = _media_movel(valores, janela)

    # Estatísticas básicas
    media = statistics.mean(valores)
    try:
        desvio = statistics.stdev(valores)
    except statistics.StatisticsError:
        desvio = 0.0

    # Detectar padrão
    padrao = _detectar_padrao(valores)

    # Previsão simples (próximos 7 dias)
    previsao = _prever_simples(valores, 7)

    analise_id = str(uuid.uuid4())[:8]
    analise = {
        "id": analise_id,
        "serie_id": serie_id,
        "total_pontos": len(valores),
        "media": round(media, 3),
        "desvio_padrao": round(desvio, 3),
        "minimo": round(min(valores), 3),
        "maximo": round(max(valores), 3),
        "ultimo_valor": round(valores[-1], 3),
        "tendencia": padrao["tendencia"],
        "direcao": padrao["direcao"],
        "volatilidade": padrao["volatilidade"],
        "tendencia_movel": [round(t, 3) for t in tendencia[-14:]],
        "previsao_7dias": [round(p, 3) for p in previsao],
        "analisado_em": datetime.utcnow().isoformat()
    }
    analises_db[analise_id] = analise

    return analise


@router.post("/serie/{serie_id}/anomalias")
async def detectar_anomalias(serie_id: str, threshold: float = 2.0):
    """Detecta anomalias na série temporal (z-score)"""
    if serie_id not in series_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    pontos = series_db[serie_id]["pontos"]
    if len(pontos) < 5:
        return {"anomalias": [], "status": "poucos pontos"}

    valores = [p["valor"] for p in pontos]
    media = statistics.mean(valores)
    try:
        desvio = statistics.stdev(valores)
    except statistics.StatisticsError:
        desvio = 1.0

    anomalias = []
    for i, (p, v) in enumerate(zip(pontos, valores)):
        if desvio > 0:
            z_score = abs(v - media) / desvio
            if z_score > threshold:
                anomalias.append({
                    "indice": i,
                    "valor": v,
                    "z_score": round(z_score, 3),
                    "timestamp": p["timestamp"],
                    "tipo": "alta" if v > media else "baixa"
                })

    return {
        "serie_id": serie_id,
        "total_pontos": len(pontos),
        "anomalias_encontradas": len(anomalias),
        "threshold_zscore": threshold,
        "anomalias": anomalias
    }


@router.get("/usuario/{user_id}/series")
async def listar_series_usuario(user_id: str):
    """Lista séries de um usuário"""
    series = [s for s in series_db.values() if s["user_id"] == user_id]
    return {
        "user_id": user_id,
        "total": len(series),
        "series": [{
            "id": s["id"],
            "nome": s["nome"],
            "tipo": s["tipo"],
            "pontos": len(s["pontos"]),
            "ultimo": s["pontos"][-1]["timestamp"] if s["pontos"] else None
        } for s in series]
    }


def _media_movel(valores: list, janela: int) -> list:
    resultado = []
    for i in range(len(valores)):
        inicio = max(0, i - janela + 1)
        janela_vals = valores[inicio:i + 1]
        resultado.append(sum(janela_vals) / len(janela_vals))
    return resultado


def _detectar_padrao(valores: list) -> dict:
    if len(valores) < 3:
        return {"tendencia": "indefinida", "direcao": "estavel", "volatilidade": "baixa"}

    # Tendência linear simples
    n = len(valores)
    x_medio = (n - 1) / 2
    y_medio = sum(valores) / n

    numerador = sum((i - x_medio) * (v - y_medio) for i, v in enumerate(valores))
    denominador = sum((i - x_medio) ** 2 for i in range(n))

    slope = numerador / denominador if denominador != 0 else 0

    if slope > 0.05:
        direcao = "crescente"
        tendencia = "melhora"
    elif slope < -0.05:
        direcao = "decrescente"
        tendencia = "piora"
    else:
        direcao = "estavel"
        tendencia = "estavel"

    # Volatilidade
    try:
        coef_var = statistics.stdev(valores) / statistics.mean(valores) if statistics.mean(valores) != 0 else 0
    except statistics.StatisticsError:
        coef_var = 0

    volatilidade = "alta" if coef_var > 0.3 else "media" if coef_var > 0.15 else "baixa"

    return {"tendencia": tendencia, "direcao": direcao, "volatilidade": volatilidade}


def _prever_simples(valores: list, steps: int) -> list:
    """Previsão com média móvel exponencial simples"""
    if not valores:
        return [5.0] * steps
    alpha = 0.3
    ema = valores[0]
    for v in valores[1:]:
        ema = alpha * v + (1 - alpha) * ema
    return [round(min(max(ema, 0), 10), 3)] * steps


plugin = SeriesTemporaisPlugin()
