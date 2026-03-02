import { Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './pages/Home';
import FindWarehouse from './pages/FindWarehouse';

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="nearest-warehouse" element={<FindWarehouse />} />
        <Route path="shipping-charge" element={<div>Shipping Charge</div>} />
        <Route path="calculator" element={<div>Estimator Calculator</div>} />
        <Route path="explorer" element={<div>Entities Explorer</div>} />
      </Route>
    </Routes>
  );
}

export default App;
