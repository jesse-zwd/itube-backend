# Generated by Django 3.1.2 on 2021-04-19 10:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0003_auto_20210419_1047'),
        ('operations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channelrecommended',
            options={'verbose_name': 'channel', 'verbose_name_plural': 'channel'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'comment', 'verbose_name_plural': 'comment'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'channel', 'verbose_name_plural': 'channel'},
        ),
        migrations.AlterModelOptions(
            name='videodislike',
            options={'verbose_name': 'dislike', 'verbose_name_plural': 'dislike'},
        ),
        migrations.AlterModelOptions(
            name='videolike',
            options={'verbose_name': 'like', 'verbose_name_plural': 'like'},
        ),
        migrations.AlterModelOptions(
            name='view',
            options={'verbose_name': 'view', 'verbose_name_plural': 'view'},
        ),
        migrations.AlterField(
            model_name='channelrecommended',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='channel'),
        ),
        migrations.AlterField(
            model_name='channelrecommended',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='createdAt'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='createdAt'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(default='', max_length=500, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='commentor'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='videos.video', verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to=settings.AUTH_USER_MODEL, verbose_name='channel'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='createdAt'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='subscriber'),
        ),
        migrations.AlterField(
            model_name='videodislike',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='createdAt'),
        ),
        migrations.AlterField(
            model_name='videodislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='videodislike',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isDisliked', to='videos.video', verbose_name='video disliked'),
        ),
        migrations.AlterField(
            model_name='videolike',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='createdAt'),
        ),
        migrations.AlterField(
            model_name='videolike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='videolike',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videosLiked', to='videos.video', verbose_name='video liked'),
        ),
        migrations.AlterField(
            model_name='view',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='createdAt'),
        ),
        migrations.AlterField(
            model_name='view',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='viewer'),
        ),
        migrations.AlterField(
            model_name='view',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.video', verbose_name='video'),
        ),
    ]