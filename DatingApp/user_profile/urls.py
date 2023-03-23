from django.urls import path 
from .views import GetProfiles,GetDetailView,follow_unfollow_profie,GetFollowers,GetFollowers_name

urlpatterns =[
 
    path('get-profile',GetProfiles.as_view(),name='get-profiles'),
    path('detail/<pk>',GetDetailView.as_view(),name='get-profile-detail'),
    path('follow', follow_unfollow_profie,name='follow-unfollow-view'),
    path('followers',GetFollowers.as_view(),name = 'get-followers'),
    path('followers',GetFollowers_name.as_view(),name = 'get-followers-names'),


]