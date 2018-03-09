# -*- coding: utf-8 -*-
#
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
import base64
import hashlib

from urllib.parse import quote


AMAZON_HTTP_METHOD = 'GET'
AMAZON_URL = 'webservices.amazon.'
AMAZON_URL_PATH = '/onca/xml'


def str_to_bytes(data: str) -> bytes:
    return bytes(data, 'utf-8')


def url_with_cctld(cctld: str, path: bool = False) -> str:
    if path:
        return '%s%s%s' % (AMAZON_URL, cctld, AMAZON_URL_PATH)

    else:
        return '%s%s' % (AMAZON_URL, cctld)


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


def query_to_sign(query: str, cctld: str) -> str:
    return '%s\n%s\n%s\n%s' % (AMAZON_HTTP_METHOD,
                               url_with_cctld(cctld=cctld),
                               AMAZON_URL_PATH,
                               query)


def hmac_sign(aws_secret_key: str, cctld: str, query: str) -> str:
    message = query_to_sign(query=query, cctld=cctld)
    sign = hmac.new(key=str_to_bytes(aws_secret_key),
                    msg=str_to_bytes(message),
                    digestmod=hashlib.sha256).digest()

    return sign


def url_from_query_and_signature(query: str, signature: str, cctld: str) -> str:
    url = 'http://%s?%s&Signature=%s' % (url_with_cctld(cctld=cctld, path=True),
                                         query,
                                         signature)

    return url
