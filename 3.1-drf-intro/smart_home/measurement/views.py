from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response


from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorSerializer, SensorUpdateSerializer


class GetSensor(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementList(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateMeasurement(UpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = SensorUpdateSerializer


class GetSensorInstance(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer