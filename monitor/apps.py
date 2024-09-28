from django.apps import AppConfig

class MonitorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "monitor"

    def ready(self):
        from django.conf import settings
        from monitor.models import Preferences
        preferences = Preferences.objects.last()
        if not preferences:
            Preferences.objects.create(
                earthquake_threshold=settings.EARTHQUAKE_THRESHOLD,
                temperature_threshold=settings.TEMPERATURE_THRESHOLD,
                humidity_threshold=settings.HUMIDITY_THRESHOLD
            )
        else:
            settings.EARTHQUAKE_THRESHOLD = preferences.earthquake_threshold
            settings.TEMPERATURE_THRESHOLD = preferences.temperature_threshold
            settings.HUMIDITY_THRESHOLD = preferences.humidity_threshold
