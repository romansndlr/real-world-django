from django.db import models
from .tag import Tag
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
