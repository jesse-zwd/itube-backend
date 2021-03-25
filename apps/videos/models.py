from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Video(models.Model):
    user = models.ForeignKey(User, related_name='videos', verbose_name='所有者', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='标题', verbose_name='标题')
    description = models.CharField(max_length=300, default='暂无视频介绍', verbose_name='描述')
    url = models.CharField(max_length=500, default='url', verbose_name='链接')
    thumbnail = models.CharField(max_length=500, default='thumbnail', verbose_name='简略图')
    createdAt = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    updatedAt = models.DateTimeField(verbose_name='更新时间', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class VideoRecommended(models.Model):
    video = models.ForeignKey(Video, verbose_name='推荐视频', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    def __str__(self):
        return self.video.title

    class Meta:
        verbose_name = '推荐视频'
        verbose_name_plural = verbose_name