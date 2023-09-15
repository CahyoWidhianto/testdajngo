from django.db import models

# Create your models here.
class VibrationData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    vibration_value = models.FloatField()