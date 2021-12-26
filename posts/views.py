from typing import Dict

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def index(request):

    posts = Post.objects.all()
    posts_data = {
        'posts':posts
    }
    return render(request, 'index.html', context=posts_data)

def get_details(request,post_id):
    post = get_object_or_404(Post, pk = post_id)

    post_data = dict({
        'posts' : post
    })

    return render(request, 'posts.html', context = post_data)
