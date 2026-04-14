from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_image', 'price', 
                 'available_qty', 'general_info', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        