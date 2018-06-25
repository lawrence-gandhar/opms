# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import * 

# Register your models here.


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbr', 'name', 'assigned_to', 'location',  'status',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbr', 'name', 'status',)

@admin.register(Usertype)
class UsertypeAdmin(admin.ModelAdmin):
    list_display = ('id','name','assigned_to', 'link', 'template_folder', 'access_list', 'status',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass  

    class Media:
        js = ('admin_js/usermodel.js',)      