from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import mixins, viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import JWTSerializer, UserSignupSerializer, UserChannelsSerializer, UserProfileUpdateSerializer
from videos.serializers import UserProfileSerializer

User = get_user_model()

# Create your views here.

class LoginViewset(TokenObtainPairView):
    serializer_class = JWTSerializer


class SignupViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSignupSerializer


class ProfileViewset(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, SessionAuthentication )
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "update":
            return UserProfileUpdateSerializer

        return UserProfileSerializer


class UsersViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = (JWTAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.exclude(is_staff=True)  
    serializer_class = UserChannelsSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('username', 'channelDescription')

