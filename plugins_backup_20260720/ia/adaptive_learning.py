"""
Plugin: Adaptive Learning — Aprendizado Adaptativo
Categoria: ia
"""
VERSAO = "1.0"
NOME = "adaptive_learning"
DESCRICAO = "Sistema de aprendizado que adapta conteudo ao usuario"
CATEGORIA = "ia"

from datetime import datetime
from collections import defaultdict

_perfis_aprendizado = {}
_progresso_usuarios = defaultdict(dict)
_dificuldade_atual = defaultdict(lambda: "medio")

NIVEIS_DIFICULDADE = ["iniciante", "basico", "medio", "avancado", "especialista"]

CONTEUDOS_POR_NIVEL = {
    "iniciante": {
        "descricao": "Primeiros passos na inteligencia emocional",
        "exercicios": ["respiracao_basica", "identificar_emocao", "diario_simples"],
        "tempo_min": 5,
    },
    "basico": {
        "descricao": "Desenvolvendo consciencia emocional",
        "exercicios": ["respiracao_4_7_8", "body_scan_curto", "diario_estruturado"],
        "tempo_min": 10,
    },
    "medio": {
        "descricao": "Regulacao e expressao emocional",
        "exercicios": ["meditacao_10min", "reestruturacao_cognitiva", "assertividade"],
        "tempo_min": 20,
    },
    "avancado": {
        "descricao": "Inteligencia emocional em relacionamentos",
        "exercicios": ["empatia_avancada", "comunicacao_nao_violenta", "mindfulness_30min"],
        "tempo_min": 30,
    },
    "especialista": {
        "descricao": "Maestria emocional",
        "exercicios": ["integracao_emocional", "lideranca_emocional", "coaching_emocional"],
        "tempo_min": 45,
    }
}

def avaliar_progresso(usuario_id: int, exercicio: str, completado: bool, tempo_min: float) -> dict:
    if usuario_id not in _perfis_aprendizado:
        _perfis_aprendizado[usuario_id] = {
            "nivel_atual": "iniciante",
            "pontos": 0,
            "exercicios_completos": 0,
            "streak": 0,
            "ultima_atividade": None,
        }
    perfil = _perfis_aprendizado[usuario_id]
    if completado:
        perfil["pontos"] += 10
        perfil["exercicios_completos"] += 1
        perfil["ultima_atividade"] = datetime.now().isoformat()
        nivel_idx = NIVEIS_DIFICULDADE.index(perfil["nivel_atual"])
        if perfil["exercicios_completos"] % 5 == 0 and nivel_idx < len(NIVEIS_DIFICULDADE) - 1:
            perfil["nivel_atual"] = NIVEIS_DIFICULDADE[nivel_idx + 1]
            return {"avancou_nivel": True, "novo_nivel": perfil["nivel_atual"], "perfil": perfil}
    return {"avancou_nivel": False, "perfil": perfil}

def obter_proximo_exercicio(usuario_id: int, emocao_atual: str = "neutro") -> dict:
    perfil = _perfis_aprendizado.get(usuario_id, {"nivel_atual": "iniciante"})
    nivel = perfil["nivel_atual"]
    conteudo = CONTEUDOS_POR_NIVEL.get(nivel, CONTEUDOS_POR_NIVEL["iniciante"])
    from plugins.ia.recommendation import recomendar_exercicios_mindfulness
    exercicios_recomendados = recomendar_exercicios_mindfulness(emocao_atual)
    return {
        "nivel": nivel,
        "descricao": conteudo["descricao"],
        "exercicio_recomendado": exercicios_recomendados[0] if exercicios_recomendados else conteudo["exercicios"][0],
        "tempo_estimado_min": conteudo["tempo_min"],
        "pontos_usuario": perfil.get("pontos", 0),
    }

def stats_adaptive_learning() -> dict:
    return {
        "usuarios_ativos": len(_perfis_aprendizado),
        "niveis": NIVEIS_DIFICULDADE,
        "plugin": "adaptive_learning v1.0"
    }
