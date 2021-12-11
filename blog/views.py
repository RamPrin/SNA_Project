from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic


class NewPostView(generic.CreateView):
    pass


class NavbarActiveMixin:
    current_view_name = None


class IndexView(NavbarActiveMixin, generic.TemplateView):
    current_view_name = 'blog:index'
    template_name = 'blog/index.html'


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    current_view_name = 'blog:profile'
    template_name = 'blog/profile.html'

    def get_login_url(self):
        return reverse('users:login')