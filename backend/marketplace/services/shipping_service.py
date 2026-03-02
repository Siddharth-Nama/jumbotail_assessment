from abc import ABC, abstractmethod
from marketplace.exceptions import MarketplaceException


TRANSPORT_MODE_AEROPLANE = 'Aeroplane'
TRANSPORT_MODE_TRUCK = 'Truck'
TRANSPORT_MODE_MINI_VAN = 'MiniVan'

AEROPLANE_THRESHOLD_KM = 500.0
TRUCK_THRESHOLD_KM = 100.0


class TransportStrategy(ABC):
    @abstractmethod
    def get_mode_name(self) -> str:
        pass

    @abstractmethod
    def calculate_base_charge(self, distance_km: float, weight_kg: float) -> float:
        pass


class AeroplaneStrategy(TransportStrategy):
    RATE_PER_KM_PER_KG = 1.0

    def get_mode_name(self) -> str:
        return TRANSPORT_MODE_AEROPLANE

    def calculate_base_charge(self, distance_km: float, weight_kg: float) -> float:
        return self.RATE_PER_KM_PER_KG * distance_km * weight_kg


class TruckStrategy(TransportStrategy):
    RATE_PER_KM_PER_KG = 2.0

    def get_mode_name(self) -> str:
        return TRANSPORT_MODE_TRUCK

    def calculate_base_charge(self, distance_km: float, weight_kg: float) -> float:
        return self.RATE_PER_KM_PER_KG * distance_km * weight_kg


class MiniVanStrategy(TransportStrategy):
    RATE_PER_KM_PER_KG = 3.0

    def get_mode_name(self) -> str:
        return TRANSPORT_MODE_MINI_VAN

    def calculate_base_charge(self, distance_km: float, weight_kg: float) -> float:
        return self.RATE_PER_KM_PER_KG * distance_km * weight_kg


def get_transport_strategy(distance_km: float) -> TransportStrategy:
    if distance_km >= AEROPLANE_THRESHOLD_KM:
        return AeroplaneStrategy()
    elif distance_km >= TRUCK_THRESHOLD_KM:
        return TruckStrategy()
    else:
        return MiniVanStrategy()
