from django import template

# Django settings from settings.py
from django.conf import settings

# Import models
from app.models import *

import datetime

# use Library
register = template.Library()

@register.filter
def self_assessment_link(value):
    link_enabled = Assessment_Settings.objects.filter(status = True, enable_self_assessment_form = True, self_assessment_users__in = list([int(value)]), self_assessment_form_start_date__lte = datetime.datetime.now(), self_assessment_form_end_date__gte = datetime.datetime.now()).count()
    if link_enabled == 1:
        return True
    return False

@register.filter
def self_assessment_grade_link(value):
    link_enabled = Assessment_Settings.objects.filter(status = True, enable_assessment_grade_form = True, assessment_graders__in = list([int(value)]), assessment_grade_start_date__lte = datetime.datetime.now(), assessment_grade_end_date = datetime.datetime.now()).count()
    if link_enabled == 1:
        return True
    return False