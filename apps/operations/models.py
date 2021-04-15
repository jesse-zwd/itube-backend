from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from videos.models import Video

User = get_user_model() 


# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length=500, default='', verbose_name='comment')
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE, verbose_name='video')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='commentor')
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='time of creating')
  
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = verbose_name


class VideoLike(models.Model):
    video = models.ForeignKey(Video, related_name="videosLiked", on_delete=models.CASCADE, verbose_name='video liked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='time of creating')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = verbose_name


class VideoDislike(models.Model):
    video = models.ForeignKey(Video, related_name='isDisliked', on_delete=models.CASCADE, verbose_name='video disliked')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='time of creating')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = 'dislike'
        verbose_name_plural = verbose_name


class View(models.Model):
    user = models.ForeignKey(User, verbose_name='viewer', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, verbose_name='video', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='time of creating')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = 'view'
        verbose_name_plural = verbose_name


class Subscription(models.Model):
    channel = models.ForeignKey(User, related_name="channels", verbose_name='channel', on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User, verbose_name='subscriber', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='time of creating')

    def __str__(self):
        return self.channel.username

    class Meta:
        verbose_name = 'channel'
        verbose_name_plural = verbose_name


class ChannelRecommended(models.Model):
    channel = models.ForeignKey(User, verbose_name='channel', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='time of creating')

    def __str__(self):
        return self.channel.username

    class Meta:
        verbose_name = 'channel'
        verbose_name_plural = verbose_name
