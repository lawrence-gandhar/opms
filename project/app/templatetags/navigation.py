from django import template

# Django settings from settings.py
from django.conf import settings

# Import models
from app.models import *

# Condition operators for models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone

# use Library
register = template.Library()

@register.filter
def assessment_links(value):

    user = CustomUser.objects.get(is_active = True, pk = int(value))

    assessments = Assessment_Settings.objects.filter(status = True).filter(
        (Q(access_users__in = [user.usertype_id]) | Q(access_users__isnull = True)),
        (Q(locations__in = [user.location_id]) | Q(locations__isnull = True))
    ).values()

    html = []

    if len(assessments) > 0:
        html.append('<li><a href="javascript:void(0);" class="menu-toggle"><i class="material-icons">widgets</i><span>Assessments</span></a>')
        html.append('<ul class="ml-menu">')

        for assess in assessments:
            html.append('<li><a href="'+link(user.usertype_id)+'assessments/'+dynamic_links(assess["name"])+'/'+str(assess["id"])+'/">'+assess["name"].title()+'</a></li>')

        html.append('</ul>')
        html.append('</li>')

    return ''.join(html)


#
# Usertype Links
#
def link(value):
    try:
        url = Usertype.objects.get(pk = value)
        link = url.link
    except ObjectDoesNotExist:
        link = ''

    return link            


#
# assessment links
#     
def dynamic_links(value):
    return value.lower().replace(" ","-")
