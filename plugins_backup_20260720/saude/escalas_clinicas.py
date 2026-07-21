"""
Plugin: Escalas Clinicas Avancadas
Categoria: saude
"""
VERSAO = "1.0"
NOME = "escalas_clinicas"
DESCRICAO = "Beck, Hamilton, Likert, Columbia, DSM-5, CID-10"
CATEGORIA = "saude"

from collections import defaultdict

_resultados_escalas = defaultdict(list)

# ── Beck Depression Inventory (BDI-II)
BDI_PERGUNTAS = [
    "Tristeza", "Pessimismo", "Fracasso passado", "Perda de prazer",
    "Sentimentos de culpa", "Sentimentos de punição", "Autodepreciação",
    "Autocritica", "Pensamentos suicidas", "Choro", "Agitação",
    "Perda de interesse", "Indecisão", "Inutilidade", "Perda de energia",
    "Mudança no sono", "Irritabilidade", "Mudança no apetite",
    "Dificuldade de concentração", "Cansaço", "Perda de interesse sexual",
]

def calcular_bdi(respostas: list) -> dict:
    if len(respostas) != 21:
        return {"erro": "Precisam de 21 respostas (0-3 cada)"}
    total = sum(int(r) for r in respostas)
    if total <= 13: nivel, cor = "Minimo", "verde"
    elif total <= 19: nivel, cor = "Leve", "amarelo"
    elif total <= 28: nivel, cor = "Moderado", "laranja"
    else: nivel, cor = "Severo", "vermelho"
    return {"total": total, "nivel": nivel, "cor": cor, "escala": "BDI-II", "max": 63}

# ── Hamilton Anxiety Scale (HAM-A)
HAMA_ITENS = [
    "Humor ansioso", "Tensão", "Medos", "Insônia",
    "Intelectual (cognitivo)", "Humor deprimido", "Somático (muscular)",
    "Somático (sensorial)", "Cardiovascular", "Respiratório",
    "Gastrointestinal", "Geniturinário", "Autonômico", "Comportamento",
]

def calcular_hama(respostas: list) -> dict:
    if len(respostas) != 14:
        return {"erro": "Precisam de 14 respostas (0-4 cada)"}
    total = sum(int(r) for r in respostas)
    if total < 17: nivel = "Leve"
    elif total < 25: nivel = "Moderado"
    else: nivel = "Severo"
    return {"total": total, "nivel": nivel, "escala": "HAM-A", "max": 56}

# ── Escala de Likert genérica
def criar_escala_likert(pergunta: str, escala: int = 5) -> dict:
    opcoes_5 = ["Discordo totalmente","Discordo","Neutro","Concordo","Concordo totalmente"]
    opcoes_7 = ["Discordo totalmente","Discordo","Discordo levemente","Neutro","Concordo levemente","Concordo","Concordo totalmente"]
    opcoes_10 = [str(i) for i in range(1,11)]
    opcoes = {5: opcoes_5, 7: opcoes_7, 10: opcoes_10}.get(escala, opcoes_5)
    return {"pergunta": pergunta, "escala": escala, "opcoes": opcoes, "tipo": "likert"}

def calcular_media_likert(respostas: list, escala: int = 5) -> dict:
    if not respostas:
        return {"media": 0, "interpretacao": "sem dados"}
    media = sum(respostas) / len(respostas)
    pct_max = (media / escala) * 100
    interpretacao = "Alta concordancia" if pct_max >= 70 else "Concordancia moderada" if pct_max >= 50 else "Baixa concordancia"
    return {"media": round(media,2), "percentual_maximo": round(pct_max,1), "interpretacao": interpretacao}

# ── Columbia Suicide Severity Rating Scale (C-SSRS)
CSSRS_PERGUNTAS = [
    "Desejo de estar morto", "Pensamentos suicidas passivos",
    "Pensamentos suicidas ativos sem plano", "Pensamentos com plano",
    "Intenção de agir", "Comportamento suicida no último mês",
]

