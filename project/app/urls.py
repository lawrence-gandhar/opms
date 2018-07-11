
from . import views

try:
    from django.urls import path, re_path

    urlpatterns = [
        path('location-select/', views.location_selects, name='location-select'),
        path('department-select/', views.department_selects, name='department-select'),
        path('designation-select/', views.designation_selects, name='designation-select'),
        path('admin-userform-details/', views.get_admin_userform_details, name='admin-userform-details'),
        path('admin-userform-list/', views.get_admin_user_list, name='admin-userform-list'),

        path('', views.index, name='index'),    
        #path('logout/', views.user_logout, name='logout'),
        re_path(r'^(?P<usertype>[\w.@+-]+)/logout/', views.user_logout),    
        re_path(r'^(?P<usertype>[\w.@+-]+)/dashboard/', views.dashboard),    # Dashboard of logged in user
        re_path(r'^(?P<usertype>[\w.@+-]+)/assessments/(?P<name>[\w.@+-]+)/(?P<id>[\d])/', views.self_assessment_form),
    ]


except ImportError:
    from django.conf.urls import url

    urlpatterns = [
        url('location-select/', views.location_selects, name='location-select'),
        url('department-select/', views.department_selects, name='department-select'),
        url('designation-select/', views.designation_selects, name='designation-select'),
        url('admin-userform-details/', views.get_admin_userform_details, name='admin-userform-details'),
        url('admin-userform-list/', views.get_admin_user_list, name='admin-userform-list'),

        url('', views.index, name='index'),    
        url(r'^(?P<usertype>[\w.@+-]+)/logout/', views.user_logout),    
        url(r'^(?P<usertype>[\w.@+-]+)/dashboard/', views.dashboard),    # Dashboard of logged in user
        url(r'^(?P<usertype>[\w.@+-]+)/assessments/(?P<name>[\w.@+-]+)/(?P<id>[\d])/', views.self_assessment_form),
    ]

