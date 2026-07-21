"""
Plugin: Google APIs — Calendar, Drive, Sheets, Sign In
Categoria: integracao
"""
VERSAO = "1.0"
NOME = "google_apis"
DESCRICAO = "Google Calendar, Drive, Sheets e Sign In com OAuth2"
CATEGORIA = "integracao"

import os
from datetime import datetime, timedelta

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")
GOOGLE_CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "primary")

async def google_obter_token(code: str, redirect_uri: str) -> dict:
    if not all([GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET]):
        return {"erro": "Google nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://oauth2.googleapis.com/token",
                data={"code": code, "client_id": GOOGLE_CLIENT_ID, "client_secret": GOOGLE_CLIENT_SECRET, "redirect_uri": redirect_uri, "grant_type": "authorization_code"}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def google_obter_perfil(access_token: str) -> dict:
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get("https://www.googleapis.com/oauth2/v2/userinfo", headers={"Authorization": f"Bearer {access_token}"})
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def google_criar_evento_calendar(access_token: str, titulo: str, inicio: str, fim: str, descricao: str = "") -> dict:
    try:
        import httpx
        evento = {
            "summary": titulo,
            "description": descricao,
            "start": {"dateTime": inicio, "timeZone": "America/Sao_Paulo"},
            "end": {"dateTime": fim, "timeZone": "America/Sao_Paulo"},
            "reminders": {"useDefault": False, "overrides": [{"method": "popup", "minutes": 30}]}
        }
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"https://www.googleapis.com/calendar/v3/calendars/{GOOGLE_CALENDAR_ID}/events",
                headers={"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
                json=evento
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def google_listar_eventos(access_token: str, dias: int = 7) -> list:
    try:
        import httpx
        agora = datetime.now().isoformat() + "Z"
        futuro = (datetime.now() + timedelta(days=dias)).isoformat() + "Z"
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                f"https://www.googleapis.com/calendar/v3/calendars/{GOOGLE_CALENDAR_ID}/events",
                headers={"Authorization": f"Bearer {access_token}"},
                params={"timeMin": agora, "timeMax": futuro, "singleEvents": True, "orderBy": "startTime"}
            )
            return r.json().get("items", [])
    except Exception:
        return []

async def google_upload_drive(access_token: str, nome_arquivo: str, conteudo: bytes, mime_type: str = "application/pdf") -> dict:
    try:
        import httpx
        metadata = {"name": nome_arquivo, "mimeType": mime_type}
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                headers={"Authorization": f"Bearer {access_token}"},
                files={"metadata": (None, str(metadata), "application/json"), "file": (nome_arquivo, conteudo, mime_type)}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

def url_google_login(redirect_uri: str, state: str = "") -> str:
    if not GOOGLE_CLIENT_ID:
        return ""
    scopes = "openid email profile https://www.googleapis.com/auth/calendar.events"
    return (f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}"
            f"&redirect_uri={redirect_uri}&response_type=code&scope={scopes}&state={state}&access_type=offline")

def stats_google_apis() -> dict:
    return {"configurado": bool(GOOGLE_CLIENT_ID), "apis": ["calendar","drive","oauth2","userinfo"], "plugin": "google_apis v1.0"}
