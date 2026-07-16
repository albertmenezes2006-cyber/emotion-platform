# EMOTION PLATFORM v24.3.0 — CONTEXTO v26

## SITE ONLINE
https://emotion-platform-albert.onrender.com

## CREDENCIAIS
API_KEY    = rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK
SERVICE_ID = srv-d97vrmcs728c73ci1mig
JWT_SECRET = 01356f6bd4852f675e8d9e9abaf9c98383eba11ca35bfac08aa96f303cd33b71

## STATUS ATUAL
- Plugins: 1.481 (100.7%)
- Score: 100%
- Deploy: ESTÁVEL
- Chat IA: Mistral Small (funcionando)
- Páginas: 9/9 OK

## PÁGINAS
/ → Home dark theme moderna
/app/avaliacao → PHQ-9 + GAD-7 interativos
/app/chat → Chat Mistral PT-BR
/app/diario → Diário emocional
/app/dashboard → Dashboard tempo real
/app/planos → Free/Pro/Clínica
/app/login → Auth JWT
/docs → Swagger 1.448 endpoints

## CHAT IA (plugins/ia/chat_ia_real.py v5)
- Mistral Small: PRINCIPAL (funcionando)
- Cache inteligente (5 min TTL)
- Fallback 11 categorias terapêuticas
- Detecção de crise → CVV 188

## APIs PRINCIPAIS
POST /api/v1/chat-ia/mensagem → Mistral
POST /api/v1/phq9-clinico/aplicar → PHQ-9
POST /api/v1/gad7-clinico/aplicar → GAD-7
POST /api/v1/auth/cadastrar → JWT
POST /api/v1/auth/login → JWT
GET  /api/v1/stripe/planos → planos
GET  /api/mobile/v1/sdk/config → mobile

## main.py (64 linhas)
- lifespan=None
- sys.setrecursionlimit(10000)
- Carga plugins ANTES do FastAPI

## DEPLOY MANUAL
python3 -c "
import urllib.request, json
req = urllib.request.Request(
    'https://api.render.com/v1/services/srv-d97vrmcs728c73ci1mig/deploys',
    data=json.dumps({'clearCache':'do_not_clear'}).encode(), method='POST')
req.add_header('Authorization','Bearer rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK')
req.add_header('Content-Type','application/json')
with urllib.request.urlopen(req,timeout=30) as r:
    print(json.loads(r.read().decode()))
"

## PRÓXIMOS PASSOS
A) Stripe real → STRIPE_SECRET_KEY no Render
B) Domínio customizado
C) Marketing → primeiros usuários
D) App Mobile (SDK pronto)
E) Claude/GPT-4 → ANTHROPIC_API_KEY / OPENAI_API_KEY
