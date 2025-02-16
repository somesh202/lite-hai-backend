from django.db import models
from django.contrib.auth import get_user_model
from authentication.models import UserProfile


class NoticeBoard(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    voters = models.ManyToManyField(get_user_model(), blank=True)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " - " + self.description
