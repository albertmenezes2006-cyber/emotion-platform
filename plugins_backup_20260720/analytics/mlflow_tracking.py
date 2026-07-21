"""
Plugin: MLflow — Tracking de Experimentos ML
Categoria: analytics
"""
VERSAO = "1.0"
NOME = "mlflow_tracking"
DESCRICAO = "MLflow para tracking de experimentos e modelos ML"
CATEGORIA = "analytics"

import os
from datetime import datetime
from collections import defaultdict

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "")
_experimentos_locais = defaultdict(list)
_runs_ativos = {}

def iniciar_run(experimento: str, params: dict = None) -> str:
    if MLFLOW_TRACKING_URI:
        try:
            import mlflow
            mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
            mlflow.set_experiment(experimento)
            run = mlflow.start_run()
            if params:
                mlflow.log_params(params)
            run_id = run.info.run_id
            _runs_ativos[run_id] = {"experimento": experimento, "inicio": datetime.now().isoformat()}
            return run_id
        except Exception:
            pass
    run_id = f"local_{len(_experimentos_locais[experimento])}"
    _experimentos_locais[experimento].append({"run_id": run_id, "params": params or {}, "metricas": {}, "inicio": datetime.now().isoformat()})
    _runs_ativos[run_id] = {"experimento": experimento, "local": True}
    return run_id

def logar_metrica(run_id: str, nome: str, valor: float, step: int = 0):
    if MLFLOW_TRACKING_URI and not _runs_ativos.get(run_id, {}).get("local"):
        try:
            import mlflow
            mlflow.log_metric(nome, valor, step=step)
            return
        except Exception:
            pass
    exp = _runs_ativos.get(run_id, {}).get("experimento", "default")
    for run in _experimentos_locais.get(exp, []):
        if run["run_id"] == run_id:
            run["metricas"][nome] = valor
            break

def finalizar_run(run_id: str):
    if MLFLOW_TRACKING_URI and not _runs_ativos.get(run_id, {}).get("local"):
        try:
            import mlflow
            mlflow.end_run()
        except Exception:
            pass
    _runs_ativos.pop(run_id, None)

def listar_experimentos() -> dict:
    return {exp: len(runs) for exp, runs in _experimentos_locais.items()}

def stats_mlflow() -> dict:
    return {
        "tracking_uri": MLFLOW_TRACKING_URI or "local",
        "experimentos": len(_experimentos_locais),
        "runs_ativos": len(_runs_ativos),
        "plugin": "mlflow_tracking v1.0"
    }
