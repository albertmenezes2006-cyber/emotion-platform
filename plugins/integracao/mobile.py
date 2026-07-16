"""
Plugin: Q7 Firebase+OneSignal
Categoria: integracao
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "mobile"
DESCRICAO = "Q7 Firebase+OneSignal"
CATEGORIA = "integracao"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q7 — MOBILE E NOTIFICAÇÕES (5 implementações)
# ═══════════════════════════════════════════════════════════════════════

FIREBASE_SERVER_KEY = _os_s10.getenv("FIREBASE_SERVER_KEY", "")
ONESIGNAL_APP_ID = _os_s10.getenv("ONESIGNAL_APP_ID", "")
ONESIGNAL_API_KEY = _os_s10.getenv("ONESIGNAL_API_KEY", "")

# ── Q7.1 Firebase Cloud Messaging
async def firebase_enviar_push(token_dispositivo: str, titulo: str, corpo: str, dados: dict = None) -> bool:
    if not FIREBASE_SERVER_KEY:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://fcm.googleapis.com/fcm/send",
                headers={"Authorization": f"key={FIREBASE_SERVER_KEY}", "Content-Type": "application/json"},
                json={
                    "to": token_dispositivo,
                    "notification": {"title": titulo, "body": corpo, "sound": "default"},
                    "data": dados or {},
                    "priority": "high"
                }
            )
            result = r.json()
            return result.get("success", 0) > 0
    except Exception:
        return False

async def firebase_enviar_topico(topico: str, titulo: str, corpo: str) -> bool:
    if not FIREBASE_SERVER_KEY:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://fcm.googleapis.com/fcm/send",
                headers={"Authorization": f"key={FIREBASE_SERVER_KEY}", "Content-Type": "application/json"},
                json={"to": f"/topics/{topico}", "notification": {"title": titulo, "body": corpo}}
            )
            return r.status_code == 200
    except Exception:
        return False

# ── Q7.2 OneSignal
async def onesignal_enviar(usuario_ids: list, titulo: str, mensagem: str, url: str = "/") -> bool:
    if not all([ONESIGNAL_APP_ID, ONESIGNAL_API_KEY]):
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://onesignal.com/api/v1/notifications",
                headers={"Authorization": f"Basic {ONESIGNAL_API_KEY}", "Content-Type": "application/json"},
                json={
                    "app_id": ONESIGNAL_APP_ID,
                    "include_external_user_ids": [str(uid) for uid in usuario_ids],
                    "headings": {"pt": titulo, "en": titulo},
                    "contents": {"pt": mensagem, "en": mensagem},
                    "url": url,
                    "web_url": url,
                }
            )
            return r.status_code == 200
    except Exception:
        return False

async def onesignal_lembrete_diario(usuario_ids: list) -> bool:
    return await onesignal_enviar(
        usuario_ids,
        "Como voce esta hoje? 🧠",
        "Registre sua emocao e acompanhe sua jornada emocional",
        "/dashboard"
    )

# ── Q7.3 Discord Bot Avançado
DISCORD_BOT_TOKEN = _os_s10.getenv("DISCORD_BOT_TOKEN", "")
DISCORD_CHANNEL_ID = _os_s10.getenv("DISCORD_CHANNEL_ID", "")

async def discord_enviar_mensagem(mensagem: str, canal_id: str = None) -> bool:
    if not DISCORD_BOT_TOKEN:
        return False
    try:
        import httpx
        canal = canal_id or DISCORD_CHANNEL_ID
        if not canal:
            return False
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"https://discord.com/api/v10/channels/{canal}/messages",
                headers={"Authorization": f"Bot {DISCORD_BOT_TOKEN}", "Content-Type": "application/json"},
                json={"content": mensagem[:2000]}
            )
            return r.status_code == 200
    except Exception:
        return False

async def discord_embed_analise(emocao: str, score: int, usuario: str) -> bool:
    if not DISCORD_BOT_TOKEN or not DISCORD_CHANNEL_ID:
        return False
    try:
        import httpx
        cores = {"alegria": 0xFFD700, "tristeza": 0x4169E1, "raiva": 0xDC143C, "neutro": 0x808080}
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages",
                headers={"Authorization": f"Bot {DISCORD_BOT_TOKEN}", "Content-Type": "application/json"},
                json={
                    "embeds": [{
                        "title": f"Nova analise — {usuario}",
                        "description": f"Emocao: **{emocao}** | Score IE: **{score}**",
                        "color": cores.get(emocao, 0x6c63ff),
                        "footer": {"text": "Emotion Intelligence Platform"}
                    }]
                }
            )
            return r.status_code == 200
    except Exception:
        return False

# ── Q7.4 Apple Push (APNS)
APNS_KEY = _os_s10.getenv("APNS_KEY", "")
APNS_KEY_ID = _os_s10.getenv("APNS_KEY_ID", "")
APNS_TEAM_ID = _os_s10.getenv("APNS_TEAM_ID", "")
APNS_BUNDLE_ID = _os_s10.getenv("APNS_BUNDLE_ID", "com.emotion.platform")

async def apns_enviar(device_token: str, titulo: str, corpo: str, badge: int = 1) -> bool:
    if not all([APNS_KEY, APNS_KEY_ID, APNS_TEAM_ID]):
        return False
    try:
        import httpx
        import time as _t
        payload = {
            "aps": {
                "alert": {"title": titulo, "body": corpo},
                "badge": badge,
                "sound": "default"
            }
        }
        async with httpx.AsyncClient(timeout=15, http2=True) as client:
            r = await client.post(
                f"https://api.push.apple.com/3/device/{device_token}",
                headers={
                    "apns-topic": APNS_BUNDLE_ID,
                    "apns-priority": "10",
                    "apns-expiration": str(int(_t.time()) + 3600),
                },
                json=payload
            )
            return r.status_code == 200
    except Exception:
        return False

# ── Q7.5 WhatsApp Business API
WHATSAPP_PHONE_ID = _os_s10.getenv("WHATSAPP_PHONE_ID", "")
WHATSAPP_TOKEN = _os_s10.getenv("WHATSAPP_TOKEN", "")

async def whatsapp_enviar_mensagem(telefone: str, mensagem: str) -> bool:
    if not all([WHATSAPP_PHONE_ID, WHATSAPP_TOKEN]):
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"https://graph.facebook.com/v18.0/{WHATSAPP_PHONE_ID}/messages",
                headers={"Authorization": f"Bearer {WHATSAPP_TOKEN}", "Content-Type": "application/json"},
                json={
                    "messaging_product": "whatsapp",
                    "to": telefone.replace("+","").replace(" ",""),
                    "type": "text",
                    "text": {"body": mensagem[:4096]}
                }
            )
            return r.status_code == 200
    except Exception:
        return False

async def whatsapp_lembrete_emocional(telefone: str, nome: str) -> bool:
    msg = f"Oi {nome}! 🧠 Como voce esta se sentindo hoje?\nRegistre sua emocao: https://emotion-platform-albert.onrender.com/dashboard"
    return await whatsapp_enviar_mensagem(telefone, msg)

@app.get("/api/notificacoes/canais")
async def canais_notificacao_ep():
    return JSONResponse({
        "canais": {
            "firebase": bool(FIREBASE_SERVER_KEY),
            "onesignal": bool(ONESIGNAL_APP_ID),
            "discord": bool(DISCORD_BOT_TOKEN),
            "apns": bool(APNS_KEY),
            "whatsapp": bool(WHATSAPP_PHONE_ID),
            "telegram": bool(_os_s10.getenv("TELEGRAM_TOKEN")),
            "sms_twilio": bool(TWILIO_ACCOUNT_SID),
            "push_web": bool(VAPID_PUBLIC_KEY),
            "email": True,
        },
        "sistema": "Q7 Mobile e Notificacoes"
    })


