"""
Testes Psicológicos Validados
Bloco 11 — PHQ-9, GAD-7, DASS-21, PCL-5
"""
PHQ9_PERGUNTAS = [
    "Pouco interesse ou prazer em fazer as coisas",
    "Se sentindo mal, deprimido ou sem perspectiva",
    "Dificuldade para adormecer, continuando dormindo ou dormindo demais",
    "Se sentindo cansado ou com pouca energia",
    "Falta de apetite ou comendo demais",
    "Se sentindo mal consigo mesmo",
    "Dificuldade de concentração",
    "Lentidão ou agitação excessiva",
    "Pensamentos de se machucar"
]

GAD7_PERGUNTAS = [
    "Se sentindo nervoso, ansioso ou no limite",
    "Não conseguindo parar ou controlar preocupações",
    "Preocupando-se muito com coisas diferentes",
    "Dificuldade para relaxar",
    "Tão agitado que fica difícil ficar parado",
    "Ficando facilmente irritado",
    "Sentindo medo de que algo ruim possa acontecer"
]

def calcular_phq9(respostas: list) -> dict:
    total = sum(respostas)
    if total <= 4: nivel = "Mínimo"; cor = "verde"
    elif total <= 9: nivel = "Leve"; cor = "amarelo"
    elif total <= 14: nivel = "Moderado"; cor = "laranja"
    elif total <= 19: nivel = "Moderadamente severo"; cor = "vermelho"
    else: nivel = "Severo"; cor = "vermelho_escuro"
    return {"total": total, "nivel": nivel, "cor": cor, "max": 27}

def calcular_gad7(respostas: list) -> dict:
    total = sum(respostas)
    if total <= 4: nivel = "Mínimo"; cor = "verde"
    elif total <= 9: nivel = "Leve"; cor = "amarelo"
    elif total <= 14: nivel = "Moderado"; cor = "laranja"
    else: nivel = "Severo"; cor = "vermelho"
    return {"total": total, "nivel": nivel, "cor": cor, "max": 21}

VERSAO = "21.0"
MODULO = "testes_psicologicos"
