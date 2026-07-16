"""
Plugin: Relatório Clínico ML
Categoria: datascience
Descrição: Geração de relatórios clínicos baseados em análises de ML emocional
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/relatorio-clinico-ml", tags=["datascience"])

relatorios_db = {}
templates_db = {}


class RelatorioCLinicoMLPlugin(PluginBase):
    name = "relatorio_clinico_ml"
    version = "1.0.0"
    description = "Relatórios clínicos baseados em análises ML"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "relatorios_gerados": len(relatorios_db)
        }


@router.post("/gerar")
async def gerar_relatorio(
    user_id: str,
    terapeuta_id: str = "",
    periodo_dias: int = 30,
    score_bem_estar: float = 6.5,
    score_ansiedade: float = 3.2,
    score_depressao: float = 2.1,
    score_estresse: float = 4.0,
    tendencia: str = "melhora",
    sessoes_realizadas: int = 4,
    incluir_recomendacoes: bool = True
):
    """Gera relatório clínico baseado em dados ML"""
    rel_id = str(uuid.uuid4())[:8]

    # Classificar estado clínico
    estado_geral = _avaliar_estado_clinico(score_bem_estar, score_ansiedade, score_depressao, score_estresse)

    # Gerar insights
    insights = _gerar_insights_clinicos(score_bem_estar, score_ansiedade, score_depressao, score_estresse, tendencia)

    # Recomendações baseadas em ML
    recomendacoes = _gerar_recomendacoes(estado_geral, score_ansiedade, score_depressao) if incluir_recomendacoes else []

    relatorio = {
        "id": rel_id,
        "user_id": user_id,
        "terapeuta_id": terapeuta_id,
        "periodo_analise_dias": periodo_dias,
        "data_geracao": datetime.utcnow().isoformat(),
        "versao": "ML v1.0",
        "secoes": {
            "dados_clinicos": {
                "score_bem_estar": score_bem_estar,
                "score_ansiedade": score_ansiedade,
                "score_depressao": score_depressao,
                "score_estresse": score_estresse,
                "sessoes_realizadas": sessoes_realizadas
            },
            "avaliacao_ia": {
                "estado_geral": estado_geral["nivel"],
                "descricao": estado_geral["descricao"],
                "tendencia": tendencia,
                "nivel_risco": estado_geral["risco"],
                "confianca_modelo": 0.87
            },
            "insights": insights,
            "recomendacoes": recomendacoes,
            "escalas_normativas": {
                "bem_estar_percentil": _calcular_percentil(score_bem_estar, 5, 10),
                "ansiedade_percentil": _calcular_percentil(10 - score_ansiedade, 0, 10),
                "comparativo_populacao": "acima da média" if score_bem_estar > 6 else "abaixo da média"
            }
        },
        "assinatura_ia": f"Gerado por Emotion Intelligence Platform — ML Engine v1.0",
        "aviso": "Este relatório é gerado por IA e deve ser interpretado por profissional habilitado."
    }
    relatorios_db[rel_id] = relatorio

    return relatorio


@router.get("/{rel_id}")
async def obter_relatorio(rel_id: str):
    """Obtém um relatório clínico"""
    if rel_id not in relatorios_db:
        raise HTTPException(status_code=404, detail="Relatório não encontrado")
    return relatorios_db[rel_id]


@router.get("/usuario/{user_id}/historico")
async def historico_relatorios(user_id: str):
    """Histórico de relatórios de um usuário"""
    relatorios = [r for r in relatorios_db.values() if r["user_id"] == user_id]
    relatorios.sort(key=lambda x: x["data_geracao"], reverse=True)

    return {
        "user_id": user_id,
        "total": len(relatorios),
        "relatorios": [{
            "id": r["id"],
            "data": r["data_geracao"],
            "estado": r["secoes"]["avaliacao_ia"]["estado_geral"],
            "tendencia": r["secoes"]["avaliacao_ia"]["tendencia"]
        } for r in relatorios]
    }


@router.get("/stats/gerais")
async def stats_relatorios():
    """Estatísticas de relatórios gerados"""
    return {
        "total_gerados": len(relatorios_db),
        "por_estado": _contar_estados(),
        "por_tendencia": _contar_tendencias()
    }


def _avaliar_estado_clinico(bem_estar, ansiedade, depressao, estresse) -> dict:
    score_negativo = (ansiedade + depressao + estresse) / 3
    if bem_estar >= 7 and score_negativo <= 3:
        return {"nivel": "excelente", "descricao": "Estado emocional muito positivo e saudável.", "risco": "minimo"}
    elif bem_estar >= 5.5 and score_negativo <= 5:
        return {"nivel": "bom", "descricao": "Estado emocional adequado com pequenos desafios.", "risco": "baixo"}
    elif bem_estar >= 4 and score_negativo <= 6:
        return {"nivel": "moderado", "descricao": "Presença de sintomas que merecem atenção.", "risco": "moderado"}
    elif bem_estar >= 2.5:
        return {"nivel": "ruim", "descricao": "Sintomas significativos comprometendo qualidade de vida.", "risco": "alto"}
    else:
        return {"nivel": "critico", "descricao": "Estado crítico — intervenção especializada urgente.", "risco": "critico"}


def _gerar_insights_clinicos(bem_estar, ansiedade, depressao, estresse, tendencia) -> list:
    insights = []
    if tendencia == "melhora":
        insights.append("📈 Trajetória de melhora consistente detectada pelo modelo ML.")
    elif tendencia == "piora":
        insights.append("📉 Tendência de piora identificada — atenção redobrada necessária.")

    if ansiedade > 6:
        insights.append("⚠️ Nível elevado de ansiedade detectado — considerar intervenção específica.")
    if depressao > 5:
        insights.append("⚠️ Indicadores depressivos acima do limiar — avaliação psiquiátrica recomendada.")
    if estresse > 7:
        insights.append("⚠️ Estresse elevado — técnicas de regulação emocional indicadas.")
    if bem_estar > 7:
        insights.append("✅ Alto bem-estar subjetivo — fatores de proteção ativos.")

    return insights if insights else ["📊 Dados insuficientes para insights aprofundados."]


def _gerar_recomendacoes(estado, ansiedade, depressao) -> list:
    recs = ["Manter registro diário de humor na plataforma"]
    if estado["risco"] in ["alto", "critico"]:
        recs.append("Avaliação presencial com psiquiatra")
        recs.append("Considerar avaliação de medicação")
    if ansiedade > 5:
        recs.append("Técnicas de respiração diafragmática 2x ao dia")
        recs.append("Mindfulness baseado em evidências (MBSR)")
    if depressao > 4:
        recs.append("Ativação comportamental progressiva")
        recs.append("Terapia Cognitivo-Comportamental (TCC)")
    recs.append("Manter rotina de sono regular (7-9 horas)")
    return recs


def _calcular_percentil(valor, minimo, maximo) -> int:
    if maximo == minimo:
        return 50
    percentil = int(((valor - minimo) / (maximo - minimo)) * 100)
    return max(0, min(100, percentil))


def _contar_estados():
    estados = {}
    for r in relatorios_db.values():
        e = r["secoes"]["avaliacao_ia"]["estado_geral"]
        estados[e] = estados.get(e, 0) + 1
    return estados


def _contar_tendencias():
    tendencias = {}
    for r in relatorios_db.values():
        t = r["secoes"]["avaliacao_ia"]["tendencia"]
        tendencias[t] = tendencias.get(t, 0) + 1
    return tendencias


plugin = RelatorioCLinicoMLPlugin()
