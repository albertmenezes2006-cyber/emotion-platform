"""Página de sucesso após pagamento"""
import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/pagamento", tags=["Pagamento"])

@router.get("/sucesso", response_class=HTMLResponse)
async def sucesso(plano: str = "pro"):
    plano_nome = "Pro" if plano == "pro" else "Clinica" if plano == "clinica" else "Teste"
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pagamento Confirmado — EmotionAI</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,sans-serif;background:#0f172a;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}}
.card{{background:#1e293b;border-radius:20px;padding:50px 40px;max-width:480px;width:100%;text-align:center;box-shadow:0 25px 50px rgba(0,0,0,0.5)}}
.icon{{width:100px;height:100px;background:linear-gradient(135deg,#10b981,#059669);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:50px;margin:0 auto 25px;animation:pop 0.6s ease}}
@keyframes pop{{0%{{transform:scale(0)}}70%{{transform:scale(1.2)}}100%{{transform:scale(1)}}}}
h1{{font-size:28px;margin-bottom:15px}}
.plano{{background:linear-gradient(135deg,#6366f1,#8b5cf6);padding:10px 24px;border-radius:30px;display:inline-block;font-size:14px;font-weight:600;margin:15px 0}}
p{{color:#94a3b8;line-height:1.6;margin:10px 0;font-size:15px}}
.steps{{background:#0f172a;border-radius:12px;padding:20px;margin:25px 0;text-align:left}}
.steps h3{{font-size:14px;color:#e2e8f0;margin-bottom:12px;text-transform:uppercase;letter-spacing:1px}}
.steps li{{padding:6px 0;color:#94a3b8;font-size:14px;list-style:none}}
.btn{{background:linear-gradient(135deg,#6366f1,#8b5cf6);color:white;border:none;padding:15px 30px;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;width:100%;margin-top:20px;text-decoration:none;display:inline-block}}
.btn:hover{{opacity:0.9;transform:translateY(-2px)}}
.small{{color:#64748b;font-size:12px;margin-top:15px}}
</style>
</head>
<body>
<div class="card">
  <div class="icon">✓</div>
  <h1>Pagamento Confirmado!</h1>
  <div class="plano">Plano {plano_nome}</div>
  <p>Seu pagamento foi processado com sucesso.</p>
  <p>Recebemos a confirmação do Mercado Pago.</p>
  
  <div class="steps">
    <h3>🚀 Próximos passos</h3>
    <ul>
      <li>✅ Acesso ao plano {plano_nome} liberado</li>
      <li>📧 Confirmação enviada por email</li>
      <li>🎯 Acesse o dashboard e comece a usar</li>
    </ul>
  </div>
  
  <a href="/app/dashboard" class="btn">Acessar Dashboard →</a>
  <p class="small">Precisa de ajuda? Fale conosco no WhatsApp</p>
</div>
</body>
</html>"""
    return HTMLResponse(html)

@router.get("/aguardando", response_class=HTMLResponse)
async def aguardando():
    html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Aguardando Pagamento — EmotionAI</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,sans-serif;background:#0f172a;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}
.card{background:#1e293b;border-radius:20px;padding:50px 40px;max-width:480px;width:100%;text-align:center;box-shadow:0 25px 50px rgba(0,0,0,0.5)}
.icon{width:100px;height:100px;border:4px solid #f59e0b;border-top-color:transparent;border-radius:50%;margin:0 auto 25px;animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
h1{font-size:26px;margin-bottom:15px}
p{color:#94a3b8;line-height:1.6;margin:10px 0}
.btn{background:linear-gradient(135deg,#6366f1,#8b5cf6);color:white;border:none;padding:15px 30px;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;text-decoration:none;display:inline-block;margin-top:20px}
</style>
</head>
<body>
<div class="card">
  <div class="icon"></div>
  <h1>Aguardando Pagamento</h1>
  <p>Estamos aguardando a confirmação do PIX.</p>
  <p>Assim que confirmarmos, seu acesso será liberado automaticamente.</p>
  <a href="/app/dashboard" class="btn">Ir para o Dashboard</a>
</div>
</body>
</html>"""
    return HTMLResponse(html)

class PaymentSuccessPlugin(PluginBase):
    name = "payment_success"
    def setup(self, app):
        app.include_router(router)

plugin = PaymentSuccessPlugin()
