# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# IntegrityError Exception for checking duplicate entry, 
# connection import to establish connection to database 
from django.db import IntegrityError, connection 

# Used for serializing object data to json string
from django.core.serializers.json import DjangoJSONEncoder 
from django.core.serializers import serialize

from django.http import HttpResponse, Http404, HttpResponseForbidden

# Paginator class import
from django.core.paginator import Paginator

# Django settings from settings.py
from django.conf import settings	

# Condition operators for models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Other imports
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import *
import sys, os, csv, json, datetime


# Create your views here.

def location_selects(request):
    if request.is_ajax():

        if request.POST["id"]!="" and request.POST["id"].isnumeric():
            departments = Department.objects.filter(Q(location_id = request.POST["id"]) | Q(location__isnull = True)).values('id','abbr','name')
            serialized_q = json.dumps(list(departments), cls=DjangoJSONEncoder)
            return HttpResponse(serialized_q)
        raise Http404      
    raise Http404    