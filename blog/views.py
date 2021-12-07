from rest_framework import viewsets, permissions

from .models import Article
from .serializers import ArticleSerializer, CreateArticleSerializer
from .permissions import IsAuthorOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateArticleSerializer

        return ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()

        query_params_filter_mapping = {
            'username': 'author__username',
            'user_id': 'author_id',
        }

        for query_param, filter_by in query_params_filter_mapping.items():
            param_value = self.request.query_params.get(query_param)

            if param_value is not None:
                kwargs = {filter_by: param_value}
                queryset = queryset.filter(**kwargs)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
