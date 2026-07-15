"""
Metas Terapêuticas — Bloco 12
"""
from datetime import datetime, timedelta

def criar_meta(titulo: str, tipo: str, prazo_dias: int = 30) -> dict:
    return {
        "titulo": titulo,
        "tipo": tipo,
        "criada_em": datetime.now().isoformat(),
        "prazo": (datetime.now() + timedelta(days=prazo_dias)).isoformat(),
        "progresso": 0,
        "concluida": False,
        "marcos": []
    }

TIPOS_META = [
    "bem_estar", "ansiedade", "depressao",
    "relacionamentos", "autoestima", "produtividade",
    "sono", "exercicio", "alimentacao", "social"
]

VERSAO = "21.0"
MODULO = "metas"
