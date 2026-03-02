import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="app-container">
      <Routes>
        <Route path="/" element={<div>Home Page</div>} />
        <Route path="/nearest-warehouse" element={<div>Nearest Warehouse</div>} />
        <Route path="/shipping-charge" element={<div>Shipping Charge</div>} />
        <Route path="/calculator" element={<div>Estimator Calculator</div>} />
        <Route path="/explorer" element={<div>Entities Explorer</div>} />
      </Routes>
    </div>
  );
}

export default App;
