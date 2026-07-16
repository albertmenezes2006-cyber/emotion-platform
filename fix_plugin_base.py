#!/usr/bin/env python3
"""Corrige plugin_base.py para aceitar plugins com e sem __init__"""
import os

def w(path, content):
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ {path}")

# ══════════════════════════════════════════════
# 1. NOVO plugin_base.py — compatível com TODOS
# ══════════════════════════════════════════════
w("plugins/plugin_base.py", '''"""
PluginBase Universal — compatível com todos os estilos de plugin
"""
from fastapi import FastAPI

class PluginBase:
    name: str = "base"
    version: str = "1.0.0"
    description: str = ""
    category: str = "geral"

    def __init__(self, nome=None):
        # Aceita chamada com ou sem argumento
        if nome is not None and not hasattr(self.__class__, "_nome_set"):
            self.name = nome

    def setup(self, app: FastAPI):
        pass

    def health_check(self) -> dict:
        return {"status": "healthy", "plugin": self.name}

    def __repr__(self):
        return f"<Plugin {self.category}/{self.name} v{self.version}>"
''')

# ══════════════════════════════════════════════
# 2. NOVO loader.py — robusto, ignora erros
# ══════════════════════════════════════════════
w("plugins/loader.py", '''"""
Loader Universal — carrega TODOS os plugins automaticamente
Ignora erros individuais sem parar o sistema
"""
import os, importlib, logging
from pathlib import Path

logger = logging.getLogger(__name__)

def load_all_plugins(app):
    plugins_dir = Path(__file__).parent
    total_ok = 0
    total_err = 0
    skip_files = {"__init__.py", "loader.py", "plugin_base.py"}
    skip_dirs = {"__pycache__"}

    for cat_dir in sorted(plugins_dir.iterdir()):
        if not cat_dir.is_dir(): continue
        if cat_dir.name in skip_dirs: continue
        if cat_dir.name.startswith("_"): continue

        for plugin_file in sorted(cat_dir.glob("*.py")):
            if plugin_file.name in skip_files: continue
            if plugin_file.name.startswith("_"): continue

            module_path = f"plugins.{cat_dir.name}.{plugin_file.stem}"
            try:
                mod = importlib.import_module(module_path)
                if hasattr(mod, "plugin"):
                    plug = mod.plugin
                    if hasattr(plug, "setup"):
                        plug.setup(app)
                        total_ok += 1
                        logger.debug(f"[OK] {module_path}")
                    else:
                        total_err += 1
                        logger.warning(f"[SEM SETUP] {module_path}")
                else:
                    # Tenta encontrar instância da classe
                    loaded = False
                    for attr_name in dir(mod):
                        attr = getattr(mod, attr_name)
                        if (isinstance(attr, object) and
                            hasattr(attr, "setup") and
                            hasattr(attr, "name") and
                            attr_name != "PluginBase"):
                            try:
                                attr.setup(app)
                                total_ok += 1
                                loaded = True
                                break
                            except Exception:
                                pass
                    if not loaded:
                        total_err += 1
                        logger.debug(f"[SEM PLUGIN] {module_path}")
            except Exception as e:
                total_err += 1
                logger.warning(f"[ERRO] {module_path}: {e}")

    logger.info(f"✅ Plugins: {total_ok} carregados, {total_err} ignorados")
    return total_ok, total_err
''')

# ══════════════════════════════════════════════
# 3. Verificar plugin_base atual para entender o problema
# ══════════════════════════════════════════════
print("\n=== VERIFICANDO plugin_base.py original ===")
try:
    with open("plugins/plugin_base.py") as f:
        print(f.read()[:500])
except:
    print("Não encontrado")
