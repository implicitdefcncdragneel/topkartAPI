from django.contrib import admin
from api.product.models import LightningDeal, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(LightningDeal)