from django.urls import path
from . import views

app_name = 'blog'  # Add namespace to URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]