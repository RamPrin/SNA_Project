from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets

from .forms import CustomUserCreationForm
from .models import CustomUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:profile')

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse('users:profile')


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        return reverse('users:profile')


class ProfileView(generic.TemplateView):
    template_name = 'users/profile.html'
