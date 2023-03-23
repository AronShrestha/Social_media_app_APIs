from rest_framework import serializers
from django.contrib.auth import authenticate
from feeds.models import *
from user.serializers import UserSerializer
# from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from rest_framework.validators import UniqueValidator
# from user.utils import send_mail


class NewsfeedSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Posts
        fields ="__all__"
        # ordering =['timestamp']


class GetPostSerializers(serializers.ModelSerializer):
    class Meta :
        model = Posts
        fields =['user','caption','image','video']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Posts
        fields = ['caption','image','video']
    
    def create(self, validated_data):
        post = Posts.objects.create(
            user = self.context.get('user'),
            caption = validated_data['caption'],
            image = validated_data['image'],
           
            )
        print("Username "+post.user.username)
        return post

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        field = ['comment_text']
    
    def create(self,validaed_data):
        comment = Comment.objects.create(
            user = self.context.get('user'),
            post = self.context.get('post'),
            comment_text = validaed_data['comment_text'], 
        )
        print(f"post {post} posted by {user}")
        return comment