# blogPosts/views.py
from django.shortcuts import render, redirect
from .models import Post


def index(request):
    if request.method == 'GET':  # index
        posts = Post.objects.all()
        return render(request, 'blogPosts/index.html', {'posts': posts})
    elif request.method == 'POST': # create
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('blogPosts:index')


def new(request):
    return render(request, 'blogPosts/new.html')


def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogPosts/show.html', {'post': post})


def edit(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogPosts/edit.html', {'post': post})


def update(request, id):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Post.objects.filter(id=id).update(title=title, content=content)
    return redirect('blogPosts:index')


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('blogPosts:index')
