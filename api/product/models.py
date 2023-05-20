from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    actual_price = models.DecimalField(max_digits=10, decimal_places=3)
    final_price = models.DecimalField(max_digits=10, decimal_places=3)
    total_units = models.PositiveIntegerField()
    available_units = models.PositiveIntegerField()
    is_lightning_deal = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name
    
class LightningDeal(models.Model):
    '''
    Lightning deals are products that are available at a discounted price on the website for a brief amount of time.
    '''
    product = models.OneToOneField(Product,on_delete=models.CASCADE, related_name='lightning_deal')
    expiry_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.product_name