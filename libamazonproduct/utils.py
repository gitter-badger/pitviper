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


import hmac
import time
import lxml
import base64
import hashlib

from urllib.parse import quote
from typing import Union

from libamazonproduct.errors import InvalidAmazonCountryError


# https://kdp.amazon.com/help?topicId=A1CT8LK6UW2FXJ
AMAZON_DOMAINS = {
    'CA': 'ca',
    'DE': 'de',
    'ES': 'es',
    'FR': 'fr',
    'IN': 'in',
    'IT': 'it',
    'JP': 'co.jp',
    'UK': 'co.uk',
    'US': 'com',
    'CN': 'cn'
}

AMAZON_HTTP_METHOD = 'GET'
AMAZON_URL = 'webservices.amazon.{domain}'
AMAZON_URL_WITH_ENDPOINT = 'webservices.amazon.{domain}/onca/xml'
AMAZON_ENDPOINT= '/onca/xml'

AMAZON_REQUEST_URL = 'http://{url}?{query}&Signature={signature}'
AMAZON_QUERY_TO_SIGN = '{method}\n{url}\n{endpoint}\n{query}'


def str_to_bytes(data: str) -> bytes:
    return bytes(data, 'utf-8')


def bytes_to_quoted_base64(data: bytes) -> str:
    return quote(base64.b64encode(data)).replace('%7E', '~')


def query_from_parameters(params: dict) -> str:
    return '&'.join(
        [
            quote(param).replace('%7E', '~') + '=' + quote(params[param]).replace('%7E', '~')
            for param in sorted(params.keys())
        ]
    )


def get_timestamp() -> str:
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def query_to_sign(query: str, country: str) -> str:
    try:
        return AMAZON_QUERY_TO_SIGN.format(method=AMAZON_HTTP_METHOD,
                                           url=AMAZON_URL.format(
                                               domain=AMAZON_DOMAINS[country]),
                                           endpoint=AMAZON_ENDPOINT,
                                           query=query)

    except KeyError as e:
        raise InvalidAmazonCountryError


def hmac_sign_query(aws_secret_key: str, country: str, query: str) -> str:
    message = query_to_sign(query=query, country=country)
    sign = hmac.new(key=str_to_bytes(aws_secret_key),
                    msg=str_to_bytes(message),
                    digestmod=hashlib.sha256).digest()

    return sign


def request_url(query: str, signature: str, country: str) -> str:
    try:
        url = AMAZON_REQUEST_URL.format(
            url=AMAZON_URL_WITH_ENDPOINT.format(domain=AMAZON_DOMAINS[country]),
            query=query,
            signature=signature)

        return url

    except KeyError as e:
        raise InvalidAmazonCountryError


class SafeXmlWrapper(object):
    def __init__(self, xml: bytes):
        self.__xml = xml

    def _safe_get_xml_element(self, path, root=None):
        elements = path.split('.')
        parent = root if root is not None else self.__xml
        for element in elements[:-1]:
            parent = getattr(parent, element, None)
            if parent is None:
                return None

        return getattr(parent, elements[-1], None)

    def _safe_get_xml_element_text(self, path, root=None):
        element = self._safe_get_xml_element(path, root)
        if element is not None:
            return element.text

        else:
            return 'None'
