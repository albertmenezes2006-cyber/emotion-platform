"""
Plugin: Prophet Forecasting — Previsao de Humor
Categoria: analytics
"""
VERSAO = "1.0"
NOME = "prophet_forecast"
DESCRICAO = "Facebook Prophet para previsao de tendencias emocionais"
CATEGORIA = "analytics"

from datetime import datetime, timedelta
from collections import defaultdict

_historico_humor = defaultdict(list)

def registrar_humor_dia(usuario_id: int, data: str, emocao: str, score: float):
    _historico_humor[usuario_id].append({
        "ds": data, "y": score, "emocao": emocao
    })

def emocao_para_score(emocao: str) -> float:
    scores = {
        "alegria": 0.9, "amor": 0.85, "gratidao": 0.8, "otimismo": 0.75,
        "neutro": 0.5, "surpresa": 0.55, "curiosidade": 0.6,
        "ansiedade": 0.3, "tristeza": 0.25, "raiva": 0.2, "medo": 0.15,
        "depressao": 0.1, "desespero": 0.05,
    }
    return scores.get(emocao.lower(), 0.5)

def prever_humor_prophet(usuario_id: int, dias_futuro: int = 7) -> dict:
    dados = _historico_humor.get(usuario_id, [])
    if len(dados) < 7:
        return {"erro": f"Precisa de pelo menos 7 dias de dados. Tem {len(dados)}", "dados_necessarios": 7 - len(dados)}
    try:
        from prophet import Prophet
        import pandas as pd
        df = pd.DataFrame(dados)
        df["ds"] = pd.to_datetime(df["ds"])
        df["y"] = df["y"].astype(float)
        m = Prophet(yearly_seasonality=False, weekly_seasonality=True, daily_seasonality=False, changepoint_prior_scale=0.05)
        m.fit(df)
        future = m.make_future_dataframe(periods=dias_futuro)
        forecast = m.predict(future)
        previsoes = forecast[["ds","yhat","yhat_lower","yhat_upper"]].tail(dias_futuro).to_dict("records")
        return {"previsoes": previsoes, "tendencia": "melhora" if previsoes[-1]["yhat"] > previsoes[0]["yhat"] else "piora", "confianca": "alta"}
    except ImportError:
        return _prever_linear_simples(dados, dias_futuro)
    except Exception as e:
        return _prever_linear_simples(dados, dias_futuro)

def _prever_linear_simples(dados: list, dias: int) -> dict:
    scores = [d["y"] for d in dados[-14:]]
    if len(scores) < 2:
        return {"previsoes": [], "tendencia": "estavel"}
    media_recente = sum(scores[-7:])/len(scores[-7:])
    media_antiga = sum(scores[:7])/len(scores[:7])
    delta = (media_recente - media_antiga) / 7
    hoje = datetime.now()
    previsoes = []
    for i in range(1, dias+1):
        data = (hoje + timedelta(days=i)).strftime("%Y-%m-%d")
        score = round(min(1.0, max(0.0, media_recente + delta * i)), 3)
        previsoes.append({"ds": data, "yhat": score, "yhat_lower": max(0, score-0.1), "yhat_upper": min(1, score+0.1)})
    tendencia = "melhora" if delta > 0.01 else "piora" if delta < -0.01 else "estavel"
    return {"previsoes": previsoes, "tendencia": tendencia, "confianca": "baixa", "metodo": "linear_simples"}

def stats_prophet() -> dict:
    return {
        "usuarios_com_historico": len(_historico_humor),
        "total_registros": sum(len(v) for v in _historico_humor.values()),
        "plugin": "prophet_forecast v1.0"
    }
