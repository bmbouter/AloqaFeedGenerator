from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import Placemark

def viewFeed(request):
    placemarks = Placemark.objects.all()
    return render_to_response('aloqaFeed.kml',
                               {'placemarks': placemarks })
