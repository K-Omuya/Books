from django import template

register = template.Library()

@register.filter
def get_choice(value, choice_dict):
    return choice_dict.get(value, value)
