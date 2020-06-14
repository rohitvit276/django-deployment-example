from django import template
register = template.Library()

@register.filter
def cutout(value, arg):
    '''
    This cuts out all the value of arg from the string
    '''
    return value.replace(arg, '')
