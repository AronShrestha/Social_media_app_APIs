from django.db import models
from user.models import User
from userProfile.models import Profile

# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    caption = models.TextField(blank=True)
    image = models.ImageField(blank=True, verbose_name="Post Image",upload_to='images/')
   

    def get_comments(self):
        return self.comments.all()

    def __str__(self) -> str:
        return str(self.caption)
    
    def get_likes(self):
        return self.likes.all()
    # timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    post = models.ForeignKey(Posts,on_delete=models.CASCADE,related_name = "comments")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True,blank=True) 
    
    # timestamp = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts,on_delete=models.CASCADE ,related_name="likes")
 
    # timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

class Unlike(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,blank=True)
  
    timestamp = models.DateTimeField(auto_now_add=True)
    # count = models.IntegerField()

    





    

