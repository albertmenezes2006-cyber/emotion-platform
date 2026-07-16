#!/usr/bin/env python3
"""
Keep-alive para o Render free tier
Faz ping a cada 14 min para não dormir
Execute em background: nohup python3 keepalive.py &
"""
import time, urllib.request, datetime

URL = "https://emotion-platform-albert.onrender.com/health"
INTERVALO = 14 * 60  # 14 minutos

while True:
    try:
        with urllib.request.urlopen(URL, timeout=30) as r:
            status = r.status
            print(f"[{datetime.datetime.now().strftime('%H:%M')}] Ping OK — HTTP {status}")
    except Exception as e:
        print(f"[{datetime.datetime.now().strftime('%H:%M')}] Ping falhou: {e}")
    time.sleep(INTERVALO)
