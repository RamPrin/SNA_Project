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


def set_widgets_class(form_class):
    """
    set "class" to "form-control" in attrs of widget of every form field
    """

    class MyFormClass(form_class):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    return MyFormClass