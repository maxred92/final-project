from django.contrib import admin
from django.db.models import Avg
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Category, Things

@admin.register(Things)
class ThingsAdmin(admin.ModelAdmin):
    """ A class that extends the capabilities of the admin panel of the model Things """
    
    date_hierarchy = "created_at"
    sortable_by = ("name", "created_at", "full_price", "created_by")
    list_filter = ("category",)
    search_fields = ("category_name", "name")
    list_display = ("name", "created_at", "full_price")

    # Custom price field with $ sign
    @admin.display(description="price")
    def full_price(self, obj):
        return f"{obj.price} $"

class ThingsInCategory(admin.StackedInline):
    model = Things

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Class for displaying things in the admin panel of the model Categories """
    
    list_display = ("name", "show_average")
    inlines = (ThingsInCategory,)

    @admin.display(description="things")
    def view_things(self, obj):
        count = obj.things_set.count()
        url = (
            reverse("admin:product_things_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Things</a>', url, count)

    @admin.display(description="avg_price")
    def show_average(self, obj):
        """ A function that shows the average price of items in each category """
        
        result = Things.objects.filter(category=obj).aggregate(Avg("price"))
        return result["price__avg"]
