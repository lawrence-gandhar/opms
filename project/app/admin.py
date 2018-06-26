# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django import forms 

# Register your models here.


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbr', 'name', 'department', 'status',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbr', 'name', 'assigned_to', 'location',  'status', 'is_parent',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbr', 'name', 'status',)

@admin.register(Usertype)
class UsertypeAdmin(admin.ModelAdmin):
    list_display = ('id','name','assigned_to', 'link', 'template_folder', 'access_list', 'status',)

#
# Create a class for form to handle the hashing of the password
# If you don't set the password as a hash then you won't be able to authenticate
#

class MyForm(forms.ModelForm):
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(MyForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = MyForm	
    pass

    class Media:
        js = ('admin_js/usermodel.js',)      
  
admin.site.unregister(Group)  