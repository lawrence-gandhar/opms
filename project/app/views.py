# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# IntegrityError Exception for checking duplicate entry, 
# connection import to establish connection to database 
from django.db import IntegrityError, connection 

# Used for serializing object data to json string
from django.core.serializers.json import DjangoJSONEncoder 
from django.core.serializers import serialize

from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseRedirect

# Paginator class import
from django.core.paginator import Paginator

# Django settings from settings.py
from django.conf import settings	

# Condition operators for models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Other imports
from django.shortcuts import render, redirect
from .models import Usertype, Location, CustomUser, Department, Designation
from .models import Assessment_Settings, AssessmentFormOptions, AssessmentFormQuestions, AssessmentFormSection

import sys, os, csv, json, datetime

#
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

#*******************************************************************************
# DEPARTMENTS FETCHED ON LOCATION SELECT - USERS FORM ADMIN   
#*******************************************************************************

@login_required
def location_selects(request):
    if request.is_ajax():
        if request.POST["id"]!="" and request.POST["id"].isnumeric():
            departments = Department.objects.filter(Q(location_id = request.POST["id"]) | Q(location__isnull = True)).filter(is_parent = True, status = Department.ACTIVE).values('id','abbr','name')
            serialized_q = json.dumps(list(departments), cls=DjangoJSONEncoder)
            return HttpResponse(serialized_q)
        raise Http404      
    raise Http404    

#*******************************************************************************
# CHILD DEPARTMENT FETCHED ON PARENT DEPARTMENT SELECT - USERS FORM ADMIN   
#******************************************************************************* 

@login_required   
def department_selects(request):
    if request.is_ajax():
        if request.POST["id"]!="" and request.POST["id"].isnumeric():
            departments = Department.objects.filter(assigned_to_id = request.POST["id"], status = Department.ACTIVE, is_parent = False).values('id','abbr','name')
            serialized_q = json.dumps(list(departments), cls=DjangoJSONEncoder)
            return HttpResponse(serialized_q)
        raise Http404      
    raise Http404   

#*******************************************************************************
# DESIGNATION FETCHED ON PARENT DEPARTMENT SELECT - USERS FORM ADMIN   
#******************************************************************************* 
   
@login_required
def designation_selects(request):
    if request.is_ajax():
        if request.POST["id"]!="" and request.POST["id"].isnumeric():
            designation = Designation.objects.filter(department_id = request.POST["id"], status = Designation.ACTIVE).values('id','abbr','name')
            serialized_q = json.dumps(list(designation), cls=DjangoJSONEncoder)
            return HttpResponse(serialized_q)
        raise Http404      
    raise Http404     

#*******************************************************************************
# GET USER DETAILS FOR LOCATION, DEPARTMENTS, DESIGNATION, ASSIGNED TO - USERS FORM ADMIN   
#*******************************************************************************  

@login_required
def get_admin_userform_details(request):
    if request.is_ajax():
        if request.POST["id"]!="" and request.POST["id"].isnumeric():
            
            data = dict({"location_id":"", "parent_department":"", "department_id":"", "designation_id":"", "assigned_to_id":""})

            try:
                users = CustomUser.objects.get(pk = request.POST["id"])
                parent_department = Department.objects.get(pk = users.department_id)
                
                data["location_id"] = users.location_id
                data["parent_department"] = parent_department.assigned_to_id
                data["department_id"] = users.department_id
                data["designation_id"] = users.designation_id
                data["assigned_to_id"] = users.assigned_to_id
            except ObjectDoesNotExist:
                pass

            serialized_q = json.dumps(data)
            return HttpResponse(serialized_q)
        raise Http404      
    raise Http404  

#*******************************************************************************
# DESIGNATION FETCHED ON PARENT DEPARTMENT SELECT - USERS FORM ADMIN   
#*******************************************************************************   
    
@login_required
def get_admin_user_list(request):
    if request.is_ajax():
        if request.POST["id"]!="" and request.POST["id"].isnumeric():
            users_list = CustomUser.objects.filter(is_active = True)
            
            try:
                assigned_department = Department.objects.get(status = Department.ACTIVE, pk = request.POST["id"])   
                users_list = users_list.filter((Q((Q(department_id = request.POST["id"])) | (Q(department_id__isnull = True)))) | ((Q(department_id = assigned_department.assigned_to_id))))
            except ObjectDoesNotExist:
                pass

            try:
                assigned_usertype = Usertype.objects.get(status = Usertype.ACTIVE, pk = request.POST["usertype_id"])
                users_list = users_list.filter(usertype_id = assigned_usertype.assigned_to_id)
            except Usertype.DoesNotExist:    
                pass

            users_list = users_list.values('id','name')
            
            serialized_q = json.dumps(list(users_list), cls=DjangoJSONEncoder)
            return HttpResponse(serialized_q)
        raise Http404      
    raise Http404 

#*******************************************************************************
# AUTHENTICATION  
#*******************************************************************************   

def index(request):
    submit = request.POST.get("submit", False)

    if submit:
        
        user = authenticate(username = request.POST["username"], password = request.POST["password"])
        
        if user is not None:
            
            login(request, user)

            url_link = '/'

            try:
                usertype_link = Usertype.objects.get(pk = int(user.usertype_id))
                url_link = usertype_link.link
            except Usertype.DoesNotExist:
                return render(request, 'app/index.html', {}) 
            except TypeError: 
                return render(request, 'app/index.html', {})      

            return redirect(url_link + 'dashboard/')
    return render(request, 'app/index.html', {})


#*******************************************************************************
# LOGOUT  
#*******************************************************************************   

@login_required
def user_logout(request, usertype = None):
    logout(request)
    return HttpResponseRedirect('/')   


#*******************************************************************************
# PASSWORD CHANGE
#*******************************************************************************    

@login_required
def change_password(request):
    if request.is_ajax():
        pass




#*******************************************************************************
# DASHBOARD  
#*******************************************************************************  

@login_required
def dashboard(request, usertype = None):
    pass
    return render(request, 'app/base.html',{})


#*******************************************************************************
# SELF ASSESSMENT FORM  
#*******************************************************************************  

@login_required
def self_assessment_form(request, usertype = None, name = None, id = None):
    #
    # Get assessment settings that fulfill user criteria 
    #
    pass
    return render(request, 'app/base.html',{})    
