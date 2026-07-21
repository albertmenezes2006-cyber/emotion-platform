"""
Plugin: Marketplace de Psicologos
Categoria: social
"""
VERSAO = "1.0"
NOME = "marketplace_psi"
DESCRICAO = "Marketplace para conectar usuarios com psicologos credenciados"
CATEGORIA = "social"

from datetime import datetime
from collections import defaultdict

_perfis_profissionais = {}
_avaliacoes = defaultdict(list)
_sessoes_marketplace = defaultdict(list)
_comissoes = defaultdict(float)

COMISSAO_PLATAFORMA_PCT = 15.0

def cadastrar_psicologo_marketplace(dados: dict) -> dict:
    import secrets
    prof_id = f"PSI-{secrets.token_hex(4).upper()}"
    _perfis_profissionais[prof_id] = {
        "id": prof_id,
        "nome": dados.get("nome",""),
        "crp": dados.get("crp",""),
        "especialidades": dados.get("especialidades",[]),
        "abordagens": dados.get("abordagens",[]),
        "valor_sessao_50min": dados.get("valor",150.0),
        "foto_url": dados.get("foto",""),
        "bio": dados.get("bio","")[:1000],
        "idiomas": dados.get("idiomas",["Português"]),
        "disponivel_online": True,
        "avaliacao_media": 0.0,
        "total_avaliacoes": 0,
        "total_sessoes": 0,
        "verificado": False,
        "cadastrado_em": datetime.now().isoformat()
    }
    return _perfis_profissionais[prof_id]

def buscar_psicologos(especialidade: str = None, max_valor: float = None, idioma: str = None) -> list:
    profs = list(_perfis_profissionais.values())
    if especialidade:
        profs = [p for p in profs if any(especialidade.lower() in e.lower() for e in p.get("especialidades",[]))]
    if max_valor:
        profs = [p for p in profs if p["valor_sessao_50min"] <= max_valor]
    if idioma:
        profs = [p for p in profs if idioma in p.get("idiomas",[])]
    profs.sort(key=lambda x: x["avaliacao_media"], reverse=True)
    return profs

def avaliar_psicologo(prof_id: str, usuario_id: int, nota: int, comentario: str = "") -> dict:
    if prof_id not in _perfis_profissionais:
        return {"erro": "Profissional nao encontrado"}
    nota = max(1, min(5, nota))
    avaliacao = {"usuario_id": usuario_id, "nota": nota, "comentario": comentario[:300], "ts": datetime.now().isoformat()}
    _avaliacoes[prof_id].append(avaliacao)
    avaliacoes = _avaliacoes[prof_id]
    media = sum(a["nota"] for a in avaliacoes) / len(avaliacoes)
    _perfis_profissionais[prof_id]["avaliacao_media"] = round(media, 2)
    _perfis_profissionais[prof_id]["total_avaliacoes"] = len(avaliacoes)
    return {"ok": True, "nova_media": round(media, 2), "total": len(avaliacoes)}

def calcular_split_pagamento(valor_total: float) -> dict:
    comissao = round(valor_total * COMISSAO_PLATAFORMA_PCT / 100, 2)
    valor_psicologo = round(valor_total - comissao, 2)
    return {
        "valor_total": valor_total,
        "plataforma": comissao,
        "psicologo": valor_psicologo,
        "comissao_pct": COMISSAO_PLATAFORMA_PCT
    }

def registrar_sessao_marketplace(usuario_id: int, prof_id: str, valor: float) -> dict:
    import secrets
    sessao_id = secrets.token_hex(8)
    split = calcular_split_pagamento(valor)
    sessao = {
        "id": sessao_id,
        "usuario_id": usuario_id,
        "profissional_id": prof_id,
        "valor": valor,
        "split": split,
        "status": "agendada",
        "ts": datetime.now().isoformat()
    }
    _sessoes_marketplace[usuario_id].append(sessao)
    _comissoes["plataforma"] = round(_comissoes.get("plataforma", 0) + split["plataforma"], 2)
    if prof_id in _perfis_profissionais:
        _perfis_profissionais[prof_id]["total_sessoes"] += 1
    return sessao

def stats_marketplace() -> dict:
    return {
        "profissionais_cadastrados": len(_perfis_profissionais),
        "total_sessoes": sum(len(v) for v in _sessoes_marketplace.values()),
        "receita_plataforma": _comissoes.get("plataforma", 0),
        "comissao_pct": COMISSAO_PLATAFORMA_PCT,
        "plugin": "marketplace_psi v1.0"
    }
