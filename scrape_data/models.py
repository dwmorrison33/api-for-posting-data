from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class ScrapeData(models.Model):
	time_added_to_db = models.DateTimeField(default=timezone.now)
	date_issued = models.CharField(max_length=255, default="")
	finaled_date = models.CharField(max_length=255, default="")
	address = models.CharField(max_length=1000, default="")
	description = models.CharField(max_length=1000, default="")
	permit_number = models.CharField(max_length=255, default="")
	permit_type = models.CharField(max_length=1000, default="")
	valuation = models.CharField(max_length=255, default="")
	fees = models.CharField(max_length=255, default="")
	contractor = models.CharField(max_length=1000, default="")
	status = models.CharField(max_length=255, default="")
	parcel_number = models.CharField(max_length=255, default="")
	owner = models.CharField(max_length=1000, default="")