from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, View, VideoLike, VideoDislike, Subscription, ChannelRecommended
from users.serializers import UsersSerializer
        

class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Subscription
        validators = [
            UniqueTogetherValidator(
                queryset=Subscription.objects.all(),
                fields=('subscriber', 'channel'),
                message="已经订阅"
            )
        ]
        fields = ('subscriber', 'channel')


class CommentsSerializer(serializers.ModelSerializer): 
    user = UsersSerializer()
    
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ViewCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = View
        validators = [
            UniqueTogetherValidator(
                queryset=View.objects.all(),
                fields=('user', 'video'),
                message="已经观看"
            )
        ]
        fields = ('user', 'video')
        

class VideoLikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = VideoLike
        validators = [
            UniqueTogetherValidator(
                queryset=VideoLike.objects.all(),
                fields=('user', 'video'),
                message="已经点赞"
            )
        ]

        fields = ("user", "video", "id")


class VideoDislikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = VideoDislike
        validators = [
            UniqueTogetherValidator(
                queryset=VideoDislike.objects.all(),
                fields=('user', 'video'),
                message="已经不赞"
            )
        ]

        fields = ("user", "video", "id")


