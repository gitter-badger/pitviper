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
from libamazonproduct.utils import hmac_sign
from libamazonproduct.utils import url_from_query_and_signature


PARAM_SERVICE = 'AWSECommerceService'
PARAM_VERSION = '2015-10-01'
PARAM_OPERATION = 'ItemLookup'
PARAM_IDTYPE = 'ASIN'
PARAM_DEFAULT_RESPONSE_GROUP = (
    'Images,ItemAttributes,Large,OfferFull,Offers,OfferSummary,Reviews'
)


def sign_asin_lookup_url(aws_access_key: str, aws_secret_key: str,
                         aws_associate_tag: str, aws_cctld: str, asin: str,
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
    hmac = hmac_sign(aws_secret_key=aws_secret_key,
                     cctld=aws_cctld,
                     query=query)

    signature = bytes_to_quoted_base64(data=hmac)

    url = url_from_query_and_signature(query=query,
                                       signature=signature,
                                       cctld=aws_cctld)
    return url
