from django.shortcuts import render
from .serializers import GetProfileSerializer,GetDetailProfileSerializer,Follow_Unfollow_Serializer,FollowerSerializer,FollowerSerializer_name
from user.error import CustomizeRenderer
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.

class GetProfiles(APIView):
    render_classes = [CustomizeRenderer]
    # permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def get(self,request):
        profiles = Profile.objects.all().exclude(user=self.request.user)
        serializer = GetProfileSerializer(profiles,many=True)
        print(serializer)
    
        return Response(serializer.data)

class GetDetailView(APIView):
    render_classes = [CustomizeRenderer]
    # permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def get(self,request,pk):
        print("In profile detail view")
        try:
            profile = Profile.objects.get(pk=pk)
            print(f"posts {profile.profiles_posts}")
            
        except Profile.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = GetDetailProfileSerializer(profile)
        print("User PK "+serializer.data['user']['username'])
        return Response(serializer.data)
    

class GetFollowers(APIView):
    render_classes = [CustomizeRenderer]
    # permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def get(self,request):
        my_profile = Profile.objects.get(user = request.user)
        print(f"Welcome {my_profile.user.username}")
        
        serializers =  FollowerSerializer(my_profile)
        return Response(serializers.data)

class GetFollowers_name(APIView):
    render_classes = [CustomizeRenderer]
    # permission_classes = [IsAuthenticated] #user resetting password when he is already logged in
    def get(self,request):
        my_profile = Profile.objects.get(user = request.user)
        print(f"Welcome {my_profile.user.username}")
        followers = {'user':[frn.username for frn in my_profile.following.all()]}
        print(f"Followers {followers}")
        serializers =  FollowerSerializer_name(followers)
        print(f"Serializer {serializers.data}")
     
  
        return Response(serializers.data)
@api_view(['GET','POST'])
def follow_unfollow_profie(request):
    if request.method == "POST":
        serializer =Follow_Unfollow_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        my_profile = Profile.objects.get(user=request.user)
        pk = serializer.data['id']
        current_profile = Profile.objects.get(pk=pk)
        if current_profile.user in my_profile.following.all():
            my_profile.following.remove(current_profile.user)
        else:
            my_profile.following.add(current_profile.user)
        
        return HttpResponse(f"Followed {current_profile.user.username}")
    return HttpResponse("Not ")


