"""
Plugin: Model Registry
Categoria: mlpipeline
Descrição: Registro centralizado de modelos ML com versionamento e staging
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from datetime import datetime
import uuid
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/model-registry", tags=["mlpipeline"])

registry_db = {}
versoes_db = {}
deployments_db = {}


class ModelRegistryPlugin(PluginBase):
    name = "model_registry"
    version = "1.0.0"
    description = "Registro centralizado de modelos ML com versionamento"
    category = "mlpipeline"

    def setup(self, app):
        app.include_router(router)
        logger.info(f"[{self.name}] Plugin carregado com sucesso")

    def health_check(self):
        return {
            "status": "healthy",
            "modelos_registrados": len(registry_db),
            "versoes_total": len(versoes_db),
            "em_producao": sum(1 for d in deployments_db.values() if d["stage"] == "producao")
        }


@router.post("/modelo/registrar")
async def registrar_modelo(
    nome: str,
    algoritmo: str,
    descricao: str = "",
    owner: str = "sistema",
    tags: list = None
):
    """Registra um novo modelo no registry"""
    modelo_id = str(uuid.uuid4())[:8]
    registry_db[modelo_id] = {
        "id": modelo_id,
        "nome": nome,
        "algoritmo": algoritmo,
        "descricao": descricao,
        "owner": owner,
        "tags": tags or [],
        "versoes": [],
        "versao_producao": None,
        "registrado_em": datetime.utcnow().isoformat()
    }
    return {"modelo_id": modelo_id, "nome": nome, "status": "registrado"}


@router.post("/modelo/{modelo_id}/versao")
async def registrar_versao(
    modelo_id: str,
    accuracy: float = 0.85,
    f1_score: float = 0.83,
    run_id: str = "",
    caminho: str = ""
):
    """Registra nova versão de um modelo"""
    if modelo_id not in registry_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")

    modelo = registry_db[modelo_id]
    versao_num = len(modelo["versoes"]) + 1
    versao_id = f"{modelo_id}_v{versao_num}"

    versao = {
        "id": versao_id,
        "modelo_id": modelo_id,
        "versao": versao_num,
        "run_id": run_id,
        "caminho": caminho or f"models/{modelo_id}/v{versao_num}",
        "metricas": {
            "accuracy": round(accuracy, 4),
            "f1_score": round(f1_score, 4)
        },
        "stage": "candidato",
        "registrado_em": datetime.utcnow().isoformat()
    }
    versoes_db[versao_id] = versao
    modelo["versoes"].append(versao_id)

    return {"versao_id": versao_id, "versao": versao_num, "stage": "candidato"}


@router.post("/versao/{versao_id}/promover")
async def promover_versao(versao_id: str, stage: str = "staging"):
    """Promove versão para staging ou produção"""
    if versao_id not in versoes_db:
        raise HTTPException(status_code=404, detail="Versão não encontrada")

    stages_validos = ["candidato", "staging", "producao", "arquivado"]
    if stage not in stages_validos:
        raise HTTPException(status_code=400, detail=f"Stages: {stages_validos}")

    versoes_db[versao_id]["stage"] = stage
    versoes_db[versao_id]["promovido_em"] = datetime.utcnow().isoformat()

    modelo_id = versoes_db[versao_id]["modelo_id"]

    # Se produção, atualizar modelo atual
    if stage == "producao":
        registry_db[modelo_id]["versao_producao"] = versao_id
        deploy_id = str(uuid.uuid4())[:8]
        deployments_db[deploy_id] = {
            "id": deploy_id,
            "modelo_id": modelo_id,
            "versao_id": versao_id,
            "stage": "producao",
            "deployed_at": datetime.utcnow().isoformat(),
            "status": "ativo"
        }

    return {
        "versao_id": versao_id,
        "novo_stage": stage,
        "status": "promovida"
    }


@router.get("/modelo/{modelo_id}")
async def detalhes_modelo(modelo_id: str):
    """Detalhes de um modelo"""
    if modelo_id not in registry_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")

    modelo = registry_db[modelo_id]
    versoes = [versoes_db[v] for v in modelo["versoes"] if v in versoes_db]

    return {
        "modelo": modelo,
        "versoes": versoes,
        "melhor_versao": max(versoes, key=lambda v: v["metricas"]["accuracy"]) if versoes else None
    }


@router.get("/modelos")
async def listar_modelos():
    """Lista todos os modelos no registry"""
    return {
        "total": len(registry_db),
        "modelos": [{
            "id": m["id"],
            "nome": m["nome"],
            "algoritmo": m["algoritmo"],
            "versoes": len(m["versoes"]),
            "em_producao": m["versao_producao"] is not None
        } for m in registry_db.values()]
    }


@router.get("/deployments")
async def listar_deployments():
    """Lista deployments ativos"""
    return {
        "total": len(deployments_db),
        "deployments": list(deployments_db.values())
    }


plugin = ModelRegistryPlugin()
