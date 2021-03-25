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

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]

        return []

    def get_serializer_class(self):
        if self.action == "list":
            return CommentsSerializer
        elif self.action == "create":
            return CommentCreateSerializer

        return CommentsSerializer


class VideoLikeViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideoLikeSerializer
    lookup_field = 'video_id'

    def get_queryset(self):
        return VideoLike.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "destroy":
            return [permissions.IsAuthenticated()]

        return []


class VideoDislikeViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideoDislikeSerializer
    lookup_field = 'video_id'

    def get_queryset(self):
        return VideoDislike.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "destroy":
            return [permissions.IsAuthenticated()]

        return []


class SubscriptionViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = SubscriptionSerializer
    lookup_field = 'channel_id'

    def get_queryset(self):
        return Subscription.objects.filter(subscriber=self.request.user.id)

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        elif self.action == "destroy":
            return [permissions.IsAuthenticated()]
        elif self.action == "retrieve":
            return [permissions.IsAuthenticated()]

        return []


class VideosLikedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideosLikedSerializer

    def get_queryset(self):
        return VideoLike.objects.filter(user=self.request.user)
        
    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]
    
        return []


class ViewsViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = ViewCreateSerializer

    def get_queryset(self):
        return View.objects.filter(user=self.request.user)
        
    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
    
        return []


class VideosViewedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideosViewedSerializer

    def get_queryset(self):
        return View.objects.filter(user=self.request.user)
        
    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]
    
        return []


class ChannelRecommendedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication )
    serializer_class = UserChannelsSerializer

    def get_queryset(self):
        channels = ChannelRecommended.objects.all().values()
        ids = []
        for c in channels:
            ids.append(c['channel_id'])
        return User.objects.filter(id__in=ids).order_by('-date_joined')

    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]

        return []