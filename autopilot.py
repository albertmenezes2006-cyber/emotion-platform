#!/usr/bin/env python3
"""
Emotion Intelligence Platform — Autopilot v1.0
Aplica blocos automaticamente e notifica no Telegram.
Uso: python3 autopilot.py
"""
import os
import sys
import json
import time
import subprocess
import py_compile
from datetime import datetime
from pathlib import Path

# ── Config
MAIN = Path(__file__).parent / "main.py"
BLOCOS_FILE = Path(__file__).parent / "blocos_fila.json"
LOG_FILE = Path(__file__).parent / "autopilot.log"
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8909749074:AAGNoB-JPZVC0Vl1dYeiN__1ktxza6GZ0s4")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "7757404855")
MARKER = '@app.get("/terapia", response_class=HTMLResponse)'

def log(msg: str):
    ts = datetime.now().strftime("%d/%m %H:%M:%S")
    linha = f"[{ts}] {msg}"
    print(linha)
    with open(LOG_FILE, "a") as f:
        f.write(linha + "\n")

def telegram(msg: str):
    try:
        import urllib.request
        import urllib.parse
        data = urllib.parse.urlencode({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data=data
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception as e:
        log(f"Telegram erro: {e}")

def backup():
    bak = str(MAIN) + ".bak"
    with open(MAIN, "r") as f:
        content = f.read()
    with open(bak, "w") as f:
        f.write(content)
    return content

def contar_linhas():
    with open(MAIN, "r") as f:
        return len(f.readlines())

def validar_sintaxe():
    try:
        py_compile.compile(str(MAIN), doraise=True)
        return True, ""
    except py_compile.PyCompileError as e:
        return False, str(e)

def restaurar_backup():
    bak = str(MAIN) + ".bak"
    if os.path.exists(bak):
        with open(bak, "r") as f:
            content = f.read()
        with open(MAIN, "w") as f:
            f.write(content)
        log("🔄 Backup restaurado")

def git_push(msg: str):
    try:
        subprocess.run(["git", "add", "."], cwd=MAIN.parent, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", msg], cwd=MAIN.parent, check=True, capture_output=True)
        subprocess.run(["git", "push"], cwd=MAIN.parent, check=True, capture_output=True)
        return True
    except Exception as e:
        log(f"Git erro: {e}")
        return False

def aplicar_bloco(bloco: dict) -> bool:
    numero = bloco.get("numero", "?")
    nome = bloco.get("nome", "")
    codigo = bloco.get("codigo", "")

    log(f"▶ Aplicando Bloco {numero} — {nome}")

    if not codigo.strip():
        log(f"⚠️  Bloco {numero} sem código — pulando")
        return False

    content = backup()
    linhas_antes = contar_linhas()

    if MARKER not in content:
        log(f"❌ Marker não encontrado")
        telegram(f"❌ *Bloco {numero} falhou*\nMarker não encontrado")
        return False

    marker_check = f"BLOCO {numero}/32500"
    if marker_check in content:
        log(f"⚠️  Bloco {numero} já aplicado — pulando")
        return True

    novo_content = content.replace(MARKER, codigo + "\n\n" + MARKER, 1)

    with open(MAIN, "w") as f:
        f.write(novo_content)

    ok, erro = validar_sintaxe()
    if not ok:
        log(f"❌ Sintaxe inválida: {erro}")
        restaurar_backup()
        telegram(
            f"❌ *Bloco {numero} — ERRO*\n"
            f"Nome: {nome}\n"
            f"Erro: `{erro[:200]}`\n"
            f"Backup restaurado automaticamente"
        )
        return False

    linhas_depois = contar_linhas()
    delta = linhas_depois - linhas_antes

    push_ok = git_push(f"feat: Bloco {numero}/32500 — {nome}")

    if push_ok:
        log(f"✅ Bloco {numero} aplicado e publicado!")
        telegram(
            f"✅ *Bloco {numero}/32500 aplicado!*\n"
            f"Nome: {nome}\n"
            f"Linhas: {linhas_antes:,} → {linhas_depois:,} (+{delta})\n"
            f"Deploy: em andamento no Render\n"
            f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
        )
    else:
        log(f"✅ Bloco {numero} aplicado (push falhou)")
        telegram(
            f"⚠️ *Bloco {numero} aplicado mas push falhou*\n"
            f"Rode: git push manualmente"
        )
    return True

def carregar_fila() -> list:
    if not BLOCOS_FILE.exists():
        log("⚠️  blocos_fila.json não encontrado — criando exemplo")
        exemplo = [
            {
                "numero": 4,
                "nome": "Especialidades Sofia",
                "status": "pendente",
                "codigo": "# Bloco 4 — cole o código aqui"
            }
        ]
        with open(BLOCOS_FILE, "w") as f:
            json.dump(exemplo, f, indent=2, ensure_ascii=False)
        return exemplo
    with open(BLOCOS_FILE, "r") as f:
        return json.load(f)

def salvar_fila(fila: list):
    with open(BLOCOS_FILE, "w") as f:
        json.dump(fila, f, indent=2, ensure_ascii=False)

def main():
    log("═" * 50)
    log("  AUTOPILOT v1.0 — Emotion Platform")
    log("═" * 50)

    telegram(
        f"🤖 *Autopilot iniciado*\n"
        f"Linhas atuais: {contar_linhas():,}\n"
        f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
    )

    fila = carregar_fila()
    pendentes = [b for b in fila if b.get("status") == "pendente"]

    log(f"📋 {len(pendentes)} blocos pendentes na fila")

    if not pendentes:
        log("✅ Nenhum bloco pendente")
        telegram("✅ *Autopilot* — Nenhum bloco pendente na fila")
        return

    sucesso = 0
    falha = 0

    for bloco in pendentes:
        ok = aplicar_bloco(bloco)
        idx = next(i for i, b in enumerate(fila) if b["numero"] == bloco["numero"])
        if ok:
            fila[idx]["status"] = "concluido"
            fila[idx]["concluido_em"] = datetime.now().isoformat()
            sucesso += 1
        else:
            fila[idx]["status"] = "erro"
            falha += 1
        salvar_fila(fila)
        if len(pendentes) > 1:
            log("⏳ Aguardando 10s antes do próximo bloco...")
            time.sleep(10)

    log("═" * 50)
    log(f"RESULTADO: {sucesso} OK | {falha} erros")
    log("═" * 50)

    telegram(
        f"🏁 *Autopilot finalizado*\n"
        f"✅ Sucesso: {sucesso} blocos\n"
        f"❌ Erros: {falha} blocos\n"
        f"Linhas finais: {contar_linhas():,}\n"
        f"⏰ {datetime.now().strftime('%d/%m %H:%M')}"
    )

if __name__ == "__main__":
    main()
