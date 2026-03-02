from django.contrib import admin
from marketplace.models import Location, Customer, Seller, Product, Warehouse


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'lat', 'lng']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_code', 'name', 'phone', 'city', 'state', 'is_active']
    search_fields = ['customer_code', 'name', 'phone']
    list_filter = ['is_active', 'state']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'city', 'state', 'is_active']
    search_fields = ['name', 'email']
    list_filter = ['is_active', 'state']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'selling_price', 'weight_kg', 'seller', 'is_available', 'stock_quantity']
    search_fields = ['name', 'sku']
    list_filter = ['is_available', 'category', 'seller']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'city', 'state', 'is_active', 'capacity_kg']
    search_fields = ['code', 'name']
    list_filter = ['is_active', 'state']
