"""
Plugin: WebRTC Video Chamada
Categoria: social
"""
VERSAO = "1.0"
NOME = "webrtc_video"
DESCRICAO = "Video chamadas via WebRTC para sessoes terapeuticas online"
CATEGORIA = "social"

import os
from datetime import datetime, timedelta
from collections import defaultdict

DAILY_API_KEY = os.getenv("DAILY_API_KEY", "")
DAILY_API_URL = "https://api.daily.co/v1"
JITSI_DOMAIN = os.getenv("JITSI_DOMAIN", "meet.jit.si")

_salas_ativas = {}
_historico_chamadas = defaultdict(list)

async def criar_sala_daily(nome_sala: str = None, duracao_minutos: int = 60) -> dict:
    if not DAILY_API_KEY:
        return _criar_sala_jitsi(nome_sala)
    try:
        import httpx, secrets
        sala = nome_sala or f"terapia-{secrets.token_hex(6)}"
        expira = int((datetime.now() + timedelta(minutes=duracao_minutos)).timestamp())
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"{DAILY_API_URL}/rooms",
                headers={"Authorization": f"Bearer {DAILY_API_KEY}", "Content-Type": "application/json"},
                json={"name": sala, "privacy": "private", "properties": {"exp": expira, "max_participants": 2, "enable_chat": True, "enable_knocking": True}}
            )
            data = r.json()
            _salas_ativas[sala] = {"url": data.get("url",""), "criado_em": datetime.now().isoformat(), "expira_em": expira}
            return {"sala": sala, "url": data.get("url",""), "provider": "daily.co"}
    except Exception as e:
        return _criar_sala_jitsi(nome_sala)

def _criar_sala_jitsi(nome_sala: str = None) -> dict:
    import secrets
    sala = nome_sala or f"emotion-terapia-{secrets.token_hex(6)}"
    url = f"https://{JITSI_DOMAIN}/{sala}"
    _salas_ativas[sala] = {"url": url, "criado_em": datetime.now().isoformat(), "provider": "jitsi"}
    return {"sala": sala, "url": url, "provider": "jitsi_meet"}

async def criar_token_participante(sala: str, usuario_id: int, role: str = "attendee") -> dict:
    if not DAILY_API_KEY:
        return {"token": f"jitsi_{sala}", "sala": sala, "url": f"https://{JITSI_DOMAIN}/{sala}"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"{DAILY_API_URL}/meeting-tokens",
                headers={"Authorization": f"Bearer {DAILY_API_KEY}", "Content-Type": "application/json"},
                json={"properties": {"room_name": sala, "is_owner": role == "therapist", "user_id": str(usuario_id), "exp": int((datetime.now() + timedelta(hours=2)).timestamp())}}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

def registrar_chamada(usuario_id: int, prof_id: int, sala: str, duracao_min: float):
    _historico_chamadas[usuario_id].append({
        "prof_id": prof_id, "sala": sala,
        "duracao_min": duracao_min, "ts": datetime.now().isoformat()
    })

def stats_webrtc() -> dict:
    return {
        "provider": "daily.co" if DAILY_API_KEY else "jitsi_meet",
        "salas_ativas": len(_salas_ativas),
        "total_chamadas": sum(len(v) for v in _historico_chamadas.values()),
        "plugin": "webrtc_video v1.0"
    }
