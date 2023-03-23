from django.db import models
from user.models import User
from user_profile.models import Profile

# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="posts")
    caption = models.TextField(blank=True)
    image = models.ImageField(blank=True,verbose_name="Post Image",upload_to='images/')
   

    # timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.TextField()
    post = models.ForeignKey(Posts,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null = True) 
    
    # timestamp = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE ,blank=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    # timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

class Unlike(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,blank=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # count = models.IntegerField()

    





    

