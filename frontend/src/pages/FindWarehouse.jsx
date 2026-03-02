import { useState } from 'react';
import { getNearestWarehouse } from '../services/api';
import { MapPin, Box, Loader2 } from 'lucide-react';
import '../forms.css';

const FindWarehouse = () => {
  const [sellerId, setSellerId] = useState('');
  const [productId, setProductId] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!sellerId || !productId) return;

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const data = await getNearestWarehouse(sellerId, productId);
      setResult(data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to find nearest warehouse');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <h2>Find Nearest Warehouse</h2>
        <p>Enter the Seller ID and Product ID to locate the closest active warehouse.</p>
      </header>

      <div className="form-card card">
        <form onSubmit={handleSearch}>
          <div className="input-group">
            <label className="input-label">Seller ID</label>
            <input
              type="number"
              className="input-field"
              value={sellerId}
              onChange={(e) => setSellerId(e.target.value)}
              placeholder="e.g. 1"
              required
            />
          </div>
          <div className="input-group">
            <label className="input-label">Product ID</label>
            <input
              type="number"
              className="input-field"
              value={productId}
              onChange={(e) => setProductId(e.target.value)}
              placeholder="e.g. 1"
              required
            />
          </div>
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? <Loader2 className="animate-spin" size={20} /> : <MapPin size={20} />}
            Find Warehouse
          </button>
        </form>
      </div>

      {error && (
        <div className="error-message card">
          <p>{error}</p>
        </div>
      )}

      {result && (
        <div className="result-card card">
          <h3>Warehouse Found: {result.warehouseName}</h3>
          <div className="result-details">
            <p><strong>Code:</strong> {result.warehouseCode}</p>
            <p><strong>Distance:</strong> {result.distanceKm} km</p>
            <p><strong>Seller Name:</strong> {result.sellerName}</p>
            <p><strong>Product:</strong> {result.productName}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default FindWarehouse;
