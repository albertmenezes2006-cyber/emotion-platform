"""
Plugin: Análise de Sentimento Avançada
Categoria: datascience
Descrição: Análise de sentimento multi-camada com léxico emocional em português
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import re
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/sentimento-avancado", tags=["datascience"])

analises_db = {}
historico_db = {}

# Léxico emocional em português
LEXICO_POSITIVO = {
    "feliz": 0.9, "alegre": 0.85, "contente": 0.8, "animado": 0.8,
    "esperancoso": 0.75, "grato": 0.85, "otimista": 0.8, "satisfeito": 0.75,
    "tranquilo": 0.7, "sereno": 0.7, "calmo": 0.65, "bem": 0.6,
    "ótimo": 0.9, "excelente": 0.95, "maravilhoso": 0.95, "incrível": 0.9,
    "amor": 0.9, "amado": 0.85, "carinho": 0.8, "paz": 0.75,
    "sucesso": 0.85, "conquista": 0.85, "vitória": 0.9, "superação": 0.85,
    "força": 0.75, "coragem": 0.8, "confiante": 0.8, "capaz": 0.75,
    "melhor": 0.7, "melhorando": 0.75, "crescendo": 0.75, "evoluindo": 0.8
}

LEXICO_NEGATIVO = {
    "triste": -0.8, "deprimido": -0.9, "ansioso": -0.7, "angustiado": -0.8,
    "desesperado": -0.95, "sozinho": -0.7, "abandonado": -0.85, "perdido": -0.7,
    "medo": -0.75, "assustado": -0.7, "apavorado": -0.85, "aterrorizado": -0.9,
    "raiva": -0.7, "furioso": -0.85, "irritado": -0.65, "revoltado": -0.75,
    "cansado": -0.5, "exausto": -0.7, "esgotado": -0.75, "sobrecarregado": -0.7,
    "culpado": -0.7, "envergonhado": -0.65, "inútil": -0.85, "fracasso": -0.85,
    "péssimo": -0.9, "terrível": -0.9, "horrível": -0.9, "insuportável": -0.9,
    "sem esperança": -0.9, "desistir": -0.8, "nunca": -0.4, "impossível": -0.6
}

INTENSIFICADORES = {
    "muito": 1.5, "bastante": 1.3, "extremamente": 1.8, "totalmente": 1.6,
    "completamente": 1.6, "super": 1.4, "mega": 1.5, "demais": 1.4,
    "pouco": 0.5, "um pouco": 0.6, "levemente": 0.6, "levemente": 0.5
}

NEGACOES = {"não", "nunca", "jamais", "nem", "nenhum", "nada", "sem"}


class AnaliseSentimentoAvancadaPlugin(PluginBase):
    name = "analise_sentimento_avancada"
    version = "1.0.0"
    description = "Análise de sentimento multi-camada com léxico em português"
    category = "datascience"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "palavras_positivas": len(LEXICO_POSITIVO),
            "palavras_negativas": len(LEXICO_NEGATIVO),
            "analises_realizadas": len(analises_db)
        }


@router.post("/analisar")
async def analisar_sentimento(texto: str, user_id: str = None):
    """Análise de sentimento completa com léxico emocional"""
    if not texto or len(texto.strip()) < 2:
        raise HTTPException(status_code=400, detail="Texto muito curto")

    texto_lower = texto.lower()
    palavras = re.findall(r'\b\w+\b', texto_lower)

    score_total = 0.0
    palavras_encontradas = []
    contexto_negacao = False

    for i, palavra in enumerate(palavras):
        # Verificar negação nas últimas 2 palavras
        if palavra in NEGACOES:
            contexto_negacao = True
            continue
        if i > 0 and palavras[i-1] not in NEGACOES:
            contexto_negacao = False

        # Verificar intensificador
        intensificador = 1.0
        if i > 0 and palavras[i-1] in INTENSIFICADORES:
            intensificador = INTENSIFICADORES[palavras[i-1]]

        # Score da palavra
        score = 0.0
        if palavra in LEXICO_POSITIVO:
            score = LEXICO_POSITIVO[palavra] * intensificador
            if contexto_negacao:
                score = -score * 0.7
            palavras_encontradas.append({
                "palavra": palavra,
                "score": round(score, 3),
                "tipo": "negativo" if contexto_negacao else "positivo"
            })
        elif palavra in LEXICO_NEGATIVO:
            score = LEXICO_NEGATIVO[palavra] * intensificador
            if contexto_negacao:
                score = -score * 0.7
            palavras_encontradas.append({
                "palavra": palavra,
                "score": round(score, 3),
                "tipo": "positivo" if contexto_negacao else "negativo"
            })

        score_total += score

    # Normalizar score para [-1, 1]
    if palavras_encontradas:
        score_normalizado = score_total / max(len(palavras_encontradas), 1)
        score_normalizado = max(-1.0, min(1.0, score_normalizado))
    else:
        score_normalizado = 0.0

    # Classificar sentimento
    if score_normalizado >= 0.5:
        sentimento = "muito_positivo"
        emocao_dominante = "felicidade"
    elif score_normalizado >= 0.1:
        sentimento = "positivo"
        emocao_dominante = "contentamento"
    elif score_normalizado >= -0.1:
        sentimento = "neutro"
        emocao_dominante = "neutro"
    elif score_normalizado >= -0.5:
        sentimento = "negativo"
        emocao_dominante = "tristeza"
    else:
        sentimento = "muito_negativo"
        emocao_dominante = "sofrimento"

    # Detectar intensidade
    intensidade = abs(score_normalizado)
    nivel_intensidade = (
        "muito_alta" if intensidade >= 0.7 else
        "alta" if intensidade >= 0.4 else
        "media" if intensidade >= 0.2 else "baixa"
    )

    analise_id = str(uuid.uuid4())[:8]
    resultado = {
        "id": analise_id,
        "texto_original": texto[:500],
        "score": round(score_normalizado, 4),
        "sentimento": sentimento,
        "emocao_dominante": emocao_dominante,
        "intensidade": nivel_intensidade,
        "palavras_detectadas": palavras_encontradas,
        "total_palavras": len(palavras),
        "palavras_emocionais": len(palavras_encontradas),
        "tem_negacao": any(p in NEGACOES for p in palavras),
        "recomendacao": _gerar_recomendacao(sentimento, intensidade),
        "analisado_em": datetime.utcnow().isoformat()
    }

    analises_db[analise_id] = resultado

    # Histórico por usuário
    if user_id:
        if user_id not in historico_db:
            historico_db[user_id] = []
        historico_db[user_id].append({
            "analise_id": analise_id,
            "score": score_normalizado,
            "sentimento": sentimento,
            "timestamp": resultado["analisado_em"]
        })
        if len(historico_db[user_id]) > 100:
            historico_db[user_id] = historico_db[user_id][-100:]

    return resultado


@router.post("/analisar/lote")
async def analisar_lote(textos: list, user_id: str = None):
    """Analisa múltiplos textos de uma vez"""
    if len(textos) > 50:
        raise HTTPException(status_code=400, detail="Máximo 50 textos por lote")

    resultados = []
    for texto in textos:
        if texto and len(texto.strip()) >= 2:
            analise = await analisar_sentimento(texto, user_id)
            resultados.append(analise)

    scores = [r["score"] for r in resultados]
    media = sum(scores) / len(scores) if scores else 0

    return {
        "total_analisados": len(resultados),
        "score_medio": round(media, 4),
        "sentimento_geral": _classificar_score(media),
        "resultados": resultados
    }


@router.get("/historico/{user_id}")
async def historico_sentimento(user_id: str, ultimos: int = 30):
    """Histórico de sentimento de um usuário"""
    historico = historico_db.get(user_id, [])
    recentes = historico[-ultimos:]

    if not recentes:
        return {"user_id": user_id, "historico": [], "tendencia": "sem_dados"}

    scores = [h["score"] for h in recentes]
    tendencia = "melhora" if scores[-1] > scores[0] else "piora" if scores[-1] < scores[0] else "estavel"

    return {
        "user_id": user_id,
        "total": len(recentes),
        "score_medio": round(sum(scores) / len(scores), 4),
        "tendencia": tendencia,
        "melhor_momento": max(scores),
        "pior_momento": min(scores),
        "historico": recentes
    }


@router.get("/lexico/stats")
async def stats_lexico():
    """Estatísticas do léxico emocional"""
    return {
        "palavras_positivas": len(LEXICO_POSITIVO),
        "palavras_negativas": len(LEXICO_NEGATIVO),
        "intensificadores": len(INTENSIFICADORES),
        "negacoes": len(NEGACOES),
        "top_positivas": sorted(LEXICO_POSITIVO.items(), key=lambda x: x[1], reverse=True)[:10],
        "top_negativas": sorted(LEXICO_NEGATIVO.items(), key=lambda x: x[1])[:10]
    }


def _gerar_recomendacao(sentimento: str, intensidade: float) -> str:
    mapa = {
        "muito_positivo": "Continue cultivando esses sentimentos positivos! 🌟",
        "positivo": "Você está num bom momento emocional. Aproveite! 😊",
        "neutro": "Momento de equilíbrio. Observe como se sente agora.",
        "negativo": "Considere técnicas de regulação emocional como respiração profunda.",
        "muito_negativo": "Recomendamos conversar com um profissional de saúde mental. 💙"
    }
    return mapa.get(sentimento, "Continue se cuidando.")


def _classificar_score(score: float) -> str:
    if score >= 0.5:
        return "muito_positivo"
    elif score >= 0.1:
        return "positivo"
    elif score >= -0.1:
        return "neutro"
    elif score >= -0.5:
        return "negativo"
    else:
        return "muito_negativo"


plugin = AnaliseSentimentoAvancadaPlugin()
