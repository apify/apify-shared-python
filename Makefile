.PHONY: clean install-dev build publish-to-pypi lint unit-tests unit-tests-cov \
	type-check check-code format 

DIRS_WITH_CODE = src tests

clean:
	rm -rf build dist .mypy_cache .pytest_cache .ruff_cache src/*.egg-info __pycache__ htmlcov .coverage

install-dev:
	uv sync --all-extras
	uv run pre-commit install

build:
	uv build --verbose

# APIFY_PYPI_TOKEN_CRAWLEE is expected to be set in the environment
publish-to-pypi:
	uv publish --verbose --token "${APIFY_PYPI_TOKEN_CRAWLEE}"

lint:
	uv run ruff format --check $(DIRS_WITH_CODE)
	uv run ruff check $(DIRS_WITH_CODE)

unit-tests:
	uv run pytest --numprocesses=auto --verbose --cov=src/apify_shared tests/unit

unit-tests-cov:
	uv run pytest --numprocesses=auto --verbose --cov=src/apify_shared --cov-report=html tests/unit

type-check:
	uv run mypy $(DIRS_WITH_CODE)

# The check-code target runs a series of checks equivalent to those performed by pre-commit hooks
check-code: lint type-check unit-tests

format:
	uv run ruff check --fix $(DIRS_WITH_CODE)
	uv run ruff format $(DIRS_WITH_CODE)
