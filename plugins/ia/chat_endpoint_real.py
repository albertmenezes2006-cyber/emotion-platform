from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import json, os, urllib.request, psycopg2, uuid

router = APIRouter(prefix="/api/v1/chat", tags=["Chat"])
MISTRAL_KEY = os.getenv("MISTRAL_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

def get_conn():
    url = DATABASE_URL.replace("postgres://", "postgresql://")
    return psycopg2.connect(url, sslmode="require", connect_timeout=10)

def init_table():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chat_mensagens (
                id VARCHAR(8) PRIMARY KEY,
                session_id VARCHAR(200),
                role VARCHAR(20),
                content TEXT,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
    except: pass

init_table()

def save_msg(session_id, role, content):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO chat_mensagens (id,session_id,role,content) VALUES (%s,%s,%s,%s)",
            (str(uuid.uuid4())[:8], session_id, role, content)
        )
        conn.commit()
        cur.close()
        conn.close()
    except: pass

def get_hist(session_id):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT role,content FROM chat_mensagens WHERE session_id=%s ORDER BY criado_em ASC LIMIT 50",
            (session_id,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{"role":r[0],"content":r[1]} for r in rows]
    except: return []

def chat_ia(mensagem):
    if not MISTRAL_KEY:
        return "IA nao configurada. Contate o administrador."
    try:
        data = json.dumps({
            "model": "mistral-small-latest",
            "messages": [
                {"role":"system","content":"Voce e um assistente de saude mental em portugues brasileiro. Responda com empatia, carinho e baseado em evidencias. Nunca substitua um profissional. Em caso de crise, indique o CVV 188."},
                {"role":"user","content":mensagem}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }).encode()
        req = urllib.request.Request(
            "https://api.mistral.ai/v1/chat/completions",
            data=data,
            headers={"Authorization":f"Bearer {MISTRAL_KEY}","Content-Type":"application/json"}
        )
        resp = urllib.request.urlopen(req, timeout=30)
        d = json.loads(resp.read().decode())
        return d["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Desculpe, estou com dificuldades tecnicas. Se precisar de ajuda urgente, ligue 188 (CVV). Erro: {str(e)[:50]}"

@router.post("/enviar")
async def enviar_chat(request: Request):
    d = await request.json()
    msg = d.get("mensagem", d.get("message", ""))
    session = d.get("session_id", "anonimo")
    if not msg:
        return JSONResponse({"erro":"Mensagem vazia"}, status_code=400)
    save_msg(session, "user", msg)
    resposta = chat_ia(msg)
    save_msg(session, "assistant", resposta)
    return JSONResponse({"resposta":resposta,"session_id":session,"modelo":"mistral","status":"ok"})

@router.get("/historico/{session_id}")
async def historico(session_id: str):
    hist = get_hist(session_id)
    return JSONResponse({"historico":hist,"total":len(hist)})

@router.delete("/limpar/{session_id}")
async def limpar(session_id: str):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM chat_mensagens WHERE session_id=%s", (session_id,))
        conn.commit()
        cur.close()
        conn.close()
    except: pass
    return JSONResponse({"ok":True})

class Plugin(PluginBase):
    name = "chat_endpoint_real"
    def setup(self, app): app.include_router(router)

plugin = Plugin()
