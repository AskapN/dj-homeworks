from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    sensor_id = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements'
    )

    def __str__(self):
        return f'Температура {self.temperature}°C в {self.sensor_id.name}'