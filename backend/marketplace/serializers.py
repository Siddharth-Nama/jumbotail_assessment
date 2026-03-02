from rest_framework import serializers
from marketplace.models import Location, Customer, Seller, Product, Warehouse


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'lat', 'lng']


class CustomerSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = [
            'id', 'customer_code', 'name', 'phone', 'email',
            'address', 'city', 'state', 'pincode', 'location',
            'is_active', 'created_at',
        ]


class SellerSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = [
            'id', 'name', 'email', 'phone', 'gstin',
            'address', 'city', 'state', 'pincode', 'location',
            'is_active', 'created_at',
        ]


class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)
    volume_cm3 = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'sku', 'selling_price',
            'weight_kg', 'length_cm', 'width_cm', 'height_cm',
            'volume_cm3', 'category', 'is_available', 'stock_quantity',
            'seller', 'created_at',
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Warehouse
        fields = [
            'id', 'name', 'code', 'location',
            'address', 'city', 'state', 'pincode',
            'contact_phone', 'is_active', 'capacity_kg', 'created_at',
        ]
