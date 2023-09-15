from django.shortcuts import render
from .models import VibrationData

def dashboard(request):
    data_sensor = VibrationData.objects.order_by("-pk").first()
    context = {'data_sensor': data_sensor}
    return render(request, 'dashboard.html', context)