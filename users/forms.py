from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser


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


@set_widgets_class
class CustomUserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser


@set_widgets_class
class CustomUserAuthenticationForm(AuthenticationForm):
    pass


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
