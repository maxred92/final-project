from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Class for extending the admin panel of the model Profile """

    list_display = ["user", "date_of_birth", "photo"]
