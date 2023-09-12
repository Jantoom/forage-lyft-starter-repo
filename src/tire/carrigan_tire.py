from src.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear: [float]):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        """Checks if an object needs servicing

        Returns:
            bool: True if the object needs servicing, otherwise False
        """
        return any(wear >= 0.9 for wear in self.tire_wear)
