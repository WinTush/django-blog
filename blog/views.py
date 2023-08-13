from django.http import HttpRequest
from django.shortcuts import render
from django.utils import timezone

from .models import Post


def index(request: HttpRequest):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})
