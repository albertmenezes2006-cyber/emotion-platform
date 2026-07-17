#!/usr/bin/env python3
"""Exportacao de dados em multiplos formatos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from plugins.plugin_base import PluginBase
from datetime import datetime
import json, csv, io

router = APIRouter(prefix="/api/v1/exportar", tags=["Exportação"])

DADOS_EXEMPLO = [
    {"data": "2026-07-01", "phq9": 8, "gad7": 6, "humor": 6, "nota": "Semana difícil"},
    {"data": "2026-07-08", "phq9": 6, "gad7": 5, "humor": 7, "nota": "Melhorando"},
    {"data": "2026-07-15", "phq9": 4, "gad7": 3, "humor": 8, "nota": "Muito melhor"},
]

@router.get("/csv/{user_id}")
async def exportar_csv(user_id: str):
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["data","phq9","gad7","humor","nota"])
    writer.writeheader()
    writer.writerows(DADOS_EXEMPLO)
    content = output.getvalue()
    return Response(content=content, media_type="text/csv",
                    headers={"Content-Disposition": f"attachment; filename=emotion_dados_{user_id}.csv"})

@router.get("/json/{user_id}")
async def exportar_json(user_id: str):
    dados = {"usuario": user_id, "exportado_em": datetime.utcnow().isoformat(),
             "plataforma": "Emotion Intelligence Platform", "dados": DADOS_EXEMPLO}
    content = json.dumps(dados, ensure_ascii=False, indent=2)
    return Response(content=content, media_type="application/json",
                    headers={"Content-Disposition": f"attachment; filename=emotion_{user_id}.json"})

@router.get("/formatos")
async def formatos_disponiveis():
    return JSONResponse({"formatos": ["csv", "json"],
                         "endpoints": {
                             "csv": "/api/v1/exportar/csv/{user_id}",
                             "json": "/api/v1/exportar/json/{user_id}"
                         }})

class ExportacaoPlugin(PluginBase):
    name = "exportacao_dados"
    def setup(self, app): app.include_router(router)
plugin = ExportacaoPlugin()
