from django.db import models
from users_api.models import Users

# Create your models here.

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

#생성시각, 수정시각 추가
class Postings(TimeStampedModel):
    name = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        ordering = ['-created_at']


#생성시각, 수정시각 추가
class Comment(TimeStampedModel):
    
    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.message