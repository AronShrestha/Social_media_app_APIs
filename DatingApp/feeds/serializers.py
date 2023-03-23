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
        fields =['user','caption','image']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Posts
        fields = ['caption','image']
    
    def create(self, validated_data):
        post = Posts.objects.create(
            user = self.context.get('user'),
            caption = validated_data['caption'],
            image = validated_data['image'],
           
            )
        print(f"Username {post.user} ")
        return post

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post','comment_text']
    
    def create(self,validated_data):
        # comment = Comment.objects.create(
        #     user = self.context.get('user'),
        #     post = validated_data['post'],
        #     comment_text = validated_data['comment_text'], 
        # )
        user = self.context.get('user')
        post = validated_data['post']
        comment_text = validated_data['comment_text']
        print(f"Printing validate data {validated_data}")
        parent = self.context.get('parent')

        if parent == "":
            comment = Comment.objects.create(
                user = user,
                post=post,
                comment_text=comment_text
            )
        else:
            replyoOf = Comment.objects.get(pk=parent)
            comment = Comment.objects.create(
                user = user,
                post=post,
                comment_text=comment_text,
                parent = replyoOf
            )

        print(f"post {comment.post} posted by {comment.user}")
        return comment

class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
