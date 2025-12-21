.PHONY: clean install-dev build publish-to-pypi lint unit-tests unit-tests-cov \
	type-check check-code format

clean:
	rm -rf .ty_cache .pytest_cache .ruff_cache build dist htmlcov .coverage

install-dev:
	uv sync --all-extras

build:
	uv build --verbose

# APIFY_PYPI_TOKEN_CRAWLEE is expected to be set in the environment
publish-to-pypi:
	uv publish --verbose --token "${APIFY_PYPI_TOKEN_CRAWLEE}"

lint:
	uv run ruff format --check
	uv run ruff check

unit-tests:
	uv run pytest --numprocesses=auto --verbose --cov=src/apify_shared tests/unit

unit-tests-cov:
	uv run pytest --numprocesses=auto --verbose --cov=src/apify_shared --cov-report=html tests/unit

type-check:
	uv run ty check

# The check-code target runs a series of checks equivalent to those performed by pre-commit hooks
# and the run_checks.yaml GitHub Actions workflow.
check-code: lint type-check unit-tests

format:
	uv run ruff check --fix
	uv run ruff format
