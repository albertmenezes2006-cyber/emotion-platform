#!/usr/bin/env python3
import urllib.request
import urllib.error
import re

BASE = "https://emotion-platform-albert.onrender.com"

OK = 0
WARN = 0
ERR = 0


def ok_msg(msg):
    global OK
    OK += 1
    print(f"    OK   {msg}")


def warn_msg(msg):
    global WARN
    WARN += 1
    print(f"    WARN {msg}")


def err_msg(msg):
    global ERR
    ERR += 1
    print(f"    ERR  {msg}")


def buscar_html(path):
    try:
        with urllib.request.urlopen(BASE + path, timeout=20) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception:
        return ""


PAGINAS = [
    ("/",             "Home"),
    ("/app/avaliacao","Avaliacao"),
    ("/app/chat",     "Chat"),
    ("/app/diario",   "Diario"),
]

print("=== ACESSIBILIDADE (WCAG 2.1) ===")

for path, nome in PAGINAS:
    print(f"\n  [{nome}]")
    html = buscar_html(path)

    if not html:
        err_msg("Pagina nao carrega")
        continue

    # Lang
    if 'lang="pt-BR"' in html or 'lang="pt"' in html:
        ok_msg("lang=pt-BR correto")
    else:
        warn_msg("lang attribute ausente")

    # Charset
    if "utf-8" in html.lower() and "charset" in html.lower():
        ok_msg("charset UTF-8")
    else:
        err_msg("Sem charset UTF-8")

    # Viewport
    if 'name="viewport"' in html:
        ok_msg("Viewport meta (mobile ready)")
    else:
        err_msg("Sem viewport — nao e mobile friendly!")

    # CSS
    if "emotion.css" in html or "<style" in html:
        ok_msg("CSS carregando")
    else:
        warn_msg("CSS nao encontrado")

    # H1
    h1_count = len(re.findall(r"<h1", html, re.IGNORECASE))
    if h1_count == 1:
        ok_msg("H1 unico presente")
    elif h1_count == 0:
        err_msg("Sem H1")
    else:
        warn_msg(f"{h1_count} H1s (deve ser 1)")

    # Alt em imagens
    imgs = re.findall(r"<img[^>]+>", html, re.IGNORECASE)
    sem_alt = [i for i in imgs if "alt=" not in i.lower()]
    if not imgs:
        ok_msg("Sem imagens (OK)")
    elif not sem_alt:
        ok_msg(f"Alt text em todas as {len(imgs)} imagens")
    else:
        warn_msg(f"{len(sem_alt)} imagens sem alt text")

    # Labels
    n_labels = len(re.findall(r"<label", html, re.IGNORECASE))
    n_inputs = len(re.findall(r"<input", html, re.IGNORECASE))
    if n_inputs == 0:
        ok_msg("Sem inputs")
    elif n_labels >= max(1, n_inputs // 2):
        ok_msg(f"{n_labels} labels para {n_inputs} inputs")
    else:
        warn_msg(f"Poucos labels: {n_labels} para {n_inputs} inputs")

    # Teclado
    usa_teclado = any(k in html for k in ["onkeydown", "keypress", "keyup", "Enter", "wcag.js", "wcag-js", "/static/wcag", "keyboard", "keydown"])
    if usa_teclado:
        ok_msg("Suporte a teclado detectado")
    else:
        warn_msg("Suporte a teclado nao detectado")

    # JavaScript
    scripts = re.findall(r"<script", html, re.IGNORECASE)
    if scripts:
        ok_msg(f"{len(scripts)} bloco(s) JavaScript")
    else:
        warn_msg("Sem JavaScript")

total = OK + WARN + ERR
score = round(OK / total * 100) if total > 0 else 0
print(f"\nScore: {OK} ok / {WARN} avisos / {ERR} erros = {score}%")
