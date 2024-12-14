from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from oauth2client.contrib.django_util.models import CredentialsField

# Create your models here.

class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    credential = CredentialsField()
    task = models.CharField(max_length=80, blank=True, null =True)
    updated_time = models.DateTimeField(auto_now=True)

class CredentialsAdmin(admin.ModelAdmin):
    pass