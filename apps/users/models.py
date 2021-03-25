from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, default='', verbose_name='昵称')
    email = models.EmailField(max_length=50, default='', verbose_name='邮箱')
    avatar = models.CharField(max_length=100, default='', verbose_name='头像')
    cover = models.CharField(max_length=500, verbose_name='封面', default='')
    channelDescription = models.CharField(max_length=500, verbose_name='频道描述')
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name