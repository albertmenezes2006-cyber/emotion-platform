"""
Plugin: Multi-Armed Bandits para Personalizacao
Categoria: ia
"""
VERSAO = "1.0"
NOME = "bandits_algorithm"
DESCRICAO = "Algoritmo epsilon-greedy e UCB para otimizacao de experiencia do usuario"
CATEGORIA = "ia"

import math
import random
from datetime import datetime
from collections import defaultdict

_experimentos_bandit = {}
_recompensas_bandit = defaultdict(lambda: defaultdict(list))
_contagem_bandit = defaultdict(lambda: defaultdict(int))

def criar_experimento_bandit(nome: str, alternativas: list, algoritmo: str = "epsilon_greedy", epsilon: float = 0.1) -> dict:
    _experimentos_bandit[nome] = {
        "nome": nome,
        "alternativas": alternativas,
        "algoritmo": algoritmo,
        "epsilon": epsilon,
        "criado_em": datetime.now().isoformat(),
        "total_trials": 0
    }
    for alt in alternativas:
        _contagem_bandit[nome][alt] = 0
    return _experimentos_bandit[nome]

def selecionar_alternativa_epsilon_greedy(experimento: str, usuario_id: int) -> str:
    if experimento not in _experimentos_bandit:
        return ""
    exp = _experimentos_bandit[experimento]
    alternativas = exp["alternativas"]
    epsilon = exp.get("epsilon", 0.1)
    if random.random() < epsilon:
        return random.choice(alternativas)
    medias = {}
    for alt in alternativas:
        recompensas = _recompensas_bandit[experimento][alt]
        medias[alt] = sum(recompensas) / len(recompensas) if recompensas else 0
    return max(medias, key=medias.get)

def selecionar_alternativa_ucb(experimento: str, c: float = 2.0) -> str:
    if experimento not in _experimentos_bandit:
        return ""
    exp = _experimentos_bandit[experimento]
    alternativas = exp["alternativas"]
    total = sum(_contagem_bandit[experimento][alt] for alt in alternativas)
    if total == 0:
        return random.choice(alternativas)
    ucb_scores = {}
    for alt in alternativas:
        n = _contagem_bandit[experimento][alt]
        recompensas = _recompensas_bandit[experimento][alt]
        media = sum(recompensas) / n if n > 0 else 0
        ucb = media + c * math.sqrt(math.log(total + 1) / (n + 1))
        ucb_scores[alt] = ucb
    return max(ucb_scores, key=ucb_scores.get)

def registrar_recompensa_bandit(experimento: str, alternativa: str, recompensa: float):
    _recompensas_bandit[experimento][alternativa].append(recompensa)
    _contagem_bandit[experimento][alternativa] += 1
    if experimento in _experimentos_bandit:
        _experimentos_bandit[experimento]["total_trials"] += 1

def obter_melhor_alternativa(experimento: str) -> dict:
    if experimento not in _experimentos_bandit:
        return {}
    alternativas = _experimentos_bandit[experimento]["alternativas"]
    stats = {}
    for alt in alternativas:
        recompensas = _recompensas_bandit[experimento][alt]
        n = _contagem_bandit[experimento][alt]
        stats[alt] = {
            "media_recompensa": round(sum(recompensas)/n, 4) if n > 0 else 0,
            "total_trials": n,
            "ultima_recompensa": recompensas[-1] if recompensas else None
        }
    melhor = max(stats, key=lambda x: stats[x]["media_recompensa"])
    return {"melhor_alternativa": melhor, "confianca": "alta" if stats[melhor]["total_trials"] > 50 else "baixa", "stats": stats}

EXPERIMENTOS_PADRAO = [
    {"nome": "cta_analisar", "alternativas": ["Analisar Agora", "Descobrir Emocoes", "Iniciar Analise", "Explorar Sentimentos"]},
    {"nome": "mensagem_boas_vindas", "alternativas": ["Ola! Como posso ajudar?", "Oi! Estou aqui para voce.", "Bem-vindo! Como esta se sentindo?"]},
    {"nome": "upsell_premium", "alternativas": ["Upgrade para Premium", "Desbloqueie mais recursos", "Potencialize sua jornada"]},
]

def inicializar_experimentos_padrao():
    for exp in EXPERIMENTOS_PADRAO:
        if exp["nome"] not in _experimentos_bandit:
            criar_experimento_bandit(exp["nome"], exp["alternativas"])

inicializar_experimentos_padrao()

def stats_bandits() -> dict:
    return {
        "experimentos_ativos": len(_experimentos_bandit),
        "total_trials": sum(e.get("total_trials",0) for e in _experimentos_bandit.values()),
        "algoritmos": ["epsilon_greedy","ucb"],
        "plugin": "bandits_algorithm v1.0"
    }
