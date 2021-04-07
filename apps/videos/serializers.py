from rest_framework import serializers
from django.db.models import Q
from django.contrib.auth import get_user_model

from .models import Video, VideoRecommended
from operations.serializers import CommentsSerializer, VideoDislikeSerializer, VideoLikeSerializer, SubscriptionSerializer
from operations.models import Comment, VideoLike, VideoDislike, Subscription, View

from users.serializers import UsersSerializer

User = get_user_model()

class VideoSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    isLiked = serializers.SerializerMethodField()
    isDisliked = serializers.SerializerMethodField()
    user = UsersSerializer()
    likesCount = serializers.SerializerMethodField()
    dislikesCount = serializers.SerializerMethodField()
    isVideoMine = serializers.SerializerMethodField()
    isSubscribed = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()

    def get_comments(self, instance):
        video_comments = Comment.objects.filter(Q(video=instance.id)).order_by('-createdAt')
        comments_serializer = CommentsSerializer(video_comments, many=True, read_only=True)
        return comments_serializer.data

    def get_isLiked(self, instance):
        return VideoLike.objects.filter(Q(video=instance.id) & Q(user=self.context["request"].user.id)).exists()

    def get_isDisliked(self, instance):
        return VideoDislike.objects.filter(Q(video=instance.id) & Q(user=self.context["request"].user.id)).exists()

    def get_likesCount(self, instance):
        return VideoLike.objects.filter(Q(video=instance.id)).count()

    def get_dislikesCount(self, instance):
        return VideoDislike.objects.filter(Q(video=instance.id)).count()

    def get_isVideoMine(self, instance):
        return instance.user_id == self.context["request"].user.id

    def get_isSubscribed(self, instance):
        return Subscription.objects.filter(Q(channel=instance.user_id) & Q(subscriber=self.context["request"].user.id)).exists()

    def get_views(self, instance):
        return View.objects.filter(Q(video=instance.id)).count()

    class Meta:
        model = Video
        fields = '__all__'


class VideosSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    views = serializers.SerializerMethodField()

    def get_views(self, instance):
        return View.objects.filter(Q(video=instance.id)).count()

    class Meta:
        model = Video
        fields = '__all__'


class VideosLikedSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()

    def get_videos(self, instance):
        videolike = VideoLike.objects.filter(Q(user=self.context["request"].user.id)).values()
        ids = []
        for v in videolike:
            ids.append(v['video_id'])
        videos_liked = Video.objects.filter(Q(id__in=ids))
        videosliked_serializer = VideosSerializer(videos_liked, many=True, read_only=True)
        return videosliked_serializer.data

    class Meta:
        model = VideoLike
        fields = ('videos',)


class VideosViewedSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()

    def get_videos(self, instance):
        view = View.objects.filter(Q(user=self.context['request'].user.id)).values()
        ids = []
        for v in view:
            ids.append(v['video_id'])
        videos_viewed = Video.objects.filter(Q(id__in=ids))
        videosViewed_serializer = VideosSerializer(videos_viewed, many=True, read_only=True)
        return videosViewed_serializer.data        

    class Meta:
        model = View
        fields = ('videos',)


class UserProfileSerializer(serializers.ModelSerializer):
    videos = serializers.SerializerMethodField()
    isMe = serializers.SerializerMethodField()
    isSubscribed = serializers.SerializerMethodField()
    subscribersCount = serializers.SerializerMethodField()
    channels = serializers.SerializerMethodField()

    def get_videos(self, instance):
        user_videos = Video.objects.filter(Q(user=instance.id))
        userVideos_serializer = VideosSerializer(user_videos, many=True, read_only=True)
        return userVideos_serializer.data

    def get_isMe(self, instance):
        return self.context['request'].user.id == instance.id

    def get_isSubscribed(self, instance):
        return Subscription.objects.filter(Q(channel=instance.id) & Q(subscriber=self.context["request"].user.id)).exists()

    def get_subscribersCount(self, instance):
        return Subscription.objects.filter(Q(channel=instance.id)).count() 

    def get_channels(self, instance):
        subscriptions = Subscription.objects.filter(Q(subscriber=instance.id)).values()
        ids = []
        for s in subscriptions:
            ids.append(s['channel_id'])
        user_channels = User.objects.filter(Q(id__in=ids))
        userChannels_serializer = UsersSerializer(user_channels, many=True, read_only=True)
        return userChannels_serializer.data

    class Meta: 
        model = User
        fields = ("id", "nickname", "first_name", "last_name", "channelDescription", "avatar", "cover", "videos", "isMe", "isSubscribed", "subscribersCount", "channels")


class VideoCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Video
        fields = ("user", "title", "description", "url", "thumbnail")
