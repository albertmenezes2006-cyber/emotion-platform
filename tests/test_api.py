"""Testes completos da API EmotionAI — pytest tests/test_api.py -v"""
import pytest, httpx, json, time

BASE = "https://emotion-platform-albert.onrender.com"

@pytest.fixture
def c():
    return httpx.Client(base_url=BASE, timeout=40)

# SISTEMA
def test_health(c):
    r = c.get("/health")
    assert r.status_code == 200
    d = r.json()
    assert d["status"] == "ok"
    assert d["plugins"] > 1000
    print(f"v{d['version']} | {d['plugins']} plugins | {d['rotas']} rotas")

def test_ping(c):
    r = c.get("/ping")
    assert r.status_code == 200
    assert r.json()["pong"] == True

# PÁGINAS
@pytest.mark.parametrize("path,min_size", [
    ("/",5000),("/app/avaliacao",8000),("/app/chat",8000),
    ("/app/diario",5000),("/app/dashboard",3000),("/app/login",3000),
])
def test_pagina(c, path, min_size):
    r = c.get(path)
    assert r.status_code == 200, f"HTTP {r.status_code} em {path}"
    assert len(r.text) >= min_size, f"{path} pequena: {len(r.text)} < {min_size}"

# CHAT IA
def test_chat_responde(c):
    r = c.post("/api/v1/chat-ia/mensagem", params={"user_id":"pytest","mensagem":"Ola"})
    assert r.status_code == 200
    d = r.json()
    assert len(d.get("resposta","")) > 10

def test_chat_ansiedade(c):
    r = c.post("/api/v1/chat-ia/mensagem", params={"user_id":"pytest","mensagem":"Estou muito ansioso"})
    assert r.status_code == 200
    resp = r.json()["resposta"].lower()
    assert any(w in resp for w in ["ansiedade","respira","calma","aqui","ajudar"])

def test_chat_crise(c):
    r = c.post("/api/v1/chat-ia/mensagem", params={"user_id":"pytest","mensagem":"quero me machucar"})
    assert r.status_code == 200
    assert r.json().get("alerta_crise") == True

def test_chat_pt_br(c):
    r = c.post("/api/v1/chat-ia/mensagem", params={"user_id":"pytest","mensagem":"Como voce pode me ajudar"})
    assert r.status_code == 200
    resp = r.json()["resposta"].lower()
    assert any(w in resp for w in ["você","estou","vamos","pode","uma","para","que"])

# PHQ-9
def test_phq9_perguntas(c):
    r = c.get("/api/v1/phq9-clinico/perguntas")
    assert r.status_code == 200
    assert len(r.json()["perguntas"]) == 9

def test_phq9_score_zero(c):
    r = c.post("/api/v1/phq9-clinico/aplicar", params={"user_id":"pytest"}, json=[0]*9)
    assert r.status_code == 200
    assert r.json()["score"] == 0

def test_phq9_score_maximo(c):
    r = c.post("/api/v1/phq9-clinico/aplicar", params={"user_id":"pytest"}, json=[3]*9)
    assert r.status_code == 200
    assert r.json()["score"] == 27

def test_phq9_alerta_suicidio(c):
    r = c.post("/api/v1/phq9-clinico/aplicar", params={"user_id":"pytest"}, json=[0]*8+[3])
    assert r.status_code == 200
    assert r.json()["alerta_suicidio"] == True

def test_phq9_score_correto(c):
    resps = [1,2,3,0,1,2,1,0,1]
    r = c.post("/api/v1/phq9-clinico/aplicar", params={"user_id":"pytest"}, json=resps)
    assert r.status_code == 200
    assert r.json()["score"] == sum(resps)

# GAD-7
def test_gad7_perguntas(c):
    r = c.get("/api/v1/gad7-clinico/perguntas")
    assert r.status_code == 200
    assert len(r.json()["perguntas"]) == 7

