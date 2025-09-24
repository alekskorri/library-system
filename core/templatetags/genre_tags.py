from pprint import pprint

from django import template
from ..models import Genre

register = template.Library()

@register.simple_tag
def get_genres():
    data_db = Genre.objects.only('genre')
    return data_db
