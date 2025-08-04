from __future__ import annotations

import base64
import contextlib
import hashlib
import hmac
import io
import json
import re
import string
import time
from datetime import datetime, timezone
from enum import Enum
from typing import Any, TypeVar, cast

PARSE_DATE_FIELDS_MAX_DEPTH = 3
PARSE_DATE_FIELDS_KEY_SUFFIX = 'At'

ListOrDict = TypeVar('ListOrDict', list, dict)
T = TypeVar('T')


def ignore_docs(method: T) -> T:
    """Mark that a method's documentation should not be rendered. Functionally, this decorator is a noop."""
    return method


@ignore_docs
def filter_out_none_values_recursively(dictionary: dict) -> dict:
    """Return copy of the dictionary, recursively omitting all keys for which values are None."""
    return cast(dict, filter_out_none_values_recursively_internal(dictionary))


@ignore_docs
def filter_out_none_values_recursively_internal(
    dictionary: dict,
    remove_empty_dicts: bool | None = None,
) -> dict | None:
    """Recursively filters out None values from a dictionary.

    Unfortunately, it's necessary to have an internal function for the correct result typing,
    without having to create complicated overloads
    """
    result = {}
    for k, v in dictionary.items():
        if isinstance(v, dict):
            v = filter_out_none_values_recursively_internal(v, remove_empty_dicts is True or remove_empty_dicts is None)  # noqa: PLW2901
        if v is not None:
            result[k] = v
    if not result and remove_empty_dicts:
        return None
    return result


@ignore_docs
def is_content_type_json(content_type: str) -> bool:
    """Check if the given content type is JSON."""
    return bool(re.search(r'^application/json', content_type, flags=re.IGNORECASE))


@ignore_docs
def is_content_type_xml(content_type: str) -> bool:
    """Check if the given content type is XML."""
    return bool(re.search(r'^application/.*xml$', content_type, flags=re.IGNORECASE))


@ignore_docs
def is_content_type_text(content_type: str) -> bool:
    """Check if the given content type is text."""
    return bool(re.search(r'^text/', content_type, flags=re.IGNORECASE))


@ignore_docs
def is_file_or_bytes(value: Any) -> bool:
    """Check if the input value is a file-like object or bytes.

    The check for IOBase is not ideal, it would be better to use duck typing,
    but then the check would be super complex, judging from how the 'requests' library does it.
    This way should be good enough for the vast majority of use cases, if it causes issues, we can improve it later.
    """
    return isinstance(value, (bytes, bytearray, io.IOBase))


@ignore_docs
def json_dumps(obj: Any) -> str:
    """Dump JSON to a string with the correct settings and serializer."""
    return json.dumps(obj, ensure_ascii=False, indent=2, default=str)


@ignore_docs
def maybe_extract_enum_member_value(maybe_enum_member: Any) -> Any:
    """Extract the value of an enumeration member if it is an Enum, otherwise return the original value."""
    if isinstance(maybe_enum_member, Enum):
        return maybe_enum_member.value
    return maybe_enum_member


@ignore_docs
def parse_date_fields(data: ListOrDict, max_depth: int = PARSE_DATE_FIELDS_MAX_DEPTH) -> ListOrDict:
    """Recursively parse date fields in a list or dictionary up to the specified depth."""
    if max_depth < 0:
        return data

    if isinstance(data, list):
        return [parse_date_fields(item, max_depth - 1) for item in data]

    if isinstance(data, dict):

        def parse(key: str, value: object) -> object:
            parsed_value = value
            if key.endswith(PARSE_DATE_FIELDS_KEY_SUFFIX) and isinstance(value, str):
                with contextlib.suppress(ValueError):
                    parsed_value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
            elif isinstance(value, dict):
                parsed_value = parse_date_fields(value, max_depth - 1)
            elif isinstance(value, list):
                parsed_value = parse_date_fields(value, max_depth)  # type: ignore # mypy doesn't work with decorators and recursive calls well
            return parsed_value

        return {key: parse(key, value) for (key, value) in data.items()}

    return data


CHARSET = string.digits + string.ascii_letters


def encode_base62(num: int) -> str:
    """Encode the given number to base62."""
    if num == 0:
        return CHARSET[0]

    res = ''
    while num > 0:
        num, remainder = divmod(num, 62)
        res = CHARSET[remainder] + res
    return res


@ignore_docs
def create_hmac_signature(secret_key: str, message: str) -> str:
    """Generates an HMAC signature and encodes it using Base62. Base62 encoding reduces the signature length.

    HMAC signature is truncated to 30 characters to make it shorter.

    Args:
        secret_key (str): Secret key used for signing signatures
        message (str): Message to be signed

    Returns:
        str: Base62 encoded signature
    """
    signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()[:30]

    decimal_signature = int(signature, 16)

    return encode_base62(decimal_signature)


def create_storage_content_signature(
    resource_id: str, url_signing_secret_key: str, expires_in_millis: int | None = None, version: int = 0
) -> str:
    """Create a secure signature for a resource like a dataset or key-value store.

    This signature is used to generate a signed URL for authenticated access, which can be expiring or permanent.
    The signature is created using HMAC with the provided secret key and includes
    the resource ID, expiration time, and version.

    Note: expires_in_millis is optional. If not provided, the signature will not expire.

    """
    expires_at = int(time.time() * 1000) + expires_in_millis if expires_in_millis else 0

    message_to_sign = f'{version}.{expires_at}.{resource_id}'
    hmac = create_hmac_signature(url_signing_secret_key, message_to_sign)

    base64url_encoded_payload = base64.urlsafe_b64encode(f'{version}.{expires_at}.{hmac}'.encode())
    return base64url_encoded_payload.decode('utf-8')
