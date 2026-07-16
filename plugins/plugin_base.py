"""
Plugin Base — todos os plugins herdam daqui
"""
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

VERSAO = "1.0"
NOME = "base"
DESCRICAO = "Plugin base"
AUTOR = "Albert Menezes"
CATEGORIA = "geral"
ATIVO = True

class PluginBase:
    def __init__(self, nome: str, versao: str = "1.0"):
        self.nome = nome
        self.versao = versao
        self.ativo = True
        self.endpoints = []
        self.middlewares = []

    def registrar_no_app(self, app: FastAPI):
        pass

    def status(self) -> dict:
        return {
            "nome": self.nome,
            "versao": self.versao,
            "ativo": self.ativo,
            "endpoints": len(self.endpoints)
        }
