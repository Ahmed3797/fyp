from django import template
from datetime import datetime

register = template.Library()

@register.filter
def parse_date(date_str):
    """
    Custom template filter to parse the date string and convert it to a datetime object.
    """
    return datetime.strptime(date_str, "%B %d, %Y")