"""
Plugin: Telemedicina e Agenda de Profissionais
Categoria: saude
"""
VERSAO = "1.0"
NOME = "telemedicina"
DESCRICAO = "Video chamada, agenda e gestao de profissionais de saude mental"
CATEGORIA = "saude"

from datetime import datetime, timedelta
from collections import defaultdict

_profissionais = {}
_agendamentos = defaultdict(list)
_salas_video = {}

ESPECIALIDADES = [
    "Psicologia Clinica", "Neuropsicologia", "Psiquiatria",
    "Terapia Cognitivo-Comportamental", "Psicanálise",
    "Gestalt-terapia", "EMDR", "Mindfulness-Based Therapy",
]

def cadastrar_profissional(dados: dict) -> dict:
    import secrets
    prof_id = secrets.token_hex(8)
    _profissionais[prof_id] = {
        "id": prof_id,
        "nome": dados.get("nome", ""),
        "crp": dados.get("crp", ""),
        "especialidade": dados.get("especialidade", "Psicologia Clinica"),
        "valor_sessao": dados.get("valor_sessao", 150.0),
        "disponibilidade": dados.get("disponibilidade", {}),
        "bio": dados.get("bio", "")[:500],
        "avaliacao_media": 0.0,
        "total_sessoes": 0,
        "ativo": True,
        "cadastrado_em": datetime.now().isoformat()
    }
    return _profissionais[prof_id]

def listar_profissionais(especialidade: str = None, max_valor: float = None) -> list:
    profs = list(_profissionais.values())
    if especialidade:
        profs = [p for p in profs if especialidade.lower() in p["especialidade"].lower()]
    if max_valor:
        profs = [p for p in profs if p["valor_sessao"] <= max_valor]
    return [p for p in profs if p.get("ativo")]

def criar_agendamento(usuario_id: int, prof_id: str, data_hora: str, tipo: str = "video") -> dict:
    import secrets
    if prof_id not in _profissionais:
        return {"erro": "Profissional nao encontrado"}
    agendamento_id = secrets.token_hex(8)
    agendamento = {
        "id": agendamento_id,
        "usuario_id": usuario_id,
        "profissional_id": prof_id,
        "profissional_nome": _profissionais[prof_id]["nome"],
        "data_hora": data_hora,
        "tipo": tipo,
        "status": "confirmado",
        "valor": _profissionais[prof_id]["valor_sessao"],
        "link_sala": f"/sala/{agendamento_id}" if tipo == "video" else None,
        "criado_em": datetime.now().isoformat()
    }
    _agendamentos[usuario_id].append(agendamento)
    return agendamento

def gerar_sala_video(agendamento_id: str) -> dict:
    sala_token = __import__("secrets").token_urlsafe(32)
    _salas_video[agendamento_id] = {
        "token": sala_token,
        "criado_em": datetime.now().isoformat(),
        "expira_em": (datetime.now() + timedelta(hours=2)).isoformat(),
        "participantes": []
    }
    return {
        "sala_id": agendamento_id,
        "link_paciente": f"/sala/{agendamento_id}?token={sala_token}&role=patient",
        "link_profissional": f"/sala/{agendamento_id}?token={sala_token}&role=therapist",
        "expira_em": _salas_video[agendamento_id]["expira_em"],
        "tecnologia": "WebRTC via Jitsi Meet ou Daily.co"
    }

def obter_agendamentos_usuario(usuario_id: int) -> list:
    return _agendamentos.get(usuario_id, [])

def stats_telemedicina() -> dict:
    return {
        "profissionais_cadastrados": len(_profissionais),
        "total_agendamentos": sum(len(v) for v in _agendamentos.values()),
        "salas_ativas": len(_salas_video),
        "especialidades": ESPECIALIDADES,
        "plugin": "telemedicina v1.0"
    }
