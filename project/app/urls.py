from django.urls import path
from . import views

urlpatterns = [
    path('location-select/', views.location_selects, name='location-select'),
    path('department-select/', views.department_selects, name='department-select'),
    path('designation-select/', views.designation_selects, name='designation-select'),
    path('admin-userform-details/', views.get_admin_userform_details, name='admin-userform-details'),
    path('admin-userform-list/', views.get_admin_user_list, name='admin-userform-list'),

    path('', views.index, name='index'),    

]