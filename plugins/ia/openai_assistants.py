"""
Plugin: OpenAI Assistants API
Categoria: ia
"""
VERSAO = "1.0"
NOME = "openai_assistants"
DESCRICAO = "OpenAI Assistants — agentes com memoria e ferramentas"
CATEGORIA = "ia"

import os, httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SOFIA_ASSISTANT_ID = os.getenv("SOFIA_ASSISTANT_ID", "")

_threads_usuarios = {}

async def criar_thread_usuario(usuario_id: int) -> str:
    if not OPENAI_API_KEY:
        return ""
    if usuario_id in _threads_usuarios:
        return _threads_usuarios[usuario_id]
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api.openai.com/v1/threads",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "OpenAI-Beta": "assistants=v2"}
            )
            thread_id = r.json().get("id", "")
            if thread_id:
                _threads_usuarios[usuario_id] = thread_id
            return thread_id
    except Exception:
        return ""

async def enviar_mensagem_assistant(usuario_id: int, mensagem: str) -> str:
    if not all([OPENAI_API_KEY, SOFIA_ASSISTANT_ID]):
        return ""
    thread_id = await criar_thread_usuario(usuario_id)
    if not thread_id:
        return ""
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            await client.post(
                f"https://api.openai.com/v1/threads/{thread_id}/messages",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "OpenAI-Beta": "assistants=v2"},
                json={"role": "user", "content": mensagem}
            )
            run_r = await client.post(
                f"https://api.openai.com/v1/threads/{thread_id}/runs",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "OpenAI-Beta": "assistants=v2"},
                json={"assistant_id": SOFIA_ASSISTANT_ID}
            )
            run_id = run_r.json().get("id", "")
            import asyncio
            for _ in range(30):
                await asyncio.sleep(1)
                status_r = await client.get(
                    f"https://api.openai.com/v1/threads/{thread_id}/runs/{run_id}",
                    headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "OpenAI-Beta": "assistants=v2"}
                )
                if status_r.json().get("status") == "completed":
                    break
            msgs_r = await client.get(
                f"https://api.openai.com/v1/threads/{thread_id}/messages",
                headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "OpenAI-Beta": "assistants=v2"}
            )
            msgs = msgs_r.json().get("data", [])
            if msgs:
                return msgs[0].get("content", [{}])[0].get("text", {}).get("value", "")
    except Exception as e:
        print(f"Assistant erro: {e}")
    return ""

def stats_assistants() -> dict:
    return {
        "disponivel": bool(OPENAI_API_KEY),
        "assistant_configurado": bool(SOFIA_ASSISTANT_ID),
        "threads_ativos": len(_threads_usuarios),
        "plugin": "openai_assistants v1.0"
    }
