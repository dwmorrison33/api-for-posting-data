from rest_framework import serializers
from .models import ScrapeData

class ScrapeDataSerializer(serializers.ModelSerializer):
        """ Serializer to represent the ScrapeData Model """
        class Meta:
                model = ScrapeData
                fields = ('time_added_to_db', 'date_issued', 'finaled_date',
                	'address', 'description', 'permit_number', 'permit_type',
                	'valuation', 'fees', 'contractor', 'status', 'parcel_number',
                	'owner'
                )