def test_gad7_score_correto(c):
    resps = [1,2,1,2,1,2,1]
    r = c.post("/api/v1/gad7-clinico/aplicar", params={"user_id":"pytest"}, json=resps)
    assert r.status_code == 200
    assert r.json()["score"] == sum(resps)

# AUTH
def test_cadastro_login(c):
    import time
    ts = int(time.time())
    email = f"pytest_{ts}@test.com"
    senha = "Test1234Segura"
    
    # Cadastrar
    r = c.post("/api/v1/auth/cadastrar",
               params={"nome":"Pytest","email":email,"senha":senha,"tipo":"paciente"})
    assert r.status_code == 200, f"Cadastro falhou: {r.status_code} {r.text[:100]}"
    d = r.json()
    token = d.get("token","")
    user_id = d.get("user_id","")
    assert len(token) > 10, f"Token invalido: {token}"
    assert user_id, "user_id ausente"
    
    # /me com token
    r3 = c.get("/api/v1/auth/me",
               headers={"Authorization": f"Bearer {token}"})
    assert r3.status_code == 200, f"/me falhou: {r3.status_code}"
    me = r3.json()
    assert me.get("email","").lower() == email.lower()
    
    # Login — usar query params como o endpoint espera
    r2 = c.post("/api/v1/auth/login",
                params={"email": email, "senha": senha})
    if r2.status_code != 200:
        # Tentar com JSON body
        r2b = c.post("/api/v1/auth/login",
                     json={"email": email, "senha": senha})
        assert r2b.status_code == 200, f"Login falhou: {r2.status_code} {r2.text[:100]}"
    
    print(f"  Auth OK: user={user_id} email={email}")


def test_login_senha_errada(c):
    r = c.post("/api/v1/auth/login", params={"email":"naoexiste@x.com","senha":"errada"})
    assert r.status_code in [400,401,422]

# DIÁRIO
def test_diario_criar(c):
    r = c.post("/api/v1/diario-emocional/entrada", params={
        "user_id":"pytest","texto":"Teste pytest","emocao_principal":"alegria","intensidade":7,"humor_geral":8
    })
    assert r.status_code == 200

def test_diario_emocoes(c):
    r = c.get("/api/v1/diario-emocional/emocoes/disponiveis")
    assert r.status_code == 200
    assert len(r.json()["emocoes"]) >= 8

# STRIPE
def test_stripe_planos(c):
    r = c.get("/api/v1/stripe/planos")
    assert r.status_code == 200
    planos = r.json()["planos"]
    assert "free" in planos
    assert "pro" in planos
    assert planos["pro"]["preco_brl"] > 0

# MOBILE
def test_mobile_sdk(c):
    r = c.get("/api/mobile/v1/sdk/config")
    assert r.status_code == 200
    assert len(r.json()["endpoints"]) >= 10

def test_mobile_home(c):
    r = c.get("/api/mobile/v1/home/pytest")
    assert r.status_code == 200
    assert len(r.json()["widgets"]) >= 3

# MULTI-LLM
def test_multilm_modelos(c):
    r = c.get("/api/v1/multi-llm/modelos")
    assert r.status_code == 200
    disponiveis = [m for m in r.json()["modelos"] if m["disponivel"]]
    assert len(disponiveis) >= 2

def test_multilm_chat(c):
    r = c.post("/api/v1/multi-llm/chat", params={"mensagem":"Ola","user_id":"pytest"})
    assert r.status_code == 200
    assert len(r.json().get("resposta","")) > 10

# SEGURANÇA
def test_jwt_invalido_rejeitado(c):
    r = c.get("/api/v1/auth/me", headers={"Authorization":"Bearer token_falso_abc"})
    assert r.status_code == 401

def test_sem_sql_injection(c):
    r = c.post("/api/v1/auth/login", params={"email":"'+OR+'1'='1--","senha":"x"})
    assert r.status_code in [400,401,422]
