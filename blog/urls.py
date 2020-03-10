from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.blog_index,name='blog_index'),
    path('add/', views.blog_add,name='blog_add'),
    path('list/', views.blog_list,name='blog_list'),
    path('detail/<blog_id>/', views.blog_detail,name='blog_detail'),
    path('delete/<blog_id>/', views.blog_delete,name='blog_delete'),
    path('update/<blog_id>/', views.blog_update,name='blog_update'),
]