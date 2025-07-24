# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('more', views.more, name='more'),
    path('news_list', views.news_list, name='news_list'),
    path('news_details/<int:pk>/', views.news_details, name='news_details'),
]