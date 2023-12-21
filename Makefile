.PHONY: clean install-dev build publish twine-check lint unit-tests type-check check-code format check-version-availability check-changelog-entry

DIRS_WITH_CODE = src tests scripts

clean:
	rm -rf build dist .mypy_cache .pytest_cache .ruff_cache src/*.egg-info __pycache__

install-dev:
	python3 -m pip install --upgrade pip
	pip install --no-cache-dir -e ".[dev]"
	pre-commit install

build:
	python3 -m build

publish:
	python3 -m twine upload dist/*

twine-check:
	python3 -m twine check dist/*

lint:
	python3 -m ruff check $(DIRS_WITH_CODE)

unit-tests:
	python3 -m pytest -n auto -ra tests/unit --cov=src/apify_shared

unit-tests-cov:
	python3 -m pytest -n auto -ra tests/unit --cov=src/apify_shared --cov-report=html

type-check:
	python3 -m mypy $(DIRS_WITH_CODE)

check-code: lint type-check unit-tests

format:
	python3 -m ruff check --fix $(DIRS_WITH_CODE)
	python3 -m ruff format $(DIRS_WITH_CODE)

check-version-availability:
	python scripts/check_version_availability.py

check-changelog-entry:
	python scripts/check_version_in_changelog.py
