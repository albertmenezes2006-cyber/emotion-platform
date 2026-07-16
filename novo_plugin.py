#!/usr/bin/env python3
"""
Criador de novos plugins — Emotion Platform
Uso: python3 novo_plugin.py <categoria> <nome> <descricao>
Ex:  python3 novo_plugin.py ia claude "Claude API direto"
"""
import sys
import os
from pathlib import Path
from datetime import datetime

CATEGORIAS = [
    "seguranca","sistemas","ia","saude","social",
    "analytics","performance","monetizacao","integracao","frontend"
]

TEMPLATE = """"""
Plugin: {descricao}
Categoria: {categoria}
Criado: {data}
"""
from fastapi import Request, Depends
from fastapi.responses import JSONResponse

VERSAO = "1.0"
NOME = "{nome}"
DESCRICAO = "{descricao}"
CATEGORIA = "{categoria}"
ATIVO = True

# ════════════════════════════════════════
# IMPLEMENTAÇÃO DO PLUGIN
# ════════════════════════════════════════

# Configurações
{NOME_UPPER}_CONFIG = {{
    "ativo": True,
    "versao": "1.0",
}}

# Funções principais
def {nome}_init():
    """Inicializa o plugin"""
    print(f"✅ Plugin {nome} inicializado")

# Endpoint de exemplo
# @app.get("/api/{nome}/status")
# async def {nome}_status_ep(request: Request):
#     return JSONResponse({{"ok": True, "plugin": "{nome}"}})

# ════════════════════════════════════════
# FIM DO PLUGIN
# ════════════════════════════════════════
"""

def criar_plugin(categoria, nome, descricao):
    if categoria not in CATEGORIAS:
        print(f"❌ Categoria invalida. Use: {CATEGORIAS}")
        return False

    pasta = Path(f"plugins/{categoria}")
    pasta.mkdir(exist_ok=True)

    arquivo = pasta / f"{nome}.py"
    if arquivo.exists():
        print(f"⚠️  Plugin ja existe: {arquivo}")
        return False

    conteudo = TEMPLATE.format(
        nome=nome,
        descricao=descricao,
        categoria=categoria,
        data=datetime.now().strftime("%d/%m/%Y"),
        NOME_UPPER=nome.upper()
    )

    arquivo.write_text(conteudo)
    print(f"✅ Plugin criado: {arquivo}")
    print(f"   Edite o arquivo e adicione sua implementacao!")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    categoria = sys.argv[1]
    nome = sys.argv[2]
    descricao = sys.argv[3] if len(sys.argv) > 3 else nome
    criar_plugin(categoria, nome, descricao)
