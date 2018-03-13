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

__ITEM_STRING_PATHS = {
    'asin' : 'ASIN',
    'editorial_reviews': 'EditorialReviews.EditorialReview.Content',

    # Item Attributes
    'title': 'ItemAttributes.Title',
    'features': 'ItemAttributes.Feature',
    'brand': 'ItemAttributes.Brand',
    'model': 'ItemAttributes.Model',
    'binding': 'ItemAttributes.Binding',
    'color': 'ItemAttributes.Color',
    'warranty': 'ItemAttributes.Warranty',
    'publisher': 'ItemAttributes.Publisher',
    'product_type_name': 'ItemAttributes.ProductTypeName',
    'product_group': 'ItemAttributes.ProductGroup',
    'label': 'ItemAttributes.Label',
    'is_adult': 'ItemAttributes.IsAdultProduct',
    'manufacturer': 'ItemAttributes.Manufacturer',
    'number_of_items': 'ItemAttributes.NumberOfItems',
    'package_quantity': 'ItemAttributes.PackageQuantity',
    'part_number': 'ItemAttributes.PartNumber',
    'release_date': 'ItemAttributes.ReleaseDate',
    'studio': 'ItemAttributes.Studio',
    'list_price_amount': 'ItemAttributes.ListPrice.Amount',
    'list_price_currency': 'ItemAttributes.ListPrice.CurrencyCode',

    'mpn': 'ItemAttributes.MPN',
    'sku': 'ItemAttributes.SKU',
    'ean': 'ItemAttributes.EAN',
    'ean_list': 'ItemAttributes.EANList.EANListElement',
    'upc': 'ItemAttributes.UPC',
    'upc_list': 'ItemAttributes.UPCList.UPCListElement',

    # Offers
    'sale_price_amount': 'Offers.Offer.OfferListing.SalePrice.Amount',
    'sale_price_currency': 'Offers.Offer.OfferListing.SalePrice.CurrencyCode',
    'price_amount': 'Offers.Offer.OfferListing.Price.Amount',
    'price_currency': 'Offers.Offer.OfferListing.Price.CurrencyCode',

    'merchant': 'Offers.Offer.Name',
    'condition': 'Offers.Offer.Condition',
    'availability': 'Offers.Offer.OfferListing.Availability',
    'availability_type': (
        'Offers.Offer.OfferListing.AvailabilityAttributes.AvailabilityType'),

    'availability_max_hours': (
        'Offers.Offer.OfferListing.AvailabilityAttributes.MaximumHours'),

    'availability_min_hours': (
        'Offers.Offer.OfferListing.AvailabilityAttributes.MinimumHours'),

    'is_eligible_for_prime': (
        'Offers.Offer.OfferListing.IsEligibleForPrime'),

    'is_eligible_for_super_saver_shipping': (
        'Offers.Offer.OfferListing.IsEligibleForSuperSaverShipping'),

    'total_offer_pages': 'Offers.TotalOfferPages',
    'total_offers': 'Offers.TotalOffers',
    'sales_rank': 'Offers.SalesRank',

    # offer Summary
    'lowest_new_price_amount': 'OfferSummary.LowestNewPrice.Amount',
    'lowest_new_price_currency': 'OfferSummary.LowestNewPrice.CurrencyCode',
}

__ITEM_LIST_DICT_KEY_PATHS = {
    # Image set
    'large_images': {
        'list': 'ImageSets.ImageSet',
        'dict': 'LargeImage',
        'key': 'URL'
    },
    'medium_images': {
        'list': 'ImageSets.ImageSet',
        'dict': 'MediumImage',
        'key': 'URL'
    },
    'small_images': {
        'list': 'ImageSets.ImageSet',
        'dict': 'SmallImage',
        'key': 'URL'
    },
    'swatch_images': {
        'list': 'ImageSets.ImageSet',
        'dict': 'SwatchImage',
        'key': 'URL'
    },
    'thumbnail_images': {
        'list': 'ImageSets.ImageSet',
        'dict': 'SwatchImage',
        'key': 'URL'
    },
    'tiny_images': {
        'list': 'ImageSets.ImageSet',
        'dict': 'TinyImage',
        'key': 'URL'
    }
}
