"""
Plugin: YouTube e Twitch API
Categoria: integracao
"""
VERSAO = "1.0"
NOME = "youtube_twitch"
DESCRICAO = "YouTube Data API e Twitch para conteudo terapeutico e lives"
CATEGORIA = "integracao"

import os

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")
TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID", "")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET", "")

CANAIS_SAUDE_MENTAL = [
    "UCemocoes", "psicologia_online", "mindfulness_brasil",
    "autoconhecimento_canal", "terapia_digital"
]

async def youtube_buscar_videos(query: str, max_results: int = 5) -> list:
    if not YOUTUBE_API_KEY:
        return []
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                "https://www.googleapis.com/youtube/v3/search",
                params={"key": YOUTUBE_API_KEY, "q": query, "part": "snippet", "type": "video", "maxResults": max_results, "relevanceLanguage": "pt", "safeSearch": "strict"}
            )
            items = r.json().get("items", [])
            return [{"titulo": i["snippet"]["title"], "canal": i["snippet"]["channelTitle"], "video_id": i["id"]["videoId"], "url": f"https://youtu.be/{i['id']['videoId']}", "thumbnail": i["snippet"]["thumbnails"]["default"]["url"]} for i in items]
    except Exception:
        return []

async def youtube_buscar_por_emocao(emocao: str) -> list:
    queries = {
        "ansiedade": "tecnicas para ansiedade meditacao guiada",
        "tristeza": "superando tristeza autocompaixao",
        "raiva": "gerenciamento raiva inteligencia emocional",
        "estresse": "reducao estresse mindfulness",
        "depressao": "saude mental bem-estar emocional",
        "neutro": "inteligencia emocional desenvolvimento pessoal",
    }
    query = queries.get(emocao, "bem estar emocional")
    return await youtube_buscar_videos(query)

async def twitch_obter_token_app() -> str:
    if not all([TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET]):
        return ""
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                "https://id.twitch.tv/oauth2/token",
                data={"client_id": TWITCH_CLIENT_ID, "client_secret": TWITCH_CLIENT_SECRET, "grant_type": "client_credentials"}
            )
            return r.json().get("access_token", "")
    except Exception:
        return ""

async def twitch_buscar_streams_saude_mental() -> list:
    token = await twitch_obter_token_app()
    if not token:
        return []
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                "https://api.twitch.tv/helix/streams",
                headers={"Client-ID": TWITCH_CLIENT_ID, "Authorization": f"Bearer {token}"},
                params={"game_id": "27471", "language": "pt"}
            )
            return r.json().get("data", [])[:5]
    except Exception:
        return []

def stats_youtube_twitch() -> dict:
    return {"youtube": bool(YOUTUBE_API_KEY), "twitch": bool(TWITCH_CLIENT_ID), "plugin": "youtube_twitch v1.0"}
