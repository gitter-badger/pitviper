# -*- coding: utf-8 -*-
# Copyright (c) 2018 Buza Aleksandar <privatni@aleksandarbuza.cr.rs>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from operator import getitem
from functools import reduce

from time import gmtime
from time import strftime

from base64 import b64encode

from hashlib import sha256
from hmac import new as hmac_new

from urllib.parse import quote

from xmltodict import parse as xml_to_dict

from pitviper.config.core import __CCTLDS
from pitviper.config.core import __HTTP_METHOD
from pitviper.config.core import __UNFROMATED_URL_WITHOUT_ENDPOINT
from pitviper.config.core import __UNFORMATED_URL_WITH_ENDPOINT
from pitviper.config.core import __ENDPOINT
from pitviper.config.core import __UNFROMATED_REQUEST_URL
from pitviper.config.core import __UNFORMATED_QUERY_TO_SIGN
from pitviper.config.core import __ISO_8601_FORMAT


from pitviper.config.item import __ITEM_STRING_PATHS
from pitviper.config.item import __ITEM_LIST_DICT_KEY_PATHS

from pitviper.errors import PitviperInvalidAmazonCountryError
from pitviper.errors import PitviperInvalidResponseError


def str_to_bytes(data: str) -> bytes:
    return bytes(data, 'utf-8')


def is_country(country: str) -> bool:
    if country in __CCTLDS.keys():
        return True

    else:
        return False


def bytes_to_quoted_base64(data: bytes) -> str:
    return quote(b64encode(data)).replace('%7E', '~')


def query_from_parameters(params: dict) -> str:
    return '&'.join(['{0}={1}'.format(
        quote(param).replace('%7E', '~'),
        quote(params[param]).replace('%7E', '~')
        ) for param in sorted(params.keys())])


def get_iso8601_timestamp() -> str:
    return strftime(__ISO_8601_FORMAT, gmtime())


def prepare_query_to_sign(query: str, country: str) -> str:
    if is_country(country=country):
        return __UNFORMATED_QUERY_TO_SIGN.format(
            method=__HTTP_METHOD,
            url=__UNFROMATED_URL_WITHOUT_ENDPOINT.format(
                cctld=__CCTLDS[country]),
            endpoint=__ENDPOINT,
            query=query)

    else:
        raise PitviperInvalidAmazonCountryError


def hmac_sign_query(key: str, country: str, query: str) -> str:
    sign = hmac_new(key=str_to_bytes(key),
                    msg=str_to_bytes(query),
                    digestmod=sha256).digest()

    return sign


def generate_request_url(query: str, signature: str, country: str) -> str:
    if is_country(country=country):
        return __UNFROMATED_REQUEST_URL.format(
            url=__UNFORMATED_URL_WITH_ENDPOINT.format(cctld=__CCTLDS[country]),
            query=query,
            signature=signature)

    else:
        raise PitviperInvalidAmazonCountryError


def response_to_dict(xml: bytes) -> dict:
    try:
        return xml_to_dict(xml)

    except Exception as e:
        raise PitviperInvalidResponse


def __safe_parse_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            if result is not None:
                return result

            else:
                return 'None'

        except KeyError as exception:
            return 'None'

    return wrapper


@__safe_parse_decorator
def __parse_full_value(item: dict, path: str):
        return reduce(getitem, path.split('.'), item)


@__safe_parse_decorator
def __parse_list_dict_key(item: dict, options: str):
    result = []

    for item in __parse_full_value(item, options['list']):
        result.append(item[options['dict']][options['key']])

    return result


def item_parser(item: dict) -> dict:
    parsed = {}

    for key, value in __ITEM_STRING_PATHS.items():
        parsed[key] = __parse_full_value(item=item, path=value)

    for key, value in __ITEM_LIST_DICT_KEY_PATHS.items():
        parsed[key] = __parse_list_dict_key(item=item, options=value)

    return parsed
