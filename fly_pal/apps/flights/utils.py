from django.http import QueryDict


def clean_sky_scanner_data(data_in):
	data_out = dict()
	data_list = []
	itineraries = data_in.get("Itineraries")

	for item in itineraries:
		prepare = {}
		prepare["leg_id"] = item.get("OutboundLegId")
		priceOptions = item.get("PricingOptions")
		if priceOptions[0]:
			prepare["price"] = priceOptions[0].get("Price")
			prepare["deeplink"] = priceOptions[0].get("DeeplinkUrl")
		bookingDetailsLink = item.get("BookingDetailsLink")
		if bookingDetailsLink:
			prepare["detail"] = bookingDetailsLink.get("Uri")

		data_list.append(prepare)
	data_out["itineraries"] = data_list
	return data_out