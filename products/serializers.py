from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
        
        
    def validate_name(self, value):
        """Check if the product name is unique excluding the current product instance."""
        request = self.context.get('request')
        print(request)
        if request and request.method == 'PUT':  # For update requests
            product_id = request.parser_context['kwargs'].get('pk')
            if Product.objects.filter(name=value).exclude(id=product_id).exists():
                raise serializers.ValidationError("A product with this name already exists.")
        elif Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("A product with this name already exists.")
        return value

