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
    use_nav_from_template_folder = models.BooleanField(default = True, db_index = True,)
    navbar_template = models.TextField(null = True, blank = True, db_index = True,)
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

    