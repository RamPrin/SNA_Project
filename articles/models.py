from django.db import models

from users.models import CustomUser


class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
