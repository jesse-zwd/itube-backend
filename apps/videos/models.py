from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Video(models.Model):
    user = models.ForeignKey(User, related_name='videos', verbose_name='owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='title', verbose_name='title')
    description = models.CharField(max_length=300, default='description', verbose_name='description')
    url = models.CharField(max_length=500, default='url', verbose_name='url')
    thumbnail = models.CharField(max_length=500, default='thumbnail', verbose_name='thumbnail')
    createdAt = models.DateTimeField(verbose_name='time of creating', default=datetime.now)
    updatedAt = models.DateTimeField(verbose_name='time of updating', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = verbose_name


class VideoRecommended(models.Model):
    video = models.ForeignKey(Video, verbose_name='video', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(verbose_name='time of creating', default=datetime.now)

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = verbose_name