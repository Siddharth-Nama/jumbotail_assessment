from django.urls import path
from marketplace.views import NearestWarehouseView, ShippingChargeView, ShippingChargeCalculateView

urlpatterns = [
    path('warehouse/nearest', NearestWarehouseView.as_view(), name='nearest-warehouse'),
    path('shipping-charge', ShippingChargeView.as_view(), name='shipping-charge'),
    path('shipping-charge/calculate', ShippingChargeCalculateView.as_view(), name='shipping-charge-calculate'),
]
