from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.conf import settings

from marketplace.models import Seller, Product, Warehouse, Customer
from marketplace.services.warehouse_service import find_nearest_warehouse
from marketplace.services.charge_service import calculate_shipping_charge
from marketplace.serializers import WarehouseSerializer
from marketplace.exceptions import MarketplaceException


class NearestWarehouseView(APIView):
    def get(self, request):
        seller_id = request.query_params.get('sellerId')
        product_id = request.query_params.get('productId')

        if not seller_id or not product_id:
            return Response(
                {'error': True, 'message': 'sellerId and productId are required query parameters.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            seller_id = int(seller_id)
            product_id = int(product_id)
        except ValueError:
            return Response(
                {'error': True, 'message': 'sellerId and productId must be valid integers.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cache_key = f'nearest_wh_{seller_id}_{product_id}'
        cached = cache.get(cache_key)
        if cached:
            return Response(cached, status=status.HTTP_200_OK)

        try:
            seller = Seller.objects.get(pk=seller_id, is_active=True)
        except Seller.DoesNotExist:
            return Response(
                {'error': True, 'message': f'Seller with id {seller_id} not found or inactive.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            product = Product.objects.get(pk=product_id, seller=seller, is_available=True)
        except Product.DoesNotExist:
            return Response(
                {'error': True, 'message': f'Product with id {product_id} not found for this seller.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            warehouse = find_nearest_warehouse(seller.location)
        except MarketplaceException as e:
            return Response(
                {'error': True, 'message': e.message},
                status=status.HTTP_404_NOT_FOUND,
            )

        response_data = {
            'warehouseId': warehouse.id,
            'warehouseName': warehouse.name,
            'warehouseCode': warehouse.code,
            'warehouseLocation': {
                'lat': warehouse.location.lat,
                'long': warehouse.location.lng,
            },
        }

        cache.set(cache_key, response_data, settings.SHIPPING_CACHE_TIMEOUT)
        return Response(response_data, status=status.HTTP_200_OK)


class ShippingChargeView(APIView):
    def get(self, request):
        warehouse_id = request.query_params.get('warehouseId')
        customer_id = request.query_params.get('customerId')
        delivery_speed = request.query_params.get('deliverySpeed', 'standard').lower()

        if not warehouse_id or not customer_id:
            return Response(
                {'error': True, 'message': 'warehouseId and customerId are required query parameters.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if delivery_speed not in ('standard', 'express'):
            return Response(
                {'error': True, 'message': 'deliverySpeed must be either "standard" or "express".'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            warehouse_id = int(warehouse_id)
            customer_id = int(customer_id)
        except ValueError:
            return Response(
                {'error': True, 'message': 'warehouseId and customerId must be valid integers.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cache_key = f'shipping_{warehouse_id}_{customer_id}_{delivery_speed}'
        cached = cache.get(cache_key)
        if cached:
            return Response(cached, status=status.HTTP_200_OK)

        try:
            warehouse = Warehouse.objects.select_related('location').get(pk=warehouse_id, is_active=True)
        except Warehouse.DoesNotExist:
            return Response(
                {'error': True, 'message': f'Warehouse with id {warehouse_id} not found or inactive.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            customer = Customer.objects.select_related('location').get(pk=customer_id, is_active=True)
        except Customer.DoesNotExist:
            return Response(
                {'error': True, 'message': f'Customer with id {customer_id} not found or inactive.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            result = calculate_shipping_charge(warehouse.location, customer.location, delivery_speed)
        except MarketplaceException as e:
            return Response(
                {'error': True, 'message': e.message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response_data = {
            'shippingCharge': result['total_charge'],
            'breakdown': {
                'distanceKm': result['distance_km'],
                'transportMode': result['transport_mode'],
                'baseCharge': result['base_charge'],
                'expressCharge': result['express_charge'],
                'standardCourierCharge': result['standard_courier_charge'],
                'deliverySpeed': delivery_speed,
            },
        }

        cache.set(cache_key, response_data, settings.SHIPPING_CACHE_TIMEOUT)
        return Response(response_data, status=status.HTTP_200_OK)


class ShippingChargeCalculateView(APIView):
    def post(self, request):
        seller_id = request.data.get('sellerId')
        customer_id = request.data.get('customerId')
        delivery_speed = str(request.data.get('deliverySpeed', 'standard')).lower()
        product_id = request.data.get('productId')

        if not seller_id or not customer_id:
            return Response(
                {'error': True, 'message': 'sellerId and customerId are required fields.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if delivery_speed not in ('standard', 'express'):
            return Response(
                {'error': True, 'message': 'deliverySpeed must be either "standard" or "express".'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            seller_id = int(seller_id)
            customer_id = int(customer_id)
        except (ValueError, TypeError):
            return Response(
                {'error': True, 'message': 'sellerId and customerId must be valid integers.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            seller = Seller.objects.select_related('location').get(pk=seller_id, is_active=True)
        except Seller.DoesNotExist:
            return Response(
                {'error': True, 'message': f'Seller with id {seller_id} not found or inactive.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            customer = Customer.objects.select_related('location').get(pk=customer_id, is_active=True)
        except Customer.DoesNotExist:
            return Response(
                {'error': True, 'message': f'Customer with id {customer_id} not found or inactive.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            warehouse = find_nearest_warehouse(seller.location)
        except MarketplaceException as e:
            return Response(
                {'error': True, 'message': e.message},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            result = calculate_shipping_charge(warehouse.location, customer.location, delivery_speed)
        except MarketplaceException as e:
            return Response(
                {'error': True, 'message': e.message},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response_data = {
            'shippingCharge': result['total_charge'],
            'nearestWarehouse': {
                'warehouseId': warehouse.id,
                'warehouseName': warehouse.name,
                'warehouseCode': warehouse.code,
                'warehouseLocation': {
                    'lat': warehouse.location.lat,
                    'long': warehouse.location.lng,
                },
            },
            'breakdown': {
                'distanceKm': result['distance_km'],
                'transportMode': result['transport_mode'],
                'baseCharge': result['base_charge'],
                'expressCharge': result['express_charge'],
                'standardCourierCharge': result['standard_courier_charge'],
                'deliverySpeed': delivery_speed,
            },
        }

        return Response(response_data, status=status.HTTP_200_OK)
