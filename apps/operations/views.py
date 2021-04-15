from rest_framework import mixins, viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model

from .models import Subscription, Comment, VideoLike, VideoDislike, Subscription, View, ChannelRecommended
from .serializers import CommentsSerializer, CommentCreateSerializer, VideoLikeSerializer, VideoDislikeSerializer, SubscriptionSerializer, ViewCreateSerializer
from videos.serializers import VideosLikedSerializer, VideosViewedSerializer
from users.serializers import UserChannelsSerializer 

User = get_user_model()

# Create your views here.

class CommentsViewset(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "create":
            return CommentCreateSerializer

        return CommentsSerializer


class VideoLikeViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideoLikeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'video_id'

    def get_queryset(self):
        return VideoLike.objects.filter(user=self.request.user)


class VideoDislikeViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideoDislikeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'video_id'

    def get_queryset(self):
        return VideoDislike.objects.filter(user=self.request.user)


class SubscriptionViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'channel_id'

    def get_queryset(self):
        return Subscription.objects.filter(subscriber=self.request.user.id)


class VideosLikedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideosLikedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return VideoLike.objects.filter(user=self.request.user)


class ViewsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = ViewCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return View.objects.filter(user=self.request.user)


class VideosViewedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideosViewedSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return View.objects.filter(user=self.request.user)


class ChannelRecommendedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication )
    serializer_class = UserChannelsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        channels = ChannelRecommended.objects.all().values()
        ids = []
        for c in channels:
            ids.append(c['channel_id'])
        return User.objects.filter(id__in=ids).order_by('-date_joined')
