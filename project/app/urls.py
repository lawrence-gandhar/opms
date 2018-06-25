from django.urls import path
from . import views

urlpatterns = [
    path('location-select/', views.location_selects, name='location-select'),
    path('department-select/', views.department_selects, name='department-select'),
    path('designation-select/', views.designation_selects, name='designation-select'),
]