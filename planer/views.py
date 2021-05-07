from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User

def post_list(request):
    user=User.objects.get(username=request.user.username)
    plans=Post.objects.filter(author=user).order_by("created_date")
    return render(request, 'planer/post_list.html', {"plans":plans})

def profile(request):
    return render(request, 'planer/profile.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(author=User.objects.get(username=request.user.username),
                                title=form["title"].value(),
                                text=form["text"].value(),
                                created_date=timezone.now()
                                )
            print(form["title"].value())
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_new')
    else:
        form = PostForm()
    return render(request, 'planer/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'planer/post_edit.html', {'form': form})
