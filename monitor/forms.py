from django import forms
from monitor.models import Preferences

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = Preferences
        fields = ['earthquake_threshold', 'temperature_threshold', 'humidity_threshold']
