from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

from .models import CustomUser
from .utils import set_widgets_class


class TemplateFormMixin:
    form_title = 'Title'
    submit_text = 'Submit'


@set_widgets_class
class DoublePasswordRegisterForm(UserCreationForm, TemplateFormMixin):
    """
    A form that consists of username and password fields
    with one additional confirming password field.
    """

    form_title = 'Register'
    submit_text = 'Register Account'

    class Meta(UserCreationForm.Meta):
        model = CustomUser


@set_widgets_class
class SinglePasswordRegisterForm(forms.ModelForm, TemplateFormMixin):
    """
    A form that creates a user, from the given username and password.
    """

    form_title = 'Register'
    submit_text = 'Register Account'

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
    form_title = 'Sign In'
    submit_text = 'Log in'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
