from marketplace.services.distance_service import haversine_distance
from marketplace.services.shipping_service import get_transport_strategy
from marketplace.exceptions import MarketplaceException

STANDARD_COURIER_CHARGE = 10.0
EXPRESS_EXTRA_PER_KG = 1.2
DEFAULT_WEIGHT_KG = 1.0

def calculate_shipping_charge(warehouse_location, customer_location, delivery_speed: str, weight_kg: float = DEFAULT_WEIGHT_KG) -> dict:
    if delivery_speed not in ('standard', 'express'):
        raise MarketplaceException(
            f'Invalid delivery speed: {delivery_speed}. Must be "standard" or "express".',
            status_code=400,
        )

    distance_km = haversine_distance(
        warehouse_location.lat,
        warehouse_location.lng,
        customer_location.lat,
        customer_location.lng,
    )

    strategy = get_transport_strategy(distance_km)
    base_charge = strategy.calculate_base_charge(distance_km, weight_kg)

    express_charge = 0.0
    if delivery_speed == 'express':
        express_charge = EXPRESS_EXTRA_PER_KG * weight_kg

    total_charge = round(STANDARD_COURIER_CHARGE + base_charge + express_charge, 2)

    return {
        'distance_km': round(distance_km, 2),
        'transport_mode': strategy.get_mode_name(),
        'base_charge': round(base_charge, 2),
        'express_charge': round(express_charge, 2),
        'standard_courier_charge': STANDARD_COURIER_CHARGE,
        'total_charge': total_charge,
        'delivery_speed': delivery_speed,
        'weight_kg': weight_kg,
    }
