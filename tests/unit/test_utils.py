import io
from datetime import datetime, timezone
from enum import Enum

from apify_shared.utils import (
    _filter_out_none_values_recursively_internal,
    filter_out_none_values_recursively,
    ignore_docs,
    is_content_type_json,
    is_content_type_text,
    is_content_type_xml,
    is_file_or_bytes,
    json_dumps,
    maybe_extract_enum_member_value,
    parse_date_fields,
)


def test__maybe_extract_enum_member_value() -> None:
    class TestEnum(Enum):
        A = 'A'
        B = 'B'

    assert maybe_extract_enum_member_value(TestEnum.A) == 'A'
    assert maybe_extract_enum_member_value(TestEnum.B) == 'B'
    assert maybe_extract_enum_member_value('C') == 'C'
    assert maybe_extract_enum_member_value(1) == 1
    assert maybe_extract_enum_member_value(None) is None


def test__filter_out_none_values_recursively() -> None:  # Copypasted from client
    assert filter_out_none_values_recursively({'k1': 'v1'}) == {'k1': 'v1'}
    assert filter_out_none_values_recursively({'k1': None}) == {}
    assert filter_out_none_values_recursively({'k1': 'v1', 'k2': None, 'k3': {'k4': 'v4', 'k5': None}, 'k6': {'k7': None}}) \
        == {'k1': 'v1', 'k3': {'k4': 'v4'}}


def test__filter_out_none_values_recursively_internal() -> None:  # Copypasted from client
    assert _filter_out_none_values_recursively_internal({}) == {}
    assert _filter_out_none_values_recursively_internal({'k1': {}}) == {}
    assert _filter_out_none_values_recursively_internal({}, False) == {}
    assert _filter_out_none_values_recursively_internal({'k1': {}}, False) == {'k1': {}}
    assert _filter_out_none_values_recursively_internal({}, True) is None
    assert _filter_out_none_values_recursively_internal({'k1': {}}, True) is None


def test__is_content_type_json() -> None:  # Copypasted from client
    # returns True for the right content types
    assert is_content_type_json('application/json') is True
    assert is_content_type_json('application/jsonc') is True
    # returns False for bad content types
    assert is_content_type_json('application/xml') is False
    assert is_content_type_json('application/ld+json') is False


def test__is_content_type_xml() -> None:  # Copypasted from client
    # returns True for the right content types
    assert is_content_type_xml('application/xml') is True
    assert is_content_type_xml('application/xhtml+xml') is True
    # returns False for bad content types
    assert is_content_type_xml('application/json') is False
    assert is_content_type_xml('text/html') is False


def test__is_content_type_text() -> None:  # Copypasted from client
    # returns True for the right content types
    assert is_content_type_text('text/html') is True
    assert is_content_type_text('text/plain') is True
    # returns False for bad content types
    assert is_content_type_text('application/json') is False
    assert is_content_type_text('application/text') is False


def test__is_file_or_bytes() -> None:  # Copypasted from client
    # returns True for the right value types
    assert is_file_or_bytes(b'abc') is True
    assert is_file_or_bytes(bytearray.fromhex('F0F1F2')) is True
    assert is_file_or_bytes(io.BytesIO(b'\x00\x01\x02')) is True

    # returns False for bad value types
    assert is_file_or_bytes('abc') is False
    assert is_file_or_bytes(['a', 'b', 'c']) is False
    assert is_file_or_bytes({'a': 'b'}) is False
    assert is_file_or_bytes(None) is False


def test__json_dumps() -> None:
    expected = """{
  "string": "123",
  "number": 456,
  "nested": {
    "abc": "def"
  },
  "datetime": "2022-01-01 00:00:00+00:00"
}"""
    actual = json_dumps({
        'string': '123',
        'number': 456,
        'nested': {
            'abc': 'def',
        },
        'datetime': datetime(2022, 1, 1, tzinfo=timezone.utc),
    })
    assert actual == expected


def test__parse_date_fields() -> None:
    # works correctly on empty dicts
    assert parse_date_fields({}) == {}

    # correctly parses dates on fields ending with -At
    expected_datetime = datetime(2016, 11, 14, 11, 10, 52, 425000, timezone.utc)
    assert parse_date_fields({'createdAt': '2016-11-14T11:10:52.425Z'}) == {'createdAt': expected_datetime}

    # doesn't parse dates on fields not ending with -At
    assert parse_date_fields({'saveUntil': '2016-11-14T11:10:52.425Z'}) == {'saveUntil': '2016-11-14T11:10:52.425Z'}

    # parses dates in dicts in lists
    expected_datetime = datetime(2016, 11, 14, 11, 10, 52, 425000, timezone.utc)
    assert parse_date_fields([{'createdAt': '2016-11-14T11:10:52.425Z'}]) == [{'createdAt': expected_datetime}]

    # parses nested dates
    expected_datetime = datetime(2020, 2, 29, 10, 9, 8, 100000, timezone.utc)
    assert parse_date_fields({'a': {'b': {'c': {'createdAt': '2020-02-29T10:09:08.100Z'}}}}) \
        == {'a': {'b': {'c': {'createdAt': expected_datetime}}}}

    # doesn't parse dates nested too deep
    expected_datetime = datetime(2020, 2, 29, 10, 9, 8, 100000, timezone.utc)
    assert parse_date_fields({'a': {'b': {'c': {'d': {'createdAt': '2020-02-29T10:09:08.100Z'}}}}}) \
        == {'a': {'b': {'c': {'d': {'createdAt': '2020-02-29T10:09:08.100Z'}}}}}

    # doesn't die when the date can't be parsed
    assert parse_date_fields({'createdAt': 'NOT_A_DATE'}) == {'createdAt': 'NOT_A_DATE'}


def test_ignore_docs() -> None:
    def testing_function(_a: str, _b: str) -> str:
        """Dummy docstring"""
        return 'dummy'

    assert testing_function is ignore_docs(testing_function)
