"""Plugin: Doacao / Tip Jar"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/doacao", tags=["Monetizacao"])
BASE   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")
SK     = os.getenv("STRIPE_SECRET_KEY", "")

class DoacaoReq(BaseModel):
    email:    str
    nome:     str = "Apoiador"
    valor:    int = 1000
    mensagem: str = ""

@router.post("/criar")
async def criar(req: DoacaoReq):
    if req.valor < 100:
        raise HTTPException(400, "Valor minimo R$ 1,00")
    if not SK:
        return {"msg": "Obrigado " + req.nome + "! Stripe nao configurado ainda."}
    try:
        import stripe
        stripe.api_key = SK
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            customer_email=req.email,
            line_items=[{"price_data": {
                "currency": "brl",
                "unit_amount": req.valor,
                "product_data": {"name": "Apoio — Emotion Platform",
                                 "description": req.mensagem or "Obrigado pelo apoio!"}
            }, "quantity": 1}],
            mode="payment",
            success_url=BASE + "/api/v1/doacao/obrigado?nome=" + req.nome,
            cancel_url=BASE + "/api/v1/doacao/page",
        )
        return {"checkout_url": session.url, "valor": f"R$ {req.valor/100:.2f}",
                "msg": "Obrigado " + req.nome + "!"}
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get("/page", response_class=HTMLResponse)
async def pagina():
    html = """<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8">
<title>Apoiar — Emotion Platform</title>
<style>
body { font-family: system-ui; background: #0f172a; color: #e2e8f0;
       display: flex; align-items: center; justify-content: center;
       min-height: 100vh; padding: 20px; }
.c { max-width: 600px; width: 100%; text-align: center; }
h1 { color: #7c3aed; }
p { color: #64748b; }
.grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; margin: 30px 0; }
.btn-val { background: #1e293b; border: 2px solid #334155; border-radius: 12px;
           padding: 20px; cursor: pointer; color: white; font-size: 16px; }
.btn-val:hover { border-color: #7c3aed; }
input { background: #1e293b; border: 1px solid #334155; border-radius: 8px;
        padding: 12px; color: white; width: 100%; margin: 8px 0; font-size: 16px; }
.btn { background: #7c3aed; color: white; border: none; border-radius: 8px;
       padding: 14px 28px; font-size: 16px; cursor: pointer; width: 100%; margin-top: 16px; }
</style></head><body><div class="c">
<div style="font-size:60px">💜</div>
<h1>Apoiar o Emotion Platform</h1>
<p>Sua contribuicao ajuda a manter a plataforma gratuita para quem precisa!</p>
<div class="grid">
  <button class="btn-val" onclick="setVal(500)">☕<br><strong>R$ 5</strong><br><small>Um cafe</small></button>
  <button class="btn-val" onclick="setVal(1000)">🍕<br><strong>R$ 10</strong><br><small>Uma pizza</small></button>
  <button class="btn-val" onclick="setVal(2000)">🎯<br><strong>R$ 20</strong><br><small>Apoio mensal</small></button>
  <button class="btn-val" onclick="setVal(5000)">🚀<br><strong>R$ 50</strong><br><small>Super apoio</small></button>
  <button class="btn-val" onclick="setVal(10000)">🏆<br><strong>R$ 100</strong><br><small>Heroi</small></button>
  <button class="btn-val" onclick="setVal(0)">💰<br><strong>Outro</strong><br><small>Voce decide</small></button>
</div>
<input type="number" id="valor" placeholder="Valor em R$" value="10">
<input type="email" id="email" placeholder="Seu email">
<input type="text"  id="nome"  placeholder="Seu nome (opcional)">
<button class="btn" onclick="doar()">💜 Apoiar Agora</button>
<script>
var val = 1000;
function setVal(v) {
  val = v;
  if (v > 0) document.getElementById("valor").value = v/100;
}
function doar() {
  var email = document.getElementById("email").value;
  var vInput = parseFloat(document.getElementById("valor").value) * 100;
  var finalVal = vInput || val;
  if (!email) { alert("Digite seu email!"); return; }
  fetch("/api/v1/doacao/criar", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({email: email, nome: document.getElementById("nome").value || "Apoiador", valor: finalVal})
  }).then(r => r.json()).then(d => {
    if (d.checkout_url) window.location = d.checkout_url;
    else alert(d.msg);
  });
}
</script>
</div></body></html>"""
    return HTMLResponse(html)

@router.get("/obrigado", response_class=HTMLResponse)
async def obrigado(nome: str = "Apoiador"):
    return HTMLResponse(f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>Obrigado!</title>
<style>body{{font-family:system-ui;background:#0f172a;color:#e2e8f0;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;}}
h1{{color:#7c3aed;}}a{{color:#7c3aed;}}</style></head>
<body><div><div style="font-size:80px">💜</div>
<h1>Obrigado, {nome}!</h1>
<p>Voce e incrivel! Seu apoio mantem a plataforma gratuita.</p>
<br><a href="/">Voltar ao site</a></div></body></html>""")

@router.get("/status")
async def status():
    return {"status": "online", "pagina": BASE + "/api/v1/doacao/page",
            "stripe_ok": bool(SK), "valores": ["R$5","R$10","R$20","R$50","R$100"]}

class DoacaoPlugin(PluginBase):
    name = "doacao"
    version = "1.0.0"
    description = "Pagina de doacao tip jar"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info("[Doacao] OK")
    def health_check(self):
        return {"status": "healthy"}

plugin = DoacaoPlugin()
