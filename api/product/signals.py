from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from api.product.models import LightningDeal, Product

@receiver(post_save, sender=Product)
def create_or_update_lightning_deal(sender, instance, created, **kwargs):
    if instance.is_lightning_deal:
        start_time = timezone.now()
        end_time = start_time + timezone.timedelta(hours=12) # The expiry time of a lightning deal is not more than 12 hours. 
        lightning_deal, _ = LightningDeal.objects.get_or_create(product=instance)
        lightning_deal.expiry_time = end_time
        lightning_deal.save()
    else:
        try:
            instance.lightning_deal.delete()
        except LightningDeal.DoesNotExist:
            pass