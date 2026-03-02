import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import FindWarehouse from './pages/FindWarehouse';
import ShippingCharge from './pages/ShippingCharge';
import Calculator from './pages/Calculator';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="nearest-warehouse" element={<FindWarehouse />} />
        <Route path="shipping-charge" element={<ShippingCharge />} />
        <Route path="calculator" element={<Calculator />} />
        <Route path="explorer" element={<div>Entities Explorer</div>} />
      </Route>
    </Routes>
  );
}

export default App;
