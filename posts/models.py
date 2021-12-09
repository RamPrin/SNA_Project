from django.db import models

from core import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
