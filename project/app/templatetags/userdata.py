from django import template

# Django settings from settings.py
from django.conf import settings

# Import models
from app.models import *

# use Library
register = template.Library()

#
# Tag to return url prefix based on user type
#

@register.simple_tag
def current_user_link(value):
    value = int(value)
    link = ''

    try:
        url = Usertype.objects.get(pk = value)
        link = url.link
    except:
        pass
    return link


#
# Filter for returning location of menu/sidebar/navigation template
#

@register.filter
def menu_template(value):
    value = int(value)
    nav_template = settings.BASE_DIR+"/app/templates/app/"

    try:
        nav_tmp = Usertype.objects.get(pk = value)

        if nav_tmp.use_nav_from_template_folder:
            nav_template += nav_tmp.template_folder +"/"+ nav_tmp.navbar_template
        else:
            nav_template += nav_tmp.navbar_template   
    except:
        pass
    return nav_template   