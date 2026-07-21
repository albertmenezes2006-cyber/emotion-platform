"""
Plugin: Gamificacao Avancada — XP, Missoes, Torneios
Categoria: social
"""
VERSAO = "1.0"
NOME = "gamificacao_avancada"
DESCRICAO = "Sistema de XP avancado, missoes diarias, torneios e clans"
CATEGORIA = "social"

from datetime import datetime, timedelta
from collections import defaultdict

_xp_usuarios = defaultdict(int)
_missoes_diarias = {}
_torneios = {}
_clans = {}
_membros_clan = defaultdict(set)
_desafios_semanais = {}

MULTIPLICADORES_XP = {
    "analise": 10, "chat_mensagem": 5, "diario": 15,
    "teste_psicologico": 25, "mindfulness": 20,
    "streak_7dias": 100, "streak_30dias": 500,
    "primeiro_login_dia": 5, "convidar_amigo": 50,
    "avaliacao_psicologo": 30, "post_social": 8,
}

NIVEIS_XP = [
    (0, "Iniciante", "🌱"),
    (100, "Explorador", "🗺️"),
    (500, "Praticante", "⭐"),
    (1500, "Desenvolvido", "🌟"),
    (3000, "Avancado", "💫"),
    (6000, "Expert", "🏆"),
    (10000, "Mestre", "👑"),
    (20000, "Lenda", "🔥"),
]

def ganhar_xp(usuario_id: int, acao: str, multiplicador: float = 1.0) -> dict:
    xp_base = MULTIPLICADORES_XP.get(acao, 5)
    xp_ganho = int(xp_base * multiplicador)
    _xp_usuarios[usuario_id] += xp_ganho
    total = _xp_usuarios[usuario_id]
    nivel_antes = calcular_nivel(total - xp_ganho)
    nivel_atual = calcular_nivel(total)
    subiu_nivel = nivel_atual["nivel"] != nivel_antes["nivel"]
    return {
        "xp_ganho": xp_ganho,
        "xp_total": total,
        "nivel": nivel_atual,
        "subiu_nivel": subiu_nivel,
        "novo_nivel": nivel_atual if subiu_nivel else None
    }

def calcular_nivel(xp: int) -> dict:
    nivel_atual = NIVEIS_XP[0]
    proximo = NIVEIS_XP[1] if len(NIVEIS_XP) > 1 else None
    for i, (xp_min, nome, emoji) in enumerate(NIVEIS_XP):
        if xp >= xp_min:
            nivel_atual = (xp_min, nome, emoji)
            proximo = NIVEIS_XP[i+1] if i+1 < len(NIVEIS_XP) else None
    xp_min, nome, emoji = nivel_atual
    progresso = 0
    if proximo:
        prox_min = proximo[0]
        progresso = round((xp - xp_min) / (prox_min - xp_min) * 100, 1)
    return {
        "nivel": nome,
        "emoji": emoji,
        "xp_atual": xp,
        "xp_nivel_atual": xp_min,
        "xp_proximo_nivel": proximo[0] if proximo else None,
        "progresso_pct": min(100, progresso),
        "proximo_nivel": proximo[1] if proximo else "MAX"
    }

def gerar_missoes_diarias(usuario_id: int) -> list:
    hoje = datetime.now().strftime("%Y-%m-%d")
    chave = f"{usuario_id}:{hoje}"
    if chave in _missoes_diarias:
        return _missoes_diarias[chave]
    import random
    missoes_disponiveis = [
        {"id": "analise_1", "titulo": "Analisar 1 emocao", "xp": 20, "tipo": "analise", "meta": 1},
        {"id": "chat_3", "titulo": "3 mensagens para Sofia", "xp": 30, "tipo": "chat", "meta": 3},
        {"id": "diario_1", "titulo": "Escrever no diario", "xp": 25, "tipo": "diario", "meta": 1},
        {"id": "mindfulness_1", "titulo": "Fazer 1 exercicio mindfulness", "xp": 35, "tipo": "mindfulness", "meta": 1},
        {"id": "login", "titulo": "Fazer login hoje", "xp": 10, "tipo": "login", "meta": 1},
    ]
    selecionadas = random.sample(missoes_disponiveis, min(3, len(missoes_disponiveis)))
    for m in selecionadas:
        m["progresso"] = 0
        m["completa"] = False
        m["data"] = hoje
    _missoes_diarias[chave] = selecionadas
    return selecionadas

def criar_torneio(nome: str, tipo: str, duracao_dias: int = 7, premio_xp: int = 500) -> dict:
    import secrets
    torneio_id = secrets.token_hex(6)
    _torneios[torneio_id] = {
        "id": torneio_id,
        "nome": nome,
        "tipo": tipo,
        "inicio": datetime.now().isoformat(),
        "fim": (datetime.now() + timedelta(days=duracao_dias)).isoformat(),
        "premio_xp": premio_xp,
        "participantes": {},
        "ativo": True
    }
    return _torneios[torneio_id]

def participar_torneio(torneio_id: str, usuario_id: int, nome: str) -> dict:
    if torneio_id not in _torneios:
        return {"erro": "Torneio nao encontrado"}
    _torneios[torneio_id]["participantes"][usuario_id] = {"nome": nome, "score": 0, "posicao": 0}
    return {"ok": True, "torneio": _torneios[torneio_id]["nome"]}

def criar_clan(nome: str, lider_id: int, descricao: str = "") -> dict:
    import secrets
    clan_id = secrets.token_hex(6)
    _clans[clan_id] = {
        "id": clan_id,
        "nome": nome,
        "lider_id": lider_id,
        "descricao": descricao[:200],
        "criado_em": datetime.now().isoformat(),
        "membros": [lider_id],
        "xp_total": 0
    }
    _membros_clan[lider_id].add(clan_id)
    return _clans[clan_id]

def entrar_clan(clan_id: str, usuario_id: int) -> dict:
    if clan_id not in _clans:
        return {"erro": "Clan nao encontrado"}
    if len(_clans[clan_id]["membros"]) >= 50:
        return {"erro": "Clan cheio (max 50 membros)"}
    _clans[clan_id]["membros"].append(usuario_id)
    _membros_clan[usuario_id].add(clan_id)
    return {"ok": True, "clan": _clans[clan_id]["nome"]}

def leaderboard_global(top_k: int = 10) -> list:
    ranking = sorted(_xp_usuarios.items(), key=lambda x: x[1], reverse=True)[:top_k]
    return [{"posicao": i+1, "usuario_id": uid, "xp": xp, "nivel": calcular_nivel(xp)["nivel"]} for i, (uid, xp) in enumerate(ranking)]

def stats_gamificacao() -> dict:
    return {
        "usuarios_com_xp": len(_xp_usuarios),
        "total_xp_distribuido": sum(_xp_usuarios.values()),
        "torneios_ativos": sum(1 for t in _torneios.values() if t.get("ativo")),
        "clans_ativos": len(_clans),
        "plugin": "gamificacao_avancada v1.0"
    }
