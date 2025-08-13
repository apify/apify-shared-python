from __future__ import annotations

import base64

from apify_shared.utils import create_hmac_signature, create_storage_content_signature, encode_base62


def test_encode_base62() -> None:
    assert encode_base62(0) == '0'
    assert encode_base62(10) == 'a'
    assert encode_base62(999999999) == '15FTGf'


# This test ensures compatibility with the JavaScript version of the same method.
# https://github.com/apify/apify-shared-js/blob/master/packages/utilities/src/hmac.ts
def test_create_valid_hmac_signature() -> None:
    # This test uses the same secret key and message as in JS tests.
    secret_key = 'hmac-secret-key'
    message = 'hmac-message-to-be-authenticated'
    assert create_hmac_signature(secret_key, message) == 'pcVagAsudj8dFqdlg7mG'


def test_create_same_hmac() -> None:
    # This test uses the same secret key and message as in JS tests.
    secret_key = 'hmac-same-secret-key'
    message = 'hmac-same-message-to-be-authenticated'
    assert create_hmac_signature(secret_key, message) == 'FYMcmTIm3idXqleF1Sw5'
    assert create_hmac_signature(secret_key, message) == 'FYMcmTIm3idXqleF1Sw5'


# This test ensures compatibility with the JavaScript version of the same method.
# https://github.com/apify/apify-shared-js/blob/master/packages/utilities/src/storages.ts
def test_create_storage_content_signature() -> None:
    # This test uses the same parameters as in JS tests.
    secret_key = 'hmac-secret-key'
    message = 'resource-id'

    signature = create_storage_content_signature(
        resource_id=message,
        url_signing_secret_key=secret_key,
    )

    version, expires_at, hmac = base64.urlsafe_b64decode(signature).decode('utf-8').split('.')

    assert signature == 'MC4wLjNUd2ZFRTY1OXVmU05zbVM0N2xS'
    assert version == '0'
    assert expires_at == '0'
    assert hmac == '3TwfEE659ufSNsmS47lR'


def test_create_storage_content_signature_with_expiration() -> None:
    secret_key = 'hmac-secret-key'
    message = 'resource-id'

    signature = create_storage_content_signature(
        resource_id=message,
        url_signing_secret_key=secret_key,
        expires_in_millis=10000,
    )

    version, expires_at, hmac = base64.urlsafe_b64decode(signature).decode('utf-8').split('.')
    assert version == '0'
    assert expires_at != '0'
