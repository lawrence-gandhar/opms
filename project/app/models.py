# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

#
# Location Model. Used for specifying the location at which the user is working
#

class Location(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    ACTIVE_INACTIVE = ((ACTIVE, 'Active'),(INACTIVE,'In-Active'))

    abbr = models.CharField(max_length = 20, unique = True, db_index = True,)
    name = models.CharField(max_length = 100, blank = True, db_index = True, null = True,)
    status = models.BooleanField(default = ACTIVE, db_index = True, choices = ACTIVE_INACTIVE, )

    def __str__(self):

        if self.name != "":
            return self.name + " ( " + self.abbr +" )"
        return self.abbr

    class META:
        ordering = ["id"]
        verbose_name_plural = 'location_tbl'

#
# Usertype Model. Used to assign roles to the users
#

class Usertype(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    ACTIVE_INACTIVE = ((ACTIVE, 'Active'),(INACTIVE,'In-Active'))

    name = models.CharField(blank=True, max_length=255, db_index = True, unique = True,)
    assigned_to = models.ForeignKey('self', db_index = True, on_delete = models.SET_NULL, null = True, blank = True,)
    status = models.BooleanField(default = ACTIVE, db_index = True, choices = ACTIVE_INACTIVE, )
    link = models.CharField(max_length=100, null = True, blank = True, db_index = True,)
    template_folder = models.CharField(max_length=20, null = True, blank = True, db_index = True,)
    use_nav_from_template_folder = models.BooleanField(default = True, db_index = True, verbose_name = 'use nav')
    navbar_template = models.CharField(max_length=250, null = True, blank = True, db_index = True,)
    access = models.ManyToManyField('self', db_index = True, blank = True, symmetrical=False, related_name = 'user_access')

    def __str__(self):
        return self.name

    def access_list(self):
        return ', '.join([ accessme.name for accessme in self.access.all()])    

    class META:
        ordering = ["id"]
        verbose_name_plural = 'usertype_tbl'

#
# Department Model. Used to specify the department in which the user is working
#

class Department(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    ACTIVE_INACTIVE = ((ACTIVE, 'Active'),(INACTIVE,'In-Active'))

    abbr = models.CharField(max_length = 20, unique = True, db_index = True,)
    name = models.CharField(max_length = 100, blank = True, db_index = True, null = True,)
    status = models.BooleanField(default = ACTIVE, db_index = True, choices = ACTIVE_INACTIVE, )
    location = models.ForeignKey('Location', blank = True, null = True, on_delete = models.SET_NULL, db_index = True,)
    is_parent = models.BooleanField(default = False, db_index = True,)
    assigned_to = models.ForeignKey('self', db_index = True, on_delete = models.SET_NULL, null = True, blank = True,)
    

    def __str__(self):

        if self.name != "":
            return self.name + " ( " + self.abbr +" )"
        return self.abbr

    class META:
        ordering = ["id"]
        verbose_name_plural = 'department_tbl'
    
#
# Designation Model. Used to specify the designation of the user
#
class Designation(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    ACTIVE_INACTIVE = ((ACTIVE, 'Active'),(INACTIVE,'In-Active'))

    abbr = models.CharField(max_length = 20, unique = True, db_index = True,)
    name = models.CharField(max_length = 100, blank = True, db_index = True, null = True,)
    status = models.BooleanField(default = ACTIVE, db_index = True, choices = ACTIVE_INACTIVE, )
    department = models.ForeignKey('Department', blank = True, null = True, on_delete = models.SET_NULL, db_index = True,)

    def __str__(self):
        
        if self.name != "":
            return self.name + " ( " + self.abbr +" )"
        return self.abbr

    class META:
        ordering = ["id"]
        verbose_name_plural = 'designation_tbl'

#
# Custom User Model. Extended from the default user model
#
class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255, db_index = True, null = True,)
    location = models.ForeignKey('Location', on_delete = models.SET_NULL, db_index = True, blank = True, null = True,)
    usertype = models.ForeignKey('Usertype', db_index = True, blank = True, null = True, on_delete = models.SET_NULL,)
    department = models.ForeignKey('Department', on_delete = models.SET_NULL, blank = True, null = True, db_index = True,)
    designation = models.ForeignKey('Designation', on_delete=models.SET_NULL, db_index = True, blank = True, null = True,)
    assigned_to = models.ForeignKey('self', db_index = True, blank = True, null = True, on_delete = models.SET_NULL,)


#
# Assessments Settings 
#     
class Assessment_Settings(models.Model):
    name = models.CharField(max_length = 250, db_index = True, blank = True, null = True,)
    abbr = models.CharField(max_length = 20, unique = True, db_index = True,)
    year = models.CharField(max_length = 4, db_index = True, blank = True, null = True,) 
    session = models.CharField(max_length = 20, db_index = True, blank = True, null = True,)
    status = models.BooleanField(default = True, db_index = True,)
    enable_self_assessment_form = models.BooleanField(default = True, db_index = True, verbose_name = "Self Assessment")
    self_assessment_users = models.ManyToManyField('Usertype', db_index = True, help_text = "Select Usertypes that can fill the self assessment form", related_name="self_assess_form_users")
    self_assessment_form_start_date = models.DateTimeField(auto_now = False, db_index = True, null = True, blank = True, verbose_name = "self assess startdate",)
    self_assessment_form_end_date = models.DateTimeField(auto_now = False, db_index = True, null = True, blank = True, verbose_name = "self assess enddate",)
    enable_assessment_grade_form = models.BooleanField(default = True, db_index = True, verbose_name = "Assessment Grading")
    assessment_graders = models.ManyToManyField('Usertype', db_index = True, help_text = "Select Usertypes that can fill the self assessment form", related_name="assess_grade_users")
    assessment_grade_start_date = models.DateTimeField(auto_now = False, db_index = True, null = True, blank = True, verbose_name = "assess grade startdate",)
    assessment_grade_end_date = models.DateTimeField(auto_now = False, db_index = True, null = True, blank = True, verbose_name = "assess grade enddate",)
    enable_assess_parameters = models.BooleanField(default = True, db_index = True, verbose_name = "Assessment Parameters Form")
    parameters_users = models.ManyToManyField('Usertype', db_index = True, help_text = "Select Usertypes that can fill the parameters form", related_name="parameter_form_users", verbose_name = "Parameter Form Fillers")
    parameters_graders = models.ManyToManyField('Usertype', db_index = True, help_text = "Select Usertypes that can grade the parameters form", related_name="parameter_grade_users", verbose_name = "Parameter Form Graders")
    parameters_start_date = models.DateTimeField(auto_now = False, db_index = True, null = True, blank = True, verbose_name = "parameters startdate",)
    parameters_end_date = models.DateTimeField(auto_now = False, db_index = True, null = True, blank = True, verbose_name = "parameters enddate",)
    self_assess_template = models.CharField(max_length = 250, blank = True, null = True, db_index = True,)
    assess_grade_template = models.CharField(max_length = 250, blank = True, null = True, db_index = True,)
    parameters_template = models.CharField(max_length = 250, blank = True, null = True, db_index = True,)

    def __str__(self):
        
        if self.name != "":
            return self.name + " ( " + self.abbr +" )"
        return self.abbr

    def self_assess_users(self):
        return ', '.join([user.name for user in self.self_assessment_users.all()])    

    def assess_graders(self):
        return ', '.join([user.name for user in self.assessment_graders.all()])

    def parameter_form_users(self):
        return ', '.join([user.name for user in self.parameters_users.all()])   

    def parameter_form_graders(self):
        return ', '.join([user.name for user in self.parameters_graders.all()])         

    class META:
        ordering = ["id"]
        verbose_name_plural = 'assessment_settings'

#
# Self Assessment Form Sections  
# 
class AssessmentFormSection(models.Model):
    name = models.CharField(max_length = 250, null = True, blank = True,)
    details = models.TextField(blank = True, null = True,)
    status = models.BooleanField(default = True, db_index = True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name_plural = 'assessment_form_section'  

#
# Self Assessment Form Sections - Questions
# 
class AssessmentFormQuestions(models.Model):

    TEXTAREA = 1
    INPUT_BOX = 2
    RADIO = 3
    CHECKBOX = 4  
    DROPDOWN = 5

    QTYPES = (
        (TEXTAREA, 'Textarea'), 
        (INPUT_BOX, 'Input Box'),
        (RADIO, 'Radio Input'),
        (CHECKBOX, 'Checkbox'),
        (DROPDOWN, 'Dropdown'),
    ) 

    section = models.ForeignKey('AssessmentFormSection',  null = True, blank = True, on_delete = models.SET_NULL, db_index = True,)
    question = models.TextField(blank = True,)
    question_type = models.BigIntegerField(db_index = True, choices = QTYPES, default = TEXTAREA,)
    status = models.BooleanField(default = True, db_index = True,)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = 'assessment_form_questions'

#
# Self Assessment Form Sections - Questions - Options (only if radio, dropdown and checkbox)
# 
class AssessmentFormOptions(models.Model):
    question = models.ForeignKey('AssessmentFormQuestions', null = True, blank = True ,on_delete = models.SET_NULL, db_index = True,)
    options = models.TextField(blank = True, null = True,)
    status = models.BooleanField(default = True, db_index = True, )

    class Meta:
        ordering = ["id"]
        verbose_name_plural = 'assessment_form_options'


