"""
Plugin: FHIR e HL7 — Interoperabilidade em Saude
Categoria: saude
"""
VERSAO = "1.0"
NOME = "fhir_hl7"
DESCRICAO = "FHIR R4 e HL7 para interoperabilidade com sistemas de saude"
CATEGORIA = "saude"

import os
from datetime import datetime

FHIR_SERVER_URL = os.getenv("FHIR_SERVER_URL", "")

def criar_patient_fhir(usuario_id: int, nome: str, data_nascimento: str, genero: str = "unknown") -> dict:
    return {
        "resourceType": "Patient",
        "id": str(usuario_id),
        "identifier": [{"system": "https://emotion-platform-albert.onrender.com", "value": str(usuario_id)}],
        "name": [{"use": "official", "text": nome, "family": nome.split()[-1] if nome else "", "given": [nome.split()[0] if nome else ""]}],
        "gender": genero,
        "birthDate": data_nascimento,
        "active": True,
        "extension": [{"url": "http://emotion-platform/privacy", "valueBoolean": True}]
    }

def criar_observation_fhir(usuario_id: int, emocao: str, intensidade: int, score_ie: int = 0) -> dict:
    return {
        "resourceType": "Observation",
        "status": "final",
        "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "survey"}]}],
        "code": {"coding": [{"system": "http://loinc.org", "code": "72166-2", "display": "Emotional state"}]},
        "subject": {"reference": f"Patient/{usuario_id}"},
        "effectiveDateTime": datetime.now().isoformat(),
        "valueString": emocao,
        "component": [
            {"code": {"text": "Intensidade"}, "valueInteger": intensidade},
            {"code": {"text": "Score IE"}, "valueInteger": score_ie}
        ]
    }

def criar_condition_fhir(usuario_id: int, cid10: str, descricao: str, status: str = "active") -> dict:
    return {
        "resourceType": "Condition",
        "clinicalStatus": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-clinical", "code": status}]},
        "subject": {"reference": f"Patient/{usuario_id}"},
        "code": {"coding": [{"system": "http://hl7.org/fhir/sid/icd-10", "code": cid10}], "text": descricao},
        "recordedDate": datetime.now().strftime("%Y-%m-%d")
    }

async def enviar_para_fhir_server(recurso: dict, tipo: str) -> dict:
    if not FHIR_SERVER_URL:
        return {"armazenado": "local", "recurso": recurso}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(f"{FHIR_SERVER_URL}/{tipo}", json=recurso, headers={"Content-Type": "application/fhir+json"})
            return r.json()
    except Exception as e:
        return {"erro": str(e), "recurso_local": recurso}

def gerar_bundle_fhir(recursos: list) -> dict:
    return {
        "resourceType": "Bundle",
        "type": "collection",
        "timestamp": datetime.now().isoformat(),
        "total": len(recursos),
        "entry": [{"resource": r} for r in recursos]
    }

def stats_fhir() -> dict:
    return {
        "fhir_server": FHIR_SERVER_URL or "nao_configurado",
        "versao_fhir": "R4",
        "recursos_suportados": ["Patient", "Observation", "Condition", "Bundle"],
        "plugin": "fhir_hl7 v1.0"
    }
