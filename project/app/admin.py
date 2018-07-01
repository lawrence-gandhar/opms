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
    list_display = ('id','name','assigned_to', 'link', 'template_folder', 'use_nav_from_template_folder', 'navbar_template', 'access_list', 'status',)

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


@admin.register(Assessment_Settings)
class Assessment_SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr', 'year', 'session', 'status', 'enable_self_assessment_form', 'self_assess_users', 'self_assessment_form_start_date', 'self_assessment_form_end_date', 'enable_assessment_grade_form', 'assess_graders', 'assessment_grade_start_date', 'assessment_grade_end_date', 'enable_assess_parameters', 'parameter_form_users', 'parameter_form_graders', 'parameters_start_date', 'parameters_end_date', 'self_assess_template', 'assess_grade_template', 'parameters_template', )


@admin.register(AssessmentFormSection)
class AssessmentFormSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'status')

@admin.register(AssessmentFormQuestions)
class AssessmentFormQuestionsAdmin(admin.ModelAdmin):
    list_display = ('section', 'question', 'question_type', 'status')    


@admin.register(AssessmentFormOptions)
class AssessmentFormOptionsAdmin(admin.ModelAdmin):
    list_display = ('question', 'options', 'status')


admin.site.unregister(Group)  