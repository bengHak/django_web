from django.db import models
from users_api.models import User

# Create your models here.

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Postings(TimeStampedModel):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    like = models.PositiveIntegerField()

    class Meta:
        ordering = ['-created_at']

class Comment(TimeStampedModel):
    
    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message