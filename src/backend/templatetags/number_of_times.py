from django import template
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def number_of_times(value, first_upper=False):
    try:
        value = int(value)
        if value not in (1, 2):
            return value
    except (TypeError, ValueError):
        return value
    templates = (
        _(f"number_of_times {'first_upper' if first_upper else 'first_lower'} 1"),
        _(f"number_of_times {'first_upper' if first_upper else 'first_lower'} 2"),
    )
    value = templates[value - 1].format(value)
    return mark_safe(value)
