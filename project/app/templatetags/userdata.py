from django import template
from app.models import *

register = template.Library()


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