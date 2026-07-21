"""
Plugin: SHAP — Explicabilidade dos Modelos
Categoria: analytics
"""
VERSAO = "1.0"
NOME = "shap_explicabilidade"
DESCRICAO = "SHAP values para explicar decisoes dos modelos de emocao"
CATEGORIA = "analytics"

def explicar_predicao(modelo, features: dict, feature_names: list = None) -> dict:
    try:
        import shap
        import numpy as np
        X = np.array([list(features.values())])
        explainer = shap.TreeExplainer(modelo)
        shap_values = explainer.shap_values(X)
        nomes = feature_names or list(features.keys())
        if isinstance(shap_values, list):
            valores = shap_values[0][0]
        else:
            valores = shap_values[0]
        contribuicoes = sorted(
            [(nomes[i], round(float(valores[i]), 4)) for i in range(len(nomes))],
            key=lambda x: abs(x[1]), reverse=True
        )
        return {
            "contribuicoes": contribuicoes[:10],
            "feature_mais_importante": contribuicoes[0][0] if contribuicoes else "desconhecido",
            "explicacao": f"A feature '{contribuicoes[0][0]}' teve maior impacto na predicao" if contribuicoes else ""
        }
    except ImportError:
        return _explicar_simples(features)
    except Exception:
        return _explicar_simples(features)

def _explicar_simples(features: dict) -> dict:
    if not features:
        return {"contribuicoes": [], "feature_mais_importante": "desconhecido"}
    mais_importante = max(features.items(), key=lambda x: abs(x[1]) if isinstance(x[1], (int,float)) else 0)
    return {
        "contribuicoes": [(k, v) for k, v in features.items() if isinstance(v, (int,float))][:5],
        "feature_mais_importante": mais_importante[0],
        "metodo": "simples_fallback"
    }

def explicar_emocao_texto(texto: str, emocao_predita: str) -> dict:
    palavras_emocao = {
        "alegria": ["feliz","otimo","maravilhoso","alegre","contente","incrivel"],
        "tristeza": ["triste","choro","deprimido","sozinho","dor","saudade"],
        "raiva": ["raiva","irritado","furioso","odio","bravo","explodindo"],
        "ansiedade": ["ansioso","nervoso","preocupado","medo","panico","agitado"],
        "amor": ["amor","carinho","apaixonado","lindo","querido","amado"],
    }
    palavras_chave = palavras_emocao.get(emocao_predita, [])
    texto_lower = texto.lower()
    encontradas = [p for p in palavras_chave if p in texto_lower]
    return {
        "emocao_predita": emocao_predita,
        "palavras_chave_encontradas": encontradas,
        "explicacao": f"Detectei '{emocao_predita}' principalmente pelas palavras: {', '.join(encontradas)}" if encontradas else f"Detectei '{emocao_predita}' pelo contexto geral do texto",
        "confianca_explicacao": "alta" if len(encontradas) >= 2 else "media" if encontradas else "baixa"
    }

def stats_shap() -> dict:
    return {"disponivel": True, "metodo_fallback": True, "plugin": "shap_explicabilidade v1.0"}
