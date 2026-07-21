"""PluginBase sem lifespan — evita RecursionError com muitos plugins"""
class PluginBase:
    name = "base"
    version = "1.0.0"
    description = ""
    category = "geral"

    def __init__(self, nome=None):
        pass

    def setup(self, app):
        """Registra rotas no app principal — SEM sub-apps FastAPI"""
        pass

    def health_check(self):
        return {"status": "healthy", "plugin": self.name}
