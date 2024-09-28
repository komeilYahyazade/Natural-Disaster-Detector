from django.shortcuts import render, HttpResponse, redirect
from monitor.models import Temperature, Humidity, Acceleration, Preferences
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from monitor.forms import PreferencesForm
from django.contrib import messages
# from monitor.utils import *

def home(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def add_temperature(request):
    value = request.POST.get('value')
    if value is not None:
        temperature = Temperature(value=value)
        temperature.save()
    return HttpResponse('')

@csrf_exempt
def add_humidity(request):
    value = request.POST.get('value')
    if value is not None:
        humidity = Humidity(value=value)
        humidity.save()
    return HttpResponse('')

@csrf_exempt
def add_acceleration(request):
    x = request.POST.get('x')
    y = request.POST.get('y')
    z = request.POST.get('z')
    if x is not None and y is not None and z is not None:
        acceleration = Acceleration(x=x, y=y, z=z)
        acceleration.save()
    return HttpResponse('')

def acceleraions(request):
    last_acceleraions =  Acceleration.objects.order_by('-timestamp').values_list('x', 'y', 'z').all()[:100]
    values = [{'x': acceleration[0], 'y': acceleration[1], 'z': acceleration[2]} for acceleration in last_acceleraions[::-1]]
    return JsonResponse(values, safe=False)

def earthquake(request):
    last_acceleration = Acceleration.objects.latest('-timestamp')
    x, y, z = last_acceleration.x, last_acceleration.y, last_acceleration.z
    if max(abs(x), abs(y), abs(z) - 10) > settings.EARTHQUAKE_THRESHOLD:
        # send_earthquacke_email()
        return JsonResponse({'status': True})
    return JsonResponse({'status': False})

def volcanic_erruption(request):
    last_temperature = Temperature.objects.latest('timestamp')
    value = last_temperature.value
    if value > settings.TEMPERATURE_THRESHOLD:
        # send_volcano_email()
        return JsonResponse({'status': True, 'value': round(value, 1)})
    return JsonResponse({'status': False, 'value': round(value, 1)})

def extreme_humidity(request):
    last_humidity = Humidity.objects.latest('timestamp')
    value = last_humidity.value
    if value > settings.HUMIDITY_THRESHOLD:
        # send_humidity_email()
        return JsonResponse({'status': True, 'value': round(value, 1)})
    return JsonResponse({'status': False, 'value': round(value, 1)})


def preferences(request):
    preferences = Preferences.objects.last()
    form = PreferencesForm(request.POST or None, instance=preferences)
    if form.is_valid():
        form.save()
        settings.EARTHQUAKE_THRESHOLD = form.cleaned_data['earthquake_threshold']
        settings.TEMPERATURE_THRESHOLD = form.cleaned_data['temperature_threshold']
        settings.HUMIDITY_THRESHOLD = form.cleaned_data['humidity_threshold']
        messages.success(request, "Preferences updated successfully!")
        return redirect('preferences')
    return render(request, 'preferences.html', {'form': form})
