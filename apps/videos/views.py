from rest_framework import mixins, viewsets, permissions, filters 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication 
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from .models import Video, VideoRecommended
from .serializers import VideoSerializer, VideoCreateSerializer
from operations.models import Subscription

# Create your views here.

class VideoViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    queryset = Video.objects.all()

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', 'description')

    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        if self.action == "list":
            return [permissions.IsAuthenticated()]

        return []

    def get_serializer_class(self):
        if self.action == "create":
            return VideoCreateSerializer

        return VideoSerializer


class FeedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        subscriptions = Subscription.objects.filter(subscriber=self.request.user).values()
        ids = []
        for s in subscriptions:
            ids.append(s['channel_id'])
        return Video.objects.filter(user__in=ids).order_by('-createdAt')

    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]

        return []
        

class VideoRecommendedViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        videos = VideoRecommended.objects.all().values()
        ids = []
        for v in videos:
            ids.append(v['video_id'])
        return Video.objects.filter(id__in=ids).order_by('-createdAt')

    def get_permissions(self):
        if self.action == "list":
            return [permissions.IsAuthenticated()]

        return []