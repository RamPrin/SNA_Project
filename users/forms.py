from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

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
class DoublePasswordRegisterForm(UserCreationForm):
    """
    A form that consists of username and password fields
    with one additional confirming password field.
    """
    class Meta(UserCreationForm.Meta):
        model = CustomUser


@set_widgets_class
class SinglePasswordRegisterForm(forms.ModelForm):
    """
    A form that creates a user, from the given username and password.
    """

    username = forms.CharField(
        widget=forms.TextInput(),
        label=_("Username"),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_("Password"),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


@set_widgets_class
class CustomAuthenticationForm(AuthenticationForm):
    pass


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
