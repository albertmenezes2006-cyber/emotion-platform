"""
Plugin: XGBoost para Classificacao Emocional
Categoria: analytics
"""
VERSAO = "1.0"
NOME = "xgboost_emocao"
DESCRICAO = "XGBoost para classificacao avancada de emocoes"
CATEGORIA = "analytics"

from collections import defaultdict

_modelos_xgb = {}
_dados_treino = defaultdict(list)

EMOCOES_CLASSES = ["alegria","tristeza","raiva","medo","ansiedade","amor","neutro","surpresa"]

def adicionar_amostra(usuario_id: int, features: dict, emocao: str):
    _dados_treino[usuario_id].append({"features": features, "emocao": emocao})

def treinar_xgboost(usuario_id: int) -> dict:
    dados = _dados_treino.get(usuario_id, [])
    if len(dados) < 10:
        return {"erro": f"Precisa de 10+ amostras. Tem {len(dados)}"}
    try:
        import xgboost as xgb
        import numpy as np
        from sklearn.preprocessing import LabelEncoder
        X = np.array([[list(d["features"].values())] for d in dados]).squeeze()
        le = LabelEncoder()
        y = le.fit_transform([d["emocao"] for d in dados])
        modelo = xgb.XGBClassifier(n_estimators=100, max_depth=4, learning_rate=0.1, use_label_encoder=False, eval_metric="mlogloss")
        modelo.fit(X, y)
        _modelos_xgb[usuario_id] = {"modelo": modelo, "encoder": le, "treinado_em": str(__import__("datetime").datetime.now())}
        return {"sucesso": True, "amostras": len(dados), "classes": list(le.classes_)}
    except ImportError:
        return {"erro": "xgboost nao instalado. pip install xgboost"}
    except Exception as e:
        return {"erro": str(e)}

def predizer_xgb(usuario_id: int, features: dict) -> dict:
    modelo_dados = _modelos_xgb.get(usuario_id)
    if not modelo_dados:
        return {"emocao": "neutro", "confianca": 0.5, "modelo": "fallback"}
    try:
        import numpy as np
        X = np.array([list(features.values())])
        proba = modelo_dados["modelo"].predict_proba(X)[0]
        classe_idx = int(proba.argmax())
        emocao = modelo_dados["encoder"].inverse_transform([classe_idx])[0]
        return {"emocao": emocao, "confianca": round(float(proba[classe_idx]), 3), "modelo": "xgboost"}
    except Exception as e:
        return {"emocao": "neutro", "confianca": 0.5, "erro": str(e)}

def stats_xgboost() -> dict:
    return {"modelos": len(_modelos_xgb), "usuarios_com_dados": len(_dados_treino), "plugin": "xgboost v1.0"}
