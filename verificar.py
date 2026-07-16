#!/usr/bin/env python3
# cd ~/emotion_platform && source venv/bin/activate && python3 verificar.py
import urllib.request
import urllib.error
BASE = "https://emotion-platform-albert.onrender.com"
testes = [('/health', 'Core'), ('/api/v1/auth/status', 'Auth JWT'), ('/api/v1/auth-pg/status', 'Auth PostgreSQL ⭐'), ('/api/v1/analytics/status', 'Analytics GA4 ⭐'), ('/api/v1/stripe/planos', 'Stripe original'), ('/api/v1/stripe-checkout/planos', 'Stripe Checkout ⭐'), ('/api/v1/stripe-checkout/configuracao', 'Stripe Config ⭐'), ('/api/v1/acessibilidade/status', 'WCAG 100% ⭐'), ('/api/v1/phq9-clinico/perguntas', 'PHQ-9'), ('/api/v1/gad7-clinico/perguntas', 'GAD-7'), ('/static/wcag.js', 'Static wcag.js ⭐'), ('/static/wcag.css', 'Static wcag.css ⭐'), ('/docs', 'Swagger'), ('/sitemap.xml', 'Sitemap')]
ok = 0
for ep, nome in testes:
    try:
        urllib.request.urlopen(BASE+ep, timeout=15)
        print(f"  ✅ {nome:35} {ep}")
        ok += 1
    except urllib.error.HTTPError as e:
        print(f"  ❌ {nome:35} {ep} → HTTP {e.code}")
    except Exception as e:
        print(f"  ❌ {nome:35} {ep} → {str(e)[:30]}")
print(f"\n  {ok}/{len(testes)} OK")
