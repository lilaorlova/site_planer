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
import calendar
from datetime import datetime


def post_list(request):
    c = calendar.HTMLCalendar()
    html_out = c.formatmonth(datetime.today().year, datetime.today().month)
    user=User.objects.get(username=request.user.username)
    plans=Post.objects.filter(author=user).order_by("created_date")
    return render(request, 'planer/post_list.html', {"plans":plans})

def profile(request):
    return render(request, 'planer/profile.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(form["title"].value())
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('base')
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
            return redirect('base')
    else:
        form = PostForm(instance=post)
    return render(request, 'planer/post_edit.html', {'form': form})

def del_(request, id_):
    Post.objects.get(id=id_).delete()
    return redirect('base')

def ready_plans(request):
    c = calendar.HTMLCalendar()
    html_out = c.formatmonth(datetime.today().year, datetime.today().month)
    user=User.objects.get(username=request.user.username)
    plans=Post.objects.filter(author=user).order_by("created_date")
    return render(request, 'planer/ready_plans.html', {"plans":plans})

