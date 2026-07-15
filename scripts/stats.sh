#!/bin/bash
cd ~/emotion_platform
echo "════════════════════════════════════════"
echo "  EMOTION PLATFORM — STATS"
echo "════════════════════════════════════════"
echo "  Linhas main.py:  $(wc -l < main.py)"
echo "  Funções def:     $(grep -c '^def \|^async def ' main.py)"
echo "  Rotas @app:      $(grep -c '^@app\.' main.py)"
echo "  Templates:       $(ls templates/*.html | wc -l)"
echo "  Módulos:         $(ls modules/*.py | wc -l)"
echo "  Commits:         $(git log --oneline | wc -l)"
echo "  Tamanho:         $(du -sh main.py | cut -f1)"
echo "════════════════════════════════════════"
