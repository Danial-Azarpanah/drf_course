from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    """
    Model for Created articles
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             blank=True, null=True,
                             related_name="articles")
    title = models.CharField(max_length=30)
    text = models.TextField()
    status = models.BooleanField()

    def __str__(self):
        return self.title


class BlockUser(models.Model):
    """
    Model to save blocked users
    """
    username = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username
