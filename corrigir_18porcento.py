#!/usr/bin/env python3
"""Corrige os 18% restantes"""
from pathlib import Path
import re

VERDE  = "\033[92m"
RESET  = "\033[0m"

def log(msg):
    print(f"  {VERDE}✅ {msg}{RESET}")

# ══════════════════════════════════════════════════
# 1. DIÁRIO — corrigir payload (422)
# Espera query params não body JSON
# ══════════════════════════════════════════════════
diario = Path("plugins/autocuidado/diario_real.py")
if diario.exists():
    txt = diario.read_text(encoding="utf-8")
    # Ver como a rota está definida
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'entrada' in linha.lower() or 'post' in linha.lower() or 'emocao' in linha.lower():
            print(f"  Diario linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 2. AGENDA — espera query params
# ══════════════════════════════════════════════════
agenda = Path("plugins/agendamento/agenda_real.py")
if agenda.exists():
    txt = agenda.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'agendar' in linha.lower() or 'paciente_id' in linha.lower() or 'terapeuta_id' in linha.lower():
            print(f"  Agenda linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 3. PRONTUÁRIO — espera query params
# ══════════════════════════════════════════════════
pront = Path("plugins/prontuario/prontuario_real.py")
if pront.exists():
    txt = pront.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'cadastrar' in linha.lower() or 'nome' in linha.lower() or 'terapeuta' in linha.lower():
            print(f"  Prontuario linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 4. RECUPERAR SENHA — espera query param ?email=
# ══════════════════════════════════════════════════
auth_jwt = Path("plugins/auth_real/auth_jwt.py")
if auth_jwt.exists():
    txt = auth_jwt.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'recuperar' in linha.lower() or 'senha' in linha.lower():
            print(f"  AuthJWT linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 5. XP GANHAR — ver assinatura
# ══════════════════════════════════════════════════
xp = Path("plugins/gamificacao/sistema_xp.py")
if xp.exists():
    txt = xp.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'ganhar' in linha.lower() or 'def ' in linha.lower():
            print(f"  XP linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 6. AFILIADOS — ver o erro 500
# ══════════════════════════════════════════════════
afil = Path("plugins/monetizacao_real/afiliados.py")
if afil.exists():
    txt = afil.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'cadastrar' in linha.lower() or 'def ' in linha.lower() or 'erro' in linha.lower():
            print(f"  Afiliados linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 7. PDF — espera email no body
# ══════════════════════════════════════════════════
pdf = Path("plugins/monetizacao_real/relatorio_pdf.py")
if pdf.exists():
    txt = pdf.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'gerar' in linha.lower() or 'email' in linha.lower() or 'def ' in linha.lower():
            print(f"  PDF linha {i}: {linha.strip()[:80]}")

# ══════════════════════════════════════════════════
# 8. KO-FI — ver por que 403
# ══════════════════════════════════════════════════
tip = Path("plugins/monetizacao_real/tip_externo.py")
if tip.exists():
    txt = tip.read_text(encoding="utf-8")
    for i, linha in enumerate(txt.split('\n'), 1):
        if 'kofi' in linha.lower() or '403' in linha or 'referer' in linha.lower():
            print(f"  Tip linha {i}: {linha.strip()[:80]}")

print("\n✅ Análise concluída!")
