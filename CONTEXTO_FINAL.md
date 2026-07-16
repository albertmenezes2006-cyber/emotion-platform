# EMOTION PLATFORM v24.3 — CONTEXTO FINAL

## SITE: https://emotion-platform-albert.onrender.com

## CREDENCIAIS
API_KEY = rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK
SERVICE_ID = srv-d97vrmcs728c73ci1mig
JWT_SECRET = 01356f6bd4852f675e8d9e9abaf9c98383eba11ca35bfac08aa96f303cd33b71

## STATUS: 12/12 endpoints funcionando

## PÁGINAS
/ → Home dark moderna
/app/avaliacao → PHQ-9 + GAD-7 interativo
/app/chat → Chat IA Mistral/Groq/Gemini
/app/diario → Diário emocional
/app/dashboard → Dashboard tempo real
/app/planos → Planos Free/Pro/Clinica
/app/login → Login/Cadastro JWT
/docs → Swagger UI FastAPI

## APIS PRINCIPAIS
POST /api/v1/chat-ia/mensagem → modelo=mistral-small (funcionando)
POST /api/v1/phq9-clinico/aplicar → PHQ-9 com scoring
POST /api/v1/gad7-clinico/aplicar → GAD-7 com scoring
POST /api/v1/auth/cadastrar → JWT token
POST /api/v1/auth/login → JWT token
GET  /api/v1/stripe/planos → planos
GET  /api/mobile/v1/sdk/config → mobile SDK
GET  /health → status JSON

## CHAT IA
- Mistral Small: FUNCIONANDO (principal)
- OpenRouter: backup
- Groq: configurado mas com issues
- Gemini: configurado

## main.py
- 64 linhas limpo
- lifespan=None (sem RecursionError)
- sys.setrecursionlimit(10000)
- Carga ANTES do FastAPI app
