from django.db import models
from user.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='following',blank=True)
    bio = models.TextField(default="I am ")
    # timestamp = models.DateTimeField(auto_now_add=True)

    def profiles_posts(self):
        return self.posts.all()

    def __str__(self):
        return str(self.user.username)
    
    # class Meta :
    #     prdering = ('-created',)