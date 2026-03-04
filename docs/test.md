# Testing Strategy & Execution (test.md)

## Unit and Integration Testing Overview
The project implements testing via the standard Django `TestCase` library. Tests are partitioned into two core files inside `backend/marketplace/tests/`.

## 1. Unit Tests (`test_services.py`)
This suite completely isolates the core logic methods from HTTP and Views, proving that the math and boundaries work without a network layer.

- `test_haversine_distance`: Hard codes actual GPS coordinates with known distances (e.g. Bangalore to Mumbai) and verifies the result falls within a 1km margin of error.
- `test_find_nearest_warehouse`: Spawns 3 dummy warehouses and a seller. Proves the loop accurately identifies the geographically closest warehouse instance. Handles the Empty DB edge fault check.
- `test_transport_strategy`: Proves the Factory limits (99km uses Minivan, 150km uses truck, 600km uses Aeroplane) and verifies their respective cost calculations.
- `test_charge_service_standard_vs_express`: Validates that replacing the 'standard' keyword with 'express' correctly injects the `1.2 * Weight` surcharge dynamically.

## 2. API Integration Tests (`test_api.py`)
This suite spins up the Django HTTP test client, mocking realistic external JSON requests and verifying caching headers, HTTP status codes, and JSON payload shapes.

**Nearest Warehouse Endpoint Checks:**
- Passing valid `sellerId` and `productId` returns `200 OK` and correctly yields the nearest warehouse PK and `long`/`lat` formats.
- Passing missing params immediately traps into HTTP `400 Bad Request`.
- Passing params for non-existent entities hits HTTP `404 Not Found`.

**Shipping Charge Evaluation Checks:**
- Valid payload returns nested `breakdown` dictionary identifying exact distance metrics and prices.
- Using invalid speed parameters (e.g., `deliverySpeed=hyperspeed`) yields HTTP `400`.

**Combined Full Post Evaluation Checks:**
- Verifies POST payload structures.
- Validates the JSON return shape combines BOTH the charge value and the targeted warehouse coordinates as requested by the document specification.

## Execution
```bash
python manage.py test marketplace.tests --verbosity=2
```

**Result:**
```text
Found 12 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
............
----------------------------------------------------------------------
Ran 12 tests in 0.100s

OK
Destroying test database for alias 'default'...
```
All 12 checks safely pass. No test failures, regressions, or system crashes identified.
