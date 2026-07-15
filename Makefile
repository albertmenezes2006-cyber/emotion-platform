.PHONY: check push full backup watch test lint security

check:
	@python3 validar.py

syntax:
	@python3 -m py_compile main.py && echo "✅ Sintaxe OK" || echo "❌ ERRO de sintaxe"

lint:
	@ruff check main.py --fix && echo "✅ Lint OK"

security:
	@bandit -r main.py -ll -q && echo "✅ Segurança OK" || echo "⚠️  Avisos de segurança"

test:
	@pytest tests/ -v --tb=short

backup:
	@cp main.py main.py.bak && echo "✅ Backup criado: main.py.bak"

push:
	@python3 validar.py && git add . && git commit -m "$(MSG)" && git push || echo "❌ Corrija os erros antes do push"

full:
	@make backup && make syntax && make lint && make test && make check && echo "🚀 TUDO OK — pronto para push!"

watch:
	@watchmedo shell-command --patterns="*.py" --recursive --command='python3 -m py_compile main.py && echo "✅ OK" || echo "❌ ERRO"' .

lines:
	@wc -l main.py

status:
	@echo "════════════════════════════════" && \
	echo "  EMOTION PLATFORM STATUS" && \
	echo "════════════════════════════════" && \
	wc -l main.py && \
	git log --oneline -5 && \
	echo "════════════════════════════════"
