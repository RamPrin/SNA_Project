from django.urls import path

from .views import RegisterView, CustomLoginView, ProfileView, CustomLogoutView

app_name = 'users'
urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
]
