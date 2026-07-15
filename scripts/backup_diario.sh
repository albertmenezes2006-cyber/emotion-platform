#!/bin/bash
cd ~/emotion_platform
TS=$(date +%Y%m%d)
cp main.py backups/main_${TS}.py
echo "✅ Backup diário: backups/main_${TS}.py"
ls -la backups/ | tail -5
