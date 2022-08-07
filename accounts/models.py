from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager
from uuid import uuid4

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    token = models.CharField(max_length=256,default=uuid4())
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
