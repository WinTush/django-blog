from typing import Optional

from django import template
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()


@register.filter
def author_details(author: User, current_user: Optional[User] = None):
    if not isinstance(author, user_model):
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        email = author.email
        return format_html('<a href="mailto:{}">{}</a>', email, name)

    return name
