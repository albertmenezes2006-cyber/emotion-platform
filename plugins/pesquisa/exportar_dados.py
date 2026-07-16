"""
Plugin: Exportacao de Dados para Pesquisa
Categoria: pesquisa
"""
VERSAO = "1.0"
NOME = "exportar_dados"
DESCRICAO = "Exportacao anonimizada de dados para pesquisa academica"
CATEGORIA = "pesquisa"

import os
import json
import hashlib
from datetime import datetime
from collections import defaultdict

_solicitacoes_pesquisa = []
_datasets_exportados = defaultdict(list)

FORMATOS_EXPORTACAO = ["json", "csv", "xlsx", "spss"]

def anonimizar_usuario(usuario_id: int, salt: str = "") -> str:
    raw = f"{usuario_id}{salt}{os.getenv('HASH_SALT','emotion_salt')}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]

def anonimizar_dataset(dados: list, campos_remover: list = None) -> list:
    campos_sensiveis = campos_remover or ["nome","email","cpf","telefone","ip","token"]
    resultado = []
    for registro in dados:
        registro_anonimizado = {}
        for k, v in registro.items():
            if k in campos_sensiveis:
                registro_anonimizado[k] = "ANONIMIZADO"
            elif k == "usuario_id":
                registro_anonimizado[k] = anonimizar_usuario(v)
            else:
                registro_anonimizado[k] = v
        resultado.append(registro_anonimizado)
    return resultado

def exportar_json(dados: list, nome_arquivo: str = "export") -> dict:
    anonimizado = anonimizar_dataset(dados)
    conteudo = json.dumps(anonimizado, ensure_ascii=False, indent=2, default=str)
    return {
        "formato": "json",
        "nome": f"{nome_arquivo}_{datetime.now().strftime('%Y%m%d')}.json",
        "conteudo": conteudo,
        "registros": len(anonimizado),
        "anonimizado": True
    }

def exportar_csv(dados: list, nome_arquivo: str = "export") -> dict:
    if not dados:
        return {"erro": "Sem dados para exportar"}
    anonimizado = anonimizar_dataset(dados)
    cabecalho = ",".join(anonimizado[0].keys())
    linhas = [cabecalho]
    for registro in anonimizado:
        linha = ",".join(f'"{str(v)}"' for v in registro.values())
        linhas.append(linha)
    return {
        "formato": "csv",
        "nome": f"{nome_arquivo}_{datetime.now().strftime('%Y%m%d')}.csv",
        "conteudo": "
".join(linhas),
        "registros": len(anonimizado),
        "anonimizado": True
    }

def solicitar_acesso_pesquisa(pesquisador_nome: str, instituicao: str, objetivo: str, email: str) -> dict:
    import secrets
    protocolo = f"PESQ-{secrets.token_hex(4).upper()}"
    solicitacao = {
        "protocolo": protocolo,
        "pesquisador": pesquisador_nome,
        "instituicao": instituicao,
        "objetivo": objetivo[:500],
        "email": email,
        "status": "pendente_aprovacao",
        "solicitado_em": datetime.now().isoformat(),
        "aprovado_em": None,
        "dados_disponiveis": ["analises_anonimizadas","scores_ie","patterns_emocionais"]
    }
    _solicitacoes_pesquisa.append(solicitacao)
    return solicitacao

def gerar_citacao_apa(dados_export: dict) -> str:
    ano = datetime.now().year
    return (f"Menezes, A. ({ano}). Emotion Intelligence Platform [Dataset]. "
            f"Emotion Intelligence Platform. "
            f"https://emotion-platform-albert.onrender.com/api/pesquisa/dados. "
            f"Protocolo: {dados_export.get('protocolo', 'N/A')}")

def stats_pesquisa() -> dict:
    return {
        "solicitacoes_pendentes": len([s for s in _solicitacoes_pesquisa if s["status"] == "pendente_aprovacao"]),
        "total_solicitacoes": len(_solicitacoes_pesquisa),
        "formatos_suportados": FORMATOS_EXPORTACAO,
        "plugin": "exportar_dados v1.0"
    }
