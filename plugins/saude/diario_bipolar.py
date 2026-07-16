"""
Plugin: Diario de Humor para Transtorno Bipolar
Categoria: saude
"""
VERSAO = "1.0"
NOME = "diario_bipolar"
DESCRICAO = "Rastreamento de humor para bipolaridade — escala de mania e depressao"
CATEGORIA = "saude"

from datetime import datetime, timedelta
from collections import defaultdict

_registros_bipolar = defaultdict(list)

ESCALA_HUMOR = {
    -4: "Depressao grave",
    -3: "Depressao moderada",
    -2: "Depressao leve",
    -1: "Ligeiramente deprimido",
     0: "Equilibrado/Eutimico",
     1: "Ligeiramente elevado",
     2: "Hipomania leve",
     3: "Hipomania moderada",
     4: "Mania",
}

FATORES_RASTREAMENTO = [
    "sono_horas", "sono_qualidade", "energia", "irritabilidade",
    "pensamentos_acelerados", "impulsividade", "sociabilidade",
    "produtividade", "apetite", "medicacao_tomada"
]

def registrar_humor_bipolar(usuario_id: int, escala: int, fatores: dict, notas: str = "") -> dict:
    escala = max(-4, min(4, escala))
    registro = {
        "data": datetime.now().strftime("%Y-%m-%d"),
        "hora": datetime.now().strftime("%H:%M"),
        "escala": escala,
        "descricao": ESCALA_HUMOR.get(escala, "Indefinido"),
        "fatores": fatores,
        "notas": notas[:500],
        "ts": datetime.now().isoformat()
    }
    _registros_bipolar[usuario_id].append(registro)
    alertas = _verificar_alertas_bipolar(usuario_id, escala)
    return {"registro": registro, "alertas": alertas}

def _verificar_alertas_bipolar(usuario_id: int, escala_atual: int) -> list:
    alertas = []
    historico = _registros_bipolar.get(usuario_id, [])
    if abs(escala_atual) >= 3:
        alertas.append({"tipo": "escala_extrema", "mensagem": f"Humor muito {'elevado' if escala_atual > 0 else 'deprimido'}. Contate seu profissional.", "urgencia": "alta"})
    if len(historico) >= 3:
        ultimos = [r["escala"] for r in historico[-3:]]
        if all(s >= 2 for s in ultimos):
            alertas.append({"tipo": "tendencia_mania", "mensagem": "3 dias consecutivos com humor elevado", "urgencia": "media"})
        elif all(s <= -2 for s in ultimos):
            alertas.append({"tipo": "tendencia_depressao", "mensagem": "3 dias consecutivos com humor deprimido", "urgencia": "media"})
    return alertas

def analisar_padrao_bipolar(usuario_id: int, dias: int = 30) -> dict:
    registros = _registros_bipolar.get(usuario_id, [])
    if len(registros) < 7:
        return {"erro": f"Precisa de 7+ registros. Tem {len(registros)}"}
    escalas = [r["escala"] for r in registros[-dias:]]
    media = sum(escalas) / len(escalas)
    amplitude = max(escalas) - min(escalas)
    episodios_mania = sum(1 for s in escalas if s >= 3)
    episodios_depressao = sum(1 for s in escalas if s <= -3)
    return {
        "media_humor": round(media, 2),
        "amplitude": amplitude,
        "episodios_mania": episodios_mania,
        "episodios_depressao": episodios_depressao,
        "estabilidade": "boa" if amplitude <= 3 else "moderada" if amplitude <= 5 else "instavel",
        "total_registros": len(escalas),
        "recomendacao": "Continue rastreando e compartilhe com seu psiquiatra"
    }

def stats_diario_bipolar() -> dict:
    return {
        "usuarios_rastreando": len(_registros_bipolar),
        "total_registros": sum(len(v) for v in _registros_bipolar.values()),
        "escala_usada": "(-4 depressao grave) a (+4 mania)",
        "plugin": "diario_bipolar v1.0"
    }
