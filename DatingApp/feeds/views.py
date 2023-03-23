from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework import generics,permissions,viewsets
from django.http import HttpResponse, JsonResponse
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from feeds.serializers import *
from user.error import CustomizeRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Posts,Comment,Like
from user_profile.models import Profile
from rest_framework.decorators import api_view


# def Home(request):
#     if request.method == "GET":
#         print("In Feed section buddy")
#         return HttpResponse("Hello World")
    
#     if request.method == "POST":
#         print("In Feed section buddy")
#         return HttpResponse("POST REQUEST")



class PostFeed(APIView):
    render_classes =[CustomizeRenderer]
    permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def post(self,request):
        serializer = PostSerializer(data =request.data,context ={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Feed Posted Successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostComment(APIView):
    render_classes =[CustomizeRenderer]
    permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def post(self,request):
        serializer = PostSerializer(data = request.data, context ={'user':request.user,'post':request.post})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Comented Posted Successfully'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetFeed(APIView):
    def get(self,request,key):

        if int(key) == 0:
            posts = Posts.objects.all()
            print(f"posts are {posts}")
            serializer = GetPostSerializers(posts , many=True)
            return Response(serializer.data)
   
        elif int(1) == 1:
            return Response({"data":"feed of what you are following"})
        
@api_view(['GET','POST'])
def newsfeeds(request):
    own_profile = Profile.objects.get(user = request.user)
    users = [user for user in own_profile.following.all()]
    posts = []
    for u in users:
        p = Profile.objects.get(user = u)
        p_posts = p.posts.all()
        posts.extend(p_posts)
    my_post = own_profile.profiles_posts()
    posts.extend(my_post)
    print(f"Showing the {own_profile} posts ={posts}")
    serializers = NewsfeedSerializer(posts, many=True)
   
    print(f"Printing the serialize +++=={serializers.data}")
    return Response(serializers.data)
