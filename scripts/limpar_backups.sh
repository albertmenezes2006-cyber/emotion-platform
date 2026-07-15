#!/bin/bash
cd ~/emotion_platform/backups
ls -t | tail -n +8 | xargs rm -f 2>/dev/null
echo "✅ Mantidos últimos 7 backups"
ls -la
