from django.db import models
from django.utils import timezone

from core import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)