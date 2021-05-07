
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def about_site(request):
    return render(request, 'blog/about_site.html', {})
