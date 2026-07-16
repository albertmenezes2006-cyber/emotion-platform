"""
Plugin: Transcricao ao Vivo e Traducao em Tempo Real
Categoria: comunicacao
"""
VERSAO = "1.0"
NOME = "transcricao_ao_vivo"
DESCRICAO = "Transcricao em tempo real durante sessoes terapeuticas"
CATEGORIA = "comunicacao"

import os
from datetime import datetime
from collections import defaultdict

_sessoes_transcricao = {}
_chunks_processados = defaultdict(list)

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

async def iniciar_sessao_transcricao(sessao_id: str, idioma: str = "pt-BR") -> dict:
    _sessoes_transcricao[sessao_id] = {
        "id": sessao_id,
        "idioma": idioma,
        "iniciado_em": datetime.now().isoformat(),
        "ativa": True,
        "chunks": 0,
        "texto_completo": ""
    }
    return {"ok": True, "sessao_id": sessao_id, "provider": "deepgram" if DEEPGRAM_API_KEY else "groq"}

async def processar_chunk_audio(sessao_id: str, audio_chunk: bytes) -> dict:
    if sessao_id not in _sessoes_transcricao:
        return {"erro": "Sessao nao encontrada"}
    sessao = _sessoes_transcricao[sessao_id]
    if not sessao["ativa"]:
        return {"erro": "Sessao encerrada"}
    texto = ""
    if DEEPGRAM_API_KEY:
        try:
            import httpx
            async with httpx.AsyncClient(timeout=10) as client:
                r = await client.post(
                    f"https://api.deepgram.com/v1/listen?language={sessao['idioma']}&model=nova-2&punctuate=true",
                    headers={"Authorization": f"Token {DEEPGRAM_API_KEY}", "Content-Type": "audio/wav"},
                    content=audio_chunk
                )
                resultado = r.json()
                channels = resultado.get("results", {}).get("channels", [])
                if channels:
                    texto = channels[0].get("alternatives", [{}])[0].get("transcript", "")
        except Exception:
            pass
    elif GROQ_API_KEY and len(audio_chunk) > 1000:
        import tempfile, os as _os
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp.write(audio_chunk)
            tmp_path = tmp.name
        try:
            import httpx
            async with httpx.AsyncClient(timeout=15) as client:
                with open(tmp_path, "rb") as f:
                    r = await client.post(
                        "https://api.groq.com/openai/v1/audio/transcriptions",
                        headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                        files={"file": ("chunk.wav", f, "audio/wav")},
                        data={"model": "whisper-large-v3", "language": "pt"}
                    )
                texto = r.json().get("text", "")
        except Exception:
            pass
        finally:
            _os.unlink(tmp_path)
    if texto:
        sessao["texto_completo"] += " " + texto
        sessao["chunks"] += 1
        _chunks_processados[sessao_id].append({"texto": texto, "ts": datetime.now().isoformat()})
    return {"texto": texto, "texto_acumulado": sessao["texto_completo"].strip(), "chunks": sessao["chunks"]}

async def traduzir_em_tempo_real(texto: str, idioma_origem: str = "pt", idioma_destino: str = "en") -> str:
    if not texto:
        return ""
    try:
        import httpx
        if GROQ_API_KEY:
            async with httpx.AsyncClient(timeout=15) as client:
                r = await client.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"},
                    json={"model": "llama-3.1-8b-instant", "messages": [{"role": "user", "content": f"Translate to {idioma_destino} without explanation: {texto}"}], "max_tokens": 200}
                )
                return r.json()["choices"][0]["message"]["content"]
    except Exception:
        pass
    return texto

def encerrar_sessao_transcricao(sessao_id: str) -> dict:
    if sessao_id not in _sessoes_transcricao:
        return {"erro": "Sessao nao encontrada"}
    sessao = _sessoes_transcricao[sessao_id]
    sessao["ativa"] = False
    sessao["encerrado_em"] = datetime.now().isoformat()
    return {"ok": True, "texto_final": sessao["texto_completo"].strip(), "chunks_processados": sessao["chunks"]}

def stats_transcricao() -> dict:
    return {
        "sessoes_ativas": sum(1 for s in _sessoes_transcricao.values() if s.get("ativa")),
        "total_sessoes": len(_sessoes_transcricao),
        "deepgram": bool(DEEPGRAM_API_KEY),
        "groq_whisper": bool(GROQ_API_KEY),
        "plugin": "transcricao_ao_vivo v1.0"
    }
