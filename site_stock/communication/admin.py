from django.contrib import admin

from .models import Communication, Message

admin.site.register(Communication)
admin.site.register(Message)
