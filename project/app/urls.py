from django.urls import path
from . import views

urlpatterns = [
    path('location-select/', views.location_selects, name='location-select'),
]