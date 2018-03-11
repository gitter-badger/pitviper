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


# https://kdp.amazon.com/help?topicId=A1CT8LK6UW2FXJ
__CCTLDS = {
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

__HTTP_METHOD = 'GET'
__UNFROMATED_URL_WITHOUT_ENDPOINT = 'webservices.amazon.{cctld}'
__UNFORMATED_URL_WITH_ENDPOINT = 'webservices.amazon.{cctld}/onca/xml'
__ENDPOINT= '/onca/xml'

__UNFORMATED_QUERY_TO_SIGN = '{method}\n{url}\n{endpoint}\n{query}'
__UNFROMATED_REQUEST_URL = 'http://{url}?{query}&Signature={signature}'

__SERVICE = 'AWSECommerceService'
__VERSION = '2015-10-01'

__ITEMLOOKUP_PARAM_OPERATION = 'ItemLookup'

__ITEMLOOKUP_ASIN_PARAM_IDTYPE = 'ASIN'
__ITEMLOOKUP_ASIN_PARAM_DEFAULT_RESPONSE_GROUP = (
    'Images,ItemAttributes,Large,OfferFull,Offers,OfferSummary,Reviews'
)

__ISO_8601_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
