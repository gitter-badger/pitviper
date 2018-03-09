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


from typing import Union

from libamazonproduct.utils import query_from_parameters
from libamazonproduct.utils import get_timestamp
from libamazonproduct.utils import bytes_to_quoted_base64
from libamazonproduct.utils import hmac_sign_query
from libamazonproduct.utils import request_url
from libamazonproduct.utils import SafeXmlWrapper


PARAM_SERVICE = 'AWSECommerceService'
PARAM_VERSION = '2015-10-01'
PARAM_OPERATION = 'ItemLookup'
PARAM_IDTYPE = 'ASIN'
PARAM_DEFAULT_RESPONSE_GROUP = (
    'Images,ItemAttributes,Large,OfferFull,Offers,OfferSummary,Reviews'
)

XML_TITLE_TEXT_PATH = 'ItemAttributes.Title'
XML_SALE_PRICE_TEXT_PATH = 'Offers.Offer.OfferListing.SalePrice.Amount'
XML_PRICE_TEXT_PATH = 'Offers.Offer.OfferListing.Price.Amount'
XML_LOWEST_NEW_PRICE_TEXT_PATH = 'OfferSummary.LowestNewPrice.Amount'


def fix_price(func):
    def func_wrapper(*args, **kwargs):
        try:
            return str(float(func(*args, **kwargs)) / 100)

        except ValueError as e:
            return 'None'

    return func_wrapper


def sign_asin_lookup_url(aws_access_key: str, aws_secret_key: str,
                         aws_associate_tag: str, country: str, asin: str,
                         response_group: Union[str, bool] = False) -> str:
    params = {}
    params['Service'] = PARAM_SERVICE
    params['Version'] = PARAM_VERSION
    params['Operation'] = PARAM_OPERATION
    params['IdType'] = PARAM_IDTYPE
    params['Timestamp'] = get_timestamp()
    params['ItemId'] = asin
    params['AWSAccessKeyId'] = aws_access_key
    params['AssociateTag'] = aws_associate_tag

    if response_group:
        params['ResponseGroup'] = response_group

    else:
        params['ResponseGroup'] = PARAM_DEFAULT_RESPONSE_GROUP

    query = query_from_parameters(params=params)
    hmac = hmac_sign_query(aws_secret_key=aws_secret_key,
                           country=country,
                           query=query)

    signature = bytes_to_quoted_base64(data=hmac)

    url = request_url(query=query, signature=signature, country=country)
    return url


class AmazonProductInterface(SafeXmlWrapper):
    def __init__(self, item):
        super(AmazonProductInterface, self).__init__(item)

    def export(self):
        return {
            'title': self.title,
            'sale_price': self.sale_price,
            'price': self.price,
            'lowest_new_price': self.lowest_new_price
        }

    @property
    def title(self) -> str:
        return self._safe_get_xml_element_text(XML_TITLE_TEXT_PATH)

    @property
    @fix_price
    def sale_price(self) -> str:
        return self._safe_get_xml_element_text(XML_SALE_PRICE_TEXT_PATH)

    @property
    @fix_price
    def price(self) -> str:
        return self._safe_get_xml_element_text(XML_PRICE_TEXT_PATH)

    @property
    @fix_price
    def lowest_new_price(self) -> str:
        return self._safe_get_xml_element_text(XML_LOWEST_NEW_PRICE_TEXT_PATH)
