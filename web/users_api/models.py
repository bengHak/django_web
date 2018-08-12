from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Users(AbstractBaseUser):
    email = models.EmailField(null=False, max_length=254)
    username = models.CharField(null=False, max_length=20) #본명
    major = models.CharField(null=False, max_length=50)
    school_id = models.IntegerField(null=False)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)
    github = models.URLField(null=True)

    def __str__(self):
        return self.username