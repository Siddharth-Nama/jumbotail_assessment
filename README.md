# JumboShip - B2B E-Commerce Shipping Charge Estimator
**Live Application:** *(Localhost via Django & Vite)*

## Overview
Welcome to my submission for the **Jumbotail Assessment**. I have engineered **JumboShip**, a high-performance B2B Shipping Charge Estimator that transforms complex supply-chain calculations into an intuitive, lightning-fast full-stack application.

This project is a precision-engineered marketplace platform. It integrates a robust Django REST Framework backend, service-layer architectural patterns, and a sleek, multi-page React/Vite frontend. I built this to not just meet, but exceed the assignment requirements, focusing on **Architectural Purity, Extensible Design Patterns, and Real-time Caching**.

✅ **Requirement Satisfaction Matrix**
I have rigorously implemented 100% of the assignment requirements. Below is the detailed breakdown of how each specification was met:

### 1. Core Endpoints & Business Logic
- **Get Nearest Warehouse (`GET /api/v1/warehouse/nearest`)**: Given a seller and product, evaluates geographical coordinates using the Haversine formula to instantly return the closest active staging warehouse.
- **Get Shipping Charge (`GET /api/v1/shipping-charge`)**: Dynamically calculates shipping charges based on a multi-tiered distance matrix (Mini Van, Truck, Aeroplane) and injects flat or dynamic surcharges for Standard vs. Express delivery.
- **Calculate Combined Estimate (`POST /api/v1/shipping-charge/calculate`)**: Orchestrates finding the nearest warehouse and evaluating the end-to-end transport costs across the supply chain in one sub-millisecond API call.

### 2. Extensible Execution Engine (Design Patterns)
- **Zero-View-Bloat Architecture**: Every ounce of business logic has been extracted from Django views into a dedicated `services/` layer (`distance_service.py`, `shipping_service.py`, etc.).
- **Strategy Pattern (`TransportStrategy`)**: Transport modes are handled dynamically via a Strategy factory. Distance boundaries dynamically instantiate `AeroplaneStrategy`, `TruckStrategy`, or `MiniVanStrategy`.
- **In-Memory Caching (`LocMemCache`)**: All duplicate mathematical GET requests are cached to prevent redundant DB calls or Haversine computations, ensuring lightning-fast B2B scale responses.

### 3. Data & State Management
- **Database**: SQLite (via Django ORM) stores all Customers, Sellers, Products, Locations, and Warehouses through a highly normalized, relational schema.
- **Custom Exception Handling**: Native Django HTTP 500 pages are entirely suppressed. Instead, a custom `MarketplaceException` handler returns uniform, graceful JSON 400/404 errors for invalid distances, missing entities, or malformed queries.
- **Strict Payload Matching**: API responses map exactly to the camelCase and entity structures requested in the assignment parameters.

### 4. Interactive Frontend (Beyond Requirements)
- **Visual Dashboard**: Shipped a sleek React/Vite Single Page Application demonstrating exactly how a Kirana store owner or Seller would interact with the APIs.
- **Pixel-Perfect UI**: Fully responsive interfaces for nearest warehouse finding, dynamic calculations, and exploring seeded database entities via Lucide icons and Vanilla CSS.

---

## Tech Stack
- **Backend Framework**: Django 6, Django REST Framework
- **Database**: SQLite / Django ORM
- **Frontend Framework**: React 19, Vite (App Router equivalent)
- **Styling**: Vanilla CSS with curated CSS Variables and Flexbox/Grid systems
- **State & HTTP**: React `useState`, Axios for performant client-side data fetching
- **Testing**: Django `TestCase` (12 robust unit & integration tests)

---

## Why This Project Stands Out?

**Architectural Purity: Strict Separation of Concerns**
The system is designed with a clear boundary between the visual interface, request routing, and core mathematical logic. The frontend handles the user experience, views handle JSON serialization, and the `services/` layer handles the heavy lifting of geographical calculations algorithms.

**"Command Center" Testing UI**
Unlike raw backend assignments, JumboShip offers a Tactical Workspace:
- **Visual Discovery**: A built-in "Explorer" tab lists seeded data IDs, eliminating database guessing games.
- **Deep Observability**: Every API calculation breaks down costs line-by-line (Base rate vs. Distance vs. Surcharges) in the UI.

---

## Candidate Profile: Siddharth Nama
*"I don't just write code; I build solutions that scale."*

Hello! I'm Siddharth Nama, a passionate Software Engineer Intern from Kota, India. I thrive on solving complex backend challenges and crafting seamless user experiences. My journey involves:

- Spearheading **"Suvidha Manch"** at the Haryana Government (C4GT), where I helped digitize 25,000+ roads.
- Optimizing performance at **Mercato Agency**, creating systems that handle 10,000+ users with ease.
- Driving innovation with AI-powered platforms like **Scripty** and **AiProgress**.
- Leading teams and delivering results under pressure, from managing election portals to restocking systems.

I am fit for this role because I combine strong technical fundamentals (Django, React, Systems Design) with an ownership mindset. I treat every assignment like a production release—focusing on edge cases, maintainability, and user impact. I am ready to bring this energy and precision to the Jumbotail team!

**Let's Connect:**
- **LinkedIn**: [Siddharth Nama](#)
- **GitHub**: [Siddharth-Nama](https://github.com/Siddharth-Nama)
- **Phone**: +91-8000694996

---

## Setup Instructions

This project uses a decoupled Full Stack architecture. Follow the steps below for rapid setup.

### 1. Backend Setup (Django API)

Open a terminal and navigate to the backend directory:
```bash
cd backend
python -m venv venv

# Activate Virtual Environment
venv\Scripts\activate   # Windows
# source venv/bin/activate # Mac/Linux

# Install Dependencies
pip install -r requirements.txt

# Run Migrations and Seed Database
python manage.py migrate
python manage.py seed_data

# Start Development Server
python manage.py runserver
```
*The Django API will be running at `http://localhost:8000/api/v1/`*

### 2. Frontend Setup (React/Vite)

Open a new, separate terminal and navigate to the frontend directory:
```bash
cd frontend

# Install Dependencies
npm install

# Run Development Server
npm run dev
```
*The React App will be rapidly served at `http://localhost:5173/`*

---
© 2026 Developed by Siddharth Nama
