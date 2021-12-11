from django.urls import path

from .views import ProfileView, IndexView

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile', ProfileView.as_view(), name='profile'),
]
