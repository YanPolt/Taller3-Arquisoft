from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(id):
    measurement = Measurement.objects.filter(pk=id)
    return measurement

def delete_measurement(id):
    measurement = Measurement.objects.filter(pk=id).delete()

def update_measurement(id, new_value, new_place):
    m = Measurement.objects.filter(id=id)
    m.update(value=new_value, place=new_place)
    return m
