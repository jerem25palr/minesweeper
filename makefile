.PHONY: tests
tests:
	@echo "Running tests..."
	export PYTHONPATH=. ;\
	pytest -v