from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Postings(TimeStampedModel):
    user_id = models.ForeignKey(users_api.Model, on_delete=models.CASCADE)
    name = models.ForeignKeyField('TargetModel', related_name='', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    class Meta:
        ordering = ['-created_at']


class Comment(TimeStampedModel):
    
    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(users_api.Model, null=True)
    image = models.ForeignKey(Image, null=True, related_name='comments')

    def __str__(self):
        return self.message