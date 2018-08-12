from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Postings(TimeStampedModel):
    user_id = models.ForeignKey("users_api.Model", on_delete=models.CASCADE)