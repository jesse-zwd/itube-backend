from django.contrib import admin

from .models import Comment, VideoLike, VideoDislike, View, Subscription, ChannelRecommended

# Register your models here.
admin.site.register(Comment)
admin.site.register(VideoLike)
admin.site.register(VideoDislike)
admin.site.register(View)
admin.site.register(Subscription)
admin.site.register(ChannelRecommended)
