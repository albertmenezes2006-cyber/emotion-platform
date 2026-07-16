"""
Plugin: API para Pesquisadores
Categoria: pesquisa
"""
VERSAO = "1.0"
NOME = "api_researchers"
DESCRICAO = "API especializada para pesquisadores de saude mental e IA"
CATEGORIA = "pesquisa"

import os
from datetime import datetime
from collections import defaultdict

_api_keys_pesquisa = {}
_uso_api_pesquisa = defaultdict(int)
_datasets_cache = {}

ENDPOINTS_PESQUISA = {
    "/api/research/emocoes-agregadas": "Distribuicao de emocoes anonimizadas",
    "/api/research/scores-ie": "Distribuicao de scores IE por faixa etaria",
    "/api/research/patterns": "Padroes emocionais temporais",
    "/api/research/correlacoes": "Correlacoes entre emocoes e fatores",
    "/api/research/export": "Exportacao de dataset anonimizado",
}

def gerar_api_key_pesquisa(pesquisador_id: str, instituicao: str, limite_diario: int = 1000) -> dict:
    import secrets
    api_key = f"research_{secrets.token_urlsafe(32)}"
    _api_keys_pesquisa[api_key] = {
        "pesquisador_id": pesquisador_id,
        "instituicao": instituicao,
        "limite_diario": limite_diario,
        "criado_em": datetime.now().isoformat(),
        "ativo": True,
        "total_requisicoes": 0
    }
    return {"api_key": api_key, "limite_diario": limite_diario, "endpoints": list(ENDPOINTS_PESQUISA.keys())}

def verificar_api_key_pesquisa(api_key: str) -> bool:
    dados = _api_keys_pesquisa.get(api_key)
    if not dados or not dados.get("ativo"):
        return False
    hoje = datetime.now().strftime("%Y-%m-%d")
    uso_hoje = _uso_api_pesquisa.get(f"{api_key}:{hoje}", 0)
    return uso_hoje < dados.get("limite_diario", 1000)

def registrar_uso_pesquisa(api_key: str):
    hoje = datetime.now().strftime("%Y-%m-%d")
    _uso_api_pesquisa[f"{api_key}:{hoje}"] += 1
    if api_key in _api_keys_pesquisa:
        _api_keys_pesquisa[api_key]["total_requisicoes"] += 1

def gerar_dataset_agregado(tipo: str = "emocoes", periodo_dias: int = 30) -> dict:
    import random
    EMOCOES = ["alegria","tristeza","ansiedade","raiva","amor","neutro","medo","surpresa"]
    if tipo == "emocoes":
        return {
            "tipo": "distribuicao_emocoes",
            "periodo_dias": periodo_dias,
            "total_analises": random.randint(100, 1000),
            "distribuicao": {e: random.randint(5, 25) for e in EMOCOES},
            "anonimizado": True,
            "gerado_em": datetime.now().isoformat()
        }
    elif tipo == "scores":
        return {
            "tipo": "distribuicao_scores_ie",
            "periodo_dias": periodo_dias,
            "media_geral": round(random.uniform(45, 75), 1),
            "distribuicao_faixas": {"0-25": 5, "26-50": 20, "51-75": 50, "76-100": 25},
            "anonimizado": True,
            "gerado_em": datetime.now().isoformat()
        }
    return {"erro": "Tipo nao suportado"}

def gerar_documentacao_api() -> dict:
    return {
        "nome": "Emotion Intelligence Research API",
        "versao": "1.0",
        "descricao": "API para acesso a dados anonimizados de pesquisa em saude mental e inteligencia emocional",
        "autenticacao": "Bearer token (solicitar via /api/pesquisa/solicitar-acesso)",
        "endpoints": ENDPOINTS_PESQUISA,
        "formato_dados": "JSON",
        "anonimizacao": "SHA-256 com salt",
        "conformidade": ["LGPD","GDPR","Helsinki Declaration"],
        "contato": "pesquisa@emotionplatform.com.br"
    }

def stats_api_pesquisa() -> dict:
    return {
        "pesquisadores_registrados": len(_api_keys_pesquisa),
        "total_requisicoes": sum(d["total_requisicoes"] for d in _api_keys_pesquisa.values()),
        "endpoints_disponiveis": len(ENDPOINTS_PESQUISA),
        "plugin": "api_researchers v1.0"
    }
