#!/bin/bash
cd ~/emotion_platform
source venv/bin/activate
export GROQ_API_KEY=$(grep GROQ_API_KEY .env 2>/dev/null | cut -d= -f2)
echo "════════════════════════════════"
echo "  AIDER — Emotion Platform"
echo "  Fale em português normalmente"
echo "  Ex: Adiciona o Bloco 7"
echo "  Ex: Corrige o erro no /chat"
echo "  Ex: Melhora o SEO da landing"
echo "════════════════════════════════"
aider main.py --model groq/llama-3.3-70b-versatile
