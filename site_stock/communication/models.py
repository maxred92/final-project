from django.contrib.auth.models import User
from django.db import models

from product.models import Things


class Communication(models.Model):
    """ Class for creating a model for starting communication with a user """
    
    things = models.ForeignKey(
        Things, related_name="communication", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="communication")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-modified_at",)

    def __str__(self):
        return f"Communication by {self.members} on {self.things}"


class Message(models.Model):
    """ Class for creating a model for sending a message to the user """

    communication = models.ForeignKey(
        Communication, related_name="messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Comment by {self.created_by} on {self.communication}"
