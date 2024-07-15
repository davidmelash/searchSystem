from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import validate_email
from django.db.models import QuerySet

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField()
    phone_number = models.IntegerField(unique=True)
    data_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    identification_number = models.IntegerField(unique=True, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)


class Contact(models.Model):
    full_name = models.CharField()
    phone_number = models.IntegerField(unique=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(blank=True, max_length=20)
    middle_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email])
    password = models.CharField(max_length=128)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = BaseUserManager()

    def __str__(self):
        """
        Magic method is redefined to show information about CustomUser.
        """
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_all() -> QuerySet:
        """
        returns data for json request with QuerySet of all users
        """
        all_users = CustomUser.objects.all()
        return all_users
