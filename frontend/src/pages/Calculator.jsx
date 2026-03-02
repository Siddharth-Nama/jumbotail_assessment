import { useState } from 'react';
import { calculateShippingCharge } from '../services/api';
import { Calculator as CalcIcon, Loader2 } from 'lucide-react';
import '../forms.css';

const Calculator = () => {
  const [sellerId, setSellerId] = useState('');
  const [customerId, setCustomerId] = useState('');
  const [deliverySpeed, setDeliverySpeed] = useState('standard');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleCalculate = async (e) => {
    e.preventDefault();
    if (!sellerId || !customerId) return;

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const payload = {
        sellerId: parseInt(sellerId),
        customerId: parseInt(customerId),
        deliverySpeed
      };
      const data = await calculateShippingCharge(payload);
      setResult(data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to calculate end-to-end shipping');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <h2>End-to-End Shipping Calculator</h2>
        <p>Calculates nearest warehouse for the seller and total shipping to the customer.</p>
      </header>

      <div className="form-card card">
        <form onSubmit={handleCalculate}>
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
            <label className="input-label">Customer ID</label>
            <input
              type="number"
              className="input-field"
              value={customerId}
              onChange={(e) => setCustomerId(e.target.value)}
              placeholder="e.g. 1"
              required
            />
          </div>
          <div className="input-group">
            <label className="input-label">Delivery Speed</label>
            <select
              className="input-field"
              value={deliverySpeed}
              onChange={(e) => setDeliverySpeed(e.target.value)}
            >
              <option value="standard">Standard</option>
              <option value="express">Express</option>
            </select>
          </div>
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? <Loader2 className="animate-spin" size={20} /> : <CalcIcon size={20} />}
            Calculate Full Estimate
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
          <h3 style={{color: '#10b981', borderBottomColor: '#10b981'}}>
            Total Estimate: ₹{result.shippingCharge}
          </h3>
          
          <div style={{marginTop: '1.5rem', marginBottom: '1rem', padding: '1rem', backgroundColor: '#f9fafb', borderRadius: '0.5rem'}}>
            <h4 style={{marginBottom: '0.5rem', color: 'var(--text-secondary)'}}>Routing Info</h4>
            <div className="result-details">
              <p><strong>Nearest Warehouse:</strong> {result.nearestWarehouse.warehouseName} ({result.nearestWarehouse.distanceKm} km from seller)</p>
              <p><strong>Seller:</strong> {result.nearestWarehouse.sellerName}</p>
              <p><strong>Customer:</strong> {result.customerName}</p>
            </div>
          </div>

          <div style={{padding: '1rem', backgroundColor: '#f9fafb', borderRadius: '0.5rem'}}>
            <h4 style={{marginBottom: '0.5rem', color: 'var(--text-secondary)'}}>Charge Breakdown</h4>
            <div className="result-details">
              <p><strong>Delivery Distance:</strong> {result.breakdown.distance_km} km</p>
              <p><strong>Transport Mode:</strong> {result.breakdown.transport_mode}</p>
              <p><strong>Base Transport Charge:</strong> ₹{result.breakdown.base_charge}</p>
              <p><strong>Delivery Speed:</strong> {result.breakdown.delivery_speed}</p>
              <p><strong>Express Surcharge:</strong> ₹{result.breakdown.express_charge}</p>
              <p><strong>Standard Courier Fee:</strong> ₹{result.breakdown.standard_courier_charge}</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Calculator;
