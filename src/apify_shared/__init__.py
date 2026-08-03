import warnings
from importlib import metadata

__version__ = metadata.version('apify-shared')

warnings.warn(
    'The `apify-shared` package is deprecated and no longer maintained. Its constants and utilities now live in the '
    'packages that need them: use `apify` (the Apify SDK for Python) or `apify-client` (the Apify API client for '
    'Python) instead. See https://github.com/apify/apify-shared-python for details.',
    DeprecationWarning,
    stacklevel=2,
)
