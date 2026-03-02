import { useState } from 'react';
import { getShippingCharge } from '../services/api';
import { Truck, Loader2 } from 'lucide-react';
import '../forms.css';

const ShippingCharge = () => {
  const [warehouseId, setWarehouseId] = useState('');
  const [customerId, setCustomerId] = useState('');
  const [deliverySpeed, setDeliverySpeed] = useState('standard');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleCalculate = async (e) => {
    e.preventDefault();
    if (!warehouseId || !customerId) return;

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const data = await getShippingCharge(warehouseId, customerId, deliverySpeed);
      setResult(data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to calculate shipping charge');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <h2>Shipping Charge Calculator</h2>
        <p>Calculate shipping costs between a known warehouse and a customer.</p>
      </header>

      <div className="form-card card">
        <form onSubmit={handleCalculate}>
          <div className="input-group">
            <label className="input-label">Warehouse ID</label>
            <input
              type="number"
              className="input-field"
              value={warehouseId}
              onChange={(e) => setWarehouseId(e.target.value)}
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
            {loading ? <Loader2 className="animate-spin" size={20} /> : <Truck size={20} />}
            Calculate Charge
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
          <h3>Total Charge: ₹{result.shippingCharge}</h3>
          <div className="result-details">
            <p><strong>Distance:</strong> {result.breakdown.distance_km} km</p>
            <p><strong>Transport Mode:</strong> {result.breakdown.transport_mode}</p>
            <p><strong>Base Transport Charge:</strong> ₹{result.breakdown.base_charge}</p>
            <p><strong>Delivery Speed:</strong> {result.breakdown.delivery_speed}</p>
            <p><strong>Surcharge (Express):</strong> ₹{result.breakdown.express_charge}</p>
            <p><strong>Standard Courier Fee:</strong> ₹{result.breakdown.standard_courier_charge}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default ShippingCharge;
