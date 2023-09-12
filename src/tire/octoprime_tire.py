from src.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear: [float]):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        """Checks if an object needs servicing

        Returns:
            bool: True if the object needs servicing, otherwise False
        """
        return sum(int(wear * 100) for wear in self.tire_wear) >= 300
