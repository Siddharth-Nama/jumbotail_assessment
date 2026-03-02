# Jumbotail B2B Shipping Charge Estimator

A full-stack B2B e-commerce shipping charge estimation system for Kirana marketplaces.

## Tech Stack

- **Backend**: Django 5 + Django REST Framework + SQLite
- **Frontend**: React 18 + Vite + Axios

## Project Structure

```
├── backend/    # Django REST API
└── frontend/   # React + Vite SPA
```

## Setup

See individual README files inside `backend/` and `frontend/`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/warehouse/nearest` | Get nearest warehouse for a seller |
| GET | `/api/v1/shipping-charge` | Get shipping charge from warehouse to customer |
| POST | `/api/v1/shipping-charge/calculate` | Full shipping estimate for seller + customer |
