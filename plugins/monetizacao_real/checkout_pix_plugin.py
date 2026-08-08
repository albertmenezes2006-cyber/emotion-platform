import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
import qrcode
import io
import base64
import httpx
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/checkout", tags=["Checkout"])

PIX_KEY = "albertmenezes2006@gmail.com"
PIX_NAME = "Albert Menezes"
PIX_CITY = "Tobias Barreto"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

PLANOS = {
    "teste": {"nome": "Teste", "valor": 1.00},
    "pro": {"nome": "Pro", "valor": 29.90},
    "clinica": {"nome": "Clinica", "valor": 99.90}
}

def campo(id, valor):
    return f"{id}{len(valor):02d}{valor}"

def gerar_payload_pix(valor, descricao="EmotionAI"):
    merchant = campo("00", "BR.GOV.BCB.PIX") + campo("01", PIX_KEY)
    payload = (
        campo("00", "01") +
        campo("26", merchant) +
        campo("52", "0000") +
        campo("53", "986") +
        campo("54", f"{valor:.2f}") +
        campo("58", "BR") +
        campo("59", PIX_NAME[:25]) +
        campo("60", PIX_CITY[:15]) +
        campo("62", campo("05", descricao[:25]))
    )
    crc = "6304"
    payload += crc
    crc_val = 0xFFFF
    for c in (payload).encode():
        crc_val ^= c << 8
        for _ in range(8):
            crc_val = (crc_val << 1) ^ 0x1021 if crc_val & 0x8000 else crc_val << 1
            crc_val &= 0xFFFF
    return payload + f"{crc_val:04X}"

def gerar_qr(payload):
    qr = qrcode.make(payload)
    buf = io.BytesIO()
    qr.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

async def alertar_telegram(plano, valor, email=""):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return
    msg = f"🔔 NOVO CHECKOUT PIX\n\nPlano: {plano}\nValor: R$ {valor:.2f}\nEmail: {email}\n\nVerifique o pagamento e libere o acesso!"
    try:
        async with httpx.AsyncClient() as client:
            await client.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                json={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
            )
    except:
        pass

@router.get("/pix/{plano}")
async def checkout_pix(plano: str, email: str = "", request: Request = None):
    from fastapi.responses import RedirectResponse
    # Verifica se veio email (do usuário logado)
    if not email and plano != "teste":
        return RedirectResponse(url="/app/login?redirect=/planos", status_code=302)

    p = PLANOS.get(plano, PLANOS["pro"])
    valor = p["valor"]
    nome = p["nome"]
    payload = gerar_payload_pix(valor, f"EmotionAI{nome}")
    qr_b64 = gerar_qr(payload)
    await alertar_telegram(nome, valor, email)
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pagar com PIX — EmotionAI {nome}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,sans-serif;background:#0f172a;color:#fff;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:20px}}
.card{{background:#1e293b;border-radius:20px;padding:40px;max-width:420px;width:100%;text-align:center;box-shadow:0 25px 50px rgba(0,0,0,0.5)}}
.logo{{font-size:48px;margin-bottom:10px}}
h1{{font-size:24px;margin-bottom:5px;color:#e2e8f0}}
.plano{{background:linear-gradient(135deg,#6366f1,#8b5cf6);padding:8px 20px;border-radius:20px;display:inline-block;font-size:14px;font-weight:600;margin:10px 0}}
.valor{{font-size:42px;font-weight:800;color:#10b981;margin:15px 0}}
.qr-box{{background:#fff;border-radius:15px;padding:15px;margin:20px 0}}
.qr-box img{{width:100%;max-width:220px}}
.pix-code{{background:#0f172a;border-radius:10px;padding:12px;font-size:11px;word-break:break-all;color:#94a3b8;margin:10px 0;text-align:left}}
.btn{{background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border:none;padding:15px 30px;border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;width:100%;margin:10px 0}}
.btn:hover{{opacity:0.9}}
.steps{{text-align:left;background:#0f172a;border-radius:12px;padding:15px;margin:15px 0}}
.steps li{{padding:5px 0;color:#94a3b8;font-size:14px}}
.seguro{{color:#64748b;font-size:12px;margin-top:15px}}
.copiado{{display:none;color:#10b981;font-size:14px;margin:5px 0}}
</style>
</head>
<body>
<div class="card">
  <div class="logo">⚡</div>
  <h1>EmotionAI</h1>
  <div class="plano">Plano {nome}</div>
  <div class="valor">R$ {valor:.2f}<span style="font-size:16px;color:#64748b">/mês</span></div>
  <div class="qr-box">
    <img src="data:image/png;base64,{qr_b64}" alt="QR Code PIX">
  </div>
  <p style="color:#94a3b8;font-size:13px;margin-bottom:8px">Ou copie o código PIX:</p>
  <div class="pix-code" id="pix-code">{payload}</div>
  <button class="btn" onclick="copiar()">📋 Copiar código PIX</button>
  <div class="copiado" id="copiado">✅ Copiado! Agora abra seu banco e pague.</div>
  <div class="steps">
    <ol>
      <li>📱 Abra o app do seu banco</li>
      <li>🔍 Vá em PIX → Pagar → Copia e Cola</li>
      <li>📋 Cole o código acima</li>
      <li>✅ Confirme o pagamento</li>
      <li>🚀 Acesso liberado em até 1 hora</li>
    </ol>
  </div>
  <p class="seguro">🔒 Pagamento 100% seguro via PIX Banco Central</p>
</div>
<script>
function copiar(){{
  navigator.clipboard.writeText(document.getElementById("pix-code").innerText);
  document.getElementById("copiado").style.display="block";
  setTimeout(()=>document.getElementById("copiado").style.display="none", 4000);
}}
</script>
</body>
</html>"""
    return HTMLResponse(html)

class CheckoutPixPlugin(PluginBase):
    name = "checkout_pix_plugin"
    def setup(self, app):
        app.include_router(router)

plugin = CheckoutPixPlugin()
