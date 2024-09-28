from django.urls import path
from monitor import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_temperature/', views.add_temperature, name='add_temperature'),
    path('add_humidity/', views.add_humidity, name='add_humidity'),
    path('add_acceleration/', views.add_acceleration, name='add_acceleration'),

    
    path('accelerations/', views.acceleraions, name='accelerations'),
    path('earthquake/', views.earthquake, name='earthquake'),
    path('volcanic_erruption/', views.volcanic_erruption, name='volcanic_erruption'),
    path('extreme_humidity/', views.extreme_humidity, name='extreme_humidity'),
    path('preferences/', views.preferences, name='preferences'),
]
