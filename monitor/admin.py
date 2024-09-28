from django.contrib import admin
from monitor.models import Temperature, Humidity, Acceleration, Preferences

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Acceleration)
admin.site.register(Preferences)