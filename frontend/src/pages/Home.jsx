import { Link } from 'react-router-dom';
import { Truck, MapPin, Calculator, Search } from 'lucide-react';
import '../home.css';

const Home = () => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Welcome to JumboShip B2B Estimator</h1>
        <p>Your one-stop solution for calculating shipping charges for your marketplace deliveries.</p>
      </header>

      <div className="features-grid">
        <Link to="/explorer" className="card feature-card">
          <Search size={40} className="feature-icon" />
          <h3>Entities Explorer</h3>
          <p>Browse our registered sellers, customers, products, and warehouses.</p>
        </Link>
        
        <Link to="/nearest-warehouse" className="card feature-card">
          <MapPin size={40} className="feature-icon" />
          <h3>Find Nearest Warehouse</h3>
          <p>Locate the closest warehouse for a specific seller and product.</p>
        </Link>

        <Link to="/shipping-charge" className="card feature-card">
          <Truck size={40} className="feature-icon" />
          <h3>Shipping Charge</h3>
          <p>Calculate shipping cost between a warehouse and a customer.</p>
        </Link>

        <Link to="/calculator" className="card feature-card">
          <Calculator size={40} className="feature-icon" />
          <h3>Full Estimator</h3>
          <p>End-to-end calculation: from seller to nearest warehouse, then to customer.</p>
        </Link>
      </div>
    </div>
  );
};

export default Home;
