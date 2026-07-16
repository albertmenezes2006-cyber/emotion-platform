"""
Plugin: Q4 Zapier+Slack+Notion
Categoria: integracao
Extraido automaticamente do main.py
"""
VERSAO = "1.0"
NOME = "automacao"
DESCRICAO = "Q4 Zapier+Slack+Notion"
CATEGORIA = "integracao"

# ═══════════════════════════════════════════════════════════════════════
# SISTEMA Q4 — AUTOMAÇÃO E INTEGRAÇÃO (11 implementações)
# ═══════════════════════════════════════════════════════════════════════

ZAPIER_WEBHOOK_URL = _os_s10.getenv("ZAPIER_WEBHOOK_URL", "")
N8N_WEBHOOK_URL = _os_s10.getenv("N8N_WEBHOOK_URL", "")
SLACK_BOT_TOKEN = _os_s10.getenv("SLACK_BOT_TOKEN", "")
SLACK_CHANNEL = _os_s10.getenv("SLACK_CHANNEL", "#geral")
NOTION_TOKEN = _os_s10.getenv("NOTION_TOKEN", "")
NOTION_DATABASE_ID = _os_s10.getenv("NOTION_DATABASE_ID", "")
GOOGLE_SHEETS_KEY = _os_s10.getenv("GOOGLE_SHEETS_KEY", "")
HUBSPOT_API_KEY = _os_s10.getenv("HUBSPOT_API_KEY", "")
AIRTABLE_API_KEY = _os_s10.getenv("AIRTABLE_API_KEY", "")
AIRTABLE_BASE_ID = _os_s10.getenv("AIRTABLE_BASE_ID", "")

# ── Q4.1 Zapier Webhook
async def zapier_disparar(evento: str, dados: dict) -> bool:
    if not ZAPIER_WEBHOOK_URL:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(ZAPIER_WEBHOOK_URL, json={"evento": evento, "dados": dados, "ts": _datetime_s7.now().isoformat()})
            return r.status_code == 200
    except Exception:
        return False

async def zapier_novo_usuario(usuario_id: int, email: str, plano: str):
    return await zapier_disparar("novo_usuario", {"usuario_id": usuario_id, "email": email, "plano": plano})

async def zapier_pagamento(usuario_id: int, valor: float, plano: str):
    return await zapier_disparar("pagamento_aprovado", {"usuario_id": usuario_id, "valor": valor, "plano": plano})

# ── Q4.2 n8n Workflow
async def n8n_disparar(workflow: str, dados: dict) -> bool:
    if not N8N_WEBHOOK_URL:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(f"{N8N_WEBHOOK_URL}/{workflow}", json=dados)
            return r.status_code in (200, 201)
    except Exception:
        return False

# ── Q4.3 Slack Bot
async def slack_enviar_mensagem(mensagem: str, canal: str = None) -> bool:
    if not SLACK_BOT_TOKEN:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(
                "https://slack.com/api/chat.postMessage",
                headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}", "Content-Type": "application/json"},
                json={"channel": canal or SLACK_CHANNEL, "text": mensagem}
            )
            return r.json().get("ok", False)
    except Exception:
        return False

async def slack_alerta_crise_usuario(usuario_id: int, resumo: str):
    msg = f":rotating_light: *CRISE DETECTADA*\nUsuario ID: `{usuario_id}`\n_{resumo[:200]}_"
    return await slack_enviar_mensagem(msg)

async def slack_novo_pagamento(valor: float, plano: str):
    msg = f":moneybag: *Novo pagamento!* R${valor:.2f} — Plano {plano}"
    return await slack_enviar_mensagem(msg)

# ── Q4.4 Notion API
async def notion_criar_pagina(titulo: str, conteudo: dict) -> dict:
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        return {}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api.notion.com/v1/pages",
                headers={"Authorization": f"Bearer {NOTION_TOKEN}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"},
                json={
                    "parent": {"database_id": NOTION_DATABASE_ID},
                    "properties": {"Name": {"title": [{"text": {"content": titulo}}]}},
                    "children": [{"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": str(conteudo)[:200]}}]}}]
                }
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

# ── Q4.5 Google Sheets
async def sheets_adicionar_linha(spreadsheet_id: str, valores: list) -> bool:
    if not GOOGLE_SHEETS_KEY:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/A1:append",
                params={"valueInputOption": "RAW", "key": GOOGLE_SHEETS_KEY},
                json={"values": [valores]}
            )
            return r.status_code == 200
    except Exception:
        return False

async def sheets_exportar_analises(usuario_id: int, analises: list) -> bool:
    spreadsheet_id = _os_s10.getenv("GOOGLE_SHEETS_ID", "")
    if not spreadsheet_id:
        return False
    linhas = [[str(a.get("emocao","")), str(a.get("intensidade","")), str(a.get("created_at",""))] for a in analises[:100]]
    for linha in linhas:
        await sheets_adicionar_linha(spreadsheet_id, linha)
    return True

