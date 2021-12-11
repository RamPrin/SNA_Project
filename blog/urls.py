from django.urls import path

from .views import ProfileView, IndexView, PostListView, PostDetailView, get_logged_profile

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('me/', get_logged_profile, name='me'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('feed/', PostListView.as_view(), name='feed'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
