import json, random
from django.forms import model_to_dict
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
import httplib, httplib2, urllib
from django.conf import settings


# Create your views here.
from social.backends.utils import load_backends
from .utils import clean_sky_scanner_data
from flights.models import Ticket



def search(request):
	client = httplib2.Http()
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept': 'application/json'
	}

	body = {}
	endpoint = settings.SKY_SCANNER_API_URL

	body["apiKey"] = settings.SKY_SCANNER_API_KEY
	queryset = request.GET

	if not queryset.get('origin'):
		return render(request, 'pages/flights.html',
		              {'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)})

	body["country"] = queryset.get('country', 'US')
	body["currency"] = queryset.get('currency', 'USD')
	body["locale"] = queryset.get('currency', 'en-US')
	body["originplace"] = queryset.get('origin', 'SFO')
	body["destinationplace"] = queryset.get('destination', 'JFK')
	body["outbounddate"] = queryset.get('outbounddate', '2015-11-25')
	if body["outbounddate"].split('/')[0]:
		sep = body["outbounddate"].split('/')
		body["outbounddate"] = "-".join([sep[2]] + sep[:2])

	body["locationschema"] = queryset.get('locationschema', 'Iata')
	body["adults"] = queryset.get('adults', '1')

	response, content = client.request(endpoint, "POST", headers=headers, body=urllib.urlencode(body))

	second_endpoint = response['location'] + '?apiKey=' + body["apiKey"]

	response, content = client.request(second_endpoint, "GET")

	context = clean_sky_scanner_data(json.loads(content))
	context['query'] = body

	return render(request, 'pages/flights.html',
		              {'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS),
		               'context': context})

def book(request):
	queryset = request.GET
	ticket_id = queryset.get('leg_id')
	user = request.user
	seat = random.choice(["WINDOW", "AISLE"])
	ticket = Ticket(ticket_id=ticket_id, owner=user, seat=seat)
	ticket.save()
	return render(request, 'pages/flights.html',
		              {'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS),
		               'messages': ["The ticket was successfully booked", ]})

def pals(request):
	queryset = request.GET
	ticket_id = queryset.get('leg_id')

	tickets = Ticket.objects.filter(ticket_id=ticket_id)

	users = []
	for ticket in tickets:
		owner = ticket.owner
		users.append(owner)
	return render(request, 'pages/pals.html',
		              {'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS),
		               'pals': users})

