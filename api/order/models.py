from django.db import models
from django.forms import ValidationError
from api.account.models import User
from api.product.models import Product
from api.utils.preferences import ORDER_STATUS

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_order")
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10,choices=ORDER_STATUS,default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.email} - {self.product.product_name}"
    
    def save(self, *args, **kwargs):
        if self.quantity > self.product.available_units:
            raise ValidationError("Quantity cannot be greater than available units.")
        
        self.product.available_units = self.product.available_units - self.quantity
        self.product.save()
        
        super().save(*args, **kwargs)