from django.urls import path

from .views import PostListView

# app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view())  # , name='feed'),
    # path('', index_view, name='index'),
    # path('me/', get_logged_profile, name='me'),
    # path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    # path('posts/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
