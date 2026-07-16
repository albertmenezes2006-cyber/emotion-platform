"""Testes automáticos — Emotion Platform v21.0"""
import py_compile
import json
from pathlib import Path

BASE = Path(__file__).parent.parent

def test_sintaxe():
    py_compile.compile(str(BASE/"main.py"), doraise=True)

def test_main_existe():
    assert (BASE/"main.py").exists()

def test_tamanho_minimo():
    assert (BASE/"main.py").stat().st_size > 100_000

def test_templates_existem():
    assert (BASE/"templates").is_dir()
    htmls = list((BASE/"templates").glob("*.html"))
    assert len(htmls) >= 10, f"Poucos templates: {len(htmls)}"

def test_requirements():
    assert (BASE/"requirements.txt").exists()

def test_modulos():
    assert (BASE/"modules").is_dir()
    assert (BASE/"modules"/"sofia.py").exists()
    assert (BASE/"modules"/"emocoes.py").exists()

def test_validar_existe():
    assert (BASE/"validar.py").exists()

def test_autopilot_existe():
    assert (BASE/"autopilot.py").exists()

def test_makefile_existe():
    assert (BASE/"Makefile").exists()

def test_blocos_fila():
    fila_path = BASE/"blocos_fila.json"
    assert fila_path.exists()
    with open(fila_path) as f:
        fila = json.load(f)
    assert len(fila) >= 10

def test_funcoes_criticas():
    with open(BASE/"main.py") as f:
        c = f.read()
    for fn in ["verificar_token","obter_perfil_sofia","detectar_emocao","detectar_idioma"]:
        assert fn in c, f"Função {fn} não encontrada"

def test_endpoints_criticos():
    with open(BASE/"main.py") as f:
        c = f.read()
    for ep in ['"/health"','"/dashboard"','"/chat"','"/terapia"']:
        assert ep in c, f"Endpoint {ep} não encontrado"

def test_sem_duplicatas_criticas():
    with open(BASE/"main.py") as f:
        c = f.read()
    for fn in ["def verificar_token(","def obter_perfil_sofia("]:
        count = c.count(fn)
        assert count == 1, f"Duplicata: {fn} aparece {count}x"
