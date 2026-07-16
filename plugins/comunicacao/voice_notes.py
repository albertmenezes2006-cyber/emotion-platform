"""
Plugin: Voice Notes e Mensagens de Audio
Categoria: comunicacao
"""
VERSAO = "1.0"
NOME = "voice_notes"
DESCRICAO = "Gravacao, transcricao e analise de mensagens de voz"
CATEGORIA = "comunicacao"

import os
from datetime import datetime
from collections import defaultdict

_voice_notes = defaultdict(list)
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "")

async def transcrever_audio_groq(audio_bytes: bytes, formato: str = "wav") -> str:
    if not GROQ_API_KEY:
        return ""
    try:
        import httpx
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=f".{formato}", delete=False) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
        async with httpx.AsyncClient(timeout=30) as client:
            with open(tmp_path, "rb") as f:
                r = await client.post(
                    "https://api.groq.com/openai/v1/audio/transcriptions",
                    headers={"Authorization": f"Bearer {GROQ_API_KEY}"},
                    files={"file": (f"audio.{formato}", f, f"audio/{formato}")},
                    data={"model": "whisper-large-v3", "language": "pt", "response_format": "json"}
                )
        import os as _os
        _os.unlink(tmp_path)
        return r.json().get("text", "")
    except Exception as e:
        print(f"Groq transcricao erro: {e}")
        return ""

async def salvar_voice_note(usuario_id: int, audio_bytes: bytes, formato: str = "wav") -> dict:
    import secrets
    note_id = secrets.token_hex(8)
    transcricao = await transcrever_audio_groq(audio_bytes, formato)
    emocao = "neutro"
    if transcricao:
        palavras_neg = ["triste","choro","dor","medo","ansioso","raiva"]
        palavras_pos = ["feliz","alegre","otimo","amor","gratidao"]
        t_lower = transcricao.lower()
        if any(p in t_lower for p in palavras_neg):
            emocao = "tristeza"
        elif any(p in t_lower for p in palavras_pos):
            emocao = "alegria"
    note = {
        "id": note_id,
        "usuario_id": usuario_id,
        "transcricao": transcricao,
        "emocao_detectada": emocao,
        "duracao_bytes": len(audio_bytes),
        "formato": formato,
        "criado_em": datetime.now().isoformat()
    }
    _voice_notes[usuario_id].append(note)
    return note

def obter_voice_notes(usuario_id: int, limite: int = 20) -> list:
    return _voice_notes.get(usuario_id, [])[-limite:]

def analisar_padrao_voz(usuario_id: int) -> dict:
    notes = _voice_notes.get(usuario_id, [])
    if not notes:
        return {"sem_dados": True}
    emocoes = [n["emocao_detectada"] for n in notes]
    from collections import Counter
    contagem = Counter(emocoes)
    return {
        "total_notas": len(notes),
        "emocao_predominante": contagem.most_common(1)[0][0],
        "distribuicao": dict(contagem),
        "ultima_nota": notes[-1]["criado_em"] if notes else None
    }

def stats_voice_notes() -> dict:
    return {
        "usuarios_com_notas": len(_voice_notes),
        "total_notas": sum(len(v) for v in _voice_notes.values()),
        "groq_whisper": bool(GROQ_API_KEY),
        "deepgram": bool(DEEPGRAM_API_KEY),
        "plugin": "voice_notes v1.0"
    }
