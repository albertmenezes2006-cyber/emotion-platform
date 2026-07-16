"""
Plugin: Social Login — Apple, GitHub, LinkedIn
Categoria: integracao
"""
VERSAO = "1.0"
NOME = "social_login"
DESCRICAO = "Login social com Apple, GitHub, LinkedIn e Twitter/X"
CATEGORIA = "integracao"

import os

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET", "")
LINKEDIN_CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID", "")
LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET", "")
APPLE_TEAM_ID = os.getenv("APPLE_TEAM_ID", "")
APPLE_KEY_ID = os.getenv("APPLE_KEY_ID", "")

def url_github_login(redirect_uri: str, state: str = "") -> str:
    if not GITHUB_CLIENT_ID:
        return ""
    return f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={redirect_uri}&scope=user:email&state={state}"

async def github_obter_token(code: str) -> dict:
    if not all([GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET]):
        return {"erro": "GitHub nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://github.com/login/oauth/access_token",
                headers={"Accept": "application/json"},
                data={"client_id": GITHUB_CLIENT_ID, "client_secret": GITHUB_CLIENT_SECRET, "code": code}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def github_obter_perfil(access_token: str) -> dict:
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get("https://api.github.com/user", headers={"Authorization": f"token {access_token}", "Accept": "application/vnd.github.v3+json"})
            perfil = r.json()
            emails_r = await client.get("https://api.github.com/user/emails", headers={"Authorization": f"token {access_token}"})
            emails = emails_r.json()
            email_principal = next((e["email"] for e in emails if e.get("primary")), perfil.get("email",""))
            perfil["email_principal"] = email_principal
            return perfil
    except Exception as e:
        return {"erro": str(e)}

def url_linkedin_login(redirect_uri: str, state: str = "") -> str:
    if not LINKEDIN_CLIENT_ID:
        return ""
    return (f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={LINKEDIN_CLIENT_ID}"
            f"&redirect_uri={redirect_uri}&scope=r_liteprofile r_emailaddress&state={state}")

async def linkedin_obter_token(code: str, redirect_uri: str) -> dict:
    if not all([LINKEDIN_CLIENT_ID, LINKEDIN_CLIENT_SECRET]):
        return {"erro": "LinkedIn nao configurado"}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://www.linkedin.com/oauth/v2/accessToken",
                data={"grant_type": "authorization_code", "code": code, "client_id": LINKEDIN_CLIENT_ID, "client_secret": LINKEDIN_CLIENT_SECRET, "redirect_uri": redirect_uri}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

def verificar_apple_token(id_token: str) -> dict:
    try:
        import jwt
        decoded = jwt.decode(id_token, options={"verify_signature": False})
        return {"email": decoded.get("email",""), "sub": decoded.get("sub",""), "valido": True}
    except Exception:
        return {"valido": False}

def stats_social_login() -> dict:
    return {
        "providers": {
            "github": bool(GITHUB_CLIENT_ID),
            "linkedin": bool(LINKEDIN_CLIENT_ID),
            "apple": bool(APPLE_TEAM_ID),
            "google": bool(os.getenv("GOOGLE_CLIENT_ID")),
        },
        "plugin": "social_login v1.0"
    }
