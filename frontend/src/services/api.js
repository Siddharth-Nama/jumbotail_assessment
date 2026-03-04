import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'https://jumbotail-assessment.onrender.com/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getNearestWarehouse = async (sellerId, productId) => {
  const response = await api.get('/warehouse/nearest', {
    params: { sellerId, productId }
  });
  return response.data;
};

export const getShippingCharge = async (warehouseId, customerId, deliverySpeed) => {
  const response = await api.get('/shipping-charge', {
    params: { warehouseId, customerId, deliverySpeed }
  });
  return response.data;
};

export const calculateShippingCharge = async (data) => {
  const response = await api.post('/shipping-charge/calculate', data);
  return response.data;
};

export default api;
