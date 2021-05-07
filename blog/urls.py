from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about_site/', views.about_site, name='about_site'),
]
