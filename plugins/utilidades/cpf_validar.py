#!/usr/bin/env python3
"""Validacao de CPF"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import re

router = APIRouter(prefix="/api/v1/cpf", tags=["CPF"])

def validar(cpf: str) -> bool:
    cpf = re.sub(r"[^0-9]", "", cpf)
    if len(cpf) != 11 or len(set(cpf)) == 1: return False
    for i in range(9, 11):
        s = sum(int(cpf[j]) * (i+1-j) for j in range(i))
        d = (s * 10 % 11) % 10
        if d != int(cpf[i]): return False
    return True

@router.get("/validar/{cpf}")
async def validar_cpf(cpf: str):
    v = validar(cpf)
    return JSONResponse({"valido": v, "cpf": cpf, "msg": "CPF valido" if v else "CPF invalido"})

class CPFPlugin(PluginBase):
    name = "cpf_validar"
    def setup(self, app): app.include_router(router)
plugin = CPFPlugin()