def calcular_cssrs(respostas: list) -> dict:
    if len(respostas) != 6:
        return {"erro": "Precisam de 6 respostas (0=Nao, 1=Sim)"}
    positivos = sum(int(r) for r in respostas)
    risco_imediato = int(respostas[4]) == 1 or int(respostas[5]) == 1
    if risco_imediato or positivos >= 4: nivel_risco = "ALTO"
    elif positivos >= 2: nivel_risco = "MODERADO"
    elif positivos >= 1: nivel_risco = "BAIXO"
    else: nivel_risco = "MINIMO"
    return {
        "nivel_risco": nivel_risco,
        "risco_imediato": risco_imediato,
        "itens_positivos": positivos,
        "acao_recomendada": "Encaminhar IMEDIATAMENTE para avaliacao profissional" if nivel_risco in ("ALTO","MODERADO") else "Monitorar e acompanhar",
        "cvv": "188 — 24h gratuito",
        "escala": "C-SSRS"
    }

# ── DSM-5 Criterios simplificados
DSM5_TRANSTORNOS = {
    "depressao_maior": {
        "nome": "Transtorno Depressivo Maior",
        "criterios_minimos": 5,
        "criterios": [
            "Humor deprimido na maior parte do dia",
            "Perda de interesse ou prazer",
            "Perda ou ganho significativo de peso",
            "Insônia ou hipersonia",
            "Agitação ou retardo psicomotor",
            "Fadiga ou perda de energia",
            "Sentimentos de inutilidade ou culpa",
            "Diminuição da concentração",
            "Pensamentos recorrentes de morte",
        ]
    },
    "transtorno_ansiedade_generalizada": {
        "nome": "Transtorno de Ansiedade Generalizada",
        "criterios_minimos": 3,
        "criterios": [
            "Ansiedade e preocupação excessivas",
            "Dificuldade em controlar a preocupação",
            "Inquietação ou sensação de estar com os nervos à flor da pele",
            "Fatigabilidade",
            "Dificuldade de concentração",
            "Irritabilidade",
            "Tensão muscular",
            "Perturbação do sono",
        ]
    }
}

def avaliar_criterios_dsm5(transtorno: str, criterios_presentes: list) -> dict:
    if transtorno not in DSM5_TRANSTORNOS:
        return {"erro": f"Transtorno nao encontrado: {transtorno}"}
    dados = DSM5_TRANSTORNOS[transtorno]
    minimo = dados["criterios_minimos"]
    positivos = len([c for c in criterios_presentes if c])
    atende = positivos >= minimo
    return {
        "transtorno": dados["nome"],
        "criterios_positivos": positivos,
        "criterios_necessarios": minimo,
        "atende_criterios": atende,
        "aviso": "Esta e uma avaliacao de rastreamento. Apenas profissional de saude pode diagnosticar.",
        "recomendacao": "Buscar avaliacao profissional" if atende else "Monitorar sintomas"
    }

# ── CID-10 Codigos relevantes
CID10_EMOCOES = {
    "F32": "Episodio depressivo",
    "F33": "Transtorno depressivo recorrente",
    "F40": "Transtornos fobicos ansiosos",
    "F41": "Outros transtornos ansiosos",
    "F42": "Transtorno obsessivo-compulsivo",
    "F43": "Reacoes ao stress grave e transtornos de adaptacao",
    "F60": "Transtornos especificos da personalidade",
    "F90": "Transtornos hipercineticos",
    "Z73": "Problemas relacionados com a organizacao do modo de vida",
}

def buscar_cid10(codigo: str) -> dict:
    descricao = CID10_EMOCOES.get(codigo.upper(), "Codigo nao encontrado na base local")
    return {"codigo": codigo.upper(), "descricao": descricao, "fonte": "CID-10 OMS"}

def stats_escalas() -> dict:
    return {
        "escalas_disponiveis": ["BDI-II", "HAM-A", "C-SSRS", "Likert", "DSM-5", "CID-10"],
        "total_avaliacoes": sum(len(v) for v in _resultados_escalas.values()),
        "plugin": "escalas_clinicas v1.0"
    }
