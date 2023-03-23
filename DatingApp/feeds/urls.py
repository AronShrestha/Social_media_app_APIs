from django.urls import path 
from feeds import views
from .views import *




urlpatterns =[
    # path('',views.Home),
    path('get-post/<key>',GetFeed.as_view(),name='get-post'),
    path('post',PostFeed.as_view(),name='post-feed'),
    path('newsfeeds', newsfeeds, name="newsfeed"),
    path('comment',PostComment.as_view(),name = 'post-comment')
    # path('',views.Home),
    # path('register',views.RegisterUser),
    # path('login',views.LoginIn.as_view(),name='login'),

]