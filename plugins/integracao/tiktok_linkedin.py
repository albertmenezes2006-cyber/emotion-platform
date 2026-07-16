"""
Plugin: TikTok e LinkedIn API
Categoria: integracao
"""
VERSAO = "1.0"
NOME = "tiktok_linkedin"
DESCRICAO = "TikTok for Business e LinkedIn para marketing e conteudo"
CATEGORIA = "integracao"

import os

TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN", "")
TIKTOK_OPEN_ID = os.getenv("TIKTOK_OPEN_ID", "")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
LINKEDIN_PERSON_ID = os.getenv("LINKEDIN_PERSON_ID", "")

async def tiktok_publicar_video(video_url: str, titulo: str, descricao: str) -> dict:
    if not all([TIKTOK_ACCESS_TOKEN, TIKTOK_OPEN_ID]):
        return {"erro": "TikTok nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://open.tiktokapis.com/v2/post/publish/video/init/",
                headers={"Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}", "Content-Type": "application/json"},
                json={"post_info": {"title": titulo[:150], "description": descricao[:150], "privacy_level": "PUBLIC_TO_EVERYONE"}, "source_info": {"source": "PULL_FROM_URL", "video_url": video_url}}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def linkedin_publicar_post(texto: str, visibilidade: str = "PUBLIC") -> dict:
    if not all([LINKEDIN_ACCESS_TOKEN, LINKEDIN_PERSON_ID]):
        return {"erro": "LinkedIn nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api.linkedin.com/v2/ugcPosts",
                headers={"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"},
                json={"author": f"urn:li:person:{LINKEDIN_PERSON_ID}", "lifecycleState": "PUBLISHED", "specificContent": {"com.linkedin.ugc.ShareContent": {"shareCommentary": {"text": texto[:3000]}, "shareMediaCategory": "NONE"}}, "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": visibilidade}}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

def gerar_conteudo_linkedin(topico: str, emocao: str) -> str:
    templates = {
        "inteligencia_emocional": "A inteligencia emocional e uma das competencias mais valorizadas no mercado atual. Nossa plataforma Emotion Intelligence usa IA para ajudar profissionais a desenvolver autoconsciencia emocional. #InteligenciaEmocional #IA #Lideranca",
        "bem_estar": "Bem-estar mental no trabalho nao e luxo, e necessidade. Com a Emotion Intelligence, monitore e desenvolva sua saude emocional. #BemEstar #SaudeMental #RH",
    }
    return templates.get(topico, f"Explorando {topico} com inteligencia artificial. #EmotionAI")

def stats_tiktok_linkedin() -> dict:
    return {"tiktok": bool(TIKTOK_ACCESS_TOKEN), "linkedin": bool(LINKEDIN_ACCESS_TOKEN), "plugin": "tiktok_linkedin v1.0"}
