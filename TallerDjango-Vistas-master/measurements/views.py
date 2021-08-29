from .logic.logic_measurements import get_all_measurements, get_measurement, delete_measurement, update_measurement
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')

def get_measurement_id(request, pk):
    measurement = get_measurement(pk)
    r = serializers.serialize('json', measurement)
    return HttpResponse(r, content_type='application/json')

def delete_measurement_id(request, pk):
    measurement = delete_measurement(pk)
    return HttpResponse("Se elimino el measurement con pk: {0}".format(pk))

def update_measurement_id(request, pk, new_value, new_place):
    updated = update_measurement( pk, new_value, new_place)
    update_json = serializers.serialize('json', updated)
    return HttpResponse(update_json, content_type='application/json')
