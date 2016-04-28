from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def partial(postcode):
    if postcode:
        format_string = postcode.split()
        if len(format_string)>1:       
            first_part = format_string [0]+ " " 
            second_part = format_string [1][:1] 
            return first_part + second_part
        else:
            return format_string [0]