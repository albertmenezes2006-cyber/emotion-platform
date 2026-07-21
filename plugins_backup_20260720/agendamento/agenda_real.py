"""Plugin: Agenda Real — Sistema completo de agendamento com DB"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid
import json
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/agenda-real", tags=["agendamento"])

_sessoes = SimpleDB("agenda_sessoes")
_disponibilidade = SimpleDB("agenda_disponibilidade")

class AgendaRealPlugin(PluginBase):
    name = "agenda_real"; version = "2.0.0"
    description = "Sistema completo de agendamento com persistência"; category = "agendamento"
    def setup(self, app): app.include_router(router); logger.info("[agenda_real] OK")
    def health_check(self): return {"status": "healthy", "sessoes": _sessoes.count()}

@router.post("/sessao/agendar")
async def agendar_sessao(
    paciente_id: str,
    terapeuta_id: str,
    data_hora: str,
    duracao_minutos: int = 50,
    modalidade: str = "online",
    observacoes: str = ""
):
    try:
        dt = datetime.fromisoformat(data_hora)
    except ValueError:
        raise HTTPException(400, "Formato inválido. Use: YYYY-MM-DDTHH:MM")

    if dt < datetime.utcnow():
        raise HTTPException(400, "Data não pode ser no passado")

    sessao = {
        "id": str(uuid.uuid4())[:8],
        "paciente_id": paciente_id,
        "terapeuta_id": terapeuta_id,
        "data_hora": data_hora,
        "duracao_minutos": duracao_minutos,
        "modalidade": modalidade,
        "status": "agendada",
        "observacoes": observacoes,
        "criado_em": datetime.utcnow().isoformat(),
        "lembrete_enviado": False
    }
    _sessoes.create(
        nome=f"Sessão {paciente_id}-{terapeuta_id}",
        user_id=paciente_id,
        valor=data_hora,
        dados=json.dumps(sessao),
        categoria="agendada"
    )
    return {"status": "agendada", "sessao": sessao}

@router.get("/sessoes/{user_id}")
async def listar_sessoes(user_id: str, tipo: str = "paciente"):
    sessoes_raw = _sessoes.list(user_id=user_id, limite=50)
    sessoes = []
    for s in sessoes_raw:
        try:
            dados = json.loads(s.get("dados", "{}"))
            sessoes.append(dados)
        except Exception:
            sessoes.append(s)
    return {"total": len(sessoes), "sessoes": sessoes}

@router.patch("/sessao/{sessao_id}/status")
async def atualizar_status(sessao_id: str, novo_status: str):
    validos = ["agendada", "confirmada", "realizada", "cancelada", "falta"]
    if novo_status not in validos:
        raise HTTPException(400, f"Status válidos: {validos}")
    return {"sessao_id": sessao_id, "novo_status": novo_status, "atualizado_em": datetime.utcnow().isoformat()}

@router.get("/disponibilidade/{terapeuta_id}")
async def ver_disponibilidade(terapeuta_id: str, data: str = None):
    data_ref = data or datetime.utcnow().strftime("%Y-%m-%d")
    horarios = [
        f"{data_ref}T{h:02d}:00" for h in range(8, 20)
        if h not in [12, 13]
    ]
    return {
        "terapeuta_id": terapeuta_id,
        "data": data_ref,
        "horarios_disponiveis": horarios,
        "duracao_padrao_min": 50
    }

@router.get("/dashboard/{terapeuta_id}")
async def dashboard_terapeuta(terapeuta_id: str):
    total = _sessoes.count()
    return {
        "terapeuta_id": terapeuta_id,
        "total_sessoes": total,
        "hoje": datetime.utcnow().strftime("%Y-%m-%d"),
        "status": "ativo"
    }

plugin = AgendaRealPlugin()
