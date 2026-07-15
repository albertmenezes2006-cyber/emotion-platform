import py_compile
import os

def test_sintaxe_main():
    """Garante que main.py compila sem erro."""
    try:
        py_compile.compile("main.py", doraise=True)
        assert True
    except py_compile.PyCompileError as e:
        assert False, f"Erro de sintaxe: {e}"

def test_main_existe():
    assert os.path.exists("main.py")

def test_templates_existem():
    assert os.path.isdir("templates")

def test_requirements_existe():
    assert os.path.exists("requirements.txt")
