"""
Métricas — Emotion Platform v21.0
Coleta dados de performance e uso em tempo real
"""
import psutil
import os
from datetime import datetime
from collections import defaultdict, deque
from typing import Dict

class MetricasPlataforma:
    def __init__(self):
        self.inicio = datetime.now()
        self.requests_total = 0
        self.requests_erro = 0
        self.requests_por_rota: Dict[str, int] = defaultdict(int)
        self.tempos_resposta: deque = deque(maxlen=1000)
        self.emocoes_detectadas: Dict[str, int] = defaultdict(int)
        self.ia_chamadas: Dict[str, int] = defaultdict(int)
        self.ia_erros: Dict[str, int] = defaultdict(int)
        self.usuarios_ativos: set = set()
        self.analises_hora: deque = deque(maxlen=24)
        self.ultima_atualizacao = datetime.now()

    def registrar_request(self, rota: str, status: int, duracao_ms: float, usuario_id: int = None):
        self.requests_total += 1
        self.requests_por_rota[rota] += 1
        self.tempos_resposta.append(duracao_ms)
        if status >= 400:
            self.requests_erro += 1
        if usuario_id:
            self.usuarios_ativos.add(usuario_id)

    def registrar_emocao(self, emocao: str):
        self.emocoes_detectadas[emocao] += 1

    def registrar_ia(self, modelo: str, sucesso: bool):
        self.ia_chamadas[modelo] += 1
        if not sucesso:
            self.ia_erros[modelo] += 1

    def tempo_medio_resposta(self) -> float:
        if not self.tempos_resposta:
            return 0.0
        return sum(self.tempos_resposta) / len(self.tempos_resposta)

    def taxa_erro(self) -> float:
        if self.requests_total == 0:
            return 0.0
        return round((self.requests_erro / self.requests_total) * 100, 2)

    def uptime_horas(self) -> float:
        delta = datetime.now() - self.inicio
        return round(delta.total_seconds() / 3600, 2)

    def cpu_percent(self) -> float:
        return psutil.cpu_percent(interval=0.1)

    def memoria_mb(self) -> float:
        proc = psutil.Process(os.getpid())
        return round(proc.memory_info().rss / 1024 / 1024, 1)

    def top_emocoes(self, n: int = 5) -> list:
        return sorted(
            self.emocoes_detectadas.items(),
            key=lambda x: x[1],
            reverse=True
        )[:n]

    def resumo(self) -> dict:
        return {
            "uptime_horas": self.uptime_horas(),
            "requests_total": self.requests_total,
            "requests_erro": self.requests_erro,
            "taxa_erro_pct": self.taxa_erro(),
            "tempo_medio_ms": round(self.tempo_medio_resposta(), 1),
            "usuarios_ativos_sessao": len(self.usuarios_ativos),
            "cpu_pct": self.cpu_percent(),
            "memoria_mb": self.memoria_mb(),
            "top_emocoes": self.top_emocoes(),
            "ia_chamadas": dict(self.ia_chamadas),
            "ia_erros": dict(self.ia_erros),
            "atualizado_em": datetime.now().strftime("%d/%m %H:%M:%S")
        }

# Instância global
metricas = MetricasPlataforma()
