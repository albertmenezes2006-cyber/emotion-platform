"""
Plugin: Data Science — Scikit-learn + Pandas + NumPy
Categoria: analytics
"""
VERSAO = "1.0"
NOME = "data_science"
DESCRICAO = "ML com scikit-learn, pandas e numpy para analise emocional"
CATEGORIA = "analytics"

from datetime import datetime
from collections import defaultdict

_modelos_treinados = {}
_datasets_usuarios = defaultdict(list)

def registrar_dado_treino(usuario_id: int, texto: str, emocao: str, intensidade: int):
    _datasets_usuarios[usuario_id].append({
        "texto": texto[:200], "emocao": emocao,
        "intensidade": intensidade, "ts": datetime.now().isoformat()
    })

def extrair_features_texto(texto: str) -> dict:
    palavras = texto.lower().split()
    return {
        "num_palavras": len(palavras),
        "num_chars": len(texto),
        "media_chars_palavra": len(texto)/max(len(palavras),1),
        "tem_exclamacao": int("!" in texto),
        "tem_interrogacao": int("?" in texto),
        "maiusculas_pct": sum(1 for c in texto if c.isupper())/max(len(texto),1),
        "palavras_negativas": sum(1 for p in ["nao","nunca","jamais","sem","mal"] if p in palavras),
        "palavras_positivas": sum(1 for p in ["sim","otimo","bom","feliz","amor"] if p in palavras),
        "num_reticencias": texto.count("..."),
        "num_emojis": sum(1 for c in texto if ord(c) > 127),
    }

def treinar_classificador_usuario(usuario_id: int) -> dict:
    dados = _datasets_usuarios.get(usuario_id, [])
    if len(dados) < 5:
        return {"erro": f"Precisa de pelo menos 5 exemplos. Tem {len(dados)}"}
    try:
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.feature_extraction.text import TfidfVectorizer
        import numpy as np
        textos = [d["texto"] for d in dados]
        labels = [d["emocao"] for d in dados]
        vec = TfidfVectorizer(max_features=100, ngram_range=(1,2))
        X = vec.fit_transform(textos)
        clf = MultinomialNB()
        clf.fit(X, labels)
        _modelos_treinados[usuario_id] = {"clf": clf, "vec": vec, "classes": list(clf.classes_), "treinado_em": datetime.now().isoformat(), "amostras": len(dados)}
        return {"sucesso": True, "amostras": len(dados), "classes": list(clf.classes_)}
    except ImportError:
        return {"erro": "scikit-learn nao instalado. pip install scikit-learn"}
    except Exception as e:
        return {"erro": str(e)}

def predizer_emocao_ml(usuario_id: int, texto: str) -> dict:
    modelo = _modelos_treinados.get(usuario_id)
    if not modelo:
        return {"emocao": "neutro", "confianca": 0.5, "personalizado": False}
    try:
        X = modelo["vec"].transform([texto])
        emocao = modelo["clf"].predict(X)[0]
        proba = modelo["clf"].predict_proba(X)[0]
        confianca = float(max(proba))
        return {"emocao": emocao, "confianca": round(confianca, 3), "personalizado": True, "modelo": "naive_bayes"}
    except Exception:
        return {"emocao": "neutro", "confianca": 0.5, "personalizado": False}

def analisar_tendencia_pandas(dados: list) -> dict:
    try:
        import pandas as pd
        import numpy as np
        df = pd.DataFrame(dados)
        if df.empty or "emocao" not in df.columns:
            return {"erro": "Dados insuficientes"}
        dist = df["emocao"].value_counts().to_dict()
        emocao_mais_freq = df["emocao"].mode()[0] if not df.empty else "neutro"
        if "intensidade" in df.columns and len(df) >= 2:
            intensidades = df["intensidade"].astype(float)
            tendencia = float(np.polyfit(range(len(intensidades)), intensidades, 1)[0])
        else:
            tendencia = 0.0
        return {
            "distribuicao": dist,
            "emocao_predominante": emocao_mais_freq,
            "tendencia_intensidade": round(tendencia, 3),
            "total_registros": len(df),
            "media_intensidade": round(float(df["intensidade"].mean()), 2) if "intensidade" in df.columns else 0,
        }
    except ImportError:
        return {"erro": "pandas nao instalado. pip install pandas"}
    except Exception as e:
        return {"erro": str(e)}

def gerar_relatorio_estatistico(dados: list) -> dict:
    try:
        import numpy as np
        intensidades = [d.get("intensidade", 3) for d in dados]
        if not intensidades:
            return {}
        return {
            "media": round(float(np.mean(intensidades)), 2),
            "desvio_padrao": round(float(np.std(intensidades)), 2),
            "minimo": int(np.min(intensidades)),
            "maximo": int(np.max(intensidades)),
            "mediana": round(float(np.median(intensidades)), 2),
            "percentil_25": round(float(np.percentile(intensidades, 25)), 2),
            "percentil_75": round(float(np.percentile(intensidades, 75)), 2),
            "total": len(intensidades),
        }
    except ImportError:
        n = len(intensidades)
        media = sum(intensidades)/n if n > 0 else 0
        return {"media": round(media,2), "total": n}
    except Exception as e:
        return {"erro": str(e)}

def stats_data_science() -> dict:
    return {
        "modelos_treinados": len(_modelos_treinados),
        "usuarios_com_dados": len(_datasets_usuarios),
        "total_amostras": sum(len(v) for v in _datasets_usuarios.values()),
        "bibliotecas": ["scikit-learn", "pandas", "numpy"],
        "plugin": "data_science v1.0"
    }
