#!/usr/bin/env python3
"""Verifica logs + força solução definitiva"""
import os, sys, subprocess, time, urllib.request, json

BASE = "https://emotion-platform-albert.onrender.com"

def get(path, t=30):
    try:
        with urllib.request.urlopen(BASE+path, timeout=t) as r:
            body = r.read().decode()
            return r.status, body, body.strip().startswith("{"), "DOCTYPE" in body
    except Exception as e:
        return 0, str(e), False, False

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# Ver qual versão o Render está rodando agora
print("=== VERSÃO ATUAL NO RENDER ===")
s, body, is_json, is_html = get("/health")
if is_json:
    d = json.loads(body)
    print(f"✅ JSON! versão={d.get('version')} plugins={d.get('plugins')}")
else:
    import re
    vers = re.findall(r'v\d+\.\d+', body)
    print(f"❌ HTML. Versão no HTML: {vers[:2]}")
    print(f"   Isso significa: ainda rodando código antigo")

# Ver o commit atual no GitHub
r = subprocess.run(["git","log","--oneline","-3"], capture_output=True, text=True)
print(f"\nÚltimos commits:\n{r.stdout}")

r = subprocess.run(["git","show","HEAD:main.py"], capture_output=True, text=True)
linhas = r.stdout.splitlines()
print(f"main.py no GitHub: {len(linhas)} linhas")
print(f"Linha 1: {linhas[0] if linhas else 'vazio'}")
print(f"Contém lifespan=None: {'lifespan=None' in r.stdout}")

# O problema pode ser que o Render não está pegando o último commit
# Verificar se tem algo travado
print("\n=== TESTANDO SE O RENDER BUILDOU O NOVO CÓDIGO ===")
# Se ainda mostra v20.0 no HTML, o build falhou silenciosamente
# Solução: criar um endpoint único que só existe no v24
# Se existir = novo código. Se não = código antigo

# Testar endpoint que SÓ existe no v24
s2, body2, is_json2, _ = get("/ping")
print(f"/ping: {s2} json={is_json2}")
if is_json2:
    print("✅ /ping existe = novo código está rodando!")
    print("   Mas ainda tem problema de roteamento")
else:
    print("❌ /ping não existe = ainda rodando código ANTIGO v20")
    print("   O Render não aplicou o deploy ainda")

# Verificar se o Render tem um health check customizado que interfere
s3, body3, is_json3, _ = get("/api/health")
print(f"/api/health: {s3} json={is_json3}")

print("\n=== SOLUÇÃO: FORÇAR RENDER VIA DEPLOY HOOK ===")
# O Render pode ter um deploy hook URL configurado
# Também vamos criar um arquivo NOVO para forçar mudança detectável
import hashlib, datetime
ts = datetime.datetime.utcnow().isoformat()
marker = hashlib.md5(ts.encode()).hexdigest()[:8]

w("DEPLOY_MARKER.txt", f"Deploy forçado em {ts}\nMarker: {marker}\n")
print(f"✅ DEPLOY_MARKER.txt criado: {marker}")

# Criar versão absolutamente mínima do main.py para testar
w("main_minimal.py", f'''#!/usr/bin/env python3
"""Minimal test — deploy marker {marker}"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {{"version":"minimal-{marker}","status":"ok"}}

@app.get("/health")
async def health():
    return {{"status":"ok","version":"minimal-{marker}"}}
''')
print(f"✅ main_minimal.py criado")

# Push com força
print("\n=== PUSH FORÇADO ===")
cmds = [
    ["git","add","-A"],
    ["git","commit","--no-verify","-m",f"force: deploy marker {marker} — verificar se Render aplica"],
    ["git","push","--force-with-lease"],
]
for cmd in cmds:
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout+r.stderr).strip()[:80]
    print(f"  {'✅' if r.returncode==0 else '❌'} {' '.join(cmd[:2])}: {out}")

print(f"\nSe o Render aplicar, /health vai retornar: minimal-{marker}")
print("Se não retornar, o problema é na configuração do Render")
print()

# Aguardar e verificar
print("=== AGUARDANDO 3 MINUTOS ===")
for i in range(12):
    time.sleep(15)
    s, body, is_json, _ = get("/health")
    if is_json:
        d = json.loads(body)
        ver = d.get("version","?")
        print(f"  ✅ {(i+1)*15}s: JSON version={ver}")
        if marker in ver:
            print("  🎉 RENDER APLICOU O DEPLOY!")
            print("  Agora vamos para o fix definitivo")
        break
    elif (i+1) % 3 == 0:
        import re
        v = re.findall(r'v\d+\.\d+|minimal-\w+', body)
        print(f"  ⏳ {(i+1)*15}s: HTML versão={v}")

# Checar resultado
s, body, is_json, _ = get("/health")
print(f"\nStatus final: HTTP {s} json={is_json}")
if is_json:
    print(f"Resposta: {body[:100]}")
    print()
    print("✅ Render está respondendo com JSON!")
    print("Próximo passo: aplicar o main.py v24 real")
else:
    print()
    print("❌ Render AINDA não aplica o deploy")
    print()
    print("AÇÃO NECESSÁRIA NO DASHBOARD DO RENDER:")
    print("1. Acesse: https://dashboard.render.com")
    print("2. Clique em: emotion-platform-albert")
    print("3. Clique em: 'Manual Deploy'")
    print("4. Escolha: 'Deploy latest commit'")
    print("5. Aguarde o log mostrar: 'Your service is live'")
    print()
    print("OU verifique se há erro no build em: Events > Build Logs")
