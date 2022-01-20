from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic.edit import ModelFormMixin

from .forms import PostCreationForm
from .models import Post


@login_required(login_url=reverse_lazy('users:login'))
def get_logged_profile(request):
    a = reverse('blog:profile', args=(request.user.username,))
    return HttpResponseRedirect(a)


def index_view(request):
    return HttpResponseRedirect(reverse('blog:feed'))


class ProfileView(ModelFormMixin, View):
    """
    View which implements both get & post functionalities for different Models:
    GET: Returns list of Post corresponding to current user
    POST: Create new Post by PostCreationForm form
    """
    form_class = PostCreationForm
    model = get_user_model()

    def __init__(self):
        self.request = None
        super().__init__()

    def get(self, request, *args, **kwargs):
        profile_user = self.model.objects.filter(**kwargs).first()

        if profile_user is None:
            raise Http404

        post_list = Post.objects.filter(author=profile_user).order_by('-pub_date')
        context = {
            'form': self.form_class,
            'profile_user': profile_user,
            'post_list': post_list,
        }
        return render(request, 'blog/profile.html', context=context)

    def post(self, request, *args, **kwargs):
        self.request = request
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        request_user = self.request.user
        form.save(user=request_user)

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.request.path


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/feed.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-pub_date')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
