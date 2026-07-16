"""
Plugin: Grupo de Terapia
Categoria: comunicacao
Descrição: Sistema de grupos terapêuticos online com moderação profissional
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/grupo-terapia", tags=["comunicacao"])

grupos_db = {}
membros_db = {}
atividades_grupo = {}

TEMAS_TERAPEUTICOS = [
    "ansiedade", "depressao", "luto", "autoestima", "relacionamentos",
    "estresse", "burnout", "fobias", "compulsoes", "trauma",
    "mindfulness", "resiliencia", "comunicacao_nao_violenta",
    "inteligencia_emocional", "autocuidado"
]


class GrupoTerapiaPlugin(PluginBase):
    name = "grupo_terapia"
    version = "1.0.0"
    description = "Grupos terapêuticos online com moderação"
    category = "comunicacao"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "grupos_ativos": sum(1 for g in grupos_db.values() if g["ativo"]),
            "temas_disponiveis": len(TEMAS_TERAPEUTICOS)
        }


@router.post("/criar")
async def criar_grupo(
    nome: str,
    tema: str,
    terapeuta_id: str,
    max_membros: int = 12,
    descricao: str = ""
):
    """Cria um grupo terapêutico"""
    if tema not in TEMAS_TERAPEUTICOS:
        raise HTTPException(
            status_code=400,
            detail=f"Tema inválido. Temas: {TEMAS_TERAPEUTICOS}"
        )

    grupo_id = str(uuid.uuid4())[:8]
    grupos_db[grupo_id] = {
        "id": grupo_id,
        "nome": nome,
        "tema": tema,
        "terapeuta_id": terapeuta_id,
        "descricao": descricao,
        "max_membros": max_membros,
        "ativo": True,
        "criado_em": datetime.utcnow().isoformat(),
        "regras": [
            "Respeito mútuo",
            "Confidencialidade total",
            "Sem julgamentos",
            "Escuta ativa",
            "Participação voluntária"
        ]
    }
    membros_db[grupo_id] = []
    atividades_grupo[grupo_id] = []

    return {
        "grupo_id": grupo_id,
        "nome": nome,
        "tema": tema,
        "status": "grupo criado com sucesso"
    }


@router.post("/{grupo_id}/entrar")
async def entrar_grupo(grupo_id: str, user_id: str, nome_exibicao: str = "Membro"):
    """Entra em um grupo terapêutico"""
    if grupo_id not in grupos_db:
        raise HTTPException(status_code=404, detail="Grupo não encontrado")

    grupo = grupos_db[grupo_id]
    membros = membros_db[grupo_id]

    if len(membros) >= grupo["max_membros"]:
        raise HTTPException(status_code=400, detail="Grupo lotado")

    # Verificar duplicata
    if any(m["user_id"] == user_id for m in membros):
        raise HTTPException(status_code=400, detail="Já é membro do grupo")

    membro = {
        "user_id": user_id,
        "nome_exibicao": nome_exibicao,
        "entrou_em": datetime.utcnow().isoformat(),
        "papel": "membro",
        "participacoes": 0
    }
    membros.append(membro)

    return {
        "status": "bem-vindo ao grupo",
        "grupo": grupo["nome"],
        "tema": grupo["tema"],
        "membros_atuais": len(membros),
        "regras": grupo["regras"]
    }


@router.post("/{grupo_id}/atividade")
async def registrar_atividade(
    grupo_id: str,
    tipo: str = "discussao",
    titulo: str = "",
    descricao: str = "",
    terapeuta_id: str = ""
):
    """Registra uma atividade no grupo"""
    if grupo_id not in grupos_db:
        raise HTTPException(status_code=404, detail="Grupo não encontrado")

    atividade = {
        "id": str(uuid.uuid4())[:8],
        "tipo": tipo,
        "titulo": titulo,
        "descricao": descricao,
        "terapeuta_id": terapeuta_id,
        "data": datetime.utcnow().isoformat(),
        "participantes": []
    }
    atividades_grupo[grupo_id].append(atividade)

    return {"status": "atividade registrada", "atividade": atividade}


@router.get("/{grupo_id}")
async def detalhes_grupo(grupo_id: str):
    """Detalhes de um grupo"""
    if grupo_id not in grupos_db:
        raise HTTPException(status_code=404, detail="Grupo não encontrado")

    return {
        "grupo": grupos_db[grupo_id],
        "membros": len(membros_db.get(grupo_id, [])),
        "atividades": len(atividades_grupo.get(grupo_id, []))
    }


@router.get("/listar/todos")
async def listar_grupos(tema: str = None):
    """Lista grupos disponíveis"""
    grupos = list(grupos_db.values())
    if tema:
        grupos = [g for g in grupos if g["tema"] == tema]
    grupos = [g for g in grupos if g["ativo"]]

    resultado = []
    for g in grupos:
        resultado.append({
            "id": g["id"],
            "nome": g["nome"],
            "tema": g["tema"],
            "membros": len(membros_db.get(g["id"], [])),
            "max_membros": g["max_membros"],
            "vagas": g["max_membros"] - len(membros_db.get(g["id"], []))
        })

    return {"total": len(resultado), "grupos": resultado}


@router.get("/temas/disponiveis")
async def listar_temas():
    """Lista temas terapêuticos disponíveis"""
    return {"temas": TEMAS_TERAPEUTICOS}


plugin = GrupoTerapiaPlugin()
