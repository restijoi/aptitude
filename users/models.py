from django.db import models
from django.conf import settings

from users.utils import user_media_path

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """User Manager"""
    def create_user(self, email, password=None, **kwargs):
        """create regular user"""
        if not email:
            raise ValueError("Email is required.")

        user = self.model(email= email, **kwargs)
        user.is_active = True
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password=None, **kwargs):
        """ create a super user"""
        user = self.create_user(email, password, **kwargs)
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """user data"""

    email = models.EmailField(max_length=500, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    handle = models.CharField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to=user_media_path, null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("first_name", "last_name")

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".title()

class UserTag(models.Model):
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
