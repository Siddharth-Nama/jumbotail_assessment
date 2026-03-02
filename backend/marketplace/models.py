from django.db import models
from django.core.validators import MinValueValidator


class Location(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = 'Location'

    def __str__(self):
        return f"({self.lat}, {self.lng})"


class Customer(models.Model):
    customer_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='customer')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Customer'
        ordering = ['name']

    def __str__(self):
        return f"{self.customer_code} - {self.name}"


class Seller(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    gstin = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='seller')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Seller'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    weight_kg = models.FloatField(validators=[MinValueValidator(0.001)])
    length_cm = models.FloatField(validators=[MinValueValidator(0.1)])
    width_cm = models.FloatField(validators=[MinValueValidator(0.1)])
    height_cm = models.FloatField(validators=[MinValueValidator(0.1)])
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    is_available = models.BooleanField(default=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} by {self.seller.name}"

    @property
    def volume_cm3(self):
        return self.length_cm * self.width_cm * self.height_cm


class Warehouse(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='warehouse')
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    capacity_kg = models.FloatField(default=10000.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Warehouse'
        ordering = ['name']

    def __str__(self):
        return f"{self.code} - {self.name}"
