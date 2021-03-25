"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from users.views import LoginViewset, SignupViewSet, ProfileViewset, UsersViewset
from videos.views import VideoViewset, FeedViewset, VideoRecommendedViewset
from operations.views import CommentsViewset, VideoDislikeViewset, VideoLikeViewset, SubscriptionViewset, VideosLikedViewset, ViewsViewset, VideosViewedViewset, ChannelRecommendedViewset

router = DefaultRouter()

router.register(r'signup', SignupViewSet, basename = 'signup')
router.register(r'profile', ProfileViewset, basename='profile')
router.register(r'videos', VideoViewset, basename='videos')
router.register(r'users', UsersViewset, basename = 'users')
router.register(r'comments', CommentsViewset, basename = 'comments')
router.register(r'videolike', VideoLikeViewset, basename = 'videolike')
router.register(r'videodislike', VideoDislikeViewset, basename='videodislike')
router.register(r'channel', SubscriptionViewset, basename = 'channel')
router.register(r'videosliked', VideosLikedViewset, basename='videosliked')
router.register(r'view', ViewsViewset, basename = 'view')
router.register(r'videosViewed', VideosViewedViewset, basename='videosViewed')
router.register(r'feed', FeedViewset, basename = 'feed')
router.register(r'videoRecommended', VideoRecommendedViewset, basename='videoRecommended')
router.register(r'channelRecommended', ChannelRecommendedViewset, basename = 'channelRecommended')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'docs/', include_docs_urls(title="Backend")),
    path('login/', LoginViewset.as_view(), name='token_obtain_pair'),
]
