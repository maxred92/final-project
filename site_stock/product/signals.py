from django.db.models import signals
from django.dispatch import receiver
from product.models import Category, Things


@receiver(signals.post_save, sender=Things)
def things_number_save(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        category.things_number += 1
        category.save()



@receiver(signals.post_delete, sender=Things)
def things_number_delete(sender, instance, **kwargs):
        category = instance.category
        category.things_number -= 1
        category.save()