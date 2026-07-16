"""
Plugin Loader — Emotion Intelligence Platform v21.0
Carrega todos os plugins automaticamente no startup.
"""
import importlib
import os
from pathlib import Path
from typing import List

PLUGINS_DIR = Path(__file__).parent
_plugins_carregados = []
_plugins_com_erro = []

def carregar_plugin(caminho_modulo: str) -> bool:
    try:
        modulo = importlib.import_module(caminho_modulo)
        _plugins_carregados.append({
            "modulo": caminho_modulo,
            "versao": getattr(modulo, "VERSAO", "1.0"),
            "nome": getattr(modulo, "NOME", caminho_modulo.split(".")[-1]),
        })
        return True
    except Exception as e:
        _plugins_com_erro.append({"modulo": caminho_modulo, "erro": str(e)})
        print(f"⚠️  Plugin {caminho_modulo}: {e}")
        return False

def carregar_todos_plugins(app=None) -> dict:
    total = 0
    sucesso = 0
    categorias = ["seguranca","sistemas","ia","saude","social","analytics","performance","monetizacao","integracao","frontend"]
    for categoria in categorias:
        pasta = PLUGINS_DIR / categoria
        if not pasta.exists():
            continue
        for arquivo in sorted(pasta.glob("*.py")):
            if arquivo.name.startswith("_"):
                continue
            modulo = f"plugins.{categoria}.{arquivo.stem}"
            total += 1
            if carregar_plugin(modulo):
                sucesso += 1
    print(f"✅ Plugins: {sucesso}/{total} carregados")
    return {"total": total, "sucesso": sucesso, "erros": len(_plugins_com_erro)}

def listar_plugins() -> List[dict]:
    return _plugins_carregados

def status_plugins() -> dict:
    return {
        "carregados": len(_plugins_carregados),
        "erros": len(_plugins_com_erro),
        "lista": _plugins_carregados,
        "erros_detalhes": _plugins_com_erro
    }
