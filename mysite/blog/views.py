from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts})

def post_detail(request, id):
    status = Post.Status.PUBLISHED
    post = get_object_or_404(Post,id=id,status=status)
    template = 'blog/post/detail.html'
    return render(request, template, {'post': post})