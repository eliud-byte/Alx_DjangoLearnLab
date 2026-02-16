from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Symmerical=False allows "Following" logic (I can follow you withour you following me)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username
    
class Register(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
