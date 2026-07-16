"""
Plugin: Modelo de Risco
Categoria: datascience
Descrição: Modelo preditivo de risco emocional e crise psicológica
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/modelo-risco", tags=["datascience"])

avaliacoes_db = {}
alertas_risco = []

# Pesos do modelo de risco (calibrado clinicamente)
PESOS_RISCO = {
    "ideacao_suicida": 0.40,
    "depressao_grave": 0.20,
    "ansiedade_grave": 0.15,
    "isolamento_social": 0.10,
    "abuso_substancias": 0.08,
    "historico_crise": 0.07
}

FATORES_PROTECAO = {
    "suporte_social": -0.15,
    "acesso_terapia": -0.12,
    "atividade_fisica": -0.08,
    "qualidade_sono": -0.08,
    "habilidades_coping": -0.10
}


class ModeloRiscoPlugin(PluginBase):
    name = "modelo_risco"
    version = "1.0.0"
    description = "Modelo preditivo de risco emocional"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "avaliacoes_realizadas": len(avaliacoes_db),
            "alertas_ativos": sum(1 for a in alertas_risco if a["nivel"] in ["alto", "critico"])
        }


@router.post("/avaliar")
async def avaliar_risco(
    user_id: str,
    ideacao_suicida: float = 0.0,
    depressao_grave: float = 0.0,
    ansiedade_grave: float = 0.0,
    isolamento_social: float = 0.0,
    abuso_substancias: float = 0.0,
    historico_crise: float = 0.0,
    suporte_social: float = 0.5,
    acesso_terapia: float = 0.5,
    atividade_fisica: float = 0.5,
    qualidade_sono: float = 0.7,
    habilidades_coping: float = 0.5
):
    """Avalia nível de risco emocional do usuário"""
    # Calcular score de risco (0 a 1)
    fatores = {
        "ideacao_suicida": min(max(ideacao_suicida, 0), 1),
        "depressao_grave": min(max(depressao_grave, 0), 1),
        "ansiedade_grave": min(max(ansiedade_grave, 0), 1),
        "isolamento_social": min(max(isolamento_social, 0), 1),
        "abuso_substancias": min(max(abuso_substancias, 0), 1),
        "historico_crise": min(max(historico_crise, 0), 1)
    }
    protecoes = {
        "suporte_social": min(max(suporte_social, 0), 1),
        "acesso_terapia": min(max(acesso_terapia, 0), 1),
        "atividade_fisica": min(max(atividade_fisica, 0), 1),
        "qualidade_sono": min(max(qualidade_sono, 0), 1),
        "habilidades_coping": min(max(habilidades_coping, 0), 1)
    }

    # Score de risco ponderado
    score_risco = sum(
        fatores[f] * peso for f, peso in PESOS_RISCO.items()
    )
    # Redução por fatores protetores
    reducao_protecao = sum(
        protecoes[f] * abs(peso) for f, peso in FATORES_PROTECAO.items()
    )
    score_final = max(0.0, min(1.0, score_risco - reducao_protecao))

    # Classificar nível
    if score_final >= 0.7:
        nivel = "critico"
        cor = "vermelho"
        acao = "Encaminhar imediatamente para profissional de saúde mental"
    elif score_final >= 0.5:
        nivel = "alto"
        cor = "laranja"
        acao = "Contato urgente com terapeuta ou psiquiatra"
    elif score_final >= 0.3:
        nivel = "moderado"
        cor = "amarelo"
        acao = "Acompanhamento terapêutico regular recomendado"
    elif score_final >= 0.1:
        nivel = "baixo"
        cor = "verde_claro"
        acao = "Monitoramento preventivo e psicoeducação"
    else:
        nivel = "minimo"
        cor = "verde"
        acao = "Manutenção das práticas de bem-estar"

    aval_id = str(uuid.uuid4())[:8]
    avaliacao = {
        "id": aval_id,
        "user_id": user_id,
        "score_risco": round(score_final, 4),
        "nivel": nivel,
        "cor": cor,
        "acao_recomendada": acao,
        "fatores_risco": {f: round(v, 3) for f, v in fatores.items()},
        "fatores_protecao": {f: round(v, 3) for f, v in protecoes.items()},
        "avaliado_em": datetime.utcnow().isoformat(),
        "recursos_emergencia": _recursos_emergencia(nivel)
    }
    avaliacoes_db[aval_id] = avaliacao

    # Gerar alerta se risco alto/critico
    if nivel in ["alto", "critico"]:
        alertas_risco.append({
            "user_id": user_id,
            "nivel": nivel,
            "score": score_final,
            "timestamp": datetime.utcnow().isoformat(),
            "avaliacao_id": aval_id
        })
        logger.warning(f"[RISCO {nivel.upper()}] Usuário {user_id} — score {score_final}")

    return avaliacao


@router.get("/historico/{user_id}")
async def historico_risco(user_id: str, ultimas: int = 10):
    """Histórico de avaliações de risco de um usuário"""
    avaliacoes = [a for a in avaliacoes_db.values() if a["user_id"] == user_id]
    avaliacoes.sort(key=lambda x: x["avaliado_em"], reverse=True)

    if not avaliacoes:
        return {"user_id": user_id, "historico": [], "tendencia": "sem_dados"}

    scores = [a["score_risco"] for a in avaliacoes[:ultimas]]
    tendencia = "piora" if len(scores) > 1 and scores[0] > scores[-1] else "melhora"

    return {
        "user_id": user_id,
        "total_avaliacoes": len(avaliacoes),
        "score_atual": avaliacoes[0]["score_risco"],
        "nivel_atual": avaliacoes[0]["nivel"],
        "tendencia": tendencia,
        "historico": avaliacoes[:ultimas]
    }


@router.get("/alertas/ativos")
async def alertas_ativos():
    """Lista alertas de risco ativos"""
    criticos = [a for a in alertas_risco if a["nivel"] == "critico"]
    altos = [a for a in alertas_risco if a["nivel"] == "alto"]

    return {
        "total_alertas": len(alertas_risco),
        "criticos": len(criticos),
        "altos": len(altos),
        "alertas": alertas_risco[-20:]
    }


@router.get("/recursos-emergencia")
async def recursos_emergencia_br():
    """Recursos de emergência em saúde mental no Brasil"""
    return {
        "cvv": {"nome": "CVV - Centro de Valorização da Vida", "telefone": "188", "chat": "cvv.org.br"},
        "samu": {"nome": "SAMU", "telefone": "192"},
        "ubs": {"nome": "UBS - Unidade Básica de Saúde", "como_encontrar": "saudebrasil.saude.gov.br"},
        "caps": {"nome": "CAPS - Centro de Atenção Psicossocial", "como_encontrar": "gov.br/saude"},
        "sos_mulher": {"nome": "SOS Mulher", "telefone": "180"},
        "disque_100": {"nome": "Disque Direitos Humanos", "telefone": "100"}
    }


def _recursos_emergencia(nivel: str) -> list:
    if nivel in ["critico", "alto"]:
        return ["CVV: 188", "SAMU: 192", "Procure um CAPS ou UBS"]
    elif nivel == "moderado":
        return ["Agende consulta com psicólogo ou psiquiatra", "CVV disponível 24h: 188"]
    else:
        return ["Mantenha acompanhamento preventivo"]


plugin = ModeloRiscoPlugin()
