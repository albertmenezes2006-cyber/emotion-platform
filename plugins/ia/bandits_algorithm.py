"""
Plugin: Multi-Armed Bandits Algorithm
Categoria: ia
Descrição: Algoritmos de bandits para otimização de intervenções terapêuticas
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import random
import math
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/bandits", tags=["ia"])

experimentos_db = {}
bracos_db = {}
recompensas_log = []


class BanditsAlgorithmPlugin(PluginBase):
    name = "bandits_algorithm"
    version = "1.0.0"
    description = "Multi-Armed Bandits para otimização de intervenções"
    category = "ia"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "experimentos_ativos": sum(1 for e in experimentos_db.values() if e["ativo"]),
            "total_decisoes": len(recompensas_log)
        }


@router.post("/experimento/criar")
async def criar_experimento(
    nome: str,
    algoritmo: str = "ucb1",
    opcoes: list = None,
    descricao: str = ""
):
    """Cria um experimento de bandits"""
    algoritmos_validos = ["ucb1", "epsilon_greedy", "thompson_sampling", "softmax"]
    if algoritmo not in algoritmos_validos:
        raise HTTPException(status_code=400, detail=f"Algoritmos: {algoritmos_validos}")

    if not opcoes:
        opcoes = ["intervencao_A", "intervencao_B", "intervencao_C"]

    exp_id = str(uuid.uuid4())[:8]

    # Inicializar braços
    bracos = {}
    for opcao in opcoes:
        braco_id = f"{exp_id}_{opcao}"
        bracos[braco_id] = {
            "id": braco_id,
            "nome": opcao,
            "tentativas": 0,
            "recompensa_total": 0.0,
            "recompensa_media": 0.0,
            "melhor_recompensa": 0.0,
            "alpha": 1,  # Para Thompson Sampling
            "beta": 1    # Para Thompson Sampling
        }
    bracos_db[exp_id] = bracos

    experimentos_db[exp_id] = {
        "id": exp_id,
        "nome": nome,
        "algoritmo": algoritmo,
        "descricao": descricao,
        "opcoes": opcoes,
        "total_decisoes": 0,
        "ativo": True,
        "criado_em": datetime.utcnow().isoformat(),
        "epsilon": 0.1,  # Para epsilon-greedy
        "temperatura": 1.0  # Para softmax
    }

    return {
        "experimento_id": exp_id,
        "algoritmo": algoritmo,
        "opcoes": opcoes,
        "status": "experimento criado"
    }


@router.post("/decidir/{exp_id}")
async def tomar_decisao(exp_id: str, user_id: str = ""):
    """Toma uma decisão usando o algoritmo de bandits"""
    if exp_id not in experimentos_db:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    exp = experimentos_db[exp_id]
    if not exp["ativo"]:
        raise HTTPException(status_code=400, detail="Experimento inativo")

    bracos = bracos_db[exp_id]
    algoritmo = exp["algoritmo"]

    # Selecionar braço
    if algoritmo == "ucb1":
        escolha = _ucb1(bracos, exp["total_decisoes"])
    elif algoritmo == "epsilon_greedy":
        escolha = _epsilon_greedy(bracos, exp["epsilon"])
    elif algoritmo == "thompson_sampling":
        escolha = _thompson_sampling(bracos)
    elif algoritmo == "softmax":
        escolha = _softmax(bracos, exp["temperatura"])
    else:
        escolha = random.choice(list(bracos.keys()))

    braco = bracos[escolha]
    exp["total_decisoes"] += 1

    return {
        "experimento_id": exp_id,
        "decisao": braco["nome"],
        "braco_id": escolha,
        "algoritmo": algoritmo,
        "decisao_numero": exp["total_decisoes"],
        "user_id": user_id
    }


@router.post("/recompensa/{exp_id}")
async def registrar_recompensa(
    exp_id: str,
    braco_nome: str,
    recompensa: float,
    user_id: str = ""
):
    """Registra recompensa para um braço"""
    if exp_id not in experimentos_db:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    bracos = bracos_db[exp_id]
    braco_id = f"{exp_id}_{braco_nome}"

    if braco_id not in bracos:
        raise HTTPException(status_code=404, detail="Braço não encontrado")

    braco = bracos[braco_id]
    recompensa = max(0.0, min(1.0, recompensa))  # Normalizar entre 0 e 1

    braco["tentativas"] += 1
    braco["recompensa_total"] += recompensa
    braco["recompensa_media"] = braco["recompensa_total"] / braco["tentativas"]
    braco["melhor_recompensa"] = max(braco["melhor_recompensa"], recompensa)

    # Atualizar Thompson Sampling
    if recompensa >= 0.5:
        braco["alpha"] += 1
    else:
        braco["beta"] += 1

    recompensas_log.append({
        "exp_id": exp_id,
        "braco": braco_nome,
        "recompensa": recompensa,
        "user_id": user_id,
        "timestamp": datetime.utcnow().isoformat()
    })

    return {
        "status": "recompensa registrada",
        "braco": braco_nome,
        "recompensa": recompensa,
        "media_atual": round(braco["recompensa_media"], 4),
        "tentativas": braco["tentativas"]
    }


@router.get("/resultados/{exp_id}")
async def resultados_experimento(exp_id: str):
    """Resultados do experimento"""
    if exp_id not in experimentos_db:
        raise HTTPException(status_code=404, detail="Experimento não encontrado")

    exp = experimentos_db[exp_id]
    bracos = bracos_db[exp_id]

    ranking = sorted(
        bracos.values(),
        key=lambda x: x["recompensa_media"],
        reverse=True
    )

    return {
        "experimento": exp["nome"],
        "algoritmo": exp["algoritmo"],
        "total_decisoes": exp["total_decisoes"],
        "ranking": [{
            "nome": b["nome"],
            "tentativas": b["tentativas"],
            "recompensa_media": round(b["recompensa_media"], 4),
            "melhor_recompensa": b["melhor_recompensa"]
        } for b in ranking],
        "melhor_opcao": ranking[0]["nome"] if ranking and ranking[0]["tentativas"] > 0 else "indefinido",
        "confianca": _calcular_confianca(ranking)
    }


@router.get("/experimentos")
async def listar_experimentos():
    """Lista todos os experimentos"""
    return {
        "total": len(experimentos_db),
        "experimentos": [{
            "id": e["id"],
            "nome": e["nome"],
            "algoritmo": e["algoritmo"],
            "decisoes": e["total_decisoes"],
            "ativo": e["ativo"]
        } for e in experimentos_db.values()]
    }


def _ucb1(bracos: dict, total_n: int) -> str:
    """Upper Confidence Bound"""
    if total_n == 0:
        return random.choice(list(bracos.keys()))

    # Primeiro, garantir que todos foram tentados pelo menos uma vez
    for bid, b in bracos.items():
        if b["tentativas"] == 0:
            return bid

    # Calcular UCB
    melhor_score = -1
    melhor_id = list(bracos.keys())[0]
    for bid, b in bracos.items():
        exploitation = b["recompensa_media"]
        exploration = math.sqrt(2 * math.log(total_n) / b["tentativas"])
        score = exploitation + exploration
        if score > melhor_score:
            melhor_score = score
            melhor_id = bid

    return melhor_id


def _epsilon_greedy(bracos: dict, epsilon: float) -> str:
    """Epsilon-Greedy"""
    if random.random() < epsilon:
        return random.choice(list(bracos.keys()))

    melhor_id = max(bracos.keys(), key=lambda x: bracos[x]["recompensa_media"])
    return melhor_id


def _thompson_sampling(bracos: dict) -> str:
    """Thompson Sampling (Beta distribution)"""
    amostras = {}
    for bid, b in bracos.items():
        amostras[bid] = random.betavariate(b["alpha"], b["beta"])
    return max(amostras, key=amostras.get)


def _softmax(bracos: dict, temperatura: float) -> str:
    """Softmax / Boltzmann"""
    ids = list(bracos.keys())
    medias = [bracos[bid]["recompensa_media"] for bid in ids]

    # Calcular probabilidades
    exp_values = [math.exp(m / max(temperatura, 0.01)) for m in medias]
    soma = sum(exp_values)
    probs = [e / soma for e in exp_values]

    # Selecionar
    r = random.random()
    acumulado = 0
    for i, p in enumerate(probs):
        acumulado += p
        if r <= acumulado:
            return ids[i]
    return ids[-1]


def _calcular_confianca(ranking: list) -> float:
    """Calcula confiança na melhor opção"""
    if len(ranking) < 2:
        return 0.5
    if ranking[0]["tentativas"] == 0:
        return 0.0
    total_tentativas = sum(r["tentativas"] for r in ranking)
    if total_tentativas < 30:
        return 0.3
    diff = ranking[0]["recompensa_media"] - ranking[1]["recompensa_media"]
    return min(0.99, 0.5 + diff * 2)


plugin = BanditsAlgorithmPlugin()
