"""
Plugin: Meta Business — Instagram e Facebook
Categoria: integracao
"""
VERSAO = "1.0"
NOME = "meta_social"
DESCRICAO = "Meta Business API para Instagram Graph e Facebook"
CATEGORIA = "integracao"

import os

META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN", "")
INSTAGRAM_ACCOUNT_ID = os.getenv("INSTAGRAM_ACCOUNT_ID", "")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID", "")

async def instagram_publicar_post(imagem_url: str, legenda: str) -> dict:
    if not all([META_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID]):
        return {"erro": "Instagram nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=30) as client:
            container_r = await client.post(
                f"https://graph.facebook.com/v18.0/{INSTAGRAM_ACCOUNT_ID}/media",
                params={"image_url": imagem_url, "caption": legenda[:2200], "access_token": META_ACCESS_TOKEN}
            )
            container_id = container_r.json().get("id", "")
            if not container_id:
                return {"erro": "Falha ao criar container"}
            publish_r = await client.post(
                f"https://graph.facebook.com/v18.0/{INSTAGRAM_ACCOUNT_ID}/media_publish",
                params={"creation_id": container_id, "access_token": META_ACCESS_TOKEN}
            )
            return publish_r.json()
    except Exception as e:
        return {"erro": str(e)}

async def facebook_publicar_post(mensagem: str, link: str = "") -> dict:
    if not all([META_ACCESS_TOKEN, FACEBOOK_PAGE_ID]):
        return {"erro": "Facebook nao configurado"}
    try:
        import httpx
        dados = {"message": mensagem, "access_token": META_ACCESS_TOKEN}
        if link:
            dados["link"] = link
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(f"https://graph.facebook.com/v18.0/{FACEBOOK_PAGE_ID}/feed", data=dados)
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def instagram_obter_insights(periodo: str = "day") -> dict:
    if not all([META_ACCESS_TOKEN, INSTAGRAM_ACCOUNT_ID]):
        return {}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get(
                f"https://graph.facebook.com/v18.0/{INSTAGRAM_ACCOUNT_ID}/insights",
                params={"metric": "impressions,reach,profile_views", "period": periodo, "access_token": META_ACCESS_TOKEN}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

def gerar_legenda_emocao(emocao: str, texto_analise: str) -> str:
    templates = {
        "alegria": "Sentindo alegria hoje! A Emotion Intelligence ajudou a identificar e celebrar essa emocao positiva. Voce tambem quer explorar suas emocoes? Link na bio! 🌟 #InteligenciaEmocional #BemEstar",
        "tristeza": "Reconhecer a tristeza e um passo importante. A Emotion Intelligence oferece suporte emocional profissional. Cuide da sua saude mental. 💙 #SaudeMental #Autocuidado",
        "ansiedade": "A ansiedade pode ser gerenciada. Com a Emotion Intelligence, encontre tecnicas personalizadas para o seu perfil. Respire. 🌿 #Ansiedade #Mindfulness",
    }
    base = templates.get(emocao, "Explorando emocoes com inteligencia artificial. Junte-se a nossa comunidade! #EmotionIntelligence #IA")
    return base[:2200]

def stats_meta() -> dict:
    return {"instagram": bool(INSTAGRAM_ACCOUNT_ID), "facebook": bool(FACEBOOK_PAGE_ID), "plugin": "meta_social v1.0"}
