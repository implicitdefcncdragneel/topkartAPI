from rest_framework import serializers

from api.order.models import Order
from api.product.models import LightningDeal, Product

class LightningDealProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product_name', 'actual_price', 'final_price', 'available_units')

class LightningDealSerializer(serializers.ModelSerializer):
    product = LightningDealProductSerializer()

    class Meta:
        model = LightningDeal
        fields = ('id', 'product', 'expiry_time')
        read_only_fields = ('id',)

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['quantity',]

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        product_id = self.context.get('product_id')
        product = Product.objects.get(pk=product_id)
        quantity = validated_data['quantity']

        if quantity > product.available_units:
            raise serializers.ValidationError("Quantity cannot be greater than available units.")
        product.available_units = product.available_units - quantity
        product.save()
        order = Order.objects.create(user=user, product=product, quantity=quantity)
        return order
    
class OrderStatusSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id','product','product_name','quantity', 'status', 'created_at')

    def get_product_name(self, obj):
        product_name = obj.product.product_name
        return product_name

class OrderApprovalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'status')