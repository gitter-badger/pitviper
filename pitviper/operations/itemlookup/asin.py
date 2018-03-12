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


__all__ = ['sign_asin_lookup_url']


from typing import Union

from pitviper.config import __SERVICE
from pitviper.config import __VERSION

from pitviper.config import __ITEMLOOKUP_PARAM_OPERATION
from pitviper.config import __ITEMLOOKUP_ASIN_PARAM_IDTYPE
from pitviper.config import __ITEMLOOKUP_ASIN_PARAM_RESPONSE_GROUP

from pitviper.utils import bytes_to_quoted_base64
from pitviper.utils import get_iso8601_timestamp
from pitviper.utils import query_from_parameters
from pitviper.utils import prepare_query_to_sign
from pitviper.utils import hmac_sign_query
from pitviper.utils import generate_request_url


__predefined_params = {
    'Service': __SERVICE,
    'Version': __VERSION,
    'Operation': __ITEMLOOKUP_PARAM_OPERATION,
    'IdType': __ITEMLOOKUP_ASIN_PARAM_IDTYPE
}


def sign_asin_lookup_url(aws_access_key: str, aws_secret_key: str,
                         aws_associate_tag: str, country: str, asin: str,
                         response_group: Union[str, bool] = False) -> str:
    params = __predefined_params
    params['Timestamp'] = get_iso8601_timestamp()
    params['ItemId'] = asin
    params['AWSAccessKeyId'] = aws_access_key
    params['AssociateTag'] = aws_associate_tag

    if response_group:
        params['ResponseGroup'] = response_group

    else:
        params['ResponseGroup'] = __ITEMLOOKUP_ASIN_PARAM_RESPONSE_GROUP

    query = query_from_parameters(params=params)
    query_to_sign = prepare_query_to_sign(query=query, country=country)
    hmac = hmac_sign_query(key=aws_secret_key,
                           country=country,
                           query=query_to_sign)

    signature = bytes_to_quoted_base64(data=hmac)
    url = generate_request_url(
        query=query,
        signature=signature,
        country=country)

    return url
