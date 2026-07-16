#!/bin/bash
# Mantém o Render acordado — rode em background
# Usage: bash keepalive_render.sh &
URL="https://emotion-platform-albert.onrender.com/health"
while true; do
    echo "[$(date +%H:%M)] Ping..."
    curl -s --max-time 30 "$URL" > /dev/null && echo "OK" || echo "FALHOU"
    sleep 840  # 14 minutos
done
