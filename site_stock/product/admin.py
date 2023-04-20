from django.contrib import admin

from .models import Category, Things


admin.site.register(Category)
admin.site.register(Things)