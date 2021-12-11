from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

# from users.models import CustomUser


@login_required(login_url=reverse_lazy('users:login'))
def get_logged_profile(request):
    a = reverse('blog:profile', args=(request.user.username,))
    return HttpResponseRedirect(a)


class NewPostView(generic.CreateView):
    pass


class IndexView(generic.TemplateView):
    template_name = 'blog/index.html'


class ProfileView(generic.DetailView):
    model = get_user_model()
    template_name = 'blog/profile.html'
    context_object_name = 'profile_user'
    
    def get_object(self, queryset=None):
        if not any(i in self.kwargs for i in ['id', 'pk']):
            return self.model(**self.kwargs)

        return super().get_object(queryset)
