from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from videos.models import Video

User = get_user_model() 


# Create your models here.

class Comment(models.Model):
    text = models.CharField(max_length=500, default='', verbose_name='评论')
    video = models.ForeignKey(Video, related_name='comments', on_delete=models.CASCADE, verbose_name='视频')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论者')
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
  
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class VideoLike(models.Model):
    video = models.ForeignKey(Video, related_name="videosLiked", on_delete=models.CASCADE, verbose_name='喜欢的视频')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name


class VideoDislike(models.Model):
    video = models.ForeignKey(Video, related_name='isDisliked', on_delete=models.CASCADE, verbose_name='讨厌的视频')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = '点踩'
        verbose_name_plural = verbose_name


class View(models.Model):
    user = models.ForeignKey(User, verbose_name='观看者', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, verbose_name='视频', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = '观看数量'
        verbose_name_plural = verbose_name


class Subscription(models.Model):
    channel = models.ForeignKey(User, related_name="channels", verbose_name='订阅频道', on_delete=models.CASCADE)
    subscriber = models.ForeignKey(User, verbose_name='订阅者', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.channel.username

    class Meta:
        verbose_name = '订阅频道'
        verbose_name_plural = verbose_name


class ChannelRecommended(models.Model):
    channel = models.ForeignKey(User, verbose_name='推荐频道', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    def __str__(self):
        return self.channel.username

    class Meta:
        verbose_name = '推荐频道'
        verbose_name_plural = verbose_name
