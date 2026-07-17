#!/bin/bash
# Keepalive profissional para Render
URL="https://emotion-platform-albert.onrender.com"

while true; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL/ping")
    TEMPO=$(date '+%H:%M:%S')
    
    if [ "$STATUS" = "200" ]; then
        echo "[$TEMPO] ✅ Site online — HTTP $STATUS"
    else
        echo "[$TEMPO] ❌ Site offline — HTTP $STATUS"
        # Tenta acordar
        curl -s "$URL/health" > /dev/null
    fi
    
    sleep 270  # 4.5 minutos
done
