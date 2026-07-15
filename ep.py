#!/usr/bin/env python3
"""
Emotion Platform CLI v2.0 — Central de Comando
════════════════════════════════════════════════
  python3 ep.py status     → status completo
  python3 ep.py health     → checa deploy
  python3 ep.py blocos     → fila de blocos
  python3 ep.py push "msg" → push seguro
  python3 ep.py lint       → ruff linter
  python3 ep.py test       → pytest
  python3 ep.py backup     → backup main.py
  python3 ep.py linhas     → conta linhas
  python3 ep.py monitor    → monitora deploy
  python3 ep.py modulos    → lista módulos
  python3 ep.py log        → últimos logs
  python3 ep.py size       → tamanho dos arquivos
  python3 ep.py git        → últimos commits
  python3 ep.py deps       → dependências
  python3 ep.py clean      → limpa cache
  python3 ep.py full       → tudo de uma vez
"""
import sys, os, subprocess, json, time
from datetime import datetime
from pathlib import Path

CMD = sys.argv[1] if len(sys.argv) > 1 else "status"
BASE = Path(__file__).parent

def run(cmd, capture=True):
    r = subprocess.run(cmd, shell=True, capture_output=capture, text=True, cwd=BASE)
    return r.stdout.strip() if capture else r.returncode

def sep(): print("─" * 40)

def header(titulo):
    print(f"\n{'═'*40}")
    print(f"  {titulo}")
    print(f"{'═'*40}")

if CMD == "status":
    header("EMOTION PLATFORM — STATUS v21.0")
    linhas = run("wc -l main.py").split()[0]
    templates = run("ls templates/*.html 2>/dev/null | wc -l")
    commits = run("git log --oneline 2>/dev/null | wc -l")
    branch = run("git branch --show-current 2>/dev/null")
    modulos = run("ls modules/*.py 2>/dev/null | wc -l")
    tamanho = run("du -sh main.py 2>/dev/null").split()[0]
    pendentes = 0
    if (BASE/"blocos_fila.json").exists():
        with open(BASE/"blocos_fila.json") as f:
            fila = json.load(f)
        pendentes = len([b for b in fila if b["status"]=="pendente"])
    print(f"  📄 main.py:      {linhas} linhas ({tamanho})")
    print(f"  📁 Templates:    {templates} HTML")
    print(f"  📦 Módulos:      {modulos} arquivos")
    print(f"  🔀 Branch:       {branch}")
    print(f"  📝 Commits:      {commits}")
    print(f"  ⏳ Blocos:       {pendentes} pendentes")
    print(f"  ⏰ Hora:         {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print("═"*40)

elif CMD == "health":
    import urllib.request
    URL = "https://emotion-platform-albert.onrender.com/health"
    try:
        with urllib.request.urlopen(URL, timeout=10) as r:
            d = json.loads(r.read())
        print(f"✅ {d.get('status')} | v{d.get('version')} | {d.get('usuarios')} users | {d.get('analises')} analises")
    except Exception as e:
        print(f"❌ Deploy com problema: {e}")

elif CMD == "blocos":
    if (BASE/"blocos_fila.json").exists():
        with open(BASE/"blocos_fila.json") as f:
            fila = json.load(f)
        p = [b for b in fila if b["status"]=="pendente"]
        c = [b for b in fila if b["status"]=="concluido"]
        header(f"BLOCOS — {len(c)} OK | {len(p)} pendentes")
        for b in p[:10]:
            print(f"  [{b['numero']:3}] {b['nome']}")
        if len(p) > 10:
            print(f"  ... +{len(p)-10} mais")
        print("═"*40)

elif CMD == "push":
    msg = " ".join(sys.argv[2:]) or f"update {datetime.now().strftime('%d/%m %H:%M')}"
    os.system(f'make push MSG="{msg}"')

elif CMD == "lint":
    os.system("make lint")

elif CMD == "test":
    os.system("pytest tests/ -v --tb=short --cov=. --cov-report=term-missing")

elif CMD == "backup":
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.system(f"cp main.py backups/main_{ts}.py")
    os.system("cp main.py main.py.bak")
    print(f"✅ Backup: backups/main_{ts}.py")

elif CMD == "linhas":
    r = run("wc -l main.py")
    print(f"📄 {r}")

elif CMD == "monitor":
    print("👁️  Monitorando a cada 5min... (Ctrl+C para parar)")
    os.system("python3 monitor.py --watch")

elif CMD == "modulos":
    header("MÓDULOS DISPONÍVEIS")
    for f in sorted((BASE/"modules").glob("*.py")):
        size = f.stat().st_size
        print(f"  📦 {f.name:<30} ({size:,} bytes)")
    print("═"*40)

elif CMD == "log":
    if (BASE/"autopilot.log").exists():
        os.system("tail -20 autopilot.log")
    else:
        print("Sem logs ainda")

elif CMD == "size":
    header("TAMANHO DOS ARQUIVOS")
    os.system("du -sh main.py modules/ templates/ 2>/dev/null | sort -h")
    print("═"*40)

elif CMD == "git":
    header("ÚLTIMOS 10 COMMITS")
    os.system("git log --oneline -10")
    print("═"*40)

elif CMD == "deps":
    os.system("pip list | grep -E 'fastapi|groq|mistral|cohere|together|langchain|ruff|pytest'")

elif CMD == "clean":
    os.system("find . -name '__pycache__' -exec rm -rf {} + 2>/dev/null")
    os.system("find . -name '*.pyc' -delete 2>/dev/null")
    print("✅ Cache limpo")

elif CMD == "full":
    print("🚀 Rodando validação completa...")
    os.system("make full")

else:
    print(__doc__)
