from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=13, unique=True)
    is_varified = models.BooleanField(default=False)
    otp = models.CharField(max_length=5, null=True, blank=True)
    password = models.CharField(max_length=100)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


