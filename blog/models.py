from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    # if the user creates a post then the user is deleted, then the post is deleted as well.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.title} by {self.author}')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.title} by {self.author}')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})