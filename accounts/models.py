from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid4)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(default="",upload_to="Images/profile_pictures")

    def __str__(self) -> str:
        return self.username

