from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/(?P<pk>[0-9]+)/', views.detail, name='detail'),
    path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archives, name='archives'),
    path('category/(?P<pk>[0-9]+)/', views.category, name='category'),
]
