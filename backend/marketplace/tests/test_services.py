from django.test import TestCase
from marketplace.models import Location, Warehouse, Seller, Customer
from marketplace.services.distance_service import haversine_distance
from marketplace.services.warehouse_service import find_nearest_warehouse
from marketplace.services.shipping_service import get_transport_strategy, AeroplaneStrategy, TruckStrategy, MiniVanStrategy
from marketplace.services.charge_service import calculate_shipping_charge
from marketplace.exceptions import MarketplaceException


class DistanceServiceTest(TestCase):
    def test_haversine_distance(self):
        lat1, lng1 = 12.9716, 77.5946
        lat2, lng2 = 19.0760, 72.8777
        dist = haversine_distance(lat1, lng1, lat2, lng2)
        self.assertAlmostEqual(dist, 845.0, places=0)


class WarehouseServiceTest(TestCase):
    def setUp(self):
        self.loc_s1 = Location.objects.create(lat=12.9716, lng=77.5946)
        self.loc_w1 = Location.objects.create(lat=12.9999, lng=77.6000)
        self.loc_w2 = Location.objects.create(lat=19.0760, lng=72.8777)

        self.w1 = Warehouse.objects.create(name='W1', code='W1', location=self.loc_w1, is_active=True)
        self.w2 = Warehouse.objects.create(name='W2', code='W2', location=self.loc_w2, is_active=True)

    def test_find_nearest_warehouse(self):
        nearest = find_nearest_warehouse(self.loc_s1)
        self.assertEqual(nearest.id, self.w1.id)

    def test_no_active_warehouse(self):
        self.w1.is_active = False
        self.w1.save()
        self.w2.is_active = False
        self.w2.save()

        with self.assertRaises(MarketplaceException):
            find_nearest_warehouse(self.loc_s1)


class ShippingServiceTest(TestCase):
    def test_transport_strategy_selection(self):
        self.assertIsInstance(get_transport_strategy(600.0), AeroplaneStrategy)
        self.assertIsInstance(get_transport_strategy(250.0), TruckStrategy)
        self.assertIsInstance(get_transport_strategy(50.0), MiniVanStrategy)


class ChargeServiceTest(TestCase):
    def setUp(self):
        self.loc_w = Location.objects.create(lat=12.9716, lng=77.5946)
        self.loc_c_far = Location.objects.create(lat=19.0760, lng=72.8777)
        self.loc_c_near = Location.objects.create(lat=12.9999, lng=77.6000)

    def test_calculate_shipping_standard_far(self):
        res = calculate_shipping_charge(self.loc_w, self.loc_c_far, 'standard', 5.0)
        self.assertEqual(res['transport_mode'], 'Aeroplane')
        self.assertEqual(res['delivery_speed'], 'standard')
        self.assertEqual(res['express_charge'], 0.0)

    def test_calculate_shipping_express_near(self):
        res = calculate_shipping_charge(self.loc_w, self.loc_c_near, 'express', 10.0)
        self.assertEqual(res['transport_mode'], 'MiniVan')
        self.assertEqual(res['delivery_speed'], 'express')
        self.assertEqual(res['express_charge'], 12.0)
