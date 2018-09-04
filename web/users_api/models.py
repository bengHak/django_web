from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError

class User(AbstractBaseUser):
    username = models.CharField(null=False, blank=False, max_length=20)
    major = models.CharField(blank=True, null=True, max_length=50)
    school_id = models.IntegerField(unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=254, blank=False, null=False)
    phone = models.CharField(default="phone_number",blank=False, null=True, max_length=50)
    career = models.TextField(null=True, blank=True)
    mentor_bool = models.BooleanField(default=False)
    github = models.URLField(null=True, blank=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)

    USERNAME_FIELD = 'school_id'

    class Meta:
        ordering = ["-id"]

    def __str__(self):  
        return self.username