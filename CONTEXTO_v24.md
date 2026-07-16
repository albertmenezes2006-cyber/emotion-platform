# EMOTION PLATFORM v24.0 — CONTEXTO ATUALIZADO

## URLS CORRETAS (prefixo /ep/)
Base: https://emotion-platform-albert.onrender.com

### Páginas
- /ep/app/avaliacao  → PHQ-9 + GAD-7
- /ep/app/chat       → Chat IA
- /ep/app/diario     → Diário emocional
- /ep/app/dashboard  → Dashboard
- /ep/app/planos     → Planos Stripe
- /ep/app/login      → Login/Cadastro
- /ep/docs           → API Docs 1477 plugins

### APIs
- GET  /ep/health
- GET  /ep/api/v1/phq9/perguntas
- POST /ep/api/v1/phq9/aplicar?user_id=X
- GET  /ep/api/v1/gad7/perguntas
- POST /ep/api/v1/gad7/aplicar?user_id=X
- POST /ep/api/v1/chat-ia/mensagem?user_id=X&mensagem=Y
- POST /ep/api/v1/multi-llm/chat?mensagem=X&user_id=Y
- POST /ep/api/v1/auth/cadastrar?nome=X&email=Y&senha=Z&tipo=W
- POST /ep/api/v1/auth/login?email=X&senha=Y
- GET  /ep/api/v1/auth/me (Bearer token)
- GET  /ep/api/v1/stripe/planos
- GET  /ep/api/mobile/v1/sdk/config
- POST /ep/api/v1/diario-emocional/entrada

### Por que /ep/?
O main.py original (v20) já tem rotas /api/v1/* e catch-all.
Os plugins estão montados como sub-aplicação em /ep/
para evitar conflito.

## ARQUITETURA
- main.py (v20) → roda em /
- plugins/ → montados em /ep/ via create_plugin_app()
- loader.py → create_plugin_app() cria FastAPI separada

## STATUS
- 1477 plugins OK
- 11/11 endpoints /ep/ funcionando
- Chat IA: Groq + Gemini + fallback
- Auth JWT funcionando
- Stripe planos configurados
- Mobile API pronta
- Multi-LLM: 6 modelos
