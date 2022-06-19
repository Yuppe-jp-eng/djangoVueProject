from django import template

register = template.Library()


@register.filter
def as_percentage_of(part, whole):
    try:
        return f"{float(part) / whole * 100:.1f}%"
    except (ValueError, ZeroDivisionError):
        return "0.0%"
