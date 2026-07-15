#!/usr/bin/env python3
"""Monitor de saúde do deploy — Emotion Platform"""
import urllib.request, json, sys, time, os
from datetime import datetime

URL   = "https://emotion-platform-albert.onrender.com/health"
TOKEN = os.getenv("TELEGRAM_TOKEN","8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
CHAT  = os.getenv("TELEGRAM_CHAT_ID","7757404855")

def check():
    try:
        with urllib.request.urlopen(URL, timeout=10) as r:
            d = json.loads(r.read())
        s = d.get("status","?")
        v = d.get("version","?")
        u = d.get("usuarios",0)
        a = d.get("analises",0)
        ts = datetime.now().strftime("%d/%m %H:%M")
        e = "✅" if s=="healthy" else "❌"
        print(f"{e} [{ts}] {s} | v{v} | {u} users | {a} analises")
        return s == "healthy", d
    except Exception as ex:
        print(f"❌ [{datetime.now().strftime('%d/%m %H:%M')}] {ex}")
        return False, {}

def notify(msg):
    try:
        import urllib.parse
        data = urllib.parse.urlencode({"chat_id":CHAT,"text":msg,"parse_mode":"Markdown"}).encode()
        urllib.request.urlopen(f"https://api.telegram.org/bot{TOKEN}/sendMessage",data=data,timeout=5)
    except: pass

if "--watch" in sys.argv:
    print("👁️  Monitorando... (Ctrl+C para parar)")
    falhas = 0
    ultimo_users = 0
    while True:
        ok, data = check()
        if not ok:
            falhas += 1
            if falhas >= 2:
                notify(f"🚨 *Deploy com problema!*\nVerifique o Render!")
                falhas = 0
        else:
            falhas = 0
            users = data.get("usuarios",0)
            if users > ultimo_users:
                notify(f"🎉 *Novo usuário!* Total: {users}")
            ultimo_users = users
        time.sleep(300)
else:
    check()
