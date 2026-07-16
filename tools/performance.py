#!/usr/bin/env python3
import urllib.request
import urllib.error
import time
import statistics

BASE = "https://emotion-platform-albert.onrender.com"

PAGINAS = [
    ("/",                                  "Home"),
    ("/app/avaliacao",                     "Avaliacao"),
    ("/app/chat",                          "Chat"),
    ("/app/diario",                        "Diario"),
    ("/app/dashboard",                     "Dashboard"),
    ("/api/v1/phq9-clinico/perguntas",     "PHQ-9 API"),
    ("/api/v1/chat-ia/modelos/disponiveis","Chat Modelos"),
    ("/health",                            "Health"),
]


def medir(path):
    tempos = []
    tamanho = 0
    for _ in range(3):
        try:
            inicio = time.time()
            with urllib.request.urlopen(BASE + path, timeout=30) as resp:
                dados = resp.read()
                tamanho = len(dados)
            tempos.append((time.time() - inicio) * 1000)
        except Exception:
            tempos.append(9999)
        time.sleep(0.3)
    return statistics.mean(tempos), tamanho


print("=== TESTE DE PERFORMANCE ===")
print(f"Site: {BASE}")
print()

resultados = []
for path, nome in PAGINAS:
    media, tamanho = medir(path)

    if media < 300:
        emoji = "OTIMO"
    elif media < 800:
        emoji = "BOM  "
    elif media < 2000:
        emoji = "LENTO"
    else:
        emoji = "RUIM "

    kb = tamanho / 1024
    print(f"  [{emoji}] {nome:<30} {media:>6.0f}ms  {kb:>6.1f}KB")
    resultados.append({"nome": nome, "ms": media})

print()
media_geral = statistics.mean(r["ms"] for r in resultados)
print(f"Media geral: {media_geral:.0f}ms")

if media_geral < 800:
    print("Performance boa!")
else:
    print("Performance pode melhorar.")
    print("Dica: ative cache e CDN (Cloudflare).")
