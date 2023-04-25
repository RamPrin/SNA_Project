from django.views import generic

from posts.models import Post


# def index_view(request):
#     return HttpResponseRedirect(reverse('blog:feed'))

class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/feed.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-pub_date')
