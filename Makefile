.PHONY: clean install-dev build publish twine-check lint unit-tests type-check check-code format check-version-availability check-changelog-entry

DIRS_WITH_CODE = src tests scripts

clean:
	rm -rf build dist .mypy_cache .pytest_cache .ruff_cache src/*.egg-info __pycache__

install-dev:
	python -m pip install --upgrade pip
	pip install --no-cache-dir -e ".[dev]"
	pre-commit install

build:
	python -m build

publish:
	python -m twine upload dist/*

twine-check:
	python -m twine check dist/*

lint:
	python -m ruff check $(DIRS_WITH_CODE)

unit-tests:
	python -m pytest -n auto -ra tests/unit

type-check:
	python -m mypy $(DIRS_WITH_CODE)

check-code: lint type-check unit-tests

format:
	python -m ruff check --fix $(DIRS_WITH_CODE)
	python -m ruff format $(DIRS_WITH_CODE)

check-version-availability:
	python scripts/check_version_availability.py

check-changelog-entry:
	python scripts/check_version_in_changelog.py
