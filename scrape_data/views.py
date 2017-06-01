from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import ScrapeData
from .serializers import ScrapeDataSerializer

@api_view(['GET', 'POST'])
def scrape_data(request):
    """
    create a new data_row or list all rows.
    These views are specifically to scrape data from any
    data format and post to an endpoint
    """

    if request.method == 'GET':
        scraped_data = ScrapeData.objects.all()
        serializer = ScrapeDataSerializer(scraped_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScrapeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
