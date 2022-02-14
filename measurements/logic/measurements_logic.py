from ..models import Measurement
from ..models import Variable


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement


# Revisar porque no se los atributos de measurement
def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.unit = new_var["unit"]
    measurement.save()
    return measurement


def create_measurement(var):
    variable = Variable.objects.get(pk=var["variable"])
    measurement = Measurement(variable=variable,
                              value=var["value"],
                              unit=var["unit"],
                              place=var["place"],
                              dateTime=var["dateTime"])
    measurement.save()
    return measurement


def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()

    return HttpResponse("Se borro")
