from marketplace.models import Warehouse
from marketplace.services.distance_service import haversine_distance
from marketplace.exceptions import MarketplaceException


def find_nearest_warehouse(seller_location):
    warehouses = Warehouse.objects.filter(is_active=True).select_related('location')

    if not warehouses.exists():
        raise MarketplaceException('No active warehouses found in the system.', status_code=404)

    nearest = None
    min_distance = float('inf')

    for warehouse in warehouses:
        dist = haversine_distance(
            seller_location.lat,
            seller_location.lng,
            warehouse.location.lat,
            warehouse.location.lng,
        )
        if dist < min_distance:
            min_distance = dist
            nearest = warehouse

    return nearest
