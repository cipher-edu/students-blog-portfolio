from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
def home(request):
    categories = Category.objects.all()
    selected_cotegory = request.GET.get('category')

    if selected_cotegory:
        post = Post.objects.filter(category__name = selected_cotegory)
    else:
        post = Post.objects.all()

    context = {
        'post':post,
        'categories':categories,
        'selected_cotegory':selected_cotegory
    }
    return render(request, 'index.html', context)
    # post = Post.objects.all()

    # context = {
    #     'post':post
    # }
    

def post_detail(request, pk):
    data = get_object_or_404(Post, pk=pk)
    context = {
        'data':data
    }

    return render(request, 'post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'post_create.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'post_update.html', context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'post_delete.html', {'post':post})