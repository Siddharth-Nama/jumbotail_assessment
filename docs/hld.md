# High Level Design (HLD)

## System Overview
The JumboShip B2B Estimator is built as a highly decoupled Client-Server architecture. The fundamental objective of the system is to calculate delivery logistics via geospatial algorithms, determining both optimal staging locations (warehouses) and pricing logic based on weight, distance, and selected delivery modes.

## Architecture Diagram Architecture
```text
[ React Vite SPA Front-End ]
          |
    (HTTP / Axios) 
          v
[ Django REST Framework Router ] 
          |
(Global Auth / Exception Middleware / Cache Middleware)
          |
[ Controllers / API Views ]  <---> [ Django LocMemCache Layer ]
          |
[ Service Layer (Business Logic) ] 
          |
[ Data Access Layer (Django ORM) ]
          |
[ SQLite Relational Database ]
```

## Core Components
### 1. Presentation Layer (Frontend)
- **Framework**: React 19 + Vite + React Router DOM
- **Concept**: A Single Page Application containing 5 primary routes. Provides form interfaces allowing end-users to simulate the endpoints natively. Contains an `api.js` Axios wrapper to seamlessly communicate with the backend.

### 2. API / Routing Layer (Backend)
- **Framework**: Django REST Framework (DRF)
- **Concept**: Handles request routing. Converts JSON API requests into Python data structures. Implements strict parameter validations and uses custom Exception Handlers to return uniform `{"error": "message"}` payload blocks.

### 3. Business Service Layer
- **Location**: `backend/marketplace/services/`
- **Concept**: Contains zero HTTP-specific code. This layer handles coordinates fetching, Haversine formula calculation, Strategy pattern selection for transport, and base rate mathematics. Highly testable and modular.

### 4. Database Schema (SQLite)
- A highly normalized schema using abstract models to handle relational logic.
- Locations map One-to-One to Customers, Sellers, and Warehouses. Products are bound to Sellers via Foreign Keys.

## Scaling Strategies (Future Proofing)
1. **Database**: Swap `SQLite` with `PostgreSQL` using PostGIS extensions for native spatial queries instead of calculating Haversine in-memory.
2. **Caching**: Replace Django `LocMemCache` with `Redis` to share cached distances and API endpoints across horizontally scaled load-balanced nodes.
3. **Queueing**: If calculating pricing requires calling external APIs, offload calculations to `Celery/RabbitMQ` background tasks.
