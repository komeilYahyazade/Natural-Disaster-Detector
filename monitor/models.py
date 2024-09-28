from django.db import models

class Temperature(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Delete the oldest Temperature objects if there are more than 100
        num_temperatures = Temperature.objects.count()
        if num_temperatures > 100:
            oldest_temperatures = Temperature.objects.order_by('timestamp').values_list('pk', flat=True)[:num_temperatures - 100]
            Temperature.objects.filter(pk__in=oldest_temperatures).delete()


class Humidity(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Delete the oldest Humidity objects if there are more than 100
        num_humidity = Humidity.objects.count()
        if num_humidity > 100:
            oldest_humidity = Humidity.objects.order_by('timestamp').values_list('pk', flat=True)[:num_humidity - 100]
            Humidity.objects.filter(pk__in=oldest_humidity).delete()


class Acceleration(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Delete the oldest Acceleration objects if there are more than 100
        num_accelerations = Acceleration.objects.count()
        if num_accelerations > 100:
            oldest_ids = list(Acceleration.objects.order_by('timestamp').values_list('id', flat=True)[:num_accelerations - 100])
            Acceleration.objects.filter(id__in=oldest_ids).delete()

class Preferences(models.Model):
    earthquake_threshold = models.FloatField()
    temperature_threshold = models.FloatField()
    humidity_threshold = models.FloatField()
    