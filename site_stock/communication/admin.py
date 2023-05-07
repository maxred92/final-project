from django.contrib import admin

from .models import Communication, Message


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = ("things", "created_at")
    list_filter = ("created_at", "modified_at")
    search_fields = ("things", "members")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("content", "communication", "created_by")
    list_filter = ("created_by", "communication", "created_at")
    search_fields = ("created_by", "created_at")
