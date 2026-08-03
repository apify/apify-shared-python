from __future__ import annotations

import importlib

import pytest

import apify_shared


def test_import_emits_deprecation_warning() -> None:
    """Importing the package warns that it is deprecated and points to the replacements."""
    with pytest.warns(DeprecationWarning, match='`apify-shared` package is deprecated'):
        importlib.reload(apify_shared)
