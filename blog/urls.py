from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_list', views.post_list, name='post_list'),
]