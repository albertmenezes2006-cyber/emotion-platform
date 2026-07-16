"""
Plugin: Sala de Grupo Terapeutico
Categoria: comunicacao
"""
VERSAO = "1.0"
NOME = "grupo_terapia"
DESCRICAO = "Salas de grupo terapeutico com facilitador e participantes"
CATEGORIA = "comunicacao"

from datetime import datetime
from collections import defaultdict

_grupos = {}
_sessoes_grupo = defaultdict(list)
_participantes_grupo = defaultdict(list)

TIPOS_GRUPO = [
    "ansiedade", "depressao", "luto", "relacionamentos",
    "autoestima", "estresse", "fobia", "trauma", "geral"
]

def criar_grupo(nome: str, tipo: str, facilitador_id: int, max_participantes: int = 8, descricao: str = "") -> dict:
    import secrets
    grupo_id = secrets.token_hex(6)
    _grupos[grupo_id] = {
        "id": grupo_id,
        "nome": nome,
        "tipo": tipo,
        "facilitador_id": facilitador_id,
        "max_participantes": max_participantes,
        "descricao": descricao[:300],
        "participantes": [facilitador_id],
        "ativo": True,
        "sessoes": 0,
        "criado_em": datetime.now().isoformat()
    }
    return _grupos[grupo_id]

def entrar_grupo(grupo_id: str, usuario_id: int, nome: str) -> dict:
    if grupo_id not in _grupos:
        return {"erro": "Grupo nao encontrado"}
    grupo = _grupos[grupo_id]
    if not grupo["ativo"]:
        return {"erro": "Grupo inativo"}
    if len(grupo["participantes"]) >= grupo["max_participantes"]:
        return {"erro": f"Grupo cheio (max {grupo['max_participantes']})"}
    if usuario_id not in grupo["participantes"]:
        grupo["participantes"].append(usuario_id)
        _participantes_grupo[grupo_id].append({"usuario_id": usuario_id, "nome": nome, "entrou_em": datetime.now().isoformat()})
    return {"ok": True, "grupo": grupo["nome"], "participantes": len(grupo["participantes"])}

def iniciar_sessao_grupo(grupo_id: str, facilitador_id: int, tema: str) -> dict:
    if grupo_id not in _grupos:
        return {"erro": "Grupo nao encontrado"}
    grupo = _grupos[grupo_id]
    if grupo["facilitador_id"] != facilitador_id:
        return {"erro": "Apenas o facilitador pode iniciar sessoes"}
    import secrets
    sessao_id = secrets.token_hex(6)
    sessao = {
        "id": sessao_id,
        "grupo_id": grupo_id,
        "tema": tema,
        "facilitador_id": facilitador_id,
        "inicio": datetime.now().isoformat(),
        "fim": None,
        "mensagens": [],
        "ativa": True
    }
    _sessoes_grupo[grupo_id].append(sessao)
    grupo["sessoes"] += 1
    return sessao

def encerrar_sessao_grupo(grupo_id: str, sessao_id: str, resumo: str = "") -> dict:
    sessoes = _sessoes_grupo.get(grupo_id, [])
    for sessao in sessoes:
        if sessao["id"] == sessao_id:
            sessao["ativa"] = False
            sessao["fim"] = datetime.now().isoformat()
            sessao["resumo"] = resumo[:500]
            return {"ok": True, "duracao_mensagens": len(sessao["mensagens"])}
    return {"erro": "Sessao nao encontrada"}

def listar_grupos(tipo: str = None, apenas_ativos: bool = True) -> list:
    grupos = list(_grupos.values())
    if tipo:
        grupos = [g for g in grupos if g["tipo"] == tipo]
    if apenas_ativos:
        grupos = [g for g in grupos if g["ativo"]]
    return grupos

def stats_grupo_terapia() -> dict:
    return {
        "grupos_ativos": sum(1 for g in _grupos.values() if g["ativo"]),
        "total_grupos": len(_grupos),
        "tipos_disponiveis": TIPOS_GRUPO,
        "plugin": "grupo_terapia v1.0"
    }
