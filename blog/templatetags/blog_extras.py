from django import template
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

user_model = get_user_model()
register = template.Library()


@register.filter
def author_details(author: User) -> str:
    if not isinstance(author, user_model):
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    return name
