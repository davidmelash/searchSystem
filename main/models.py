from django.db import models

# Create your models here.

class Profile(models.Model):
    full_name = models.CharField()
    phone_number = models.IntegerField()
    data_of_birth = models.DateField()
    address = models.TextField()
    identification_number = models.IntegerField()
