import { NavLink } from 'react-router-dom';
import { Package } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="navbar">
      <NavLink to="/" className="nav-brand">
        <Package size={24} />
        <span>JumboShip</span>
      </NavLink>
      <div className="nav-links">
        <NavLink to="/explorer" className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'}>Explorer</NavLink>
        <NavLink to="/nearest-warehouse" className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'}>Find Warehouse</NavLink>
        <NavLink to="/shipping-charge" className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'}>Shipping Charge</NavLink>
        <NavLink to="/calculator" className={({isActive}) => isActive ? 'nav-link active' : 'nav-link'}>Full Calculator</NavLink>
      </div>
    </nav>
  );
};

export default Navbar;
