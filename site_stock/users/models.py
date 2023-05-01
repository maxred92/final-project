from django.db import models
from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Phone number') 
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



