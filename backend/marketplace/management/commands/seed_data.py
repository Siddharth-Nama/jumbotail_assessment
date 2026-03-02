from django.core.management.base import BaseCommand
from marketplace.models import Location, Customer, Seller, Product, Warehouse


class Command(BaseCommand):
    help = 'Seed the database with initial marketplace data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        Location.objects.all().delete()

        loc_cust1 = Location.objects.create(lat=11.232, lng=23.445495)
        loc_cust2 = Location.objects.create(lat=17.232, lng=33.445495)
        loc_seller1 = Location.objects.create(lat=12.9716, lng=77.5946)
        loc_seller2 = Location.objects.create(lat=19.0760, lng=72.8777)
        loc_seller3 = Location.objects.create(lat=18.5204, lng=73.8567)
        loc_wh1 = Location.objects.create(lat=12.99999, lng=37.923273)
        loc_wh2 = Location.objects.create(lat=11.99999, lng=27.923273)

        Customer.objects.create(
            customer_code='CUST-123', name='Shree Kirana Store', phone='9847000001',
            email='shree.kirana@example.com', address='MG Road, Block A',
            city='Hyderabad', state='Telangana', pincode='500001', location=loc_cust1
        )
        Customer.objects.create(
            customer_code='CUST-124', name='Andheri Mini Mart', phone='9101000002',
            email='andheri.minimart@example.com', address='Andheri West, Shop 12',
            city='Mumbai', state='Maharashtra', pincode='400053', location=loc_cust2
        )

        seller1 = Seller.objects.create(
            name='Nestle Seller', email='nestle.seller@example.com', phone='9000000001',
            gstin='22AAAAA0000A1Z5', address='Nestle India, Industrial Area',
            city='Bangalore', state='Karnataka', pincode='560001', location=loc_seller1
        )
        seller2 = Seller.objects.create(
            name='Rice Seller', email='rice.seller@example.com', phone='9000000002',
            gstin='29BBBBB0000B1Z4', address='Rice Mills, APMC Yard',
            city='Mumbai', state='Maharashtra', pincode='400001', location=loc_seller2
        )
        seller3 = Seller.objects.create(
            name='Sugar Seller', email='sugar.seller@example.com', phone='9000000003',
            gstin='27CCCCC0000C1Z3', address='Sugar Factory Road',
            city='Pune', state='Maharashtra', pincode='411001', location=loc_seller3
        )

        Product.objects.create(
            name='Maggie 500g Packet', description='Nestle Maggie 500g noodle pack',
            sku='NESTLE-MAGGIE-500G', selling_price=10.00,
            weight_kg=0.5, length_cm=10.0, width_cm=10.0, height_cm=10.0,
            seller=seller1, is_available=True, stock_quantity=500, category='Food & Beverages'
        )
        Product.objects.create(
            name='Rice Bag 10Kg', description='Premium basmati rice 10kg bag',
            sku='RICE-BAG-10KG', selling_price=500.00,
            weight_kg=10.0, length_cm=1000.0, width_cm=800.0, height_cm=500.0,
            seller=seller2, is_available=True, stock_quantity=200, category='Grocery'
        )
        Product.objects.create(
            name='Sugar Bag 25Kg', description='Refined white sugar 25kg bag',
            sku='SUGAR-BAG-25KG', selling_price=700.00,
            weight_kg=25.0, length_cm=1000.0, width_cm=900.0, height_cm=600.0,
            seller=seller3, is_available=True, stock_quantity=150, category='Grocery'
        )

        Warehouse.objects.create(
            name='Bangalore Warehouse', code='BLR_Warehouse', location=loc_wh1,
            address='Whitefield Industrial Area', city='Bangalore',
            state='Karnataka', pincode='560066', contact_phone='8000000001',
            is_active=True, capacity_kg=50000.0
        )
        Warehouse.objects.create(
            name='Mumbai Warehouse', code='MUMB_Warehouse', location=loc_wh2,
            address='Bhiwandi Logistics Park', city='Mumbai',
            state='Maharashtra', pincode='421302', contact_phone='8000000002',
            is_active=True, capacity_kg=75000.0
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
