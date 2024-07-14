from django.contrib import admin

# Register your models here.
from django.contrib import admin

from main.models import Profile, Contact

admin.site.register(Profile)
admin.site.register(Contact)