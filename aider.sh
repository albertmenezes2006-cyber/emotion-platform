#!/bin/bash
cd ~/emotion_platform
source venv/bin/activate
export GROQ_API_KEY=$(cat .env 2>/dev/null | grep GROQ_API_KEY | cut -d= -f2)
echo "════════════════════════════════════════"
echo "  AIDER — Emotion Platform"
echo "  Fale em português — ele programa"
echo "  Ex: Adiciona o Bloco 7 dialetos BR"
echo "  Ex: Corrige o bug no endpoint /chat"
echo "  Sair: /exit"
echo "════════════════════════════════════════"
aider main.py modules/ --model groq/llama-3.3-70b-versatile
