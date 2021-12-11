from django.contrib.auth import authenticate, login
from django.urls import reverse

from users.models import CustomUser


def custom_get_success_url(request):
    next_param = request.GET.get('next', None)
    if next_param:
        return next_param

    return reverse('blog:me')


def login_as_demo_user(request):
    username = 'demo_user'
    password = '123'

    user, _ = CustomUser.objects.get_or_create(username=username, password=password)

    if user:
        authenticate(username=username, password=password)
        login(request, user)
        return True

    return False