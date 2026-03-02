# B2B E-Commerce Shipping Charge Estimator

A full-stack application for calculating shipping charges in a B2B Kirana marketplace (like Jumbotail). 

**Tech Stack:** 
- **Backend**: Django 6, Django REST Framework, SQLite
- **Frontend**: React 19, Vite, React Router, Axios, Lucide Icons, Vanilla CSS
- **Architecture**: Service Layer Pattern, Strategy Pattern (for transport modes)

---

## 🚀 Quick Start Guide

### 1. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate # Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data   # Populates the mock database
python manage.py runserver
```
The Django API will be running at `http://localhost:8000/api/v1/`.

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```
The React App will be running at `http://localhost:5173/`.

---

## 🗄️ Database Seeds (Test Data)
Running `python manage.py seed_data` creates:
- **Customers**: ID 1 (Hyderabad), ID 2 (Mumbai)
- **Sellers**: ID 1 (Bangalore), ID 2 (Mumbai), ID 3 (Pune)
- **Products**: ID 1 (Maggie), ID 2 (Rice Bag), ID 3 (Sugar Bag)
- **Warehouses**: ID 1 (Bangalore), ID 2 (Mumbai)

---

## 🔌 API Endpoints

### 1. Find Nearest Warehouse
**`GET /api/v1/warehouse/nearest?sellerId={id}&productId={id}`**
Finds the closest active warehouse to a specified seller's location using the Haversine distance formula.

### 2. Get Shipping Charge
**`GET /api/v1/shipping-charge?warehouseId={id}&customerId={id}&deliverySpeed={standard|express}`**
Calculates the transport cost based on distance:
- `< 100km`: Mini Van (₹3/km/kg)
- `100 - 499km`: Truck (₹2/km/kg)
- `>= 500km`: Aeroplane (₹1/km/kg)
Adds a standard ₹10 courier charge, plus optionally ₹1.2/kg for express delivery.

### 3. Full Shipping Estimate
**`POST /api/v1/shipping-charge/calculate`**
```json
{
  "sellerId": 1,
  "customerId": 1,
  "deliverySpeed": "standard"
}
```
Orchestrates finding the nearest warehouse for the seller and calculating the shipping cost to the customer in one combined API call.

---

## ⚙️ Architecture & Design Decisions

1. **Service Layer**: Business logic (Haversine formula, finding warehouses, shipping rates) is isolated in `backend/marketplace/services/` rather than cluttering views or models.
2. **Strategy Pattern**: Transport modes (Aeroplane, Truck, MiniVan) are implemented as strategy classes in `shipping_service.py` to make future scaling/modifications of transport modes simple.
3. **Caching**: Uses `LocMemCache` (extendable to Redis) to cache the API responses for 5 minutes (`300s`) for duplicate requests, significantly improving performance.
4. **Exception Handling**: Global DRF exception handler standardizes all responses to an `{ "error": "message" }` format.
5. **No Code Comments**: Strictly adhering to assignment constraints requiring code to speak for itself without inline comments.
