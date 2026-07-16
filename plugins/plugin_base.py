"""PluginBase Universal com DB integrado"""
from fastapi import FastAPI

class PluginBase:
    name = "base"
    version = "1.0.0"
    description = ""
    category = "geral"

    def __init__(self, nome=None):
        pass

    def setup(self, app: FastAPI):
        pass

    def health_check(self) -> dict:
        return {"status": "healthy", "plugin": self.name}

    def get_db(self, table_name: str = None):
        """Retorna instância de DB para o plugin"""
        from plugins.db_manager import SimpleDB
        table = table_name or f"plugin_{self.name.replace('-','_')}"
        return SimpleDB(table)
