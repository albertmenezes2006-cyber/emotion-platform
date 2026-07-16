"""
Plugin: Memoria Episodica para Sofia IA
Categoria: ia
"""
VERSAO = "1.0"
NOME = "memory_episodica"
DESCRICAO = "Memoria de longo prazo episodica para Sofia — lembra contextos e padroes"
CATEGORIA = "ia"

import hashlib
from datetime import datetime, timedelta
from collections import defaultdict

_memorias_episodicas = defaultdict(list)
_padroes_usuario = defaultdict(dict)
_contextos_importantes = defaultdict(list)
_gatilhos_emocionais = defaultdict(list)

TIPOS_MEMORIA = ["episodio","padrao","gatilho","conquista","crise","insight"]

def salvar_episodio(usuario_id: int, tipo: str, conteudo: str, emocao: str, importancia: int = 5) -> dict:
    importancia = max(1, min(10, importancia))
    episodio = {
        "id": hashlib.md5(f"{usuario_id}{datetime.now().isoformat()}".encode()).hexdigest()[:8],
        "tipo": tipo,
        "conteudo": conteudo[:500],
        "emocao": emocao,
        "importancia": importancia,
        "ts": datetime.now().isoformat(),
        "acessos": 0
    }
    _memorias_episodicas[usuario_id].append(episodio)
    if len(_memorias_episodicas[usuario_id]) > 200:
        _memorias_episodicas[usuario_id].sort(key=lambda x: x["importancia"], reverse=True)
        _memorias_episodicas[usuario_id] = _memorias_episodicas[usuario_id][:150]
    if tipo == "gatilho":
        _gatilhos_emocionais[usuario_id].append({"gatilho": conteudo[:100], "emocao": emocao, "ts": episodio["ts"]})
    return episodio

def recuperar_memorias_relevantes(usuario_id: int, contexto: str, limite: int = 5) -> list:
    memorias = _memorias_episodicas.get(usuario_id, [])
    if not memorias:
        return []
    contexto_lower = contexto.lower()
    pontuadas = []
    for mem in memorias:
        score = 0
        palavras_contexto = contexto_lower.split()
        conteudo_lower = mem["conteudo"].lower()
        matches = sum(1 for p in palavras_contexto if p in conteudo_lower and len(p) > 3)
        score += matches * 2
        score += mem["importancia"]
        dias_atras = (datetime.now() - datetime.fromisoformat(mem["ts"])).days
        score += max(0, 10 - dias_atras)
        mem["_score_relevancia"] = score
        pontuadas.append(mem)
    pontuadas.sort(key=lambda x: x["_score_relevancia"], reverse=True)
    selecionadas = pontuadas[:limite]
    for mem in selecionadas:
        mem["acessos"] += 1
    return selecionadas

def detectar_padroes_usuario(usuario_id: int) -> dict:
    memorias = _memorias_episodicas.get(usuario_id, [])
    if len(memorias) < 5:
        return {"padroes_identificados": 0}
    from collections import Counter
    emocoes = [m["emocao"] for m in memorias]
    contagem_emocoes = Counter(emocoes)
    emocao_dominante = contagem_emocoes.most_common(1)[0][0] if emocoes else "neutro"
    gatilhos = _gatilhos_emocionais.get(usuario_id, [])
    gatilhos_frequentes = Counter([g["gatilho"][:30] for g in gatilhos]).most_common(3)
    importancias = [m["importancia"] for m in memorias[-10:]]
    tendencia = "crescente" if len(importancias) >= 2 and importancias[-1] > importancias[0] else "decrescente" if len(importancias) >= 2 and importancias[-1] < importancias[0] else "estavel"
    padroes = {
        "emocao_dominante": emocao_dominante,
        "distribuicao_emocoes": dict(contagem_emocoes),
        "gatilhos_frequentes": gatilhos_frequentes,
        "tendencia_importancia": tendencia,
        "total_memorias": len(memorias),
        "padroes_identificados": len(set(emocoes)),
    }
    _padroes_usuario[usuario_id] = padroes
    return padroes

def gerar_contexto_sofia(usuario_id: int, mensagem_atual: str) -> str:
    padroes = _padroes_usuario.get(usuario_id) or detectar_padroes_usuario(usuario_id)
    memorias = recuperar_memorias_relevantes(usuario_id, mensagem_atual, 3)
    partes = []
    if padroes.get("emocao_dominante"):
        partes.append(f"Emocao predominante historica: {padroes['emocao_dominante']}")
    if memorias:
        partes.append("Memorias relevantes recentes:")
        for m in memorias[:2]:
            partes.append(f"  - [{m['tipo']}] {m['conteudo'][:100]}")
    gatilhos = _gatilhos_emocionais.get(usuario_id, [])[-3:]
    if gatilhos:
        partes.append(f"Gatilhos emocionais identificados: {', '.join(g['gatilho'][:30] for g in gatilhos)}")
    return " | ".join(partes) if partes else ""

def stats_memoria_episodica() -> dict:
    return {
        "usuarios_com_memoria": len(_memorias_episodicas),
        "total_episodios": sum(len(v) for v in _memorias_episodicas.values()),
        "usuarios_com_padroes": len(_padroes_usuario),
        "tipos_memoria": TIPOS_MEMORIA,
        "plugin": "memory_episodica v1.0"
    }
