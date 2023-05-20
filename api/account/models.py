import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from api.utils.preferences import USER_ROLE

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide a valid email address")

    def create_user(self,email,password,**extra_fields):

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Base User Account: An email address is required")

        user = self.model(email=email,**extra_fields)

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusers must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusers must have is_superuser=True")

        if not password:
            raise ValueError("Superusers must have a password")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Admin Account: An email address is required")

        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name="email address", db_index=True, unique=True)
    user_role = models.CharField(choices=USER_ROLE,max_length=10,default="Unknown",null=False,blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.email