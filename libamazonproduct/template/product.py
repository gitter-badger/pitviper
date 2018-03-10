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

__all__ = [
    # General
    '_ASIN',

    # Item Attributes
    '_TITLE',
    '_BRAND',
    '_MODEL',
    '_MPN',
    '_SKU',
    '_EAN',
    '_EAN_LIST',
    '_UPC',
    '_UPC_LIST',
    '_BINDING',
    '_COLOR',
    '_WARRANTY',
    '_STUDIO',
    '_PUBLISHER',
    '_PRODUCT_TYPE_NAME',
    '_PRODUCT_GROUP',
    '_LABEL',
    '_IS_ADULT',

    # Offers
    '_IS_PRIME',
    '_SALE_PRICE_AMOUNT',
    '_SALE_PRICE_CURRENCY',
    '_PRICE_AMOUNT',
    '_PRICE_CURRENCY',
    '_LOWEST_NEW_PRICE_AMOUNT',
    '_LOWEST_NEW_PRICE_CURRENCY'
]

# General
_ASIN = 'ASIN'

# Item Attributes
_TITLE = 'ItemAttributes.Title'
_BRAND = 'ItemAttributes.Brand'
_MODEL = 'ItemAttributes.Model'
_MPN = 'ItemAttributes.MPN'
_SKU = 'ItemAttributes.SKU'
_EAN = 'ItemAttributes.EAN'
_EAN_LIST = 'ItemAttributes.EANList.EANListElement'
_UPC = 'ItemAttributes.UPC'
_UPC_LIST = 'ItemAttributes.UPCList.UPCListElement'
_BINDING = 'ItemAttributes.Binding'
_COLOR = 'ItemAttributes.Color'
_WARRANTY = 'ItemAttributes.Warranty'
_STUDIO = 'ItemAttributes.Magformers'
_PUBLISHER = 'ItemAttributes.Publisher'
_PRODUCT_TYPE_NAME = 'ItemAttributes.ProductTypeName'
_PRODUCT_GROUP = 'ItemAttributes.ProductGroup'
_LABEL = 'ItemAttributes.Label'
_IS_ADULT = 'ItemAttributes.IsAdultProduct'

# Offers
_IS_PRIME = 'Offers.Offer.OfferListing.IsEligibleForPrime'
_SALE_PRICE_AMOUNT = 'Offers.Offer.OfferListing.SalePrice.Amount'
_SALE_PRICE_CURRENCY = 'Offers.Offer.OfferListing.SalePrice.CurrencyCode'
_PRICE_AMOUNT = 'Offers.Offer.OfferListing.Price.Amount'
_PRICE_CURRENCY = 'Offers.Offer.OfferListing.Price.CurrencyCode'

# Offer Summary
_LOWEST_NEW_PRICE_AMOUNT = 'OfferSummary.LowestNewPrice.Amount'
_LOWEST_NEW_PRICE_CURRENCY = 'OfferSummary.LowestNewPrice.CurrencyCode'
