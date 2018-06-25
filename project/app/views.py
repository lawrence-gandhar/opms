# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

# Create your views here.

def location_selects(request):
    if request.is_ajax():
        return HttpResponse('')