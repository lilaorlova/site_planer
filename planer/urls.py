from django.urls import path
from . import views


urlpatterns = [
    path('planer/', views.post_list, name='base'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
