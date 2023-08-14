from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post


def index(request: HttpRequest):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request: HttpRequest, slug: str):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
