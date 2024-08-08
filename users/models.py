from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from datetime import datetime
 
class UserAccount(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(_("First Name"),max_length=255)
    last_name=models.CharField(_("Last Name"),max_length=255)
    email=models.EmailField(_("Email Address"),unique=True,max_length=255)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=datetime.now)
    
    objects=CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["last_name", "first_name"]
    
    class Meta:
        verbose_name =_("Users")
        verbose_name_plural =_("Users")
    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
