from django.db.models import signals
from django.dispatch import receiver

from product.models import Things

@receiver(signals.post_save, sender=Things)
def things_number_save(sender, instance, created, **kwargs):
    """ Function to increase the number of items in a category """
    
    if created:
        category = instance.category
        category.things_number += 1
        category.save()


@receiver(signals.post_delete, sender=Things)
def things_number_delete(sender, instance, **kwargs):
    """ Function to reduce the number of items in a category """
    
    category = instance.category
    category.things_number -= 1
    category.save()
