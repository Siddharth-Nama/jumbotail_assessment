from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from marketplace.models import Location, Customer, Seller, Product, Warehouse

class APITests(APITestCase):
    def setUp(self):
        self.loc_s = Location.objects.create(lat=12.9716, lng=77.5946)
        self.loc_w = Location.objects.create(lat=12.9999, lng=77.6000)
        self.loc_c = Location.objects.create(lat=19.0760, lng=72.8777)

        self.seller = Seller.objects.create(
            name='Test Seller', email='seller@test.com', phone='123', location=self.loc_s
        )
        self.customer = Customer.objects.create(
            customer_code='C-1', name='Test Customer', phone='123', location=self.loc_c
        )
        self.product = Product.objects.create(
            name='Test Product', sku='SKU-1', selling_price=10.0,
            weight_kg=5.0, length_cm=10, width_cm=10, height_cm=10,
            seller=self.seller
        )
        self.warehouse = Warehouse.objects.create(
            name='Test Warehouse', code='W-1', location=self.loc_w, capacity_kg=1000
        )

    def test_nearest_warehouse_success(self):
        url = reverse('nearest-warehouse')
        response = self.client.get(url, {'sellerId': self.seller.id, 'productId': self.product.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['warehouseId'], self.warehouse.id)

    def test_nearest_warehouse_missing_params(self):
        url = reverse('nearest-warehouse')
        response = self.client.get(url, {'sellerId': self.seller.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_shipping_charge_success(self):
        url = reverse('shipping-charge')
        response = self.client.get(url, {
            'warehouseId': self.warehouse.id,
            'customerId': self.customer.id,
            'deliverySpeed': 'express'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['breakdown']['deliverySpeed'], 'express')
        self.assertIn('shippingCharge', response.data)

    def test_shipping_charge_missing_params(self):
        url = reverse('shipping-charge')
        response = self.client.get(url, {'warehouseId': self.warehouse.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_shipping_charge_calculate_post(self):
        url = reverse('shipping-charge-calculate')
        data = {
            'sellerId': self.seller.id,
            'customerId': self.customer.id,
            'deliverySpeed': 'standard'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nearestWarehouse']['warehouseId'], self.warehouse.id)
        self.assertEqual(response.data['breakdown']['deliverySpeed'], 'standard')

    def test_shipping_charge_calculate_invalid_speed(self):
        url = reverse('shipping-charge-calculate')
        data = {
            'sellerId': self.seller.id,
            'customerId': self.customer.id,
            'deliverySpeed': 'invalid_speed'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
