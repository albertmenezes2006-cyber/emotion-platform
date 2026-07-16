"""
Plugin: P4 WebSocket+Push+SMS
Categoria: sistemas
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "websocket"
DESCRICAO = "P4 WebSocket+Push+SMS"
CATEGORIA = "sistemas"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA P4 — WEBSOCKET + PUSH NOTIFICATIONS + SMS
# ═══════════════════════════════════════════════════════════════════════

_conexoes_ws: dict = {}
_push_subscriptions: dict = {}
_sms_log: list = []

# ── P4.1 WebSocket Manager
class WebSocketManager:
    def __init__(self):
        self.conexoes_ativas: dict = {}

    async def conectar(self, websocket, usuario_id: int):
        await websocket.accept()
        if usuario_id not in self.conexoes_ativas:
            self.conexoes_ativas[usuario_id] = []
        self.conexoes_ativas[usuario_id].append(websocket)
        registrar_auditoria_s8("WS_CONECTADO", usuario_id=usuario_id)

    def desconectar(self, websocket, usuario_id: int):
        if usuario_id in self.conexoes_ativas:
            try:
                self.conexoes_ativas[usuario_id].remove(websocket)
            except ValueError:
                pass
            if not self.conexoes_ativas[usuario_id]:
                del self.conexoes_ativas[usuario_id]

    async def enviar_para_usuario(self, usuario_id: int, mensagem: dict):
        import json
        conexoes = self.conexoes_ativas.get(usuario_id, [])
        desconectados = []
        for ws in conexoes:
            try:
                await ws.send_text(json.dumps(mensagem, ensure_ascii=False))
            except Exception:
                desconectados.append(ws)
        for ws in desconectados:
            self.desconectar(ws, usuario_id)

    async def broadcast(self, mensagem: dict):
        for usuario_id in list(self.conexoes_ativas.keys()):
            await self.enviar_para_usuario(usuario_id, mensagem)

    def usuarios_online(self) -> list:
        return list(self.conexoes_ativas.keys())

    def total_conexoes(self) -> int:
        return sum(len(v) for v in self.conexoes_ativas.values())

ws_manager = WebSocketManager()


@app.websocket("/ws/{usuario_id}")
async def websocket_endpoint(websocket: _WebSocket, usuario_id: int):
    await ws_manager.conectar(websocket, usuario_id)
    try:
        await ws_manager.enviar_para_usuario(usuario_id, {
            "tipo": "conectado",
            "msg": "Conexao estabelecida",
            "usuarios_online": len(ws_manager.usuarios_online())
        })
        while True:
            data = await websocket.receive_text()
            import json
            try:
                msg = json.loads(data)
                tipo = msg.get("tipo", "ping")
                if tipo == "ping":
                    await ws_manager.enviar_para_usuario(usuario_id, {"tipo": "pong"})
                elif tipo == "analise":
                    texto = msg.get("texto", "")
                    if texto:
                        emocao = detectar_emocao(texto)
                        await ws_manager.enviar_para_usuario(usuario_id, {
                            "tipo": "resultado_analise",
                            "emocao": emocao,
                            "texto": texto[:100]
                        })
            except Exception:
                pass
    except _WebSocketDisconnect:
        ws_manager.desconectar(websocket, usuario_id)

@app.get("/api/ws-status")
async def ws_status_ep(request: Request):
    return JSONResponse({
        "conexoes_ativas": ws_manager.total_conexoes(),
        "usuarios_online": len(ws_manager.usuarios_online()),
        "sistema": "P4 WebSocket"
    })

# ── P4.2 Push Notifications (Web Push)
VAPID_PUBLIC_KEY = _os_s10.getenv("VAPID_PUBLIC_KEY", "")
VAPID_PRIVATE_KEY = _os_s10.getenv("VAPID_PRIVATE_KEY", "")

def salvar_push_subscription(usuario_id: int, subscription: dict):
    _push_subscriptions[usuario_id] = {
        "subscription": subscription,
        "criado_em": _datetime_s7.now().isoformat(),
        "ativo": True
    }

async def enviar_push_notification(usuario_id: int, titulo: str, corpo: str, url: str = "/dashboard"):
    if usuario_id not in _push_subscriptions:
        return False
    sub = _push_subscriptions[usuario_id]
    if not sub.get("ativo"):
        return False
    try:
        from pywebpush import webpush
        import json
        webpush(
            subscription_info=sub["subscription"],
            data=json.dumps({"title": titulo, "body": corpo, "url": url}),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims={"sub": "mailto:albertmenezes2006@gmail.com"}
        )
        return True
    except Exception:
        return False

async def push_lembrete_diario(usuario_id: int):
    return await enviar_push_notification(
        usuario_id,
        "Como voce esta hoje? 🧠",
        "Faca sua analise emocional diaria",
        "/dashboard"
    )

async def push_nova_conquista(usuario_id: int, conquista: str):
    return await enviar_push_notification(
        usuario_id,
        "Nova conquista desbloqueada! 🏆",
        f"Voce ganhou: {conquista}",
        "/gamificacao"
    )

@app.post("/api/push/subscribe")
async def push_subscribe_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario:
        return JSONResponse({"erro": "Nao autorizado"}, status_code=401)
    body = await request.json()
    subscription = body.get("subscription", {})
    if subscription:
        salvar_push_subscription(usuario.get("id"), subscription)
    return JSONResponse({"ok": True, "sistema": "P4 Push Notifications"})

@app.get("/api/push/vapid-key")
async def vapid_key_ep():
    return JSONResponse({
        "publicKey": VAPID_PUBLIC_KEY or "configure_VAPID_PUBLIC_KEY",
        "sistema": "P4 Web Push"
    })

# ── P4.3 SMS via Twilio
TWILIO_ACCOUNT_SID = _os_s10.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = _os_s10.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_FROM_NUMBER = _os_s10.getenv("TWILIO_FROM_NUMBER", "")

async def enviar_sms(telefone: str, mensagem: str) -> bool:
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER]):
        return False
    try:
        import httpx
        from base64 import b64encode
        auth = b64encode(f"{TWILIO_ACCOUNT_SID}:{TWILIO_AUTH_TOKEN}".encode()).decode()
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json",
                headers={"Authorization": f"Basic {auth}"},
                data={
                    "From": TWILIO_FROM_NUMBER,
                    "To": telefone,
                    "Body": mensagem[:160]
                }
            )
            sucesso = r.status_code == 201
            _sms_log.append({
                "telefone": _mascarar_dado_s8(telefone),
                "sucesso": sucesso,
                "ts": _datetime_s7.now().isoformat()
            })
            return sucesso
    except Exception as e:
        print(f"SMS erro: {e}")
        return False

async def sms_codigo_2fa(telefone: str, codigo: str) -> bool:
    mensagem = f"Emotion Intelligence: seu codigo de verificacao e {codigo}. Valido por 10 minutos."
    return await enviar_sms(telefone, mensagem)

async def sms_alerta_crise(telefone: str, nome: str) -> bool:
    mensagem = f"Emotion Intelligence: {nome}, estamos preocupados com voce. Ligue 188 (CVV) se precisar de apoio."
    return await enviar_sms(telefone, mensagem)

def stats_sms() -> dict:
    total = len(_sms_log)
    sucesso = sum(1 for s in _sms_log if s.get("sucesso"))
    return {
        "total_enviados": total,
        "sucesso": sucesso,
        "falhas": total - sucesso,
        "taxa_sucesso": round((sucesso/total*100) if total > 0 else 0, 1),
        "twilio_configurado": bool(TWILIO_ACCOUNT_SID)
    }


