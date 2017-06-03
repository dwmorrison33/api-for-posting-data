from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class ScrapeData(models.Model):
	time = models.DateTimeField(default=timezone.now)
	date = models.CharField(max_length=255, blank=True, null=True)
	addr = models.CharField(max_length=1000, blank=True, null=True)
	desc = models.CharField(max_length=1000, blank=True, null=True)
	per_number = models.CharField(max_length=255, blank=True, null=True)
	per_type = models.CharField(max_length=1000, blank=True, null=True)
	value = models.IntegerField(max_length=255, blank=True, null=True)
	fees = models.IntegerField(max_length=255, blank=True, null=True)
	contract = models.CharField(max_length=1000, blank=True, null=True)
	stats = models.CharField(max_length=255, blank=True, null=True)
	parcel_number = models.CharField(max_length=255, blank=True, null=True)
	owned = models.CharField(max_length=1000, blank=True, null=True)