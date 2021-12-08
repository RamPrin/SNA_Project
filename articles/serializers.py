from rest_framework import serializers

from users.models import CustomUser
from users.serializers import UserSerializer
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CreateArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        exclude = ('author',)
