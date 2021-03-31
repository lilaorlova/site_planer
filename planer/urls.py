from django.urls import path
from . import views


urlpatterns = [
    path('planer/', views.post_list, name='post_list'),
]
