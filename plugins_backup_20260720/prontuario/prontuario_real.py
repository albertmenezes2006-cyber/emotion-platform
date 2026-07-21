"""Plugin: Prontuário Real — Prontuário eletrônico com DB"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid
import json
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/prontuario-real", tags=["prontuario"])

_pacientes = SimpleDB("prontuario_pacientes")
_evolucoes = SimpleDB("prontuario_evolucoes")
_planos = SimpleDB("prontuario_planos")

class ProntuarioRealPlugin(PluginBase):
    name = "prontuario_real"; version = "2.0.0"
    description = "Prontuário eletrônico completo com persistência"; category = "prontuario"
    def setup(self, app): app.include_router(router); logger.info("[prontuario_real] OK")
    def health_check(self): return {"status": "healthy", "pacientes": _pacientes.count()}

@router.post("/paciente/cadastrar")
async def cadastrar_paciente(
    nome: str,
    data_nascimento: str,
    terapeuta_id: str,
    queixa_principal: str = "",
    historico_familiar: str = "",
    medicamentos: str = "",
    cid10: str = ""
):
    paciente_id = str(uuid.uuid4())[:8]
    paciente = {
        "id": paciente_id,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "terapeuta_id": terapeuta_id,
        "queixa_principal": queixa_principal,
        "historico_familiar": historico_familiar,
        "medicamentos": medicamentos,
        "cid10": cid10,
        "status": "ativo",
        "criado_em": datetime.utcnow().isoformat()
    }
    _pacientes.create(
        nome=nome, user_id=terapeuta_id,
        valor=paciente_id, dados=json.dumps(paciente)
    )
    return {"paciente_id": paciente_id, "status": "cadastrado", "paciente": paciente}

@router.post("/evolucao/registrar")
async def registrar_evolucao(
    paciente_id: str,
    terapeuta_id: str,
    subjetivo: str = "",
    objetivo: str = "",
    avaliacao: str = "",
    plano: str = "",
    tecnicas_usadas: str = "",
    humor_sessao: int = 5
):
    evolucao_id = str(uuid.uuid4())[:8]
    evolucao = {
        "id": evolucao_id,
        "paciente_id": paciente_id,
        "terapeuta_id": terapeuta_id,
        "formato": "SOAP",
        "subjetivo": subjetivo,
        "objetivo": objetivo,
        "avaliacao": avaliacao,
        "plano": plano,
        "tecnicas_usadas": [t.strip() for t in tecnicas_usadas.split(",") if t.strip()],
        "humor_sessao": humor_sessao,
        "data_sessao": datetime.utcnow().isoformat()
    }
    _evolucoes.create(
        nome=f"Evolução {paciente_id}",
        user_id=paciente_id,
        valor=str(humor_sessao),
        dados=json.dumps(evolucao)
    )
    return {"evolucao_id": evolucao_id, "status": "registrada", "evolucao": evolucao}

@router.get("/paciente/{paciente_id}/historico")
async def historico_paciente(paciente_id: str):
    evolucoes_raw = _evolucoes.list(user_id=paciente_id, limite=50)
    evolucoes = []
    for e in evolucoes_raw:
        try:
            evolucoes.append(json.loads(e.get("dados", "{}")))
        except Exception:
            pass
    humores = [e.get("humor_sessao", 5) for e in evolucoes]
    media_humor = sum(humores)/len(humores) if humores else 5.0
    return {
        "paciente_id": paciente_id,
        "total_evolucoes": len(evolucoes),
        "media_humor_sessoes": round(media_humor, 2),
        "tendencia": "melhora" if len(humores) >= 2 and humores[0] > humores[-1] else "estavel",
        "evolucoes": evolucoes
    }

@router.get("/terapeuta/{terapeuta_id}/pacientes")
async def listar_pacientes(terapeuta_id: str):
    pacientes_raw = _pacientes.list(user_id=terapeuta_id, limite=100)
    pacientes = []
    for p in pacientes_raw:
        try:
            pacientes.append(json.loads(p.get("dados", "{}")))
        except Exception:
            pass
    return {"total": len(pacientes), "pacientes": pacientes}

plugin = ProntuarioRealPlugin()
