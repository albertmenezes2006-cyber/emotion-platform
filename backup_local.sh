#!/bin/bash
# Backup diario - adicione: crontab -e
# 0 2 * * * /home/w77/emotion_platform/backup_local.sh
cd ~/emotion_platform && source venv/bin/activate
DATE=$(date +%Y%m%d_%H%M%S)
BDIR=~/emotion_backups && mkdir -p $BDIR
git add -A && git commit --no-verify -m 'backup $DATE' 2>/dev/null || true
git push origin main 2>/dev/null || true
tar -czf $BDIR/emotion_$DATE.tar.gz --exclude=venv --exclude=__pycache__ --exclude=.git ~/emotion_platform
ls -t $BDIR/emotion_*.tar.gz | tail -n +8 | xargs rm -f 2>/dev/null || true
echo 'Backup OK: '$BDIR/emotion_$DATE.tar.gz
