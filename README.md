# Apify Shared Python

> ⚠️ **DEPRECATED - this package is no longer maintained.**
>
> The `apify-shared` package is not used by any Apify Python library anymore - its constants and utilities were moved
> into the packages that need them. Already published versions stay installable from PyPI, but there will be no
> further releases, bug fixes, or security updates, and this repository has been archived.

## What to use instead

- The [Apify SDK for Python](https://docs.apify.com/sdk/python) (the `apify` package) exposes the Actor constants,
  such as `ActorEnvVars`, `ApifyEnvVars`, `ActorEventTypes`, and `WebhookEventType`.
- The [Apify API client for Python](https://docs.apify.com/api/client/python) (the `apify-client` package) provides
  fully typed models and literals for the API resources it works with.

The signing helpers (`encode_base62`, `create_hmac_signature`, and `create_storage_content_signature`) have no public
replacement - they are an implementation detail of the packages above. Copy them into your own project if you depend
on them.

If you want to develop Apify Actors in Python, check out the [Apify SDK for Python](https://docs.apify.com/sdk/python).

## Installation

Requires Python 3.10+

The last published version is still available on its [PyPI listing](https://pypi.org/project/apify-shared), so
existing installations keep working. Importing the package emits a `DeprecationWarning`. Do not add it to new projects.
