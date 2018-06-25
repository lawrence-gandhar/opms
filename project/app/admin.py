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
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

@admin.register(Usertype)
class UsertypeAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass  

    class Media:
        js = ('admin_js/usermodel.js',)      