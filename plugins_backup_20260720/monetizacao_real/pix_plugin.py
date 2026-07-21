#!/usr/bin/env python3
"""PIX integrado — pagamento instantâneo brasileiro"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from plugins.plugin_base import PluginBase
import qrcode
import io
import base64

router = APIRouter(prefix="/api/v1/pix", tags=["PIX"])

# Payload PIX estático
PIX_KEY = "albertmenezes2006@gmail.com"
PIX_NAME = "Albert Menezes"
PIX_CITY = "Sao Paulo"

def gerar_payload_pix(valor: float, descricao: str = "Emotion Platform") -> str:
    """Gera payload PIX Copia e Cola"""
    
    def campo(id: str, valor: str) -> str:
        tamanho = str(len(valor)).zfill(2)
        return f"{id}{tamanho}{valor}"
    
    merchant_account = (
        campo("00", "BR.GOV.BCB.PIX") +
        campo("01", PIX_KEY)
    )
    
    valor_str = f"{valor:.2f}"
    nome_limpo = PIX_NAME[:25]
    cidade_limpa = PIX_CITY[:15]
    desc_limpa = descricao[:20].replace(" ", "")
    
    payload = (
        campo("00", "01") +
        campo("26", merchant_account) +
        "52040000" +
        "5303986" +
        campo("54", valor_str) +
        "5802BR" +
        campo("59", nome_limpo) +
        campo("60", cidade_limpa) +
        campo("62", campo("05", desc_limpa))
    )
    
    # CRC16
    def crc16(data: str) -> str:
        crc = 0xFFFF
        for char in data:
            crc ^= ord(char) << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc <<= 1
                crc &= 0xFFFF
        return format(crc, '04X')
    
    payload_sem_crc = payload + "6304"
    return payload_sem_crc + crc16(payload_sem_crc)

def gerar_qr_pix(payload: str) -> str:
    """Gera QR Code do PIX em base64"""
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

@router.get("/gerar/{valor}")
async def gerar_pix(valor: float, descricao: str = "EmotionPlatform"):
    payload = gerar_payload_pix(valor, descricao)
    qr_base64 = gerar_qr_pix(payload)
    return JSONResponse({
        "payload": payload,
        "qr_code": f"data:image/png;base64,{qr_base64}",
        "valor": valor,
        "chave": PIX_KEY,
        "nome": PIX_NAME
    })

@router.get("/pagar/{valor}", response_class=HTMLResponse)
async def pagina_pix(valor: float, descricao: str = "EmotionPlatform"):
    payload = gerar_payload_pix(valor, descricao)
    qr_base64 = gerar_qr_pix(payload)
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagar com PIX — Emotion Platform</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .card {{
            background: white;
            border-radius: 24px;
            padding: 40px;
            max-width: 440px;
            width: 100%;
            text-align: center;
            box-shadow: 0 25px 50px rgba(0,0,0,0.2);
        }}
        .pix-logo {{
            font-size: 48px;
            margin-bottom: 8px;
        }}
        h1 {{
            color: #1a1a2e;
            font-size: 24px;
            margin-bottom: 8px;
        }}
        .valor {{
            font-size: 42px;
            font-weight: 800;
            color: #00B4D8;
            margin: 16px 0;
        }}
        .qr-container {{
            background: #f8f9fa;
            border-radius: 16px;
            padding: 20px;
            margin: 24px 0;
            border: 3px dashed #00B4D8;
        }}
        .qr-container img {{
            width: 200px;
            height: 200px;
            border-radius: 8px;
        }}
        .payload-box {{
            background: #f0f4ff;
            border-radius: 12px;
            padding: 16px;
            margin: 16px 0;
            word-break: break-all;
            font-size: 11px;
            color: #555;
            font-family: monospace;
            max-height: 80px;
            overflow: hidden;
        }}
        .btn-copiar {{
            background: linear-gradient(135deg, #00B4D8, #0077B6);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 16px 32px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            width: 100%;
            transition: transform 0.2s;
        }}
        .btn-copiar:hover {{ transform: translateY(-2px); }}
        .btn-copiar:active {{ transform: translateY(0); }}
        .instrucoes {{
            margin-top: 24px;
            text-align: left;
            color: #666;
            font-size: 14px;
        }}
        .instrucoes li {{
            padding: 6px 0;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .badge-seguro {{
            background: #e8f5e9;
            color: #2e7d32;
            border-radius: 20px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 600;
            display: inline-block;
            margin-top: 16px;
        }}
        .copiado {{
            display: none;
            color: #2e7d32;
            font-weight: 700;
            margin-top: 8px;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="pix-logo">⚡</div>
        <h1>Pagar com PIX</h1>
        <p style="color:#888">Emotion Intelligence Platform</p>
        
        <div class="valor">R$ {valor:.2f}</div>
        
        <div class="qr-container">
            <img src="data:image/png;base64,{qr_base64}" alt="QR Code PIX">
            <p style="color:#888;font-size:13px;margin-top:8px">
                Escaneie com seu banco
            </p>
        </div>
        
        <p style="color:#666;font-size:14px;margin-bottom:8px">
            Ou copie o código PIX:
        </p>
        
        <div class="payload-box" id="payload">
            {payload}
        </div>
        
        <button class="btn-copiar" onclick="copiarPix()">
            📋 Copiar código PIX
        </button>
        
        <div class="copiado" id="copiado">
            ✅ Código copiado! Cole no seu banco.
        </div>
        
        <ol class="instrucoes">
            <li>📱 Abra seu banco</li>
            <li>🔍 Vá em PIX → Pagar</li>
            <li>📋 Cole o código ou escaneie o QR</li>
            <li>✅ Confirme o pagamento</li>
        </ol>
        
        <div class="badge-seguro">
            🔒 Pagamento 100% seguro via PIX
        </div>
    </div>
    
    <script>
        function copiarPix() {{
            const payload = document.getElementById('payload').textContent.trim();
            navigator.clipboard.writeText(payload).then(() => {{
                document.getElementById('copiado').style.display = 'block';
                document.querySelector('.btn-copiar').textContent = '✅ Copiado!';
                setTimeout(() => {{
                    document.getElementById('copiado').style.display = 'none';
                    document.querySelector('.btn-copiar').textContent = '📋 Copiar código PIX';
                }}, 3000);
            }});
        }}
    </script>
</body>
</html>"""
    return HTMLResponse(html)

class PixPlugin(PluginBase):
    name = "pix_plugin"
    def setup(self, app):
        app.include_router(router)

plugin = PixPlugin()
