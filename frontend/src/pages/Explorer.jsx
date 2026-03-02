import { Users, Building2, Package2, Store } from 'lucide-react';
import '../forms.css';

const Explorer = () => {
  return (
    <div className="page-container" style={{maxWidth: '800px'}}>
      <header className="page-header">
        <h2>Entities Explorer</h2>
        <p>Reference guide for the seeded database entities. Use these IDs to test the application APIs.</p>
      </header>

      <div className="features-grid">
        <div className="card">
          <h3 style={{display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary)', marginBottom: '1rem'}}>
            <Store size={24} /> Customers
          </h3>
          <ul style={{listStyle: 'none', display: 'grid', gap: '0.5rem'}}>
            <li><strong>ID 1:</strong> Shree Kirana Store (Hyderabad)</li>
            <li><strong>ID 2:</strong> Andheri Mini Mart (Mumbai)</li>
          </ul>
        </div>

        <div className="card">
          <h3 style={{display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary)', marginBottom: '1rem'}}>
            <Users size={24} /> Sellers
          </h3>
          <ul style={{listStyle: 'none', display: 'grid', gap: '0.5rem'}}>
            <li><strong>ID 1:</strong> Nestle Seller (Bangalore)</li>
            <li><strong>ID 2:</strong> Rice Seller (Mumbai)</li>
            <li><strong>ID 3:</strong> Sugar Seller (Pune)</li>
          </ul>
        </div>

        <div className="card">
          <h3 style={{display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary)', marginBottom: '1rem'}}>
            <Package2 size={24} /> Products
          </h3>
          <ul style={{listStyle: 'none', display: 'grid', gap: '0.5rem'}}>
            <li><strong>ID 1:</strong> Maggie 500g (Seller 1)</li>
            <li><strong>ID 2:</strong> Rice Bag 10Kg (Seller 2)</li>
            <li><strong>ID 3:</strong> Sugar Bag 25Kg (Seller 3)</li>
          </ul>
        </div>

        <div className="card">
          <h3 style={{display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary)', marginBottom: '1rem'}}>
            <Building2 size={24} /> Warehouses
          </h3>
          <ul style={{listStyle: 'none', display: 'grid', gap: '0.5rem'}}>
            <li><strong>ID 1:</strong> Bangalore WH (50K kg capacity)</li>
            <li><strong>ID 2:</strong> Mumbai WH (75K kg capacity)</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Explorer;
