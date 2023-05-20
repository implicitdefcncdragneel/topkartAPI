from rest_framework import serializers

from api.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.DecimalField(required=False, max_digits=10, decimal_places=3)
    available_units = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'actual_price', 'final_price', 'total_units', 'available_units', 'is_lightning_deal')

    def validate(self, attrs):
        if 'available_units' in attrs and 'total_units' in attrs:
            available_units = attrs['available_units']
            total_units = attrs['total_units']
            if available_units is not None and total_units is not None and available_units > total_units:
                raise serializers.ValidationError("Available units cannot be greater than total units.")

        if 'final_price' in attrs and 'actual_price' in attrs:
            final_price = attrs['final_price']
            actual_price = attrs['actual_price']
            if final_price is not None and actual_price is not None and final_price > actual_price:
                raise serializers.ValidationError("Final price cannot be greater than actual price.")

        return attrs

    def create(self, validated_data):
        if 'final_price' not in validated_data:
            validated_data['final_price'] = validated_data['actual_price']
        if 'available_units' not in validated_data:
            validated_data['available_units'] = validated_data['total_units']
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        instance.product_name = validated_data.get('product_name', instance.product_name)
        actual_price = validated_data.get('actual_price', instance.actual_price)
        final_price = validated_data.get('final_price', instance.final_price)
        total_units = validated_data.get('total_units', instance.total_units)
        available_units = validated_data.get('available_units', instance.available_units)

        if available_units <= total_units:
            instance.available_units = available_units
        else:
            raise serializers.ValidationError("Available units cannot be greater than total units.")

        if final_price <= actual_price:
            instance.final_price = final_price
        else:
            raise serializers.ValidationError("Final price cannot be greater than actual price.")

        instance.is_lightning_deal = validated_data.get('is_lightning_deal', instance.is_lightning_deal)
        instance.save()
        return instance
