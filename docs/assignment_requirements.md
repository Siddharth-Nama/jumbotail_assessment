# Assignment Requirements

## Problem Statement
Build a simple application with APIs to calculate the shipping charge for delivering a product in a B2B e-commerce marketplace.

## Context
Imagine building a B2B e-commerce marketplace that helps Kirana stores discover and order the products they need to run their shops. It works similarly to consumer platforms like Flipkart or Amazon but focuses on the specific needs of small retailers.

## Entities
1. **Customer**: Kirana stores with contact details and exact geographical coordinates `{lat, lng}`. 
2. **Seller and Product**: Sellers located anywhere in India selling products with attributes like weight and dimensions.
3. **Warehouse**: Marketplace warehouses present across the country where sellers drop products.

## Delivery Logistics Concept
- When a customer places an order, the seller finds the **nearest warehouse** to their location and drops the items.
- Products are shipped from the warehouse to the customer's location.
- **Transport Mode** depends on distance:
  - Mini Van: 0-100Km (3 Rs/km/kg)
  - Truck: 100-499Km (2 Rs/km/kg)
  - Aeroplane: 500Km+ (1 Rs/km/kg)
- **Delivery Speed** options:
  - Standard: Rs 10 standard courier charge + calculated shipping charge.
  - Express: Rs 10 standard + Rs 1.2 per kg Extra + calculated shipping charge.

## Required API Endpoints
1. **Get Nearest Warehouse for a Seller**
   - `GET /api/v1/warehouse/nearest?sellerId=&productId=`
   - Returns the nearest warehouse ID and coordinates.

2. **Get Shipping Charge for Customer from Warehouse**
   - `GET /api/v1/shipping-charge?warehouseId=&customerId=&deliverySpeed=`
   - Returns the total calculated shipping charge.

3. **Get Combined Shipping Estimate for Seller and Customer**
   - `POST /api/v1/shipping-charge/calculate`
   - Orchestrates finding the nearest warehouse and calculating the total cost.

## "Must Have" Constraints Met
- [x] Store entities in a structured data store.
- [x] Graceful exception handling for invalid/missing parameters, or unsupported locations.
- [x] Clean, modular, well-documented code.

## "Good to Have" Constraints Met
- [x] Use Design Patterns (Strategy and Service Repository patterns implemented).
- [x] Write Unit Tests for APIs and Edge Cases (12 robust integration & unit tests written).
- [x] Response Caching (`LocMemCache` implemented on all identical GET pulls).
