.PHONY: all check push full backup lint test security status health monitor blocos modulos log size git clean help

# Verificações
syntax:
	@python3 -m py_compile main.py && echo "✅ Sintaxe OK"

lint:
	@ruff check main.py --fix && echo "✅ Lint OK"

security:
	@bandit -r main.py -ll -q && echo "✅ Segurança OK" || true

test:
	@pytest tests/ -v --tb=short --cov=. --cov-report=term-missing 2>/dev/null || pytest tests/ -v

check:
	@python3 validar.py

# Utilidades
backup:
	@python3 ep.py backup

linhas:
	@python3 ep.py linhas

status:
	@python3 ep.py status

health:
	@python3 ep.py health

monitor:
	@python3 monitor.py --watch

blocos:
	@python3 ep.py blocos

modulos:
	@python3 ep.py modulos

log:
	@python3 ep.py log

size:
	@python3 ep.py size

git:
	@python3 ep.py git

clean:
	@python3 ep.py clean

deps:
	@python3 ep.py deps

# Deploy seguro
push:
	@python3 validar.py && \
	git add . && \
	git commit -m "$(MSG)" && \
	git push || echo "❌ Corrija os erros"

# Autopilot
autopilot:
	@python3 autopilot.py

# Tudo de uma vez
full:
	@make backup
	@make syntax
	@make lint
	@make test
	@make check
	@echo "🚀 TUDO OK — rode: make push MSG='mensagem'"

# Ajuda
help:
	@echo ""
	@echo "════════════════════════════════════════"
	@echo "  EMOTION PLATFORM — COMANDOS"
	@echo "════════════════════════════════════════"
	@echo "  make syntax    → sintaxe Python"
	@echo "  make lint      → Ruff linter"
	@echo "  make test      → Pytest + cobertura"
	@echo "  make security  → Bandit segurança"
	@echo "  make check     → Validador completo"
	@echo "  make backup    → Backup main.py"
	@echo "  make status    → Status do projeto"
	@echo "  make health    → Checa deploy"
	@echo "  make monitor   → Monitora 24/7"
	@echo "  make blocos    → Fila de blocos"
	@echo "  make modulos   → Lista módulos"
	@echo "  make log       → Logs autopilot"
	@echo "  make size      → Tamanho arquivos"
	@echo "  make git       → Últimos commits"
	@echo "  make clean     → Limpa cache"
	@echo "  make full      → Tudo de uma vez"
	@echo "  make autopilot → Aplica blocos"
	@echo "  make push MSG='texto' → Push seguro"
	@echo "════════════════════════════════════════"
	@echo ""

obs:
	@python3 ep.py obs

saude:
	@python3 -c "from modules.saude import verificar_saude_sistema; import json; print(json.dumps(verificar_saude_sistema(), indent=2, ensure_ascii=False))"

metricas:
	@python3 -c "from modules.metricas import metricas; import json; print(json.dumps(metricas.resumo(), indent=2, ensure_ascii=False))"
