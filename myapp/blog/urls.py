# blog/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('', views.post_list, name='post_list'), 
    path('posts/', views.posts_view, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
# blog/urls.py
