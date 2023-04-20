from django.db import models
from django.contrib.auth.models import User







class Category(models.Model):
    name = models.CharField(max_length=255)
    things_number = models.IntegerField(default=0, verbose_name='Things number')

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Things(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Things'
        indexes = [models.Index(fields=['name'], name='things_names_idx')]
        
    def __str__(self):
        return self.name