# ── Q4.6 Airtable
async def airtable_criar_registro(tabela: str, campos: dict) -> dict:
    if not all([AIRTABLE_API_KEY, AIRTABLE_BASE_ID]):
        return {}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{tabela}",
                headers={"Authorization": f"Bearer {AIRTABLE_API_KEY}", "Content-Type": "application/json"},
                json={"fields": campos}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

# ── Q4.7 HubSpot CRM
async def hubspot_criar_contato(email: str, nome: str, plano: str) -> dict:
    if not HUBSPOT_API_KEY:
        return {}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api.hubapi.com/crm/v3/objects/contacts",
                headers={"Authorization": f"Bearer {HUBSPOT_API_KEY}", "Content-Type": "application/json"},
                json={"properties": {"email": email, "firstname": nome.split()[0], "lifecyclestage": "customer", "plan": plano}}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

async def hubspot_registrar_negocio(usuario_id: int, valor: float, plano: str) -> dict:
    if not HUBSPOT_API_KEY:
        return {}
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                "https://api.hubapi.com/crm/v3/objects/deals",
                headers={"Authorization": f"Bearer {HUBSPOT_API_KEY}", "Content-Type": "application/json"},
                json={"properties": {"dealname": f"Plano {plano} - Usuario {usuario_id}", "amount": str(valor), "dealstage": "closedwon", "pipeline": "default"}}
            )
            return r.json()
    except Exception as e:
        return {"erro": str(e)}

# ── Q4.8 GitHub Actions webhook
async def github_disparar_workflow(workflow: str, inputs: dict = None) -> bool:
    github_token = _os_s10.getenv("GITHUB_TOKEN", "")
    repo = _os_s10.getenv("GITHUB_REPO", "albertmenezes2006-cyber/emotion-platform")
    if not github_token:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.post(
                f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/dispatches",
                headers={"Authorization": f"Bearer {github_token}", "Accept": "application/vnd.github.v3+json"},
                json={"ref": "main", "inputs": inputs or {}}
            )
            return r.status_code == 204
    except Exception:
        return False

# ── Q4.9 Make (Integromat)
async def make_disparar_cenario(webhook_url: str, dados: dict) -> bool:
    if not webhook_url:
        return False
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.post(webhook_url, json=dados)
            return r.status_code in (200, 201)
    except Exception:
        return False

# ── Q4.10 Automação interna
_automacoes_ativas: dict = {}

def registrar_automacao(nome: str, gatilho: str, acao: str, ativo: bool = True):
    _automacoes_ativas[nome] = {
        "gatilho": gatilho,
        "acao": acao,
        "ativo": ativo,
        "execucoes": 0,
        "criado_em": _datetime_s7.now().isoformat()
    }

def registrar_execucao_automacao(nome: str):
    if nome in _automacoes_ativas:
        _automacoes_ativas[nome]["execucoes"] += 1
        _automacoes_ativas[nome]["ultima_execucao"] = _datetime_s7.now().isoformat()

registrar_automacao("novo_usuario_zapier", "cadastro", "zapier_novo_usuario")
registrar_automacao("pagamento_slack", "pagamento_aprovado", "slack_novo_pagamento")
registrar_automacao("crise_slack", "crise_detectada", "slack_alerta_crise")
registrar_automacao("usuario_hubspot", "cadastro", "hubspot_criar_contato")

# ── Q4.11 Endpoints
@app.get("/api/automacoes")
async def automacoes_ep(request: Request, db=Depends(get_db)):
    usuario = await verificar_token(request, db)
    if not usuario or usuario.get("plano") != "admin":
        return JSONResponse({"erro": "Nao autorizado"}, status_code=403)
    return JSONResponse({
        "automacoes": _automacoes_ativas,
        "integracoes": {
            "zapier": bool(ZAPIER_WEBHOOK_URL),
            "n8n": bool(N8N_WEBHOOK_URL),
            "slack": bool(SLACK_BOT_TOKEN),
            "notion": bool(NOTION_TOKEN),
            "hubspot": bool(HUBSPOT_API_KEY),
            "airtable": bool(AIRTABLE_API_KEY),
            "sheets": bool(GOOGLE_SHEETS_KEY),
        },
        "sistema": "Q4 Automacao"
    })

@app.post("/api/webhook/zapier")
async def webhook_zapier_ep(request: Request):
    try:
        dados = await request.json()
        registrar_evento_analytics(0, "zapier_webhook", dados)
        return JSONResponse({"ok": True, "recebido": True})
    except Exception:
        return JSONResponse({"ok": False})


