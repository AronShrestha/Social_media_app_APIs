from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from user.serializers import UserSerializer


class FollowerSerializer_name(serializers.Serializer):
   
    user = serializers.CharField()

class FollowerSerializer(serializers.ModelSerializer):
    
    # user = serializers.CharField()
    class Meta:
        model = Profile
        # fields = "__all__"
        fields = ["following"]

class GetProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"

class GetDetailProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"

class Follow_Unfollow_Serializer(serializers.Serializer):
    id = serializers.CharField()


