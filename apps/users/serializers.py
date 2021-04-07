from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from videos.models import Video
from operations.models import Subscription

User = get_user_model()


class JWTSerializer(TokenObtainPairSerializer):
    def get_channels(self):
        subscriptions = Subscription.objects.filter(Q(subscriber=self.user.id)).values()
        Ids = []
        for s in subscriptions:
            Ids.append(s['channel_id'])
        user_channels = User.objects.filter(Q(id__in=Ids))
        userChannels_serializer = UsersSerializer(user_channels,many=True, read_only=True)
        return userChannels_serializer.data

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # Add custom claims
        data['nickname'] = self.user.nickname
        data['avatar'] = self.user.avatar
        data['id'] = self.user.id
        data['channels'] = self.get_channels()

        return data
        

class UserSignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label="邮箱", help_text="邮箱", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True)
    nickname = serializers.CharField(label="昵称", help_text="昵称", required=True, allow_blank=False)

    def validate(self, attrs):
        attrs["email"] = attrs["username"]
        return attrs

    class Meta:
        model = User
        fields = ("password", "username", "nickname")


class UsersSerializer(serializers.ModelSerializer):
    subscribersCount = serializers.SerializerMethodField()

    def get_subscribersCount(self, instance):
        return Subscription.objects.filter(Q(channel=instance.id)).count()

    def get_videosCount(self, instance):
        return Video.objects.filter(Q(user=instance.id)).count()

    class Meta:
        model = User
        fields = ("nickname", "avatar", "id", "subscribersCount")


class UserChannelsSerializer(serializers.ModelSerializer):
    subscribersCount = serializers.SerializerMethodField()
    videosCount = serializers.SerializerMethodField()
    isSubscribed = serializers.SerializerMethodField()
    isMe = serializers.SerializerMethodField()

    def get_subscribersCount(self, instance):
        return Subscription.objects.filter(Q(channel=instance.id)).count()

    def get_videosCount(self, instance):
        return Video.objects.filter(Q(user=instance.id)).count()
    
    def get_isSubscribed(self, instance):
        return Subscription.objects.filter(Q(channel=instance.id) & Q(subscriber=self.context["request"].user.id)).exists()

    def get_isMe(self, instance):
        return instance.id == self.context["request"].user.id

    class Meta:
        model = User
        fields = ('subscribersCount', 'videosCount', "nickname", "avatar", "id", 'isSubscribed', 'isMe')


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "cover", "avatar", "channelDescription")




