from django.db import models
from django.conf import settings

# Create your models here.
class Ticket(models.Model):
	SEAT_CHOICES = (
		('WINDOW', 'window'),
		('AISLE', 'aisle')
	)
	ticket_id = models.CharField(max_length=128)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	seat = models.CharField(max_length=128, choices=SEAT_CHOICES, default="WINDOW")