from django.contrib.auth.models import User
from django.db import models

from product.models import Things

class Communication(models.Model):
    things = models.ForeignKey(Things, related_name='communication', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='communication')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modified_at',)

class Message(models.Model):
    communication = models.ForeignKey(Communication, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)