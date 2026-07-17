#!/usr/bin/env python3
"""Validacao de CRP de psicologos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import re

router = APIRouter(prefix="/api/v1/crp", tags=["CRP"])

def validar_formato_crp(crp: str) -> dict:
    """Valida formato do CRP brasileiro"""
    crp = crp.strip().upper()
    padrao = r"^(\d{2})/(\d{4,6})$"
    match = re.match(padrao, crp)
    if not match:
        return {"valido": False, "erro": "Formato invalido. Use: 06/123456"}
    regiao = match.group(1)
    numero = match.group(2)
    regioes = {
        "01": "DF", "02": "GO", "03": "SP", "04": "MG",
        "05": "ES", "06": "RJ", "07": "RS", "08": "SC",
        "09": "PR", "10": "BA", "11": "SE", "12": "AL",
        "13": "PE", "14": "PB", "15": "RN", "16": "CE",
        "17": "PI", "18": "MA", "19": "PA", "20": "AM",
        "21": "RR", "22": "AP", "23": "AC", "24": "MT",
        "25": "MS", "26": "RO", "27": "TO"
    }
    estado = regioes.get(regiao, "Desconhecido")
    return {
        "valido": True,
        "crp": crp,
        "regiao": regiao,
        "numero": numero,
        "estado": estado,
        "link_cfp": f"https://cadastro.cfp.org.br/",
        "msg": f"CRP {crp} — Regiao {regiao} ({estado})"
    }

@router.get("/validar/{crp}")
async def validar_crp(crp: str):
    return JSONResponse(validar_formato_crp(crp))

@router.get("/regioes")
async def listar_regioes():
    return JSONResponse({
        "regioes": {
            "03": "Sao Paulo", "06": "Rio de Janeiro",
            "08": "Santa Catarina", "09": "Parana",
            "07": "Rio Grande do Sul", "04": "Minas Gerais",
            "10": "Bahia", "01": "Distrito Federal"
        }
    })

class CRPPlugin(PluginBase):
    name = "validacao_crp"
    def setup(self, app):
        app.include_router(router)

plugin = CRPPlugin()
