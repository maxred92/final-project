from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from PIL import Image


class Profile(models.Model):
    """ Class for creating the Profile model """

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(max_length=10, blank=True, null=True)
    phone_number = PhoneNumberField(null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)

    class Meta:
        ordering = ("user",)
        verbose_name_plural = "Profile"

    def __str__(self):
        return "Profile for user {}".format(self.user.username)
    
    def save(self):
        """ Feature to shrink profile picture on upload """

        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
