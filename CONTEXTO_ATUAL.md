# EMOTION INTELLIGENCE PLATFORM v24.3.0 — CONTEXTO

## CREDENCIAIS RENDER
API_KEY    = rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK
SERVICE_ID = srv-d97vrmcs728c73ci1mig
JWT_SECRET = 01356f6bd4852f675e8d9e9abaf9c98383eba11ca35bfac08aa96f303cd33b71

## SITE ONLINE
https://emotion-platform-albert.onrender.com

## STATUS
- Versão: 24.3.0
- Plugins: 1.481 (100.7% da meta)
- Rotas: 1.448
- Score: 100%
- Deploy: ESTÁVEL

## main.py (64 linhas — NÃO MODIFICAR MANUALMENTE)
- lifespan=None (evita RecursionError no Python 3.14)
- sys.setrecursionlimit(10000)
- Carrega plugins ANTES do app FastAPI
- Catch RecursionError por plugin

## ARQUITETURA
emotion_platform/
├── main.py                 ← 64 linhas LIMPO
├── plugins/                ← 1.481 plugins em 109 categorias
│   ├── plugin_base.py      ← classe base
│   ├── db_manager.py       ← PostgreSQL + SQLite
│   ├── loader.py           ← carregamento universal
│   ├── avaliacao_psicologica/
│   │   ├── phq9_real.py    ← /api/v1/phq9-clinico/
│   │   └── gad7_real.py    ← /api/v1/gad7-clinico/
│   ├── ia/chat_ia_real.py  ← /api/v1/chat-ia/
│   ├── auth_real/          ← /api/v1/auth/
│   ├── monetizacao_real/   ← /api/v1/stripe/
│   ├── mobile_api/         ← /api/mobile/v1/
│   └── ia_avancada/        ← /api/v1/multi-llm/
├── static/css/emotion.css  ← design system
├── templates/              ← 6 páginas HTML
└── Procfile                ← uvicorn main:app

## URLs FUNCIONANDO
/health                              → JSON status v24.3
/ping                                → JSON pong
/docs                                → API Docs 1448 rotas
/api/v1/phq9-clinico/perguntas       → PHQ-9 perguntas
/api/v1/phq9-clinico/aplicar         → POST List[int] 9 respostas
/api/v1/gad7-clinico/perguntas       → GAD-7 perguntas
/api/v1/gad7-clinico/aplicar         → POST List[int] 7 respostas
/api/v1/chat-ia/mensagem             → POST chat Groq/Gemini
/api/v1/chat-ia/modelos/disponiveis  → GET modelos
/api/v1/stripe/planos                → GET planos Free/Pro/Clinica
/api/v1/auth/cadastrar               → POST JWT token
/api/v1/auth/login                   → POST JWT token
/api/v1/auth/me                      → GET Bearer token
/api/v1/multi-llm/chat               → POST 6 modelos
/api/mobile/v1/sdk/config            → GET config SDK
/app/avaliacao                       → HTML PHQ-9 + GAD-7
/app/chat                            → HTML Chat IA
/app/diario                          → HTML Diário
/app/planos                          → HTML Planos + Stripe
/app/login                           → HTML Login/Cadastro
/app/dashboard                       → HTML Dashboard

## IAs CONFIGURADAS
[OK] Groq LLaMA3 (GROQ_API_KEY configurado)
[OK] Google Gemini (GEMINI_API_KEY configurado)
[OK] Mistral (MISTRAL_API_KEY configurado)
[OK] OpenRouter 250+ modelos (OPENROUTER_API_KEY configurado)
[--] Claude (falta ANTHROPIC_API_KEY)
[--] GPT-4 (falta OPENAI_API_KEY)

## PLANOS STRIPE
- free:      Gratuito (5 avaliações/mês)
- pro:       R$ 49,90/mês (ilimitado)
- clinica:   R$ 199,90/mês (50 terapeutas)
- enterprise: Sob consulta

## DEPLOY
- Render.com — uvicorn main:app --host 0.0.0.0 --port $PORT
- Auto-deploy no push para main
- Para deploy manual: python3 -c "
  import urllib.request, json
  req = urllib.request.Request(
      'https://api.render.com/v1/services/srv-d97vrmcs728c73ci1mig/deploys',
      data=json.dumps({'clearCache':'do_not_clear'}).encode(), method='POST')
  req.add_header('Authorization', 'Bearer rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK')
  req.add_header('Content-Type', 'application/json')
  with urllib.request.urlopen(req, timeout=30) as r:
      print(json.loads(r.read().decode()))
  "

## COMANDOS ESSENCIAIS
python3 status_plugins.py       → ver todos os 1481 plugins
python3 -m py_compile main.py   → verificar main.py
git add -A && git commit --no-verify -m "msg" && git push → deploy

## PRÓXIMOS PASSOS
A) Stripe real: adicionar STRIPE_SECRET_KEY no Render
B) Claude: adicionar ANTHROPIC_API_KEY no Render
C) GPT-4: adicionar OPENAI_API_KEY no Render
D) Marketing: Product Hunt, LinkedIn, grupos psicologia
E) App Mobile: React Native/Flutter (SDK pronto em /api/mobile/v1/)
