#!/bin/bash
echo "=== EMOTION PLATFORM v24 STARTING ==="
echo "Start command: uvicorn app_ep:app"
exec uvicorn app_ep:app --host 0.0.0.0 --port ${PORT:-10000}
