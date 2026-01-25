from django.urls import path

from measurement.views import GetSensor, Measurement, UpdateMeasurement, GetSensorInstance

urlpatterns = [
    path('sensors/update/<pk>/, UpdateData.as_view()', UpdateMeasurement, name='UpdateData'),
    path('sensors/', GetSensor.as_view(), name='GetData'),
    path('sensors/<pk>/', GetSensorInstance, name='GetDataInstance'),
    path('measurement/', Measurement, name='Measurement'),
]
