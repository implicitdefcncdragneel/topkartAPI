from django.utils import timezone

from api.product.models import LightningDeal, Product

def refresh_lightning_deals():
    start_time = timezone.now()
    end_time = start_time + timezone.timedelta(hours=12)

    # Delete existing lightning deals
    LightningDeal.objects.all().delete()

    # Create new lightning deals for eligible products
    products = Product.objects.filter(is_lightning_deal=True)
    for product in products:
        LightningDeal.objects.create(product=product, expiry_time=end_time)