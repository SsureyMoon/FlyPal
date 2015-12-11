from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
from django.utils import timezone


class User(AbstractUser):

    # username   = models.CharField()
    # last_login = models.DateTimeField(blank=True)
    # is_active  = models.BooleanField()
    profile_img_url = models.TextField(null=True)
    gender = models.CharField(max_length=128, null=True)
    location = models.CharField(max_length=128, null=True)
    facebook_id = models.CharField(max_length=128, null=True)
    twitter_id = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return self.username
