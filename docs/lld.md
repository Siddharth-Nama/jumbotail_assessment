# Low Level Design (LLD)

## Django Models (Data Dictionary)

| Model | Attributes | Relationships |
|-------|------------|---------------|
| `Location` | `lat` (Decimal), `lng` (Decimal) | Base coordinate system used by all entities. |
| `Customer` | `customer_code`, `name`, `phone` | `OneToOneField` to `Location` |
| `Seller` | `name`, `email`, `phone`, `gstin` | `OneToOneField` to `Location` |
| `Warehouse` | `code`, `name`, `is_active` | `OneToOneField` to `Location` |
| `Product` | `name`, `price`, `weight_kg`, dimensions (`length_cm`, `width_cm`, `height_cm`) | `ForeignKey` to `Seller` |

*Note: The `Product` model features an `@property` attribute `volume_cm3` that dynamically computes total physical volume on read.*

---

## Service Layer Blueprint

### 1. `distance_service.py`
- **Method**: `haversine_distance(loc1, loc2)`
- **Behavior**: Uses math trigonometric ratios to calculate great circle distance between two Earth coordinates. Returns `float` distance in kilometers.

### 2. `warehouse_service.py`
- **Method**: `find_nearest_warehouse(seller_location)`
- **Behavior**: Fetches all active warehouses from the ORM. Iterates over them applying `haversine_distance`. Stores the minimum found distance and returns the `Warehouse` object. Raises `MarketplaceException` if DB is empty.

### 3. `shipping_service.py` (Strategy Pattern)
- **Interface**: `TransportStrategy` abstract class requiring `calculate_cost(distance, weight)`.
- **Implementations**:
  - `AeroplaneStrategy` (>= 500 km) — 1 Rs/km/kg
  - `TruckStrategy` (100 - 499 km) — 2 Rs/km/kg
  - `MiniVanStrategy` (< 100 km) — 3 Rs/km/kg
- **Method**: `get_transport_strategy(distance_km)` acts as a factory returning the correct initialized class instance based on distance boundaries.

### 4. `charge_service.py`
- **Method**: `calculate_shipping_charge(warehouse_location, customer_location, delivery_speed)`
- **Behavior**:
  1. Identifies distance from warehouse to customer.
  2. Resolves transport strategy.
  3. Calculates base charge by mapping arbitrary standard weights (or sum of product weights). Assumes 1kg standard for formula validation if no product is explicitly iterated.
  4. Resolves delivery speed logic (Standard vs Express rate injection).
  5. Returns a detailed calculation dictionary breaking down all cost steps.

---

## Caching Strategy
- The cache key is constructed using a deterministic string formatting: `shipping_{warehouse_id}_{customer_id}_{speed}`.
- Handled actively in `views.py` using Django's `cache.get()` and `cache.set()`.
- Timeout set to `300s` in base `settings.py`.

## Exception Handling
- Defined `exceptions.py` which extends `APIException`.
- Added custom payload mapping via `marketplace_exception_handler` injected directly into `REST_FRAMEWORK` settings payload so that native 500s are transformed into readable `{"error": True, "message": "Reason"}` JSON objects.
